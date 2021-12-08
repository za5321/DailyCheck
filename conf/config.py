import json


class Config:
    def __init__(self):
        with open('conf\\config.json', 'r', encoding='UTF-8') as file:
            self.conf = json.load(file)

    def db_connection(self):
        import pymssql
        import decimal
        return pymssql.connect(self.conf['Database']['ip'], self.conf['Database']['id'],
                               self.conf['Database']['password'], self.conf['Database']['name'])

    def ftp_connection(self) -> dict:
        return self.conf["FTP"]

    def socket(self) -> str:
        return self.conf["Socket"]["server"]

    def event(self, flag: str):
        return self.conf["Event"][flag]

    def task(self, flag: str):
        return self.conf["Task"][flag]

    def win_defender(self, flag: str):
        return self.conf["WinDefender"][flag]

    def logging(self, flag: str):
        return self.conf["Logging"][flag]
