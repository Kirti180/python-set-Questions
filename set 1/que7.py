num=13
flag=True
for i in range(2,num):
    if num%i==0:
        # print("Prime number")
        flag=False
        break
if flag:
    print("Prime number")
else:
    print("Not prime number")