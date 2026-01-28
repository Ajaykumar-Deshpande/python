# List :-goup of items that is ordrered  and list are mutable (changeable), snd allow dupicate elements


items=["book","pen","laptop"]
print(items)


print(items[0])


items.pop(0)
print(items)

items.append("bucket") 
print(items)

items.remove("pen")
print(items)

items.insert(1,"fan")
print(items)


items[1]="bottle"
print(items)




l=[1,5,3,8,7,2]

print(l[0::2])

print(len(l))  

SORTED1=(sorted(l))  
print(SORTED1) 

rev=SORTED1.reverse()

print(SORTED1)

print(sum(l))




# Nested List
m=[[1 , 2],[3 , 4],[5,6]]
print(m)  
print(m[0][0])    

