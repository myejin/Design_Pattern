class EventManager:
    def __init__(self):
        print("[EventManager] 안녕하세요. 이벤트를 대신 준비하겠습니다.")

    def arrange(self):
        """
        클라이언트와 subsystem을 분리하는 역할을 맡는다.
        컴퍼지션을 통해 subsystem을 생성한다.
        하지만 subsystem은 EventManager(퍼사드)의 존재도 모른다. (그냥 수행한다.)
        """
        print("[EventManager] 호텔리어 부르고..\n")
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        print("[EventManager] 플로리스트 부르고..\n")
        self.florist = Florist()
        self.florist.setFlowerRequirements()

        print("[EventManager] 케이터링 서비스 부르고..\n")
        self.caterer = Caterer()
        self.caterer.setCuisine()

        print("[EventManager] 음악가도 부르고..\n")
        self.musician = Musician()
        self.musician.setMusicType()

        print("[EventManager] 업체와 컨텍&준비 완료했습니다!")


class Hotelier:
    def __init__(self):
        print("!Hotelier! 호텔 예약이 필요하신가요?")

    def __isAvailable(self):
        print("!Hotelier! 이벤트 날 예약이 가능합니다!")
        return True

    def bookHotel(self):
        if self.__isAvailable():
            print("!Hotelier! 예약이 완료되었어요.\n")


class Florist:
    def __init__(self):
        print("!Florist! 이벤트용 꽃이 필요하신가요?")

    def setFlowerRequirements(self):
        print("!Florist! 카네이션, 장미, 튤립을 준비할게요.\n")


class Caterer:
    def __init__(self):
        print("!Caterer! 뷔페를 준비할까요?")

    def setCuisine(self):
        print("!Caterer! 중국, 일본, 서양 음식으로 준비하겠습니다.\n")


class Musician:
    def __init__(self):
        print("!Musician! 음악이 필요하신가요?")

    def setMusicType(self):
        print("!Musician! 재즈, 클래식이 연주될거에요.\n")


class You:
    def __init__(self):
        print("당신: 결혼 준비가 너무 어렵다..")

    def askEventManager(self):
        """
        EventManager를 인스턴스화한다.
        퍼사드 클래스가 인터페이스를 간소화하였기 때문에 arrange 매소드만 호출하면 된다.
        """
        print("당신: 이벤트 매니저를 고용해보자")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("당신: 감사합니다. 덕분에 이벤트 준비를 잘 마쳤어요!")


if __name__ == "__main__":
    you = You()
    you.askEventManager()
