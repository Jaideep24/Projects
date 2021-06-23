#!/usr/bin/env python
# coding: utf-8

# In[ ]:


name=input("Enter name")
osnv=input(f"Hello {name}, this test has been made to see how much you have understood your chapter, it contains objective type questions from the notes you have and have to be answered in few words, your final marks will be displayed after your last answer. Best of luck. Press enter to begin the test")
import pandas as pd
pd.set_option('max_colwidth', 0)
test=pd.read_csv("https://raw.githubusercontent.com/Jaideep24/Timepass/master/Testfile.csv",index_col=[0])#enter name of file in which questions are saved
# print((test))
# test.to_csv("advadav.csv")
marks=0
question_num=0
for i in range(len(test.index)):
    a=(test.iloc[i])
    print(a)
    if str(a[0])=="Nothing":
        a[0]=""
        
    else:
        question_num=i
        a[0]=a[0].replace("Main Question","")
    a[1]=a[1].replace("Question","")
    a[2]=a[2].replace("Answer","")
    print(a[0])
    print("Q",(i+1-question_num),".",end="")
    b=input(a[1])
    if b==str(a[2]):
        print("Correct Answer")
        marks+=1
    else:
        print("Incorrect answer, the correct answer is ",a[2])
print("Your final score is ",marks)


# In[2]:


vn=input("Press enter to exit")

