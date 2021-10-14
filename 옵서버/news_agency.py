from news_publisher import NewsPublisher
from subscriber import SMSSubscriber, EmailSubscriber, AnyOtherSubscriber

if __name__ == "__main__":
    news_publisher = NewsPublisher()
    print("[구독자 등록]")
    for Sub in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Sub(news_publisher)
    print("구독자 목록 :", news_publisher.subscribers())
    print()

    news_publisher.addNews("안녕하세요!")
    news_publisher.notifySubscribers()

    print("\n구독 취소자 : ", type(news_publisher.detach()).__name__)
    print("구독자 목록 : ", news_publisher.subscribers())
    print()

    news_publisher.addNews("두번째 뉴스입니다.")
    news_publisher.notifySubscribers()
