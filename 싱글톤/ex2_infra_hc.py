class HealthCheck(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self._servers = []

    def addServer(self):
        self._servers.append("서버 1")
        self._servers.append("서버 2")
        self._servers.append("서버 3")
        self._servers.append("서버 4")

    def changeServer(self):
        self._servers.pop()
        self._servers.append("서버 5")


if __name__ == "__main__":
    hc1 = HealthCheck()
    hc2 = HealthCheck()

    hc1.addServer()
    print("헬스체크 스케줄링 (1)..")
    for i in range(4):
        print("Checking", hc1._servers[i])

    hc2.changeServer()
    print("헬스체크 스케줄링 (2)..")
    for i in range(4):
        print("Checking", hc2._servers[i])
