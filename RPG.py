ull_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    stats = {'STR': strength, 'INT': intelligence, 'CHA' : charisma} 
    for stat in stats.values():
      if not isinstance(stat, int):
        return "All stats should be integers" 
    for stat in stats.values():
      if stat < 1 :
        return "All stats should be no less than 1"    
    for stat in stats.values():
      if stat > 4 :   
        return "All stats should be no more than 4"
    if sum(stats.values() ) != 7:
        return "The character should start with 7 points"
    STR = strength*full_dot + (10-strength)*empty_dot 
    INT = intelligence*full_dot + (10-intelligence)*empty_dot
    CHA = charisma*full_dot + (10-charisma)*empty_dot
    return name + "\n" + "STR " + STR + "\n" + "INT " + INT + "\n" + "CHA " + CHA
def run_RPG():
   print("⚔️ Welcome to the RPG Character Creator! ⚔️")
   print("Rules:")
   print("- Name: max 10 characters, no spaces")
   print("- Stats: STR, INT, CHA (1 to 4)")
   print("- Total stat points must be exactly 7\n")
   name = input("Enter your character's name: ")
   strength = int(input("Enter your character's strength (1-4): "))
   intelligence = int(input("Enter your character's intelligence (1-4): "))
   charisma = int(input("Enter your character's charisma (1-4): "))
   print(create_character(name, strength, intelligence, charisma))
run_RPG()