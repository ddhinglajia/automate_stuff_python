def displayInventory(Inventory):
    print('Inventory:')
    totalItems=0
    for k,v in Inventory.items(): # for all the keys and values
        print( str(v) +' ' + str(k))
        totalItems = totalItems + v #adds total values for all the keys
    print('Total number of items: ' + str(totalItems))

def addToInventory(Inventory, toAddItems):
    
    for item in toAddItems: # things in the loot
        Inventory.setdefault(item,0) # to add any new item if there
        Inventory[item] +=1 # adds things to previos values
    return Inventory
        
        

playInv = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12} #dict

dragonloot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] #list


    

displayInventory(playInv)


playInv = addToInventory(playInv,dragonloot)
displayInventory(playInv)
