
def add(y,x):
    return y+x
def subtract(y,x):
    return y-x 
def multiply(y,x):
    return y*x 
def devide(y,x):
    return y/x 
def module(y,x):
    return y%x 

operators=['+','-','*','/','%']
stack_number=[]
stack_operation=[]

hearicy={
    '+':1,
    '-':1,
    '*':2,
    '/':2,
    '%':2,
    '^':3,
    '(':4
    }


def calculation(string):
    stack_number=[]
    stack_operation=[]
    top_operation=''
    digit=0
    for i in string:
        if i.isdigit():
            if digit==0:
                digit=1
                stack_number.append(i)
            else:
                x=str(stack_number.pop())
                stack_number.append(int(x+str(i)))
            # stack_number.append(i)
            # print(stack_number,stack_operation)
        else:
            digit=0
            if len(stack_operation)==0:
                stack_operation.append(i)
            else:
                top_operation=stack_operation.pop()
                # print(top_operation,i)
                # print(stack_operation, stack_number,")")
                if i==')':
                    while True:
                        if top_operation=='(':
                            break
                        else:
                            if len(stack_number)<2:
                                pass
                            else:
                                x=int(stack_number.pop())
                                y=int(stack_number.pop())
                                if top_operation=='+':
                                    result=add(y,x)
                                elif top_operation=='-':
                                    result=subtract(y,x)
                                elif top_operation=='*':
                                    result=multiply(y,x)
                                elif top_operation=='/':
                                    result=devide(y,x)
                                elif top_operation=='%':
                                    result=module(y,x)
                                stack_number.append(result)
                                top_operation=stack_operation.pop()
                            
                # print(stack_operation, stack_number,">")
                elif i=='(':
                    stack_operation.append(top_operation)
                    stack_operation.append(i)
                elif hearicy[top_operation]>=hearicy[i]:
                    # print(len(stack_number))
                    if len(stack_number)<2:
                        stack_operation.append(top_operation)
                        stack_operation.append(i)
                        pass
                    else:
                        result=0
                        x=int(stack_number.pop())
                        y=int(stack_number.pop())
                        # print(x,y)
                        if top_operation=='+':
                            result=add(y,x)
                        elif top_operation=='-':
                            result=subtract(y,x)
                        elif top_operation=='*':
                            result=multiply(y,x)
                        elif top_operation=='/':
                            result=devide(y,x)
                        elif top_operation=='%':
                            result=module(y,x)
                        if result==0:
                            pass
                        else:
                            stack_number.append(result)
                        if top_operation=='(':
                            stack_number.append(y)
                            stack_number.append(x)
                            stack_operation.append(top_operation)
                        stack_operation.append(i)
                        # print(stack_number,stack_operation)
                
                elif hearicy[top_operation]<hearicy[i]:
                    # print(stack_operation, stack_number,"<")
                    # print('hello')
                    stack_operation.append(top_operation)
                    stack_operation.append(i)
                    
        # print(stack_number,stack_operation)
    # print(stack_operation, stack_number,"w")
    while len(stack_operation)!=0:
        if len(stack_number)<2:
            sign=stack_operation.pop()
            if sign=='-':
                x=stack_number.pop()
                x=-x
                stack_number.append(x)
            elif sign=='+':
                break
        else:
            top_operation=stack_operation.pop()
            x=int(stack_number.pop())
            y=int(stack_number.pop())
            if top_operation=='+':
                result=add(y,x)
            elif top_operation=='-':
                result=subtract(y,x)
            elif top_operation=='*':
                result=multiply(y,x)
            elif top_operation=='/':
                result=devide(y,x)
            elif top_operation=='%':
                result=module(y,x)
            stack_number.append(result)
    # print(stack_number[0])
    print(stack_number[0])
    return stack_number[0]

# calculation('1+2')
# calculation('48*34')
# calculation('28/35')
# calculation('28-35')            
            
            
                