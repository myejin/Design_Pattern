from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print("Personal Section")


class AlbumSection(Section):
    def describe(self):
        print("Album Section")


class PatentSection(Section):
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    def describe(self):
        print("Publication Section")


class Profile(metaclass=ABCMeta):
    """
    객체생성에 필요한 인터페이스 제공
    각 프로필에 들어갈 섹션에 대한 정보가 없다.
    서브클래스에 결정을 위임한다.
    """

    def __init__(self):
        self.sections = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        """팩토리 메소드"""
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):
    """
    ConcreteProduct를 생성하는 서브클래스1
    어떤 섹션(Product의 서브클래스)를 생성할지 결정한다.
    """

    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())


class facebook(Profile):
    """
    ConcreteProduct를 생성하는 서브클래스2
    어떤 섹션(Product의 서브클래스)를 생성할지 결정한다.
    """

    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


if __name__ == "__main__":
    # 서비스 종류에 따라 알맞은 내용을 포함하는 프로필을 생성하자.
    profile_type = input("어떤 프로필을 만들까요? (LinkedIn 또는 FaceBook) ")
    profile = eval(profile_type.lower())()
    print("프로필 생성..", type(profile).__name__)
    print("포함된 섹션들 --", profile.getSections())
