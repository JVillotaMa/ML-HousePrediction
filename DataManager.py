from Analyzer import scatter
import csv 


def neigh_divider(full_list): ##Returns a dict that keys are neighborhood and values the data of the house
    toRet = {}
    for row in full_list:
        print(row)
        neig=row[1]
        if toRet.get(neig)==None:
            toRet[neig]=list()
            toRet.get(neig).append(row)
        else: toRet.get(toRet.get(neig).append(row))
    return toRet

def openCSV(fileName):
    with open(fileName, newline='') as csvfile:
        reader = list(csv.reader(csvfile, delimiter=';', quotechar='|'))
        return neigh_divider(reader)

def addFreatures(input,objective):
    with open(input, newline='') as input_file:
       with open(objective, newline='') as objective_file:
        with open('data/generated_output.csv',mode='w+',newline='') as output:
            reader_input = list(csv.reader(input_file, delimiter=';', quotechar='|'))
            reader_objective = list(csv.reader(objective_file, delimiter=';', quotechar='|'))
            output_writer = csv.writer(output, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row_input in reader_input:
                for row_objective in reader_objective:
                    if row_input[0]==row_objective[0]:
                        output_writer.writerow(row_objective+row_input[1:])
                        

def differentNeigh(fileName):
    with open(fileName, newline='') as csvfile:
        reader = list(csv.reader(csvfile, delimiter=';', quotechar='|'))
        toRet = set()
        for row in reader:
            toRet.add(row[1])
        return list(toRet)

differentNeigh('data/generated_output.csv')