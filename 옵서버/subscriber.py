from abc import ABCMeta, abstractmethod


class Subscriber(metaclass=ABCMeta):
    """구독자, 옵서버"""

    @abstractmethod
    def update(self):
        pass


class SMSSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)  # 임포트를 시켜야하나,,

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)  # 임포트를 시켜야하나,,

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class AnyOtherSubscriber:
    """옵서버와 서브젝트의 느슨한 관계를 나타내는 옵서버"""

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)  # 임포트를 시켜야하나,,

    def update(self):
        print(type(self).__name__, self.publisher.getNews())
