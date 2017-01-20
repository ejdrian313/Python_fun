import csv


def main():
    a = input('Enter the name of file (without .csv) to make a map: ')
    z = input('Enter the name of map you want to create (without .txt): ')
    loadMap(a, z)
    
    
def loadMap(filename, mapname):
    mapFile = open(filename + '.csv')
    mapReader = csv.reader(mapFile)
    
    count = 0
    new = open(mapname + '.txt', 'w')
    for row in mapReader:
        for each in row:
            if each == '#':
                new.write(each)
                new.write(str(count))
                count += 1
            elif each == ',':   #add more elif each == 'sign'
                count += 1      #to add different stuff etc.
            else:
                count +=1
        new.write('\n')
        count = 0
    new.close()
    mapFile.close()


if __name__ == "__main__":
    main()
