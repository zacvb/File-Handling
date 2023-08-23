import pickle
f=open("student.dat",'rb')
rec=int(input("enter roll no:"))
found=False
try:
    while True:
        s=pickle.load(f)
        if s[0]==rec:
            print(s)
            found=True
except EOFError:
    f.close
if found==False:
    print("no such records found")
else:
    print("search successfull")