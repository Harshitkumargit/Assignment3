s=input("enter string ")
c=input("enter the character ")
l=len(s)
count=0
for i in range(l):
    if (s[i]==c):
        count+=1
        
print("The total number of times",c,"has occured is ",count)
