class EventLog:
    def __init__(self):
        import datetime
        self.date = (datetime.date.today() - datetime.timedelta(days=3, hours=9)).strftime('%Y-%m-%d %H:%M:%S')
        self.path: list = self.config()
        self.results: dict = {}

    @staticmethod
    def config() -> list:
        from conf.config import Config
        return Config().event("path")

    def get_event(self) -> dict:
        files: list = self.config()
        for i, file in enumerate(files):
            text = ["app", "secu", "sys"][i]
            self.results[text] = self.check_event(file)
        return self.results

    def check_event(self, file: str) -> str:
        from Evtx import Evtx as evtx, BinaryParser as BinaryParser
        from bs4 import BeautifulSoup
        count = 0
        result = ""
        try:
            with evtx.Evtx(file) as log:
                for evt in log.records():
                    try:
                        soup = BeautifulSoup(evt.xml(), "lxml")
                        time = soup.timecreated.attrs.get('systemtime')
                        level = soup.level.get_text()
                    except UnicodeDecodeError:
                        break
                    except BinaryParser.ParseException:
                        continue
                    else:
                        if time > self.date and level in ['1', '2', '3']:
                            count += 1
                            result += f"<event{count}>"
                            result += str(soup).replace("<html><body>", "").replace("</body></html>", "")
                            result += f"</event{count}>"
                        elif time < self.date and count > 0:
                            break
                        else:
                            continue

            result = result.replace("<html><body>", "").replace("</body></html>", "")
        except FileNotFoundError:
            result = "FileNotFound"
        return result
