from data_storege import save_contract,load_contract

def remove_contract(index):
    contracts = load_contract()
    if 0<index<=len(contracts):
        del contracts[index-1]
        save_contract(contracts)
        print("Contract removed successfully.\n")
    else:
        print("Invalid Index")
        
    
    