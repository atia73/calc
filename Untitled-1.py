def sum(arg1,arg2):
    return arg1+arg2;
def dif(arg1,arg2):
    return arg1-arg2;
def multi(arg1,arg2):
    return arg1*arg2;
def div(arg1,arg2):
    return arg1/arg2
list1 =['+','-','/','*','%']
eq=input("enter your eq\n",) 
eq2=list(eq)
for i in range(len(eq2)):
   if eq2[i] in list1 :
        if eq2[i] =='+':
            print(sum(int(eq[:i]),int(eq[i+1:])))
        elif eq2[i] =='-':
            print(dif(int(eq[:i]),int(eq[i+1:])))
        elif eq2[i] =='*':
            print(multi(int(eq[:i]),int(eq[i+1:])))
        elif eq2[i] =='/':
            print(div(int(eq[:i]),int(eq[i+1:])))
