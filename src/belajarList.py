listBilangan = [1,2,3,4,5]
print(listBilangan)
print(len(listBilangan))
# show acces listbilangan
print(listBilangan[0])
# edit item list 
listBilangan[0] = 99
print(listBilangan)
print(listBilangan[1:])
print(listBilangan[:2])
# add item list 
listBilangan.append(99)
print(listBilangan)
# add list to list
addBilangan = [9,2,3,5]
listBilangan.extend(addBilangan)
print(listBilangan)
listBilangan.remove(99)
print(listBilangan)
# sort list 
listBilangan.sort()
print(listBilangan)
# belajar condition
for item in listBilangan:
    print(item)