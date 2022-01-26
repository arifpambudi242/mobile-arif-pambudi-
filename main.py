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

# print(result)


'''
Problem 4
========
'''

# Given 2 inputs, list of users
userList = [
	{ 'user_id': 1, 'email': 'test@test.com' },
    { 'user_id': 2, 'email': 'test2@test.com' }
]

# And list of products
buyerList = [
	{ 'buyer': 1, 'name': 'iPhone', 'price': 21000000 },
    { 'buyer': 1, 'name': 'Samsung', 'price': 14000000 }
]

'''Assume list of users and list of products might be very large

Return list of products with user mapped as buyer, example result would be:

[
	{
'buyer': {
'user_id': 1,
'email': 'test@test.com'
},
'name': 'iPhone',
'price': 21000000
},
. . .
]
'''

result = [{'buyer' : user, 'name' : product['name'], 'price' : product['price']} for user, product in zip(userList, buyerList) if product['buyer'] == user['user_id']]
# print(result)


listParentandChild = [
	{ 'id': '001', 'title': 'Label 01', 'parent': None, 'children': ['002', '003'] },
	{ 'id': '002', 'title': 'Label 02', 'parent': '001', 'children': ['004'] },
	{ 'id': '003', 'title': 'Label 03', 'parent': '001', 'children': [] },
	{ 'id': '004', 'title': 'Label 04', 'parent': '002', 'children': [] },
	{ 'id': '005', 'title': 'Label 05', 'parent': None, 'children': [] }
]

parents = []
child = []
for parent in listParentandChild:
    if parent['parent'] != None:
        parent.append({
            'id' : 
        })


'''
[
	{
		id: “001”,
	title: “Label 01”,
	children: [
	{
	id: “002”,
	title: “Label 02”,
	children: [
	{
	id: “004”,
	title: “Label 004”,
	children : []
}
]
},
{
	id: “003”,
	title: “Label 03”,
	children: []
}
]
},
{
	id: “005”,
	title: “Label 05”,
	children: []
},
'''