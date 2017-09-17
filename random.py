from datetime import datetime

class RandomNumber:

    seed = datetime.now().timestamp()/2

    @staticmethod
    def getRandom(minnum,maxnum):
        # print('using Seed:', RandomNumber.seed)
        RandomNumber.seed = ((minnum + RandomNumber.seed)*maxnum)

        randomNumber = (RandomNumber.seed % (maxnum*2.2 + 1))

        # adjust for lower limit
        if randomNumber < minnum and randomNumber > (minnum+1)/2:
           randomNumber += minnum/2

        if randomNumber < minnum/2:
            randomNumber += minnum

        return int(randomNumber)


if __name__ == '__main__':

    result = []

    arrDict = {"higher":0, "lower":0}
    arrCalculate = {}
    minnum = 0
    maxnum = 10

    for i in range(0,int(100)):

        random_int = RandomNumber.getRandom(minnum,maxnum)
        result += [random_int]

        if random_int > int((minnum+maxnum)/2):
            arrDict["higher"] += 1
        else:
            arrDict["lower"] += 1

        if random_int < minnum:
            print(random_int)

    arrLen = len(result)

    for val in arrDict:
        print(val)
        percentage = (arrDict[val]/arrLen)*100

        arrCalculate[val] =percentage


    print(arrDict)

    print(arrCalculate)