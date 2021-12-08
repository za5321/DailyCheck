import datetime


class WinDefender:
    def __init__(self):
        self.file = self.config("path")
        day = self.config("day")
        self.date = (datetime.date.today() - datetime.timedelta(days=day)).strftime('%Y-%m-%d %H:%M:%S')
        self.result = ""

    @staticmethod
    def config(flag):
        from conf.config import Config
        return Config().win_defender(flag)

    def get_wdef(self) -> str:
        import Evtx.Evtx as evtx
        from bs4 import BeautifulSoup
        try:
            with evtx.Evtx(self.file) as log:
                flag_update = 0
                flag_check = 0
                for wdef in log.records():
                    soup = BeautifulSoup(wdef.xml(), "lxml")
                    time = datetime.datetime.strptime(soup.timecreated.attrs.get('systemtime'),
                                                         '%Y-%m-%d %H:%M:%S.%f') + datetime.timedelta(hours=9)
                    time = time.strftime('%Y-%m-%d %H:%M:%S')
                    if time > self.date:
                        eventid = soup.eventid.string
                        if eventid == '1001':
                            flag_update = 1
                        elif eventid == '2000':
                            flag_check = 1
                self.result = "정상" if flag_update == 1 and flag_check == 1 \
                    else "정의 업데이트 필요" if flag_update == 1 and flag_check != 1 \
                    else "검사 필요" if flag_update != 1 and flag_check == 1 \
                    else "오류"
        except FileNotFoundError:
            self.result = "FileNotFound"
        return self.result