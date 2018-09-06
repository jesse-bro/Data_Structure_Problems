### Problem:
### Given a non-empty array of integers,
### Find the duplicated integers.

### Solution:
def single(num):
    print(num)#Testing purposes/ not needed
    num.sort()#Testing purposes/ not needed
    print(num)#Testing purposes/ not needed
    dup = set()
    output = []
    for i in num:
        if i not in dup:
            dup.add(i)
        else:
            output.append(i)
    return output
        
test = [2,2,1,1,3,4,4,8,5,0,9]
test2 = [2,2,1]

print(single(test))
print(single(test2))
