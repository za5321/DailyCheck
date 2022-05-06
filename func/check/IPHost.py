def config() -> str:
    from conf.config import Config
    return Config().socket()


class IPHost:
    @staticmethod
    def get_hostname() -> str:
        import socket
        return socket.gethostname()

    @staticmethod
    def get_ip() -> str:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server: str = config()
        s.connect((server, 1))
        return s.getsockname()[0]
