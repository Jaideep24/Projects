#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Project Exercise 2: βSlot Gameβ:
The player starts with Rs. 10 credit, with each turn costing Rs. 2. If the Fruit Machine
βrollsβ two of the same symbol, the user wins Rs. 2. The player wins Rs. 10 for three of
the same and Rs. 50 for 3 Bells. The player loses Rs. 1 if two skulls are rolled and all of
his/her money if three skulls are rolled. The player can choose to quit with the winnings
after each roll or keep playing until there is no money left.
"""
import random



a=10
b=["π","π₯­","π","π₯","π"]

first=None
second=None
third=None

#def play():
    
    
    #print(first,second,third)
def quit():
    global a
    while True:
        answer=input("You have Rs."+str(a)+" Wanna play more?")
        answer=answer.lower()
        if answer=="yes" or answer=="y":
            return True
            print("You now have Rs.",a,"credit")
            break
        elif answer=="no" or answer=="n":
            print("You are left with Rs.",a)
            print("BYE BYE, you know where to come to try your luck on some more money πππππ")
            return False
        else :
            print("Wrong Input!")
def check_point():
    global a,first,second,third,fourth
    if first==second  or second==third or first == third:
        if (first and second )=="π" or (second and third)=="π"         or (first and third)=="π":
            win=-1
        elif first==second==third:
            if first=="bell" and second=="bell" and third=="bell":
                win=50
            elif first=="π" and second=="π" and third=="π":
                win=-1*a
            else :
                win=10
        else :
            win=2
    else:
        win=0
    a+=win
    if win>0:
        if win==50:
            print(first, second, third,"JACKPOT!!! You win Rs.",win)
        else:
            print(first, second, third,"Congrats!! You win Rs.",win)
    else:
        print(first, second, third,"It's OK, You lose Rs.",win)
        


def run():
    print('''WELCOME TO THE ONE AND ONLY π€π€π€π€π€π€ SLOT MACHINE π€π€π€π€π€π€

 ::::GAME RULES::::
You'll start with Rs.10 and each turn costs Rs.2. You'll be asked if you want to quit.
Answer with yes/no. you can also use y/n
βrollsβ two of the same symbol\t -\t wins\t -\t Rs. 2. 
βrollsβ three same symbols    \t -\t wins\t -\t Rs. 10. 
βrollsβ three BELLS           \t -\t wins\t -\t Rs. 50. 
βrollsβ two SKULLS            \t -\t loses\t -\t Rs. 1. 
βrollsβ three SKULLS          \t -\t loses\t -\t all of the money. 
''')
    global a,first,second,third
    ask=quit()
    while a>0 and ask==True:
        a-=2
        first=random.choice(b)
        second=random.choice(b)
        third=random.choice(b)
        
        check_point()
        if a<=0:
            break
        ask=quit()
    print("OOPS!!!!,You're out of credits,See you later alligator.")
    dsofn=input("press enter to exit")
run()


# In[ ]:




