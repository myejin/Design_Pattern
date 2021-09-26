class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """객체를 생성할 때 호출되는 메소드"""
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()

    print(MetaSingleton._instances)
    print(logger1)
    print(logger2)
