#!/usr/bin/env python
# coding: utf-8

# In[21]:


#       find the which number is largest
num=eval(input("enter your first number"))
num2=eval(input("enter your second number"))
num3=eval(input("enter your third number"))
if(num>num2) and (num>num3):
    print("the largest number is:-",num)
elif(num2>num) and (num2>num3):
    print("the largest number is:-",num2)
else:
    print("the largest number is:-",num3)


# In[22]:


#       average of of marks obtain by student
maths=eval(input("enter your maths marks"))
hindi=eval(input("enter your hindi marks"))
english=eval(input("enter your english marks"))
sanskrit=eval(input("enter your sanskrit marks"))
science=eval(input("enter your science marks"))
sum=(maths+hindi+english+sanskrit+science)
print("the total marks is:-",sum)
average=sum/5
print("the average is:-",average)


# In[23]:


#          the area of the reactangle
x=eval(input("enter your length of your rectangle"))
y=eval(input("enter your width of your rectangle"))
area=x*y
print("the area of the rectangle is:-",area)


# In[24]:


#        THE AREA OF THE CIRCLE
rad=eval(input("enter your radius"))
area=22/7*rad*rad
print("your area of the cirle is:-",area)


# In[25]:


#             the random gaps in number system

x=eval(input("enter your value..you want to start... "))
y=eval(input("enter your value ..which you want to end the number"))
z=eval(input("enter your value ..how many gap you want in your number"))
num=list(range(x,y,z))
print(num)


# In[29]:


#   find this number is odd or evan
x=eval(input("enter your number i am tell which type of number this is:="))
sum=x%2
if(sum==0):
    print("this number is even")
else:
    print("this number is odd")


# In[32]:


#   this is tabe calculator
num=eval(input("enter your number which want to show on your screen..table maker:="))
end=eval(input("enter your number which you want to end the table:="))
for i in range(1,end+1):
    print(num,"x",i,"=",num*i)


# In[34]:


#  show the odd numbers
x=eval(input("enter your end squence number"))
for i in range(x):
    if(i%2!=0):
        print("this is your odd number:-",i)
        continue
        


# In[1]:


#  show the even numbers
x=eval(input("enter your end squence number"))
for i in range(x):
    if(i%2==0):
        print("this is your even number:-",i)
        continue
        


# In[ ]:


#         find the student marks
print("the student name is list:-ram,shyam,anuj")
x=input("enter your student name")
marks={"ram":20,"shyam":33,"anuj":49}
print(marks[x])

