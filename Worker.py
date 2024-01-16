from Absence import Absence
from Date import Date

class Worker:
    def __init__(self,infoString:str):
        info = infoString.split(";")
        self.name = info[0]
        self.surname = info[1]
        self.pesel = info[2]
        self.birth = info[3]
        self.gender = info[4]
        self.absenceList = []
        
    def __str__(self):
        deli = ";"
        return self.name+deli+self.surname+deli+self.pesel+deli+self.birth+deli+self.gender
    
    def calculateAge(self)->str:
        birthDate = Date(self.birth)
        return str(self.absenceList[0].absenceBeginning.year - birthDate.year)
    
    def __eq__(self,other):
        return self.pesel == other.pesel

