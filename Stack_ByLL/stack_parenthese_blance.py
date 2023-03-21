from stack_LL import Stack as stack

def check(pattern):
    obj=stack()
    for i in pattern:
        if i == '(' or i == '{' or i == '[' or i == '<' :
            obj.push(i)
        else:
            try:
                if obj.peak() == '(' and i==')':
                    obj.pop()
                elif obj.peak() == '[' and i == ']':
                    obj.pop()
                elif obj.peak() == '{' and i == '}':
                    obj.pop()
                elif obj.peak() == '<' and i == '>':
                    obj.pop()
            except:
                print("parantheses is not balanced")
                return True
    if obj.isempty():
        print("parenthises is balanced")
    else:
        print("parenthises is not blanced")
    return True