#!/usr/bin/env python3

#######Rename files depending on a special condition#######

# rename a file from 123_01-01-2016 --> 00123_01_01_2016

#This script get the items listed in the current working directory 
#stores the list in a variable 'testo' and iterates through the list;
#given the regex in odlInv, find one by one the matching group (1)
#based on the lenght of this group, adds 1,2 or 3 '0' to the beginning
#of the file name - there is a try except clause because if the regex finds 
#no match, it will return an 'AttributeError' : None Object 


import os, re, sys #import the three modules we will be using in the script

#assign to testo the listdir of the cwd = current working directory
testo = os.listdir(os.getcwd()) 

for inventario in testo: #iterates trough the list of strings stored in 'testo'
    try:
    	# compile the regex according to the filename.search and find the match
    	# 1 by 1 based on the first .group(1) = (\d{2,5})
        oldInv = re.compile(r'(\d{2,5})[-|_]\d{1,2}-\d{1,2}-\d{4}').search(inventario).group(1)    
        
        # based on the lenght of our match we rename it:
        # first goes in the existing file name = file_dir + '/' + inventario 
        # then we input the renaming method = file_dir + '/0' + inventario
        # and we add 1,2 or 3 zeros at the beginnnig of the file to match 
        # the five digit inventory we are after
        if len(oldInv) == 4: 
            os.rename(file_dir + '/' + inventario, file_dir + '/0' + inventario)
        elif len(oldInv) == 3:
            os.rename(file_dir + '/' + inventario, file_dir + '/00' + inventario)
        elif len(oldInv) == 2:
            os.rename(file_dir + '/' +  inventario, file_dir + '/000' + inventario)

        # we need to add a try exception clause because if the regex doesn't 
        # find any match it will return a AttributeError: None Object
        # and will stop the iteration - so we need to force it to continue 
        # trough the list if some of the inventory are already correct
    except AttributeError:
        continue