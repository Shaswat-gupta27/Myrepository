with open("shasu.txt","w") as f:
    f.write('0110')
    f.close()
with open("shasu.txt","r") as f:
    l=list(f.read())
    sum1=0
    for each in l:
        sum1=sum1+int(each)
    print(sum1)
    f.close()
    