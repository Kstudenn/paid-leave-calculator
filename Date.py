from calendar import monthrange

class Date:
    def __init__(self, string):
        self.day = int(string[0:2])
        self.month = int(string[3:5])
        self.year = int(string[6:])

    def __str__(self):
        return str(self.day)+"."+str(self.month)+"."+str(self.year)

    def __sub__(self, other):
        selfDays = 0
        otherDays = 0
        for month in range(other.month-1):
            otherDays += monthrange(other.year,month+1)[1]
        otherDays += other.day
        for month in range(self.month-1):
            selfDays += monthrange(self.year,month+1)[1]
        selfDays += self.day
        return abs(selfDays-otherDays)

    def __lt__(self, other):
        if (self.year == other.year):
            if (self.month == other.month):
                if (self.day < other.day):
                    return True
                else:
                    return False
            if (self.month < other.month):
                return True
            else:
                return False
        elif (self.year < other.year):
            return True

    def __gt__(self, other):
        return not (self < other)
