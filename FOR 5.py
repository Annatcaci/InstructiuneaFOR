n=int(input("Introduceti n"))
s1=s2=s3=s4=s5=s6=0
e=p=1
for i in range(1,n):
    s1+=i
    s2=(i-1)*i
print(s1)
print(s2)
for i in range(1,n):
    e*=i
    s3+=e    
print(s3)
for i in range(1,n):
    a=int(str(i)+"2")
    s4+=a
print(s4)
for i in range(1,n):
    s5+=i/(i+1)
print(s5)
for i in range(1,n):
    a=int("2"+str(i))
    s6+=a
print(s6)