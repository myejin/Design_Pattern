class Borg1:
    """모든 객체가 같은 상태를 공유하는 패턴"""

    __shared_state = {"1": "2"}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.x = 1


class Borg2(object):
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        """인스턴스를 생성하는 메소드"""
        obj = super(Borg2, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


if __name__ == "__main__":
    b = Borg1()
    b1 = Borg1()
    b.y = 4

    # __dict__ : 인스턴스에 할당된 인스턴스 속성 출력
    print("Borg1 b : ", b, b.__dict__)
    print("Borg1 b1 : ", b1, b1.__dict__)

    b = Borg2()
    b1 = Borg2()
    b.x = 4

    print("Borg2 b : ", b, b.__dict__)
    print("Borg2 b1 : ", b1, b1.__dict__)
