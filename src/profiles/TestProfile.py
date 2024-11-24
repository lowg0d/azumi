import time

from ..managers import Mission


class Test(Mission):
    def __init__(self, data) -> None:
        super().__init__(data)

    def execute(self):
        while True:
            time.sleep(5)
            print("test")
