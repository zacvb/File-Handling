import pickle
def write1():
    f=open("student.dat","ab")
    ch='y'
    while ch=='y':
        rollno=int(input("enter roll no:"))
        name=input("enter name")
        age=int(input("age:"))
        s=[rollno,name,age]
        pickle.dump(s,f)
        ch=input("enter y to add more records")
    f.close()
write1()
