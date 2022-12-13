# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 11:37:49 2022

@author: bluea
"""
first_name = " "
last_name = " "
first_names = []
last_names = []
corrected_names = []

while last_name:
    first_name = input("Enter your name:")
    if first_name == "":
        break;
    last_name = input("Enter your last name:")
    if last_name == "":
        break;
    if first_name != "":
        first_names.append(first_name)
    if last_name != "":
        last_names.append(last_name)
    
first_names[:1].clear()
last_names[:1].clear()
last_names.sort()


for i in last_names:
    print(i)
    
    
    

#for i in range(last_name):
  #  if (last_name[0]) >= 65:
 #       name_list.append(i)
#print(chr(name))
