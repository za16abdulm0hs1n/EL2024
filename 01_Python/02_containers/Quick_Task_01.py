#Finding max in List through loop

def find_max (ls):
    max = 0
    for num in ls:
        if max < num:
            max = num
    return(max)


ls = [10,20,4,45,99]
print('Largest Number in the list = ', find_max(ls))