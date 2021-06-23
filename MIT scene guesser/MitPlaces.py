#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import tree
import pandas as pd
pd.options.display.max_rows = 4000
pd.set_option("display.max_columns", None)
main=pd.read_csv("Scene hierarchy - Places365.csv",index_col=[0])
main.columns=main.iloc[0]

main=main.transpose()
main=main.drop(columns=["category"])
category=[]
answers=[]
subanswers=[]
for i in main:
    category.append(i)
    for j in main[i]:
        subanswers.append(j)
   
    answers.append(subanswers)
    subanswers=[]
clf = tree.DecisionTreeClassifier()
clf=clf.fit(answers,category)
answerlist=[]
questions=list(main.index)
for i in questions:
    answer=input(f"Is it {i}?")
    if answer.lower()=="yes":
        answerlist.append(1)
    else:
        answerlist.append(0)
result=clf.predict([answerlist])
print("I think it's a ",result[0])


# In[ ]:




