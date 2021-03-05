 #Health management system


print("Welcome to Health Management System!")
print("Do you want to lock the details or see the details?")
c=int(input("Enter\n1: for locking the details\n2:For seeing the details "))

if c==1:

    print("For whom do you want to lock the details?Enter")
    print("1:For Astha\n2:For kabeer\n3:For Prakhar")
    a=int(input())
    print("What do you wanna lock?Enter")
    b=int(input("1:For diet\n2:For Exercise"))
    def getdate():
        import datetime
        return datetime.datetime.now()

    if a==1 and b==1:

            f=open('astha1.txt','a')
            print("Enter what you have eaten: ")
            x=input()
            r = str(getdate())
            f.write("\n")
            f.write(r)
            f.write("\t\t")
            f.write(x)

    if a==1 and b==2:
            f=open("astha2.txt","a")
            y=input("What have you exercised:")
            s = str(getdate())
            f.write("\n")
            f.write(s)
            f.write("\t\t")
            f.write(y)

    if a==2 and b==1:
            f = open('kabeer1.txt','a')
            x=input("Enter what you have eaten: ")
            t = str(getdate())
            f.write("\n")
            f.write(t)
            f.write("\t\t")
            f.write(x)
    if a == 2 and b == 2:
            f = open("kabeer2.txt", "a")
            y = input("What have you exercised:")
            u = str(getdate())
            f.write("\n")
            f.write(u)
            f.write("\t\t")
            f.write(y)


    if a == 3 and b == 1:
             f = open('prakhar1.txt','a')
             x=input("Enter what you have eaten: ")
             v = str(getdate())
             f.write("\n")
             f.write(v)
             f.write("\t\t")
             f.write(x)



    if a == 3 and b == 2:
            f = open("prakhar2.txt", "a")
            y = input("What have you exercised:")
            w = str(getdate())
            f.write("\n")
            f.write(w)
            f.write("\t\t")
            f.write(y)



elif c==2:
     print("Whose details do you wanna see?Enter")
     print("1:For Astha\n2:For kabeer\n3:For Prakhar")
     a = int(input())
     print("Which detail you want to see ?Enter")
     b = int(input("1:For diet\n2:For Exercise"))

     if a == 1 and b == 1:
         f=open("astha1.txt","r")
         x=f.read()
         print(x)

     if a == 1 and b == 2:
         f=open("astha2.txt","r")
         x=f.read()
         print(x)

     if a == 2 and b == 1:
         f=open("kabeer1.txt","r")
         x=f.read()
         print(x)

     if a == 2 and b == 2:
         f=open("kabeer2.txt","r")
         x=f.read()
         print(x)

     if a == 3 and b == 1:
         f=open("prakhar1.txt","r")
         x=f.read()
         print(x)

     if a == 3 and b == 2:
         f=open("prakhar2.txt","r")
         x=f.read()
         print(x)

