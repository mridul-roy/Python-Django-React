from data_storege import load_contract

def view_contract():
    contracts = load_contract()
    print("Saved Contracts:\n")
    for i, contract in enumerate(contracts, start=1):
        print(f"""{i}. Name: {contract['name']} Email: {contract['email']} Phone Number: {contract['phone_num']} Address: {contract['address']} Date of Birth: {contract['date_of_birth']} Nationality: {contract['nationality']}""")

