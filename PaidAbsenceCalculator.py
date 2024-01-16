from Absence import Absence
from Date import Date
from Worker import Worker

YOUNG_ADULT_PAID_LEAVE_DAYS = 33
ELDERLY_PAID_LEAVE_DAYS = 14

class PaidAbsenceCalculator:
    maxPaidSickDays = 0
    totalAbsentDays = 0
    paidSickDays = 0
    paidGrant = 0
    calculatedPeriod = Absence("00.00.0000", "00.00.0000")
    
    
    @staticmethod
    def setMaxPaidSickDays(birthString: str):
        birth = Date(birthString)
        PaidAbsenceCalculator.maxPaidSickDays = ELDERLY_PAID_LEAVE_DAYS if (
            (PaidAbsenceCalculator.calculatedPeriod.absenceBeginning.year - birth.year) >= 51) else YOUNG_ADULT_PAID_LEAVE_DAYS

    @staticmethod
    def calculateAbsenceDays(absenceList: list):
        PaidAbsenceCalculator.totalAbsentDays = 0
        PaidAbsenceCalculator.paidSickDays = 0
        PaidAbsenceCalculator.paidGrant = 0

        leftPaidSickDays = PaidAbsenceCalculator.maxPaidSickDays

        for absence in absenceList:
            isBeginningDateDuringCalculationPeriod = PaidAbsenceCalculator.calculatedPeriod.absenceBeginning < absence.absenceEnding
            isEndingDateDuringCalculationPeriod = PaidAbsenceCalculator.calculatedPeriod.absenceEnding > absence.absenceBeginning

            if (not isBeginningDateDuringCalculationPeriod):
                # częśc nie zawarta w liczonym okresie, ale liczy sie do maxPaidSickDays
                result = absence.absenceEnding - absence.absenceBeginning
                leftPaidSickDays -= result
                PaidAbsenceCalculator.maxPaidSickDays -= result
                if (PaidAbsenceCalculator.maxPaidSickDays < 0):
                    PaidAbsenceCalculator.maxPaidSickDays = 0
                if (leftPaidSickDays < 0):
                    leftPaidSickDays = 0
                continue

            if (isBeginningDateDuringCalculationPeriod and isEndingDateDuringCalculationPeriod):
                # częśc nie zawarta w liczonym okresie, ale liczy sie do maxPaidSickDays
                if (absence.absenceBeginning < PaidAbsenceCalculator.calculatedPeriod.absenceBeginning):
                    result = PaidAbsenceCalculator.calculatedPeriod.absenceBeginning - \
                        absence.absenceBeginning
                    leftPaidSickDays -= result
                    PaidAbsenceCalculator.maxPaidSickDays -= result
                    if (leftPaidSickDays < 0):
                        leftPaidSickDays = 0
                    if (PaidAbsenceCalculator.maxPaidSickDays < 0):
                        PaidAbsenceCalculator.maxPaidSickDays = 0
                    # dobrze
                    result = absence.absenceEnding - \
                        PaidAbsenceCalculator.calculatedPeriod.absenceBeginning
                    leftPaidSickDays -= result
                    PaidAbsenceCalculator.totalAbsentDays += result
                    if (leftPaidSickDays < 0):
                        PaidAbsenceCalculator.paidGrant += abs(
                            leftPaidSickDays)
                        leftPaidSickDays = 0
                    continue

                # częśc  zawarta w liczonym okresie, ale bez części wykraczającej poza okres
                elif (absence.absenceEnding > PaidAbsenceCalculator.calculatedPeriod.absenceEnding):
                    result = PaidAbsenceCalculator.calculatedPeriod.absenceEnding - absence.absenceBeginning
                    leftPaidSickDays -= result
                    PaidAbsenceCalculator.totalAbsentDays += result
                    if (leftPaidSickDays < 0):
                        PaidAbsenceCalculator.paidGrant += abs(
                            leftPaidSickDays)
                        leftPaidSickDays = 0
                    continue
                # częśc zawarta całkowicie w liczonym okresie
                else:
                    result = absence.absenceEnding - absence.absenceBeginning
                    leftPaidSickDays -= result
                    PaidAbsenceCalculator.totalAbsentDays += result
                    if (leftPaidSickDays < 0):
                        PaidAbsenceCalculator.paidGrant += abs(
                            leftPaidSickDays)
                        leftPaidSickDays = 0
                    continue

        if (leftPaidSickDays > 0):
            PaidAbsenceCalculator.paidSickDays = abs(
                PaidAbsenceCalculator.maxPaidSickDays - leftPaidSickDays)
        else:
            PaidAbsenceCalculator.paidSickDays = PaidAbsenceCalculator.maxPaidSickDays
