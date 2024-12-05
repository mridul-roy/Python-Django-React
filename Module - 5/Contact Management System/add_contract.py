from data_storege import save_contract, load_contract

def add_contract(name, email, phone_num, address, date_of_birth, nationality):
    contracts = load_contract()

    for contract in contracts:
        if contract['phone_num'] == phone_num:
            print("This phone number is already assigned to another contact.")
            return

    contract = {
        'name': name,
        'email': email,
        'phone_num': phone_num,
        'address': address,
        'date_of_birth': date_of_birth,
        'nationality': nationality           
    }
    contracts.append(contract)

    save_contract(contracts)
    print("Contract added successfully.")

