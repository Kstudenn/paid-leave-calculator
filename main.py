from Absence import Absence
from Date import Date
from Worker import Worker
import PaidAbsenceCalculator as pdc

beginning = input("Please Enter time period for report (in year 2023 for default input).\n Enter starting date (dd.mm.yyyy): ")
ending = input("Enter ending date (dd.mm.yyyy): ")
#beginning = "01.01.2023"
#ending = "30.12.2023"

pdc.PaidAbsenceCalculator.calculatedPeriod = Absence(beginning, ending)
workersList = []

with open('input.csv', encoding="utf-8") as inputFile:

    for line in inputFile:
        newWorker = Worker(line.strip())
        contentTable = line.split(";")
        newAbsence = Absence(contentTable[5], contentTable[6])

        if (not [x for x in workersList if x.pesel == newWorker.pesel]):
            newWorker.absenceList.append(newAbsence)
            workersList.append(newWorker)
            continue

        for worker in workersList:
            if (worker == newWorker):
                worker.absenceList.append(newAbsence)

with open('raport.csv', 'w', encoding="utf-8") as outputFile:
    for worker in workersList:
        pdc.PaidAbsenceCalculator.setMaxPaidSickDays(worker.birth)
        # dobrze
        pdc.PaidAbsenceCalculator.calculateAbsenceDays(worker.absenceList)
        outputFile.write(str(worker) + ";" + worker.calculateAge() + ";" + str(pdc.PaidAbsenceCalculator.totalAbsentDays) +
                         ";" + str(pdc.PaidAbsenceCalculator.paidSickDays) + ";" + str(pdc.PaidAbsenceCalculator.paidGrant)+"\n")
