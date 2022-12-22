l_range=int(input("enter the lower range: "))
u_range=int(input("enter the upper range: "))
a=[(x,x**2) for x in range(l_range,u_range+1)]
print(a)
