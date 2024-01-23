#!/bin/python3
import re

if __name__ == '__main__':
    #N = int(input().strip())
    #6
    datas = ['riya riya@gmail.com',
    'julia julia@julia.me',
    'julia sjulia@gmail.com',
    'julia julia@gmail.com',
    'samantha samantha@gmail.com',
    'tanya tanya@gmail.com']
    abc = ' '.join('abcdefghijklmnopqrstuvwxyz').split(' ')
    gmailNames = []
    pattern = "@gmail[.].{2,3}$"
    #for N_itr in range(N):
    for data in datas:
        #first_multiple_input = input().rstrip().split()
        #firstName = first_multiple_input[0]
        #emailID = first_multiple_input[1]
        _ = data.split(' ')
        firstName = _[0]
        emailID = _[1]

        if re.search(pattern,emailID) != None:
            gmailNames.append(firstName)

    datas_sorted = sorted(gmailNames)
    for data in datas_sorted:
        print(data)

    '''gmailNames_sorted = []
    for i in range(gmailNames-1):
        if gmailNames[i] == gmailNames[i+1]:
            gmailNames_sorted[i] = gmailNames[i]
            gmailNames_sorted[i+1] = gmailNames[i+1]
        else:
            j = 0
            lett_1 = gmailNames[i][j]
            lett_2 = gmailNames[i+1][j]
            while abc.index(lett_1) == abc.index(lett_2):
                if abc.index(lett_1) > abc.index(lett_2):
                    gmailNames_sorted[i] = gmailNames[i]
                    
                else:
                    gmailNames_sorted[i] = gmailNames[i+1]'''