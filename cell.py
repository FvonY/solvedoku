class Cell():
    def __init__(self, value=None):
        if value is None:
            self.value = None
            self.possible = [i for i in range(1, 10)]
        else:
            self.value = value
            self.possible = []

    def checkSolved(self):
        if len(self.possible) == 1:
            self.value = self.possible[0]
            return True
        return False

    def getValueAsString(self):
        if self.value == 0 or self.value is None:
            return " "
        else:
            return f"{self.value}"
