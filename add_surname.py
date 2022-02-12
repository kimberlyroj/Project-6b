# Author: Kimberly Rojas
# GitHub username: kimberlyroj
# Date: 2/11/2022
# Description: A function named add_surname that takes as a parameter a list of first names.

def add_surname(first_name_list):
    full_list = [name+' Kardashian' for name in first_name_list if name[0]=='K']
    return full_list
first_name_list = ["Kiki", "Krystal", "Pavel", "Annie", "MaryKay", "Koala"]
print(add_surname(first_name_list))