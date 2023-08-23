def story():
    sum=0
    f=open("python.txt", "r")
    data=f.read()
    for i in data:
        if i.isdigit():
            if int(i)%2==0:
                sum=sum+int(i)
    print(sum)
story()
