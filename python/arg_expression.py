def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
print(f"list1 = {list1}")
list2 = extendList(123,[])
list3 = extendList('a')

list1.append(78)

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = {list3}") 

