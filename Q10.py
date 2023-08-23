import pickle
def readdata():
    file=open("student.dat",'rb')
    try:
        while True:
            list1=pickle.load(file)
            print(list1)
    except EOFError:
        file.close()
readdata()
        