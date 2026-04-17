#simple program
#calculator

print('Calculator')

print('''options are \n1.add\n2.subtract\n3.multiplication\n4.division\n5.exit''')
s=True

while s:
        a=int(input('enter first no:'))
        b=int(input('enter second no:'))
        c=int(input('Enter option:'))
        if c==1:
            print(a+b)
            
        elif c==2:
            print(a-b)
            
        elif c==3:
            print(a*b)
            
        elif c==4:
            print(a/b)
            
        else:
            break  