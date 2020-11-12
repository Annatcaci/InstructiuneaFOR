a=int(input("Introduveti numerele"))
b=int(input("Introduveti numerele"))
if a%2==0:
    a+=1
st=a
stp=b
for i in range(st,stp,2):
    print(i)