from data_storege import load_contract

def search_contract(query):
    contracts = load_contract()
    result = []
    for contract in contracts:
        if query in contract['name'].lower() or query in contract['address'].lower() or query in contract['phone_num'] or query in contract['date_of_birth'] or query in contract['nationality'].lower():
            result.append(contract)
    print("Search result:\n")
    for i, contract in enumerate(result, start=1):
        print(f"""{i}. Name: {contract['name']} Email: {contract['email']} Phone Number: {contract['phone_num']} Address: {contract['address']} Date of Birth: {contract['date_of_birth']} Nationality: {contract['nationality']}""")
