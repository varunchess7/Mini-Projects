num = 1

while num <= 100000:
    if num == 1 or 2:
        print(num)
    
    elif num % 2 != 0:
        print(num)
    else:
        break 
    num += 1
