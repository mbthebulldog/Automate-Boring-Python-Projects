def display_stuff(inventory):
    print('This yo stuff:')
    total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total += v
    print('Total: ' + str(total))

def addToStuff(inventory, added_items):
    for item in added_items:
        if item in inventory:
           inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

stuff = {'gold coin': 42, 'dagger': 1, 'rapier': 3}
dragon_loot = ['gold coin', 'filing cabinet', 'gold coin', 'rapier', 'meat stick', 'fireball', 'filing cabinet', 'gold coin', 'tasty cake', 'penis cup']
stuff = addToStuff(stuff, dragon_loot)
display_stuff(stuff)