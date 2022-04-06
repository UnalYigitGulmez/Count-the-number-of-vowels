r = str(input(""))
L = len(r)
i = 0
j = 0
m = 0
vowels = ("a", "e", "ı", "i", "o","ö", "u","ü")

for i in range  (L) :
    
    for j in range(8) :
        
        if r[i]==vowels[j]:

            print("One of the vowels is -->" , r[i])
            m = m + 1    
            
        j = j + 1
        
    i = i + 1

print("Total vowels we have is ", m)
