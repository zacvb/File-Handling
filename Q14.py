import csv
def write():
    x=open("python.csv","w",newline='')
    y=["item number","item name","quantity","price"]
    data=csv.writer(x)
    data.writerow(y)
    ans='y'
    while ans =='y':
        ino=int(input("number"))
        ina=input("name")
        q=int(input("quantity"))
        p=int(input("price")) 
        z=[ino,ina,q,p]
        data.writerow(z)
        ans=input("y/n")
    x.close()
def read():
    x=open("python.csv","r")
    data=csv.reader(x)
    for i in data:
        print(i)
    x.close()
def search():
    x=open("python.csv","r")
    n=input("enter item number:")
    data=csv.reader(x)
    for i in data:
        if i[0]==n:
            print("found",i)
        else:
            ("not found")
    x.close()
write()
read()
search()