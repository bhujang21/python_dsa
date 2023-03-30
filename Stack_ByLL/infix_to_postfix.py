from stack_LL import Stack as stack

def infix_to_postfix(exp):
    pre={'+':1,'-':1,'*':2,'/':2,'^':3,'(':0,')':0}
    result=""
    obj=stack()
    for i in exp:
        print("this is obj",obj)
        if i in pre:
            data=pre[i]
            if not obj.isempty():
                while obj.n > 0 and pre[obj.peak()]>=data:
                    if obj.peak() == "(" or obj.peak() == ")":
                        obj.pop()
                        break 
                    result+=obj.pop()
                else:
                    obj.push(i)
                    #result+=i
            else:
                obj.push(i)
        else:
            result+=i
    while not obj.isempty():
        result+=obj.pop()
    return result

print(infix_to_postfix('a*b-(c+d)+e'))