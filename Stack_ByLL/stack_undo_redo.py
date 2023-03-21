from stack_LL import Stack as stack

def undo_redo(string,pattern):
    obj=stack()
    r_obj=stack()
    for i in string:
        obj.push(i)
    
    for i in pattern:
        if i.lower() == "u":
            try:
                r_obj.push(obj.pop())
            except:
                pass
        elif i.lower() == "r":
            try:
                obj.push(r_obj.pop())
            except:
                pass
    result=""
    travle=obj.top
    while travle:
        result=travle.data+result
        travle=travle.next
    return result
        
   
print(undo_redo("my name is","uur"))