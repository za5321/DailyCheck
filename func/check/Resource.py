class Resource:
    def __init__(self):
        self.mem = self.get_mem()
        self.cpu = self.get_cpu()

    @staticmethod
    def get_mem() -> str:
        import psutil
        return str(psutil.virtual_memory().percent)

    @staticmethod
    def get_cpu() -> str:
        import subprocess

        cmd: list = ["wmic", "cpu", "get", "loadpercentage"]
        fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout
        data = fd_popen.read().strip().decode('utf-8')
        fd_popen.close()
        return data[19:22].strip()
