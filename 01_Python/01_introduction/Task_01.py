# Number Counter Function 
def number_counter(num = 0, ls =[]):
    if ls != [] :
        return (ls.count(num))
    else:
        print("There is no list to check!")

num = 4
ls = [1,4,6,7,4]
#print(number_counter(num,ls))

#____________________________________________________________________

#Vowel Check Function
def vowel_check(let = ' '):
    vowel_list = ['a','e','i','o','u']
    let=let.lower()
    if let in vowel_list:
        print('the letter is vowel')
    else:
        print('the letter is not vowel')

#vowel_check('C')

#________________________________________________________________________

import os

print('\n', os.getenv('HOME'), '\n')
print('\n', os.getenv('PATH'), '\n')

