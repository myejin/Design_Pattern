class Subject:
    def __init__(self):
        """
        옵서버 목록 유지
        서브젝트의 핵심부분 캡슐화
        """
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer1:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ":: Got", args, "From", subject)


class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ":: Got", args, "From", subject)


if __name__ == "__main__":
    subject = Subject()
    observer1 = Observer1(subject)
    observer2 = Observer2(subject)
    subject.notifyAll("notification")
