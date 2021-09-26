class Singleton:
    """인스턴스를 꼭 필요한 시점에 생성한다."""

    __instance = None

    def __init__(self):
        if Singleton.__instance is None:
            print("__init__ 메서드 호출.. 인스턴스는", Singleton.__instance)
        else:
            print("인스턴스 이미 존재해, 재사용할거야:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = Singleton()
            print("인스턴스를 이제서야 생성하고 이 인스턴스를 반환한다.")
        return cls.__instance


if __name__ == "__main__":
    s = Singleton()
    print("안녕")
    print("인스턴스 드디어 생성,", Singleton.getInstance())
    s1 = Singleton()
