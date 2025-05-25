print('NAME:basavanagouda.y' ,'USN:1AY24AI017')
#fantasy game inventory.py
inventory={
    'sword':2,
    'shield':1,
    'healingposition':5,
    'gold coin':100
    }
def display_inventory(inv):
    print("inventory:")
    total_items=0
    for item,count in inv.items():
        print(f"{count} x {item}")
        total_items+=count
    print(f"\ntotal number of items:{total_items}")
display_inventory(inventory)
