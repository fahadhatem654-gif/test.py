# print("==== Player Info ====")
# name = input("Enter Your Name : ")
# age = int(input("Enter Your Age : "))
# city = input("Enter Your City : ")
# job = input("Enter Your Job : ")

# print(" ")
# print(" ")

# print(f"Welcome {name.upper()} the Brave from {city} who works as {job.capitalize()}!")
# print(f"{name} the brave from {city} who works as {job}!")
# print(f"{name.capitalize()} the Brave from {city.capitalize()} who works as {job.capitalize()}!")
# print(f"Length of name : {len(name)}")
# print(f"Number of 'a' in name : {name.count('a')}")
# print(f"Name afetr replace : {name.replace('a' , '@')}")
# print(" ")

# print(f"==== Health & Stats ====")
health = 100
mana = 50
# damage = int(input("Input : damage = "))
# potion = int(input("Input : Potion = "))
# x = health - damage
# x1 = health + potion
# print(f"Health after damage : {x}")
# print(f"Health after potion : {x1}")
# print(f"Max Health : {max(health , x)}")
# print(f"Min Health : {min(health , x)}")
# print(f"Rounded Mana : {round(mana)}")
# print(" ")
# print("==== Battle Decisions ====")
# if health > 50 : 
#     print('You are strong!')
#     if health == 50 :
#         print("Number are equal")
#     elif health < 20 :
#         print("Danger Heal soon")    
# elif health < 50:
#     print("Second number is bigger")
# print(" ")
# print("==== Inventory (List) ====")
# list_Inventory = ['sword' , 'shield' , 'potion' ]
# print(f"Input : initial inventory = {list_Inventory}")
# added_item = input("Added item : ")   
# added_items = input(f"Added items : ") 
# list_Inventory.append(added_item)
# list_Inventory.append(added_items)
# list_Inventory.pop()
# print(f"Inventory Length : {len(list_Inventory)}")
# print(f"Count of 'potion' : {list_Inventory.count('potion')} ")
# print(f"Min item : {min(list_Inventory)}")
# print(f"Max item : {max(list_Inventory)}")
# print(" ")
# print("==== Rare Item (Tuple) ====")
# Tuple_Rare = ('magic_ring' , 'dragon_egg' , 'crystal orb')
# print(f"Original rare item : {Tuple_Rare}")
# print(f"Total rare : {len(Tuple_Rare)}")
# print(f"Count of 'magic_ring' : {Tuple_Rare.count('magic_ring')}")
# print(f"Index of 'dargon_egg' : {Tuple_Rare.index('dargon_egg')}")
# list_rare = list(Tuple_Rare)
# list_rare.extend(["phoenix_feather" , "crystal_orb"])
# print(f"Rare items after conversion yo list and modification : \n {list_rare}")
# list_rare.remove('dragon_egg')
# list_rare.remove('crystal orb')
# Tuple_Rare = tuple(list_rare)
# print(f"Final rare items tuple : {Tuple_Rare}")
# print("==== Treasures (Set) ====")
# Set_Treasures = {"gold" , "Silver" , "dimaond" }
# Set_Treasures2 = {"emerald" , "pearl"}
# print(f"Original set : {Set_Treasures}")
# Set_Treasures.add('ruby')
# Set_Treasures.update({Set_Treasures2})
# print(f"Added ruby and updated 'emerald', 'pearl' : {Set_Treasures}")
# Set_Treasures.discard('pearl')
# print(f"After discard 'pearl' : {Set_Treasures}")
# print(f"Union with Set 1 and Set 2 : {Set_Treasures.union(Set_Treasures2)}")
# print(f"Intersection : {Set_Treasures.intersection(Set_Treasures2)}")
# print(f"Diffrence : {Set_Treasures.difference(Set_Treasures2)}")
# print(f"Symmetric differnce : {Set_Treasures.symmetric_difference(Set_Treasures2)}")
print(f" ")
print("==== Player Dictionary ====")
player_dict = {
    "name":"Alice" , 
    "age" : 25 , 
    "level":5 , 
    "health":100,
    "mana":50,
    
}
print(f"Original Player info : {player_dict}")
player_dict["status"]="active"
player_dict.pop("mana")
print(f"Upadated player Info : {player_dict}")
print(f"Keys : {player_dict.keys()}")
print(f"Values : {player_dict.values()}")
print(f"Item : {player_dict.items()}")




