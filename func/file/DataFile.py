import datetime
import os


class DataFile:
    def __init__(self, hostname: str):
        from func.file.Logger import Logger
        self.logger = Logger().logger

        date = datetime.datetime.today().date()
        self.path = "C:\\DailyCheck\\"
        self.filename = f"daily_check_{str(date)}_{hostname}.log"

    @staticmethod
    def config():
        from conf.config import Config
        return Config().ftp_connection()

    def is_file(self) -> bool:
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        try:
            open(f"{self.path}{self.filename}", 'rb')
        except FileNotFoundError:
            return False
        else:
            return True

    def create(self, data: dict):
        f = open(f"{self.path}{self.filename}", mode='wt', encoding='UTF-8')
        f.write(str(data))
        f.close()

    def delete(self):
        os.remove(f"{self.path}{self.filename}")

    def send(self) -> bool:
        import ftplib

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
