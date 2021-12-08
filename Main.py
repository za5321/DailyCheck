from func.file.Logger import Logger
l = Logger()
logger = l.logger
l.set_handler()


def decorator(func):
    def decorated(*args, **kwargs):
        logger.info(f"{func.__name__.upper()} STARTED")
        func(*args, **kwargs)
        logger.info(f"{func.__name__.upper()} COMPLETED")
    return decorated


class CheckSvr:
    def __init__(self):
        from func.check.IPHost import IPHost
        from func.GetSvrInfo import GetSvrInfo

        self.g = GetSvrInfo()
        self.check_result = "<server></server>"
        i = IPHost()

        self.hostname, self.ip = i.get_hostname(), i.get_ip()
        self.svr_id: int = self.g.get_svr_id(self.hostname, self.ip)
        if self.svr_id == -1:
            logger.error(f"HOSTNAME: {self.hostname} IP: {self.ip} ---> 일치하는 서버가 없습니다.")
        else:
            logger.info(f"HOSTNAME: {self.hostname} IP: {self.ip}")
            self.write_data("server", "hostname", self.hostname)
            self.write_data("server", "ip", self.ip)

    @decorator
    def disk(self):
        from func.check.Disk import Disk

        disk_list: list = self.g.get_svr_info(self.svr_id, "disk").split()
        if disk_list:
            self.write_data("server", "disk")
            for letter in disk_list:
                result: str = Disk(letter).get_disk()
                self.write_data("disk", letter, result) if result != "NODATA" \
                    else logger.error(f"{letter}드라이브 데이터가 없습니다.")

    @decorator
    def resource(self):
        from func.check.Resource import Resource

        r = Resource()
        cpu: str = r.cpu if r.cpu else "0"
        mem: str = r.mem if r.mem else "0"
        self.write_data("server", "cpu", cpu)
        self.write_data("server", "memory", mem)

    @decorator
    def service(self):
        from func.check.Service import Service

        svc_list: list = self.g.get_svr_info(self.svr_id, "svc").split()
        if svc_list:
            self.write_data("server", "service")
            for svc in svc_list:
                result: str = Service(svc).get_svc()
                self.write_data("service", svc, result) if result != "-1" \
                    else logger.error(f"{svc}가 없습니다.")

    @decorator
    def event(self):
        from func.check.EventLog import EventLog

        event_results: dict = EventLog().get_event()
        if event_results:
            self.write_data("server", "eventlog")
            for key in event_results.keys():
                self.write_data("eventlog", key, event_results[key]) if event_results[key] != "FileNotFound" \
                    else logger.error("이벤트 로그파일이 없습니다.")

    @decorator
    def task(self):
        from func.check.Task import Task

        task_list: list = self.g.get_svr_info(self.svr_id, "task").split()
        if task_list:
            self.write_data("server", "tasklog")
            for task in task_list:
                result: str = Task(task).get_task()
                self.write_data("tasklog", task, result) if result != "FileNotFound" \
                    else logger.error("작업스케쥴러 로그파일이 없습니다.")

    @decorator
    def windows_defender(self):
        from func.check.WinDefender import WinDefender

        if self.g.get_svr_info(self.svr_id, "wdef") == 1:
            result: str = WinDefender().get_wdef()
            self.write_data("server", "windefender", result) if result != "FileNotFound" \
                else logger.error("윈도우 디펜더 로그파일이 없습니다.")

    def write_data(self, parent: str, input: str, string: str = None):
        from func.file.NewTag import NewTag
        n = NewTag(self.check_result)
        self.check_result = n.create(parent, input, string)

    def to_data_file(self, flag: str):
        from func.file.DataFile import DataFile
        w = DataFile(self.hostname)

        if flag == "create":
            w.delete() if w.is_file() else None
            w.create(self.check_result)
            logger.info("데이터 파일을 생성했습니다.")
            return
        elif flag == "send":
            result = w.send() if w.is_file() else logger.error("전송할 데이터 파일이 없습니다.")
            logger.info("데이터 파일을 전송했습니다." if result else "데이터 파일 전송에 실패했습니다.")
            return result
        elif flag == "delete":
            w.delete() if w.is_file() else logger.error("삭제할 데이터 파일이 없습니다.")
            logger.info("데이터 파일을 삭제했습니다.")
            return


if __name__ == "__main__":
    import sys

    logger.info("=========================================================================")
    logger.info("DAILY CHECK STARTED")
    c = CheckSvr()
    if c.svr_id == -1:
        logger.info("DAILY CHECK FINISHED::-1")
        logger.info("=========================================================================")
        sys.exit(-1)
    else:
        c.disk()
        c.resource()
        c.service()
        c.event()
        c.task()
        c.windows_defender()

        c.to_data_file("create")
        result = c.to_data_file("send")
        c.to_data_file("delete")

        logger.info("DAILY CHECK FINISHED::0" if result else "DAILY CHECK FINISHED::-1")
        logger.info("=========================================================================")
        sys.exit(0)
