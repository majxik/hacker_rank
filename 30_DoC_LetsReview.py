
#read input, n will give number of words will be required to process
n = int(input("How many words for review: "))

#methode for iterrating each word given and split even and odd indexed letter
def wordReviewer(n):
#It will run number of times given as n
    for index in range(0, n):
        string = input()
        index1 = 0
        even = []
        odd = []
#even letters to list even, odd letters to list odd
        for letter in string:
            if index1 % 2 == 0:
                even.append(letter)
            elif index1 % 2 == 1:
                odd.append(letter)
            index1 += 1
#print result as requested, letters without space and list with 1 space
        print("".join(even),"".join(odd))

wordReviewer(n)

#for running in PC, to see result
input()
