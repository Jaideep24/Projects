#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import re
project=open("project-data.txt","r")
project=(project.read()).replace(",",";")
projectitem=re.split("\n",project)
#print(projectitem)
projectlist=[]
a={}

t=""
for i in projectitem:
    if i=="":
        continue
    # elif (i[0]).isdigit()==False and i[len(i)-1]==".":
    #   i=i.replace(".","")
    if (i[0]).isdigit():
        if len(re.split("\.",i))==2:

            a["Topic"]=((re.split('\.',i))[1])

            if a["Topic"]=="":
                n=projectitem.index(i)
                a["Topic"]=projectitem[n+2]
            t=a["Topic"]
    elif len(re.split("=",i))==2:
        a["Word"]=((re.split("=",i))[0])
        a["Meaning"]=((re.split("=",i))[1])
        a["Topic"]=t
    elif len(re.split(":",i))==2:
        a["Example"]=((re.split(":",i))[1])
        if i[len(i)-1]!=".":
            n=projectitem.index(i)
            a["Example"]+=" "+projectitem[n+1]
        projectlist.append(a)
        a={}
    else:
        continue
# print(projectlist)
projectfile=pd.DataFrame(projectlist)
print(projectfile.head())
projectfile.to_csv("projectfile.csv")
import pandas as pd
pd.options.display.max_rows = 4000
pd.set_option("display.max_columns", None)
a=pd.read_csv("projectfile.csv",index_col=[0])
a.head(4000)
for i in a["Topic"].unique():
    print(i)
ask=input("What topic do you want")
question=a[a["Topic"]==ask]
question.reset_index(inplace=True)
question.head()
import random
print(len(question))
questionitem=a.iloc[random.randint(0,(len(a)-1))]
questionitem[0]=questionitem[0].replace("Topic","")
questionitem[1]=questionitem[1].replace("Word","")
questionitem[2]=questionitem[2].replace("Meaning","")
questionitem[3]=questionitem[3].replace("Example","")
print(questionitem[1])
answeroptionset=set()
answeroptionset.add(questionitem[2])
answeroption=[]
while len(answeroptionset)<4:
  
    questionitemer=question.iloc[random.randint(0,(len(question)-1))]
    questionitemer[2]=questionitemer[2].replace("Meaning","")
    answeroptionset.add(questionitemer[3])
answeroption=list((answeroptionset))
#print(answeroption)
for i in range(len(answeroption)):
    print(i+1,end=". ")
    print(answeroption[i])
    if questionitem[2]==answeroption[i]:
        correctanswer=answeroption[i]
useranswer=input("Enter Option number(type \"Hint\" to get an example):")
if useranswer=="Hint":
    print(questionitem[3])
    useranswer=input()

if correctanswer==answeroption[int(useranswer)-1]:
    print("Correct answer")
else:
    print("Incorrect answer, the correct answer is ",correctanswer)

