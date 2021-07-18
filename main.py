from geopy.geocoders import Nominatim
import random


locator = Nominatim(user_agent="myGeocoder")

randomGeocodeNumber = 1000


def generateRandomAddressList():

    randomAdress = [None] * randomGeocodeNumber

    for i in range(0, randomGeocodeNumber):
        randomAdress[i] = generateRandomAddress()

    return randomAdress


def generateRandomAddress():

    itemList = []

    randomLat = random.uniform(41.105, 41.118)
    randomLong = random.uniform(29.004, 29.028)

    location = locator.reverse(str(randomLat) + "," + str(randomLong))

    itemList.append(randomLat)
    itemList.append(randomLong)
    itemList.append(location.address)
    itemList.append("https://maps.google.com/?q=" + location.address)


    return itemList


def printPart1(randomAdress):

    print("\n\n//////////////////////////////////////   PART 1   //////////////////////////////////////\n\n")

    for itemNumber in range(randomGeocodeNumber):
        print("item#" + str(itemNumber + 1) + " " + str(randomAdress[itemNumber][0]) + "," + str(randomAdress[itemNumber][1]) + ", " + str(randomAdress[itemNumber][2]) + ", " + str(randomAdress[itemNumber][3]))


def printPart3(randomAdress, Cells):

    print("\n\n//////////////////////////////////////   PART 3   //////////////////////////////////////\n\n")

    cellNumbers = {}

    for itemNumber in range(randomGeocodeNumber):
        cellNumbers[itemNumber] = findCellNumber(randomAdress[itemNumber][0], randomAdress[itemNumber][1], Cells)

    sortedCellNumbers = sorted(cellNumbers.items(), key=lambda x: (x[1], x[0]), reverse=False)

    for numbers in sortedCellNumbers:
        print("item#" + str(numbers[0] + 1) + " " + str(randomAdress[numbers[0]][0]) + "," + str(randomAdress[numbers[0]][1]) + ", " + str(randomAdress[numbers[0]][2]) + ", " + "hücre#no" + str(numbers[1]) + ", " + str(randomAdress[numbers[0]][3]))


def generateCell():

    # maslak bölgesinin köşe koordinatları
    leftmostLongitude = 29.003065
    rightmostLongitude = 29.028883
    upmostLatitude = 41.121186
    undermostLatitude = 41.104038

    latitudeLength = 111000
    longitudeLength = 111321

    cellLatitude = (1 / latitudeLength) * 500
    cellLongitude = (1 / longitudeLength) * 500

    cellNumber = 1

    Cells = {}

    while(upmostLatitude > undermostLatitude - cellLatitude):

        while (leftmostLongitude < rightmostLongitude + cellLongitude):

            Cells[cellNumber] = {
                "leftmostLongitude": leftmostLongitude,
                "rightmostLongitude": leftmostLongitude + cellLongitude,
                "upmostLatitude": upmostLatitude,
                "undermostLatitude": upmostLatitude - cellLatitude
            }
            cellNumber += 1
            leftmostLongitude += cellLongitude

        leftmostLongitude = 29.003065

        upmostLatitude -= cellLatitude


    return Cells


def findCellNumber(latitude, longitude, Cells):

    cellKeys = Cells.keys()

    for cellNumber in cellKeys:

        if Cells[cellNumber]["leftmostLongitude"] <= longitude <= Cells[cellNumber]["rightmostLongitude"] and \
                Cells[cellNumber]["upmostLatitude"] >= latitude >= Cells[cellNumber]["undermostLatitude"]:

            return cellNumber


def main():

    randomAdress = generateRandomAddressList()

    printPart1(randomAdress)

    Cells = generateCell()

    printPart3(randomAdress, Cells)


if __name__ == '__main__':

    main()

