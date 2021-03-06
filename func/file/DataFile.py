import datetime


class DataFile:
    def __init__(self, hostname: str):
        from func.file.Logger import Logger
        self.logger = Logger().logger

        self.date = datetime.datetime.today().date()
        self.path = "C:\\DailyCheck\\"
        self.filename = f"daily_check_{str(self.date)}_{hostname}.log"

    @staticmethod
    def config():
        from conf.config import Config
        return Config().ftp_connection()

    def is_file(self) -> bool:
        try:
            open(f"{self.path}{self.filename}", 'rb')
        except FileNotFoundError:
            return False
        else:
            return True

    def create(self, data: str):
        f = open(f"{self.path}{self.filename}", mode='wt', encoding='UTF-8')
        f.write(data.replace("&lt;", "<").replace("&gt;", ">"))
        f.close()

    def delete(self):
        import os
        os.remove(f"{self.path}{self.filename}")

    def send(self) -> bool:
        import ftplib
        import os

        con: dict = self.config()
        ftp = ftplib.FTP()
        try:
            ftp.connect(con["ip"], con["port"])
        except TimeoutError:
            self.logger.error("FTP 서버 연결에 실패했습니다.")
            return False
        else:
            ftp.login(con["id"], con["password"])

            os.chdir(self.path)
            f = open(self.filename, mode='rb')
            try:
                ftp.storbinary(f"STOR {self.filename}", f)
            except TimeoutError:
                self.logger.error("데이터 파일 전송에 실패했습니다.")
            f.close()
            ftp.close()
            return True
