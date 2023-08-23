import pickle,os
f1=open("student.dat",'rb')
f2=open("temp.dat",'wb')
rno=int(input("enter roll no to be delted"))
found=False
try:
    while True:
        s=pickle.load(f1)
        if s[0]==rno:
            found=True
        else:
            pickle.dump(s,f2)
except:
    f1.close()
    f2.close()
if found==False:
    print("no such record found")
else:
    print("record deleted")
os.remove("student.dat")
os.rename("temp.dat","student.dat")