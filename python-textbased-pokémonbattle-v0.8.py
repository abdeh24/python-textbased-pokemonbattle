import random

enemyhp = round(random.randint(15, 45))
yourhp = round(random.randint(15, 45))
yourmaxhp = yourhp

pokemontypearray = ["Charmeleon", "Wartortle", "Metapod", "Kakuna", "Ivysaur", "Pidgeotto"]
pokemontype = pokemontypearray[round(random.randint(0, 5))]
items = ["Fresh-Water", "Potion", "Full-Restore"]
youritems = [items[round(random.randint(0, 2))], items[round(random.randint(0, 2))]]
opts1 = ["Fight", "Stats", "Items", "Run"]
opts2 = ["Use", "Back"]

print("a Simple Text based Pokemon Fight")
print("By Ashari4803")
print("v0.8")
print("--------------------------------------")
print("!: A wild", pokemontype, "encountered!")
print()
print("?: Enemy Stats: HP=", enemyhp)
print("?: Your Stats: HP=", yourhp)
print()


turn = True #true is you, false is enemy
onmatch = True
onitems = False

while onmatch == True:
    if yourhp > yourmaxhp:
        yourhp = yourmaxhp
    if turn == True:
        if onitems == False:
            print("--------------------------------------")
            print("?: Action | Fight, Stats, Items, Run")
            print()
            option1 = input("$: ")
            print("--------------------------------------")
            print()
            if option1 == opts1[0]:
                damagedeal = round(random.randint(2, 15))
                print("!: You deal", damagedeal, "damage!")
                enemyhp -= damagedeal
                turn = False
                print()
            elif option1 == opts1[1]:
                print("?: Enemy Stats: HP=", enemyhp)
                print("?: Your Stats: HP=", yourhp)
                print()
            elif option1 == opts1[2]:
                print(youritems)
                print()
                print("?: Action | Use <item>, Back")
                onitems = True
                print()
            elif option1 == opts1[3]:
                chance = round(random.randint(1, 5))
                if chance == 5:
                    print("!: You got away! What a coward!")
                    onmatch = False
                else:
                    print("!: You failed to escape!")
                    turn = False
                print()
            else:
                print("!: Invalid Action!")
        else:
            option2 = input("$: ")
            print()
            if option2 == opts2[0]:
                print("?: Which Items?")
                print()
                print("--------------------------------------")
            elif option2 == opts2[0] + " " + items[0]:
                print("!: Healed 30HP!")
                yourhp += 30
                print()
                youritems.remove("Fresh-Water")
                onitems = False
                turn = False
                print("--------------------------------------")
            elif option2 == opts2[0] + " " + items[1]:
                print("!: Healed 20HP!")
                yourhp += 20
                print()
                youritems.remove("Potion")
                onitems = False
                turn = False
                print("--------------------------------------")
            elif option2 == opts2[0] + " " + items[2]:
                print("!: Your HP Maxed!")
                yourhp = yourmaxhp
                print()
                youritems.remove("Full-Restore")
                onitems = False
                turn = False
                print("--------------------------------------")
            elif option2 == opts2[1]:
                onitems = False
            elif option2 != opts2:
                print("!: Invalid Action!")
                print()
                print("--------------------------------------")
    elif turn == False:
        damagedeal = round(random.randint(2, 15))
        print("!:", pokemontype, "deal", damagedeal, "damage on you!")
        yourhp -= damagedeal
        turn = True
        print()
    if enemyhp <= 0:
        print("!: You win!")
        onmatch = False
    elif yourhp <= 0:
        print("!: You lost!")
        onmatch = False
