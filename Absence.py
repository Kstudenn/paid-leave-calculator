from Date import Date


class Absence:
    def __init__(self, stringBeginning, stringEnding):
        self.absenceBeginning = Date(stringBeginning)
        self.absenceEnding = Date(stringEnding)
