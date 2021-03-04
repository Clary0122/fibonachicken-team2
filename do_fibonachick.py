#def fibonachi(num):
#    if x==0: return 0
#    if x==1: return 1
def chicken(x):
    if x == 0: return 0
    if x == 1: return 1
    a,b = 1,1
    while 1:
        c = a+b
        if c > x: return a + chicken(x-b)
        elif c == x: return b
        a, b = b, c

#num = int(input('How many people are you: '))
#print('chicken: {}'.format(chicken(num)))    
