class NewsPublisher:
    """뉴스 게시자, 서브젝터"""

    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        """옵서버 등록"""
        self.__subscribers.append(subscriber)

    def detach(self):
        """옵서버 등록 취소"""
        return self.__subscribers.pop()

    def subscribers(self):
        """구독자 목록 반환"""
        return [type(s).__name__ for s in self.__subscribers]

    def notifySubscribers(self):
        """모든 구독자에게 알림을 보낸다."""
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        """새 뉴스 등록"""
        self.__latestNews = news

    def getNews(self):
        """최신뉴스 확인"""
        return "Got News:", self.__latestNews
