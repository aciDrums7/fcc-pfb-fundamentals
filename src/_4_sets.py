""" Sets """

set1 = {"Roger", "Syd"}
set2 = {"Roger"}
set3 = {"Luna"}

intersect = set1 & set2
print(intersect)

union = set1 | set3
print(union)

difference = set1 - set2
print(difference)

isSuperSet = set1 > set2
print(isSuperSet)

print(list(set1))

#! Cannot contain same element
set1 = {"Roger", "Syd", "Roger"}
print(set1)
