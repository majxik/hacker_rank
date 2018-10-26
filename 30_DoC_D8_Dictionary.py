#Read, how many entries will follow
entries = int(input())

#Ini. index and dictionary
index1 = 0
index2 = 0
phoneBook = {}

#First loop will create PhoneBook dictionary
while index1 != entries:
    namePhone = [str(x) for x in input().split(" ")]
    phoneBook[namePhone[0]] = namePhone[1]
    index1 += 1

#Second loop will search in PhoneBook
while index2 != entries:
    search = [str(x) for x in input().split()]
    if search[0] in phoneBook:
        print(search[0],"=",phoneBook[search[0]], sep='')
    else:
        print("Not found")
    index2 += 1

input()
