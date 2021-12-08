import datetime


class Task:
    def __init__(self, task):
        self.file = self.config("path")
        hour = self.config("hour")
        self.date = datetime.datetime.today() - datetime.timedelta(hours=hour)
        self.task = task
        self.result = ""

    @staticmethod
    def config(flag):
        from conf.config import Config
        return Config().task(flag)

    def get_task(self) -> str:
        import Evtx.Evtx as evtx
        from bs4 import BeautifulSoup
        try:
            with evtx.Evtx(self.file) as log:
                for task in log.records():
                    soup = BeautifulSoup(task.xml(), "lxml")
                    if soup.data and soup.data.string.replace("\\", '') == self.task:
                        time = datetime.datetime.strptime(soup.timecreated.attrs.get('systemtime'),
                                                          '%Y-%m-%d %H:%M:%S.%f') + datetime.timedelta(hours=9)
                        time = time.strftime('%Y-%m-%d %H:%M:%S')
                        if time > str(self.date) and soup.eventid.string == '102':
                            self.result = "1"
        except FileNotFoundError:
            self.result = "FileNotFound"
        return self.result
