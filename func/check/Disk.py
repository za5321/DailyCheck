class Disk:
    def __init__(self, letter: str):
        self.letter = letter

    def get_disk(self) -> str:
        import shutil
        try:
            usage = shutil.disk_usage(self.letter)
        except FileNotFoundError:
            return "NODATA"
        else:
            percent = int(100 - (usage.free / usage.total * 100))
            return f"{percent}%"
