# Tuples :-goup of items that is ordrered  and Tuples are inmutable (unchangeable),.
# Methods of Tuples



gender= ("male","female","others" )
print(len(gender))
print(gender)
print(gender[0])
print(gender[1:3]) # slicing

gender[1]="transgender"
print(gender)


print(gender.count("male"))

gender= ("male","female","others" ,(1,2,3))
print(gender)




# Sets: Sets are the  collection of unique items and sets are unordered
# set operations

s={12,2,3}
print(type(s))
s.add(4)
s.remove(3)
s.pop() # This method will remove any item in given set we can not predict which item will get pop
print(s)


s1={1,2,3}
s2={3,5,6}
s3=s1|s2 # output{1, 2, 3, 5, 6}
s3=s1&s2 #output{3}
s3=s1-s2 # output {1,2}
print(s3)