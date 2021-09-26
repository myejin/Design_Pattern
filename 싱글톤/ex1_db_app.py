import sqlite3
from sqlite3.dbapi2 import connect


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    def connect(self):
        if not hasattr(self, "connection"):
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj


if __name__ == "__main__":
    db1 = Database().connect()
    print("[db1] 커서", db1, "커넥션", db1.connection)

    db2 = Database().connect()
    print("[db2] 커서", db2, "커넥션", db2.connection)
