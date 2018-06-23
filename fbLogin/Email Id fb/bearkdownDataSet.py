import csv
import codecs

def saveToFile(filename, data):
    print("going to create : " + filename + " with length of data : "+str(len(data)))
    with open(filename, 'a') as csvfile:
        fieldnames =['user'];
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for entries in data:
            writer.writerow(entries)

index = 1
dataSet = []
filename = 'Man_Email/Man_Email'
with codecs.open(filename + '.csv', encoding='iso-8859-1') as csvfile:
    textReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    print("******")
    for row in textReader:
        #print(row)
        if len(row) > 0 :
            if len(row[0]) > 0 :
                dataSet.append({"user":row[0].encode('utf-8')})
                if len(dataSet) > 20000:
                    fname = filename + "_dataset_" + str(index) + ".csv"
                    saveToFile(fname, dataSet)
                    dataSet = []
                    index +=1

    fname = filename + "_dataset_" + str(index) + ".csv"
    saveToFile(fname, dataSet)
                    
                    
