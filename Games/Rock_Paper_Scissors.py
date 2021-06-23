#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello")
z=input("What is your name: ")
x=int(input("What is your age: "))
if x>6 :
    print("Hi,",z,"let's play rock paper scissors✊✋✌")
    j=int(input("Please enter the number of rounds you wish to play: "))
    import random


    b=random.randint(1,3)

    if b==1:
        b="Rock"
    if b==2:
        b="Paper"
    if b==3:
        b="Scissors"
    v=1
    t=1
    count=1
    while count <=j:

        a=input("Please enter Rock, Paper or Scissors: ")
        if a==b:
            print("It's a tie!!!")

        elif a=="Rock"and b=="Paper":
            print("Oh, you lost")
            t=t+1
        elif a=="Rock" and b=="Scissors":
            print("You Won!!!")
            v=v+1
        elif a=="Paper" and b=="Rock":
            print("You Won!!!")
            v=v+1
        elif a=="Paper" and b=="Scissors":
            print("Oh, you lost")
            t=t+1
        elif a=="Scissors" and b=="Rock":
            print("Oh, you lost")
            t=t+1
        elif a=="Scissors" and b=="Paper":
            print("You Won!!!")
            v=v+1


        count=count+1
    print()
    print("Your score =",v)
    print("Oppenent's score=",t)
    if v>t:
        print("Well done, you deserve the win")
    else:
        print("Bummer....")
else:
    print("Sorry, you haven't completed enough of your life to play this game😕😕.")


# In[ ]:




