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

#3 blanced paranthesis or not by using stack
# "([)]"
def par_check(pattern):
    obj=stack.Stack()
    for i in pattern:
        if i == "(" or i== "[" or i == "{":
            obj.push(i)
        else:
            try:
                if obj.peak() == "(" and i ==")":
                    obj.pop()
                elif obj.peak() == "[" and i =="]":
                    obj.pop()
                elif obj.peak() == "{" and i =="}":
                    obj.pop()
            except:
                print("pranthesis are not blanced")
                return True
    if obj.isempty():
        print("Pranthesis are balnced")
    else:
        print("ptanthesis are not blanced")

    return True

par_check("{[()]}()[]")