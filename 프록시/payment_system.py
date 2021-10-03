from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    """Subject"""

    @abstractmethod
    def do_pay(self):
        pass


class Bank(Payment):
    """RealSubject"""

    def __init__(self):
        self.card = None
        self.account = None

    def __getAccount(self):
        self.account = self.card  # 카드번호와 계좌번호가 같다고 가정
        return self.account

    def __hasFunds(self):
        print("Bank::", self.__getAccount(), "계좌에 충분한 돈이 있어요.")
        return True

    def setCard(self, card):
        self.card = card

    def do_pay(self):
        if self.__hasFunds():
            print("Bank:: 상품을 구매할게요.")
            return True
        else:
            print("Bank:: 잔액이 부족합니다.")
            return False


class DebitCard(Payment):
    """Proxy"""

    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Card(Proxy):: 카드번호를 입력하세요 : ")
        self.bank.setCard(card)
        return self.bank.do_pay()


class You:
    def __init__(self):
        """프록시를 호출, 생성한다."""
        print("You:: 셔츠를 하나 사야겠다.")
        self.debitCard = DebitCard()
        self.isPurchased = None

    def make_payment(self):
        """프록시의 메소드를 호출한다."""
        self.isPurchased = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurchased:
            print("You:: 예쁜 셔츠를 사서 너무 좋다.")
        else:
            print("You:: 돈을 더 모아야겠어..")


if __name__ == "__main__":
    you = You()
    you.make_payment()
