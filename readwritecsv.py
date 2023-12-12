import csv
import os


path = os.getcwd()


#function write
def writecsv(data):
    csvfile = os.path.join(path,'file.csv')
    with open(csvfile,'a',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(data)


#fucntion read
def readcsv():
    with open('file.csv',newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
        return data


