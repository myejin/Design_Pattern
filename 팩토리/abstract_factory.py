from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()


class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self):
        pass


class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)


class ChickenPizza(NonVegPizza):
    def serve(self, VegPizza):
        """인자로 받은 VegPizza 에 Chicken을 올려 피자를 완성한다."""
        print(type(self).__name__, "is served with Chicken on", type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        """인자로 받은 VegPizza 에 Ham을 올려 피자를 완성한다."""
        print(type(self).__name__, "is served with Ham on ", type(VegPizza).__name__)


class PizzaStore:
    def __init__(self, factory_list):
        self.factory_list = factory_list

    def makePizzas(self):
        for factory in self.factory_list:
            self.factory = eval(factory + "PizzaFactory")()
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


##### 추상팩토리패턴의 효용성, 위 코드는 변경하지 않고 한국공장과 피자정보 클래스만 새로 구현 #####
class KoreanPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return SeoulVegPizza()

    def createNonVegPizza(self):
        return SalmonPizza()


class SeoulVegPizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)


class SalmonPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, "is served with Salmon on ", type(VegPizza).__name__)


if __name__ == "__main__":
    store1 = PizzaStore(["Indian", "US"])
    store1.makePizzas()
    store2 = PizzaStore(["Indian", "US", "Korean"])
    store2.makePizzas()
