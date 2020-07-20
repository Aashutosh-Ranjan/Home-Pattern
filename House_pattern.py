n = int(input("enter a no >= 10 for home pattern \n" ) or 15)
for i in range(int(2*n/3)+1):
    if i==0:
        print((int(n/6)+1)*'  '+(n-2*(int(n/6)+1))*'* ')    
    elif i<=int(n/6):
        print((int(n/6)-i+1)*'  '+'*'+(2*i)*'  '+'*'+(n-2*int(n/6)-4)*'  '+'*')
    elif i==int(n/6)+1 or i==int(2*n/3):
        print('* '*n)
        x=2*i-1
    elif i==int(5*n/12)-1 :
        a,b = divmod(2*x,3)
        print('* '+' '*(a-1)+'_ '*int((a+b)/2+1)+' '*(a-1)+'* '+(n-x-3)*'  '+'*')
    elif i>int(5*n/12)-1:
        print('* '+' '*(a-1)+'!'+'  '*int((a+b)/2-1)+' ! '+' '*(a-1)+'* '+(n-x-3)*'  '+'*')
    else:
        print('* '+'  '*x+'* '+(n-x-3)*'  '+'*')

print(" "*int((n*2-19)/2)+"STAY HOME STAY SAFE")
