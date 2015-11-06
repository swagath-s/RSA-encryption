def gcd(x, y):
    if y>x:
        temp = x
        x = y
        y = temp
    r = 0
    while(y):
        r = x%y
        x = y
        y = r
        
    x = abs(x) #accounting for negative integers
    return x

