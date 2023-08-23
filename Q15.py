import csv
def search():
    x=open("python.csv","r")
    data=csv.reader(x)
    for i in data:
        if i[3]>='1000' and i [3]<='60000':
            print("item found",i)
        else:
            print("item not found")
            break
    x.close()
search() 