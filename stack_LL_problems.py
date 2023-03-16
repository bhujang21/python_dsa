import stack_LL as stack

#1.reverse a string by using stack

def reverse_string(string):
    obj=stack.Stack()
    for i in string:
        obj.push(i)
    result=""
    tra=obj.top
    while tra:
        result+=tra.data
        tra=tra.next
    return result
print(reverse_string("my contry name is India"))

#2. As per given pattern do undo and redo on given string by using stack

def text_editor(string,pattern):
    obj=stack.Stack()
    r_obj=stack.Stack()
    for i in string:
        obj.push(i)
    for i in pattern:
        if i.lower() == 'u':
            try:
                r_obj.push(obj.pop())
            except:
                # print(obj.custom_travle())
                pass
        elif i.lower() == 'r':
            try:
                obj.push(r_obj.pop())
            except:
                # print(obj.custom_travle())
                pass
    return obj.custom_travle()

print(text_editor("bhujang","uuuuuuuuuuuuuu"))
    