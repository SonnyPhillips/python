import pandas as pd
import string
import time

PasswordLoop = True
Tab=[]
PurchaseHistory = []
TabTotal=0

Carling = ["Carling",3.5 ]
Guinness = ["Guinness",4.0 ]
Madri = ["Madri",3.5 ]
Items = [Carling,Guinness,Madri]
#The inital version will onyl use local lists for data on drinks



while (PasswordLoop == True):
    print("**************")
    print("Insert User Password")
    Password = "Password"

    Guess = input()
    if (Guess == Password):
        PasswordLoop = False
    #simple password system
        
MenuLoop = True
while (MenuLoop == True):
    print("Menu(1), Price Enquiry(2), Tabs(3) or Purchase History (4)")
    Choice = int(input())
    if (Choice == 1):
        print("Menu Items:")
        print(Guinness[0],"",Carling[0],"",Madri[0])
        Choice = input()
        Choice = Choice.lower()
        if (Choice == "carling"):
            Tab.append(Carling[1])
            PurchaseHistory.append(Carling[0])
        if (Choice == "guinness"):
            Tab.append(Guinness[1])
            PurchaseHistory.append(Guinness[0])
        if (Choice == "madri"):
            Tab.append(Madri[1])
            PurchaseHistory.append(Madri[0])
        print (PurchaseHistory)
        print (Tab)
        print("pay tab? (y or n)")#this version does not have user profiles
        Choice = input()
        Choice = Choice.lower()
        if (Choice=="y"):
            Tab = []
            print("Tab has been payed")
        if (Choice=="n"):
            print("Tab has been stored")#this would use a menu write function

    elif (Choice == 2):
        print("What item would you like to price check?")
        print(Guinness[0],"",Carling[0],"",Madri[0])
        Choice = input()
        Choice = Choice.lower()
        if (Choice =="carling"):
            print (Carling)
        if (Choice == "guinness"):
            print (Guinness)
        if (Choice == "madri"):
            print(Madri)


    elif (Choice == 3):
        print("current tabs: ", Tab )
        i=0
        TabTotal = sum(Tab)
        print("TAB TOTAL: ",TabTotal)
        print ("Pay tab? y or n")
        Choice = input()
        Choice = Choice.lower()
        if (Choice == "y"):
            Tab = []
        else:
            print("tab has not been payed")



    elif (Choice == 4):
        print("Purchase history: ",PurchaseHistory)

    else:
        print("Invalid (Only accepts 1-4)")
