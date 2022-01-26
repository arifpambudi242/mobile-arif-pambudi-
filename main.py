# # problem 1
# givenList = [
# 	{ 'id': '0001', 'deleted': True },
# 	{ 'id': '0002', 'deleted': False },
#     { 'id': '0003', 'deleted': False },
#     { 'id': '0004', 'deleted': False }
# ]

# # answer
# result = [id['id'] for id in givenList if not id['deleted']]


# problem 2

givenObject = {
    'VALUE_1': True,
    'VALUE_2': False,
    'VALUE_3': True
}

# And list of banks, eg:

listOfBanks = [
	{ 'id': 'VALUE_1', 'color': '#32a852', 'label': 'Permata' },
    { 'id': 'VALUE_2', 'color': '#f59b78', 'label': 'Mandiri' },
    { 'id': 'VALUE_3', 'color': '#f67c12', 'label': 'BCA' }
]

'''
Return list of banks that only has id in selection is True, in the example input above, the result would be:
'''


# Answer
selectedBanks = [bank for val , bank in zip(givenObject, listOfBanks) if givenObject[val]]
# print(selectedBanks)

# for val , bank in zip(givenObject, listOfBanks):




# problem 3

listofBankCode = [
	{ 'id': '0001', 'bankCode': '002', 'name': 'test01' },
    { 'id': '0002', 'bankCode': '008', 'name': 'test02' },
    { 'id': '0003', 'bankCode': '009', 'name': 'test03' }
]

listOfIds = ['0001', '0003']

# answer

result = [bankcode for bankcode in listofBankCode if bankcode['id'] in listOfIds]

print(result)


