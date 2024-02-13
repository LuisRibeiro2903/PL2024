import sys
import pdb

class EMD_DTO:

    #_id,nome/primeiro,nome/último,idade,modalidade,resultado    
    def __init__(self,
                 _id: str,
                 first_name: str,
                 last_name: str,
                 age: int,
                 category: str,
                 result: bool):
        self.id = _id,
        self.first_name = first_name,
        self.last_name = last_name,
        self.age = age,
        self.category = category,
        self.result = result

    
def populate_emd () -> list[EMD_DTO]:
    pdb.set_trace()
    emd = []
    sys.stdin.readline() #Used to skip the csv header
    for line in sys.stdin:
        emd.append(parseLine(line.strip().split(',')))

def parseLine (values : list[str]):
    return EMD_DTO(values[0],
                   values[3],
                   values[4],
                   int(values[5]),
                   values[8],
                   values[12] == 'true')


def category_csv(emd : list[EMD_DTO]):
    data = [['modalidade']]
    tmp = [e.category for e in emd]
    print(tmp)

def aptos_csv(aptos, entradas):
    percentagem_aptos = (aptos / entradas) * 100
    print("Atletas aptos: " + str(percentagem_aptos) + "%")
    print("Atletas inaptos: " + str(100 - percentagem_aptos) + "%")


def main ():
    emd = populate_emd()
    category_csv(emd)

if __name__ == '__main__':
    main()
    