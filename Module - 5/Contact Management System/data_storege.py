import json

def save_contract(contract):
    with open('contract_file.csv','w') as file:
        json.dump(contract,file,indent=4)
        
        
def load_contract():
    with open('contract_file.csv','r') as file:
        return json.load(file)