import json
# problem 1
givenList = [
	{ 'id': '0001', 'deleted': True },
	{ 'id': '0002', 'deleted': False },
    { 'id': '0003', 'deleted': False },
    { 'id': '0004', 'deleted': False }
]

# problem 2

givenObject = {
    'VALUE_1': True,
    'VALUE_2': False,
    'VALUE_3': True
}

listOfBanks = [
	{ 'id': 'VALUE_1', 'color': '#32a852', 'label': 'Permata' },
    { 'id': 'VALUE_2', 'color': '#f59b78', 'label': 'Mandiri' },
    { 'id': 'VALUE_3', 'color': '#f67c12', 'label': 'BCA' }
]

'''
Return list of banks that only has id in selection is True, in the example input above, the result would be:
'''


# problem 3

listofBankCode = [
	{ 'id': '0001', 'bankCode': '002', 'name': 'test01' },
    { 'id': '0002', 'bankCode': '008', 'name': 'test02' },
    { 'id': '0003', 'bankCode': '009', 'name': 'test03' }
]

listOfIds = ['0001', '0003']



# Problem 4

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



# list parent


listParentandChild = [
	{ 'id': '001', 'title': 'Label 01', 'parent': None, 'children': ['002', '003'] },
	{ 'id': '002', 'title': 'Label 02', 'parent': '001', 'children': ['004'] },
	{ 'id': '003', 'title': 'Label 03', 'parent': '001', 'children': [] },
	{ 'id': '004', 'title': 'Label 04', 'parent': '002', 'children': [] },
	{ 'id': '005', 'title': 'Label 05', 'parent': None, 'children': [] }
]



class App:
    def __init__(self):
        pass
    
    # problem 1 answer
    def undeleted(self, givenList):
        return [id['id'] for id in givenList if not id['deleted']]
    
    # problem 2 answer
    def bankSelector(self, givenObject, listOfBanks):
        # banks = [] 
        # for bank in listOfBanks:
        #     if bank['id'] in givenObject:
        #         if givenObject[bank['id']]:
        #             banks.append(bank)
        return [bank for bank in listOfBanks if givenObject.get(bank['id'])]
    
    # problem 3 answer
    def bankSelectorbyCode(self, listOfIds, listofBankCode):
        return [bankcode for bankcode in listofBankCode if bankcode['id'] in listOfIds]
    
    # problem 4 answer
    def buyerMapper(self, userList, buyerList):
        usermap = {}
        for user in userList:
            usermap[user['user_id']] = user
        buyerandProductList = []
        for buyer in buyerList:
            buyerandProductList.append({
                'buyer' : usermap.get(buyer['buyer']),
                'name' : buyer['name'],
                'price' : buyer['price'],
            })

        return buyerandProductList
    
    # problem 5 answer   
    def parentChildTree(self, obj):
        objCopy = obj.copy()
        objwithkey = {}
        for o in obj:
            objwithkey[o['id']] = o
        for ob, res in zip(obj, objCopy):
            if ob['children'] != []:
                childs = ob['children'].copy()
                for ind, child in enumerate(childs):
                    res['children'][ind] = objwithkey[child]
        return [parent for parent in objCopy if parent['parent'] == None]



                        




app = App()

# answer of problem 1
print(app.undeleted(givenList))
# answer of problem 2
print(app.bankSelector(givenObject, listOfBanks))
# answer of problem 3
print(app.bankSelectorbyCode(listOfIds, listofBankCode))
# answer of problem 4
print(app.buyerMapper(userList, buyerList))
# answer of problem 5
print(app.parentChildTree(listParentandChild))