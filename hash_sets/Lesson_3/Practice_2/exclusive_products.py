"""

You manage inventories for two stores, inventory1 and inventory2. 
Find the exclusive items for each store, ignoring case, and return 
them sorted alphabetically.

"""
def exclusive_products(inventory1, inventory2):
         
    inv_1 = [item.upper() for item in inventory1]
    inv_2 = [item.upper() for item in inventory2]
        
    set_inv_1 = set(inv_1)
    set_inv_2 = set(inv_2)
    
    result_1 = list(set_inv_1 - set_inv_2)
    result_2 = list(set_inv_2 - set_inv_1)
    
    result_1.sort()
    result_2.sort()
    
    return result_1, result_2
    
inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]



inventory1 = ["Shirt", "Jeans", "Hat"]
inventory2 = ["jeans", "Belt", "Boots"]
print(exclusive_products(inventory1, inventory2))
# Expected output: (['HAT', 'SHIRT'], ['BELT', 'BOOTS'])

inventory1 = ["T-Shirt", "hoodie", "Backpack"]
inventory2 = ["Backpack", "Hoodie", "t-shirt"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], [])

inventory1 = []
inventory2 = ["Dress", "Skirt", "Coat"]
print(exclusive_products(inventory1, inventory2))
# Expected output: ([], ['COAT', 'DRESS', 'SKIRT'])