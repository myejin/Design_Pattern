from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


class ForestFactory:
    """직접 클래스를 호출하지 않고 여러 타입의 객체를 생성할 수 있다."""

    def make_sound(self, object_type):
        return eval(object_type)().do_say()


if __name__ == "__main__":
    ff = ForestFactory()
    animal = input("어느 동물 울음소리를 만들까요? (Dog 또는 Cat) ")
    ff.make_sound(animal)
