def count():
    f=open("python.txt","r")
    data=f.read()
    c=0
    x=data.split()
    for i in x:
        if len(i)==5:
            c=c+1
    print(c)
count()
