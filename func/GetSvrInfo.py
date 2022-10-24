from conf.config import Config


class GetSvrInfo:
    def __init__(self):
        self.con = Config().db_connection()

    def get_svr_id(self, hostname: str, ip: str) -> int:
        cursor = self.con.cursor()
        sql = f"SELECT SERVERID FROM SERVER WITH(NOLOCK) WHERE HOSTNAME = '{hostname}' AND IP = '{ip}'"
        cursor.execute(sql)
        row = cursor.fetchone()
        return row[0] if row else -1

    def get_svr_info(self, serverid: int, flag: str) -> list:
        info = []

        cursor = self.con.cursor()
        sql = f"EXEC DC_SELECT_SERVER_INFO {str(serverid)}, {flag}"
        cursor.execute(sql)
        row = cursor.fetchone()
        while row:
            info.append(row[0])
            row = cursor.fetchone()
        return info
