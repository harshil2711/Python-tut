from datetime import datetime


print('welcome to management system')
choicee = int(input('press 1 to lock OR 2 for retrive : '))
person = int(input(('press 1 for rahul , 2 for manav , 3 for yash : ')))
infoo = int(input('press 1 for excercise and 2 for diet: '))

# To get a current date and time
def getdate():
    d = datetime.now()
    print(d)


def showw():
    if person==1:
        if infoo==1:
            r = open('rahulexe.txt','r')
            print(r.read())
        else:
            l = open('rahuldiet.txt','r')
            print(l.read())

    elif person ==2:
        if infoo==1:
            m = open('manavexe.txt','r')
            print(m.read())

        else:
            v = open('manavdiet.txt','r')
            print(v.read())
            
    else:
        if infoo==1:
            y = open('yashexe.txt','r')
            print(y.read())
        else:
            h = open('yashdiet.txt','r')
            print(h.read())


def lockk():
    if person==1:
        if infoo==1:
            exerciser = input("Enter the excercise name : ")
            re = open('rahulexe.txt','a')
            re.write(f'[{datetime.today()}] {exerciser} \n')
        else:
            dietr = input("Enter the diet name : ")
            rd = open('rahuldiet.txt','a')
            rd.write(f'[{datetime.today()}] {dietr} \n')

    elif person==2:
        if infoo==1:
            exercisem = input("Enter the excercise name : ")
            me = open('manavexe.txt','a')
            me.write(f'[{datetime.today()}] {exercisem} \n')
        else:
            dietm = input("Enter the excercise name : ")
            me = open('manavdiet.txt','a')
            me.write(f'[{datetime.today()}] {dietm} \n')
             
    else:
        if infoo==1:
            exercisey = input("Enter the excercise name : ")
            ye = open('yashexe.txt','a')
            ye.write(f'[{datetime.today()}] {exercisey} \n')
        else:
            diety = input("Enter the diet name : ")
            yd = open('yashdiet.txt','a')
            yd.write(f'[{datetime.today()}] {diety} \n')
                    
    

if choicee==1:
    lockk()
else:
    showw()





