#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class bank_account:
  def __init__(self):
    self.accno = ""
    self.balance = 0
    self.acctype = ""
  def AAC(self,accNO):
    self.accno = accNO

  def GAN(self):
    return self.accno

  def GB(self):
    return self.balance

  def GAT(self):
    return self.acctype

  def SB(self,amount):
    self.balance = amount

  def SAT(self,acctype):
    self.acctype = acctype
  def output(self):
    return self.accno, self.balance, self.acctype
accno = []
for i in range(0,10,1):
  accno.append(bank_account())
BO1 = True
l = 0
while BO1 == True:
  option = int(input("""
  1. Add an account
  2. Get Balance
  3. Account Type Status
  4. Set Balance
  5. Set Account Type
  6. Exit
  What would you like to do?
  """))
  if option == 1:
    x = input("Please enter account number - ")
    accno[l].AAC(x)
    l+=1
  elif option == 2:
    x = input("Which account would you like the balance of? - ")
    for i in range(0,10,1):
      if x == accno[i].GAN():
        y = accno[i].GB()
        print(y)
        break
  elif option == 3:
    x = input("Which account would you like to know the account type? - ")
    for i in range(0,10,1):
      if x == accno[i].GAN():
        y = accno[i].GAT()
        print(y)
        break
  elif option == 4:
    x = input("To Which account would you like to set the balance to? - ")
    z = input("What ammount would you like to set? - ")
    for i in range(0,10,1):
      if x == accno[i].GAN():
        accno[i].SB(z)
        break
  elif option == 5:
    x = input("To which account would you like to change the account type? - ")
    z = input("What would you to like to change the account type to? - ")
    for i in range(0,10,1):
      if x == accno[i].GAN():
        accno[i].SAT(z)
        break
  elif option == 6:
    break
for i in range(0,10,1):
  print(aacno[i].output())

