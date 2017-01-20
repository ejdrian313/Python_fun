import csv


def main():
    a = input('Podaj nazwę pliku .csv do wczytania mapy: ')
    loadMap(a)
    
    
def loadMap(name):
    mapFile = open(name + '.csv')
    mapReader = csv.reader(mapFile)
    
    count = 1
    new = open('maplevel1.txt', 'w')
    for row in mapReader:
        for each in row:
            if each == '#':
                new.write(each)
                new.write(str(count))
                count += 1
            elif each == ',':
                count += 1
            else:
                count +=1
        new.write('\n')
        count = 1
    new.close()
    mapFile.close()

    
main()
