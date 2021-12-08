import psutil


class Service:
    def __init__(self, svc: str):
        self.svc = svc

    def get_svc(self) -> str:
        def is_service(svc):
            service = None
            service = psutil.win_service_get(svc)
            service = service.as_dict()
            return service
        try:
            service = is_service(self.svc)
        except psutil.NoSuchProcess:
            return "-1"
        else:
            return "1" if service and service["status"] == "running" else "0"
