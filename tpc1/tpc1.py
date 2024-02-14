import sys

class EMD_DTO:
    #_id,nome/primeiro,nome/último,idade,modalidade,resultado    

    def __init__(self,
                 _id: str,
                 first_name: str,
                 last_name: str,
                 age: int,
                 category: str,
                 result: bool):
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.category = category
        self.result = result

    
def populate_emd () -> list[EMD_DTO]:
    emd = []
    sys.stdin.readline() #Used to skip the csv header
    for line in sys.stdin:
        emd.append(parseLine(line.strip().split(',')))
    return emd

def parseLine (values: list[str]) -> EMD_DTO:
    return EMD_DTO(values[0],
                   values[3],
                   values[4],
                   int(values[5]),
                   values[8],
                   values[12] == 'true')

def write_csv(file_name: str, data: list[list[str]]):
    with open(file_name, 'w', encoding='utf-8') as file:
        for row in data:
            file.write(','.join(row) + '\n')

def category_csv(emd: list[EMD_DTO]):
    data = [['modalidade']]
    categories = sorted(set([e.category for e in emd]))  # Get unique categories and sort them
    for category in categories:
        data.append([category])  # Append each category as a separate list. This is done to use the generic "write_csv" function
    write_csv('modalidades_ordenadas.csv', data)

def apt_csv(emd: list[EMD_DTO]):
    data = [['aptos,inaptos']]
    total = float(len(emd))
    total_apt = len(['dummy' for e in emd if e.result])
    apt_percentage = total_apt / total * 100
    inapt_percentage = 100 - apt_percentage
    data.append([str(apt_percentage), str(inapt_percentage)])
    write_csv('aptos_inaptos_percentagem.csv', data)

def age_group_csv(emd: list[EMD_DTO], delta=5):
    data = [['_id','nome/primeiro','nome/último','idade','escalão etário']]
    ordered_by_age = sorted(emd, key=lambda x: x.age)
    for e in ordered_by_age:
        lower_bound = (e.age // delta) * delta
        upper_bound = lower_bound + (delta - 1)
        interval = f'[{lower_bound}-{upper_bound}]' 
        data.append([e.id,e.first_name,e.last_name,str(e.age),interval])
    write_csv('escalões_etários.csv', data)



def main ():
    emd = populate_emd()
    category_csv(emd)
    apt_csv(emd)
    age_group_csv(emd)

if __name__ == '__main__':
    main()
    