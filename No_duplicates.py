### Problem:
### Given a non-empty array of integers,
### every element appears twice except for one.
### Find that single one.

### Solution:
def single(num):
    print(num)
    #Testing purposes
    num.sort()
    print(num)
    no_dup = set()
    for i in num:
        if i not in no_dup:
            no_dup.add(i)
        else:
            no_dup.remove(i)
    return no_dup
        
test = [2,2,1,1,3,4,4,8,5,0,9]
test2 = [2,2,1]

print(single(test))
print(single(test2))
