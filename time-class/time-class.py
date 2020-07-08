import math


class AbstractTime:
    hrs = 0
    mins = 0
    secs = 0

    def __init__(self, hrs=0, mins=0, secs=0):
        self.hrs = hrs
        self.mins = mins
        self.secs = secs



class Time(AbstractTime):

    def scale(self, addSecs):
        return self.normalising(self.hrs, self.mins, self.secs + addSecs)

        # return self.secs + addSecs, self.mins, self.hrs


    def normalising(self, hrs, mins, secs):
        # print(self.normalising_helper(self.secs, 's'))
        returnDict = self.normalising_helper(secs, 's')
        self.secs = returnDict.get('forThis')

        if 'forNext' in returnDict:
            returnDict = self.normalising_helper(mins + returnDict.get('forNext'), 'm')
        else:
            returnDict = self.normalising_helper(mins, 'm')
        self.mins = returnDict.get('forThis')

        if 'forNext' in returnDict:
            returnDict = self.normalising_helper(hrs + returnDict.get('forNext'), 'h')
        else: 
            returnDict = self.normalising_helper(hrs, 'h')
        self.hrs = returnDict.get('forThis')

        # return self.hrs, self.mins, self.secs



    def normalising_helper(self, inputNum, inputType):
        boundaryUpper = 0
        returnDict = {}

        if inputType == 's':
            boundaryUpper = 60
        elif inputType == 'm':
            boundaryUpper = 60
        elif inputType == 'h':
            boundaryUpper = 24

        if inputNum >= boundaryUpper:
            forNext = inputNum / boundaryUpper
            forThis = inputNum % boundaryUpper
            returnDict.update({'forNext': math.floor(forNext)})
            returnDict.update({'forThis': forThis})
        else:
            forThis = inputNum % boundaryUpper
            returnDict.update({'forThis': forThis})


        return returnDict


    def timeString(self):
        returnString = ''
        returnString = self.add_zero(self.hrs) + ':' + self.add_zero(self.mins) + ':' + self.add_zero(self.secs)

        return str(returnString)


    def add_zero(self, inputNum):
        returnString = str(inputNum)
        if inputNum < 10:
            returnString = '0' + returnString
        else: 
            return str(inputNum)

        return returnString









now = Time(2, 20, 100)
# print(now.timeString())
# print(now.normalising_helper(20, 'm'))
print(now.scale(500))
print(now.timeString())


