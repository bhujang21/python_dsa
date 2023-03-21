import stack_LL as stack

def reverse(string):
    result=""
    obj=stack.Stack()
    for i in string:
        obj.push(i)
    travle=obj.top
    if travle:
        while travle:
            result+=travle.data
            travle=travle.next
        return result
    raise ValueError("reverse(x) x is empty")

print(reverse("my name is bhujang"))