#  Zelda the Ice of the Valcano

import random
import time

    
    

print("you must go with Zelda and acomplish tasks to defend her and slay all enenemys")


def Akala():
    print("first go to the Akala and take back the castle")
    print("you will need to defeat 4 gaurdains with the master sword and hylain shield. you will also be wearing the hero's set")
    gaurdain_skywatcher = 300
    gaurdain_scout = 400
    small_gaurdain  = 100
    gaurdain_tulus = 300
    Link = 300
    
    
    print("you first will face a small gaurdain")
    while small_gaurdain > 1:
        for _ in range(1):
            move = input("you can choose to attack or put your shield out and parry the gaurdains attack")
            if move == "parry":
                print("since you parryed it is the gaurdains turn but know worry all of that attak will go to him")
                attack_gaurdain = random.randint(10, 50)
                print("you reflected " + attack_gaurdain + " hit points back to the gaurdain")
                small_gaurdain = small_gaurdain - attack_gaurdain
            else:
                Link_attack = random.randint(10, 50)
                print("you took " + Link_attack + " hit points away from the gaurdain")
                small_gaurdain = small_gaurdain - Link_attack
                print("it is now the gaurdains turn to attack")
                gaurdain_attack = random.randint(10, 50)
                print("the gaurdain took " + gaurdain_attack + " hit points away from you")
                Link = Link - gaurdain_attack 
                if Link < 1:
                    print("sorry game over")
                    break
        print("you can't choose to parry so now you must attack")
        Link_attack = random.randint(10, 50)
        print("you took " + Link_attack + " hit points away to the gaurdain")
        small_gaurdain = small_gaurdain - Link_attack
        print("it is now the gaurdains turn to attack")
        gaurdain_attack = random.randint(10, 50)
        print("you lost" + gaurdain_attack + " hit points from you")
        Link = Link - gaurdain_attack 
        if Link < 1:
            print("sorry game over")


    print("next will face a gaurdain tulus")
    Link = 300
    while gaurdain_tulus > 1:
        for _ in range(3):
            move = input("you can choose to attack or put your shield out and parry the gaurdains attack")
            if move == parry:
                print("since you parryed it is the gaurdains turn but know worry all of that attak will go to him")
                attack_gaurdain = random.randint(10, 50)
                gaurdain_tulus = gaurdain_tulus - attack_gaurdain
            else:
                Link_attack = random.randint(Number_list)
                gaurdain_tulus = gaurdain_tulus - Link_attack
                print("it is now the gaurdains turn to attack")
                gaurdain_attack = random.randint(10, 50)
                Link = Link - gaurdain_attack 
                if link < 1:
                    print("sorry game over")
                
        print("you can't choose to parry so now you must attack")
        Link_attack = random.randint(10, 50)
        gaurdain_tulus = gaurdain_tulus - Link_attack
        print("it is now the gaurdains turn to attack")
        gaurdain_attack = random.randint(10, 50)
        Link = Link - gaurdain_attack 
        if link < 1:
            print("sorry game over")


    print("next will face a gaurdain skywatcher")
    Link = 300
    while gaurdain_skywatcher > 1:
        for _ in range(3):
            move = input("you can choose to attack or put your shield out and parry the gaurdains attack")
            if move == "parry":
                print("since you parryed it is the gaurdains turn but know worry all of that attak will go to him")
                attack_gaurdain = random.randint(10, 50)
                gaurdain_skywatcher = gaurdain_skywatcher - attack_gaurdain
            else:
                Link_attack = random.randint(10, 50)
                gaurdain_skywatcher = gaurdain_skywatcher - Link_attack
                print("it is now the gaurdains turn to attack")
                gaurdain_attack = random.randint(10, 50)
                Link = Link - gaurdain_attack 
                if Link < 1:
                    print("sorry game over")
                
        print("you can't choose to parry so now you must attack")
        Link_attack = random.randint(10, 50)
        gaurdain_skywatcher = gaurdain_skywatcher - Link_attack
        print("it is now the gaurdains turn to attack")
        gaurdain_attack = random.randint(10, 50)
        Link = Link - gaurdain_attack 
        if Link < 1:
            print("sorry game over")


    print("last you will face a gaurdain scout")
    Link = 300
    while gaurdain_scout > 1:
        for _ in range(3):
            move = input("you can choose to attack or put your shield out and parry the gaurdains attack")
            if move == parry:
                print("since you parryed it is the gaurdains turn but know worry all of that attak will go to him")
                attack_gaurdain = random.randint(10, 50)
                gaurdain_scout = gaurdain_scout - attack_gaurdain
            else:
                Link_attack = random.randint(Number_list)
                gaurdain_scout = gaurdain_scout - Link_attack
                print("it is now the gaurdains turn to attack")
                gaurdain_attack = random.randint(10, 50)
                Link = Link - gaurdain_attack 
                if link < 1:
                    print("sorry game over")
                
        print("you can't choose to parry so now you must attack")
        Link_attack = random.randint(10, 50)
        gaurdain_scout = gaurdain_scout - Link_attack
        print("it is now the gaurdains turn to attack")
        gaurdain_attack = random.randint(10, 50)
        Link = Link - gaurdain_attack 
        if link < 1:
            print("sorry game over")


    print("it seems now you have proven yourself worthy to go on to your next task")