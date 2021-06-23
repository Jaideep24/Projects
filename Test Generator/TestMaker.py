#!/usr/bin/env python
# coding: utf-8

# In[1]:


testlist=[]
test={}
while True:
    d=input("Main question")
    if d=="y":
        main=input("Enter main question")
    else:
        main="Nothing"
    a=input("Question")
    b=input("Answer")
    test["Main Question"]=main
    test["Question"]=a
    test["Answer"]=b
    testlist.append(test)
    test={}
    c=input("Quit")
    if c=="y":
        break


# In[2]:


import pandas as pd
testfile=pd.DataFrame(testlist)
print(testfile)
testfile.to_csv("Testfile.csv")


# In[ ]:


[',Question,Answer', '0,Mention the date on which the city of Paris was in a state of alarm,14 July 1789', '1,Name the book which put forward the democratic principle.,The Social Contract', '2,Name the extreme situation where the basic means of livelihood are endangered,Subsistence crisis', '3,Mention the first and most important cause of the French Revolution.,Despotic Rule of Louis XVI', '4,How much percent of the population did the peasents constitute,90%', '5,Name the only estate burdened with the payment of taxes.,Peasents', '6,Name the famous political club.(Do not write the word club),Jacobins', '7,What is the time period from 1793 to 1794 referred to as?,The Reign of Terror', '8,"According to the laws issued by the Robespierre\'s government, what were all French men called?",Citoyen', '9,When did Assembly declare was against Prussia and Austria?,April 1792', '']

