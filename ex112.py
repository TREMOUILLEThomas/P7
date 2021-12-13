a=int(input("nombre de table à afficher : "))
b=int(input("nombre de multiplicateurs : "))
t=0
for i in range(1,a+1):
    print("table de" , i)
    for w in range(1,b+1):
        t=i*w
        print(i,"fois",w,"=",t)