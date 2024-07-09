import mysql.connector as my
from random import *
from tkinter import *
import turtle
import pickle
import time

def instructo():
    root.destroy()
    root1=Tk()
    root1.geometry("700x600")
    bg1=PhotoImage(file="bg02.png")
    label0=Label(root1,image=bg1)
    label0.place(x=0,y=0,relwidth=1,relheight=1)

    label3=Label(root1,
                 text='''                                              Instructions 
    The target of the game is to move the player i.e "yellow square" to the
    end point i.e "red circle", by moving through the maze.

    Controls:

    Upper arrow key : To move Up
    Down arrow key :  To move Down
    Right arrow key : To move Right
    Left arrow key :  To move Left

    *Win the Rock,Paper and Scissor game after this to know a secret trick. 
    ''',
                 font=("Times New Roman",18),
                 bd=1,relief='sunken',fg='black',bg="#f8f1d0",justify=LEFT)
    label3.pack(pady=50,ipadx=10,fill=BOTH)

    exit_button=Button(root1,text="Understood",command=root1.destroy,
                       font=("Impact",22),bg='#ffcc00',fg='black')
    exit_button.pack(pady=20)
    root1.mainloop()


def leader():
    root.destroy()
    global level
    root1=Tk()
    root1.geometry('300x300')
    bg1=PhotoImage(file="bg04.png")
    label0=Label(root1,image=bg1)
    label0.place(x=0,y=0,relwidth=1,relheight=1)



    label2=Label(root1,
                 text="Select Level",
                 font=("Times New Roman",25,"bold"),
                 bd=1,relief='sunken',bg='#006680',fg='white')
    label2.pack(pady=20,ipady=10,ipadx=10)


    level=1
    def lev(event):
        global level
        if clicked.get()=='Level 1':
            level=1
        elif clicked.get()=='Level 2':
            level=2
        elif clicked.get()=='Level 3':
            level=3
        elif clicked.get()=='Level 4':
            level=4
        elif clicked.get()=='Level 5':
            level=5

    options=[
        'Level 1',
        'Level 2',
        'Level 3',
        'Level 4',
        'Level 5',
        ]

    clicked=StringVar()
    clicked.set(options[0])

    drop=OptionMenu(root1,clicked,*options,command=lev)
    drop.pack(pady=20,ipady=20,ipadx=20,fill=BOTH)

    
    exit_button=Button(root1,text="SHOW",command=root1.destroy,
                       font=("Times New Roman",22),relief="groove",
                       bg='azure',fg='black')
    exit_button.pack(pady=20)

    root1.mainloop()

    rankings(level)


def box():
    root=Tk()
    bg1=PhotoImage(file="bg02.png")
    label0=Label(root,image=bg1)
    label0.place(x=0,y=0,relwidth=1,relheight=1)
    label3=Label(root,
             text='''A Great Time Saver:
    Press and hold the key for rapid movement in corresponding direction''',
             font=("Times New Roman",18),
             bd=1,relief='sunken',bg='#e7e1d2',fg='black',justify=LEFT)
    label3.pack(pady=40,ipadx=10,fill=BOTH,anchor="center")


    exit_button=Button(root,text=" Got It ",command=root.destroy,
                       font=("Impact",22),bg='#ffcc00',fg='black',relief="ridge")
    exit_button.pack(pady=40)
    root.mainloop()



def addrec(t1,names,t,level):
        mydb=my.connect(
            host="localhost",
            database="high scores",
            user="root",
            password="1234")
        mycursor=mydb.cursor()
        val=(t1,names.strip(),t,level)
        sql="insert into rankings(sort,name,time,level) values(%s,%s,%s,%s)"
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
        mydb.close()

                

        
def rps():
    root=Tk()
    root.geometry('500x600')
    bg1=PhotoImage(file="bg02.png")
    label0=Label(root,image=bg1)
    label0.place(x=0,y=0,relwidth=1,relheight=1)
    rockimage=PhotoImage(file="rock2.png")
    paperimage=PhotoImage(file="paper2.png")
    scissorimage=PhotoImage(file="scissor2.png")
    objimages=[rockimage,paperimage,scissorimage]
    Modes=[
        ("Rock   ","a",0),
        ("Paper  ","b",1),
        ("Scissor","c",2)]
    
    mini=StringVar()
    l=["Rock","Paper","Scissor"]
    r=choice(l)
    mini.set(r)

    for option,valu,numb in Modes:
        Radiobutton(root,text=option,variable=mini,
                    font=("Impact",20),indicatoron=0,
                    image=objimages[numb],compound='left',
                    width=250,value=valu).pack(anchor=CENTER)
    def selected(value):
        l=["a","b","c"]
        z=choice(l)
        if z==value:
            mylabel=Label(root,text="try again")
            mylabel.pack()
        elif z=="a":
            if value=="c":
                root.destroy()
                box()
            else:
                mylabel=Label(root,text="try again")
                mylabel.pack()
        elif z=="b":
            if value=="a":
                root.destroy()
                box()
            else:
                mylabel=Label(root,text="try again")
                mylabel.pack()
        elif z=="c":
            if value=="b":
                root.destroy()
                box()
                
            else:
                mylabel=Label(root,text="try again")
                mylabel.pack()
                    
    myButton=Button(root,text="Continue",command=lambda:selected(mini.get()),
                    font=("Times New Roman",22),bg='#ffcc00',
                    fg='black',relief="ridge")
    myButton.pack(pady=30)

    root.mainloop()


    
def calling():
    global repeat
    repeat=1
    root.destroy()
    rps()
    play()

def convert(sec):
        mins=sec//60
        sec=sec%60
        hours=mins//60
        mins=mins%60
        a,b,c=int(hours),int(mins),sec
        return a,b,c



def rankings(level):
        mydb=my.connect(
            host="localhost",
            database="high scores",
            user="root",
            password="1234")
        s="select * from rankings"
        mycursor=mydb.cursor()
        mycursor.execute("alter table rankings drop column rank")
        mydb.commit()
        mycursor.execute(s)
        m=mycursor.fetchall()
        m.sort()
        mycursor.execute("delete from rankings")
        mydb.commit()
        mycursor.execute("alter table rankings add rank int")
        mydb.commit()
        c=1
        for i in m:
            i1=i+(c,)
            if i1[3]==level:
                sql1="""insert into rankings(sort,name,time,level,rank) values(%s,%s,%s,%s,%s)"""
                mycursor.execute(sql1,i1)
                mydb.commit()
                c=c+1
            else:
                sql1="""insert into rankings(sort,name,time,level) values(%s,%s,%s,%s)"""
                mycursor.execute(sql1,i)
                mydb.commit()
        q="select rank,name,time from rankings "
        q1=q+"where level="+str(level)+";"
        mycursor.execute(q1)
        myresult=mycursor.fetchall()
        zlx="LEADERBOARD FOR LEVEL "+str(level)+":"
        mycursor.close()
        mydb.close()
        
        l5=""
        for x in myresult:
            l=list(x)
            l[0]=str(l[0])
            l5=l5+' '.join(l)+"\n"

        root=Tk()

        label3=Label(root,
                     text=zlx+"\n"+l5,
                     font=("Times New Roman",18),
                     bd=1,relief='sunken',bg='#eae4dd',fg='black',justify=LEFT)
        label3.pack(ipady=0,ipadx=10,fill=BOTH)

        exit_button=Button(root,text=" OK ",command=root.destroy,font=(18),bg='#987654',fg='white')
        exit_button.pack(pady=20)
        root.mainloop()

def turt(levels):
    wn=turtle.Screen()
    wn.bgcolor("black")
    wn.title("MAZE")
    wn.setup(1000,700)


    class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("azure")
            self.penup()
            self.speed(0)
    class Player(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("yellow")
            self.penup()
            self.speed(0)
        def up(self):
            movex=player.xcor()
            movey=player.ycor()+24
            if (movex,movey) not in walls:
                self.goto(self.xcor(),self.ycor()+24)
        def down(self):
            movex=player.xcor()
            movey=player.ycor()-24
            if (movex,movey) not in walls:
                self.goto(self.xcor(),self.ycor()-24)
        def right(self):
            movex=player.xcor()+24
            movey=player.ycor()
            if (movex,movey) not in walls:
                self.goto(self.xcor()+24,self.ycor())
        def left(self):
            movex=player.xcor()-24
            movey=player.ycor()
            if (movex,movey) not in walls:
                self.goto(self.xcor()-24,self.ycor())
        def collide(self,other):
            a=self.xcor()-other.xcor()
            b=self.ycor()-other.ycor()
            if (a**2+b**2)<5:
                return True
            else:
                return False
    class Treasure(turtle.Turtle):
        def __init__(self,x,y):
            turtle.Turtle.__init__(self)
            self.shape("circle")
            self.color("red")
            self.penup()
            self.speed(0)
            self.goto(x,y)
        def destroy(self):
            self.goto(2000,2000)
            self.hideturtle()

    T=[]
    def setup_maze(level):
        for y in range(len(level)):
            for x in range(len(level[y])):
                char=level[y][x]
                screen_x=-410+(x*24)
                screen_y=340-(y*24)
                if char=="X" or char=="O":
                    pen.goto(screen_x,screen_y)
                    pen.stamp()
                    walls.append((screen_x,screen_y))
                if char=="P":
                    player.goto(screen_x,screen_y)
                if char=="T":
                    T.append(Treasure(screen_x,screen_y))


                           
    pen=Pen()
    player=Player()

    walls=[]

    setup_maze(levels[1])
    start=time.time()
    turtle.listen()
    turtle.onkeypress(player.left,"Left")
    turtle.onkeypress(player.right,"Right")
    turtle.onkeypress(player.up,"Up")
    turtle.onkeypress(player.down,"Down")
    wn.tracer(0)
    c=0
    while True:
        for i in T:
            if player.collide(i):
                i.destroy()
                T.remove(i)
                turtle.Screen().bye()
                stop=time.time()
                c=1
               
                root=Tk()
                bg1=PhotoImage(file="bg04.png")
                label0=Label(root,image=bg1)
                label0.place(x=0,y=0,relwidth=1,relheight=1)
                q,v,w=convert(stop-start)
                label3=Label(root,
                text="time taken "+str(q)+":"+str(v)+":"+str(int(w))+"."+str(int((w-int(w))*1000)),
                font=("Times New Roman",18),
                bd=1,relief='sunken',bg='white',fg='red')
                label3.pack(pady=20,ipady=10,ipadx=10)
                endb=Button(root,text=" OK ",command=root.destroy,
                            font=("Times New Roman",22),relief="ridge",
                            bg='brown',fg='white')
                endb.pack(pady=20)
                root.mainloop()
               
        if c==1:
            break
        wn.update()

       

    t=str(q)+":"+str(v)+''':'''+str(int(w))+"."+str(int((w-int(w))*1000))
    t1=stop-start
    return t1,t

    



names=''
level=[]
def play():
    global level
    root=Tk()
    root.geometry("500x500")
    bg1=PhotoImage(file="bg05.png")
    label0=Label(root,image=bg1)
    label0.place(x=0,y=0,relwidth=1,relheight=1)
    label1=Label(root,
                 text="Enter Your Name",
                 font=("Times New Roman",30,"bold"),
                 bd=1,relief='sunken',bg='#004455',fg='#ffffff')
    label1.pack(pady=40,ipady=10,ipadx=10)


       
    def get_text():
        global names
        names=my_text.get()
        root.destroy()
       
    my_text=Entry(root,font=("Times New Roman",25,"bold"),
                  fg="#004455",bd=3,relief='ridge')
    my_text.pack(pady=20)


    button_frame=Frame(root)
    button_frame.pack()    

    get_text_button=Button(root, text="OK", command=get_text,
                           font=("Times New Roman",25),bg='#ffcc00',fg='black')
    get_text_button.pack(pady=30)
    root.mainloop()



    root=Tk()
    root.geometry('500x500')
    bg1=PhotoImage(file="bg03.png")
    label0=Label(root,image=bg1)
    label0.place(x=0,y=0,relwidth=1,relheight=1)

    label2=Label(root,
                 text="Select Level",
                 font=("Times New Roman",25,"bold"),
                 bd=1,bg='#ffcc00',fg='dark blue')
    label2.pack(pady=30,ipady=10,ipadx=10)


    level=1
    def lev(event):
        global level
        if clicked.get()=='Level 1':
            level=1
        elif clicked.get()=='Level 2':
            level=2
        elif clicked.get()=='Level 3':
            level=3
        elif clicked.get()=='Level 4':
            level=4
        elif clicked.get()=='Level 5':
            level=5

    options=[
        'Level 1',
        'Level 2',
        'Level 3',
        'Level 4',
        'Level 5',
        ]

    clicked=StringVar()
    clicked.set(options[0])

    drop=OptionMenu(root,clicked,*options,command=lev)
    drop.pack(pady=30,ipady=20,ipadx=20,fill=BOTH)

    
    exit_button=Button(root,text="LET'S PLAY",command=root.destroy,
                       font=("Times New Roman",20,"bold"),relief="groove",bg='white',fg='dark blue')
    exit_button.pack(pady=30)

    root.mainloop()



        
        

    levels=[""]

    f=open("mazes.txt","rb")
    for i in range(1,level+1):
        x=pickle.load(f)
        if i==level:
            levels.append(x)
            break
    f.close()
    t1,t=turt(levels)

    


    
    addrec(t1,names,t,level)
    rankings(level)
def escape():
    global repeat
    root.destroy()
    repeat=1
repeat=0

while repeat==0:
    root=Tk()
    root.geometry('800x575')
    bg1=PhotoImage(file="title2.png")
    label00=Label(root,image=bg1)
    label00.place(x=0,y=0,relwidth=1,relheight=1)

    button_frame=Frame(root)
    button_frame.pack()

    play_button=Button(root,text="      PLAY       ",command=calling,font=("Helvetica",20,"bold"),
                       relief="ridge",bg='dark blue',fg='white',width=14)
    play_button.place(x=300,y=250)

    instruction_button=Button(root,text='  Instructions  ', command=instructo,font=("Helvetica",20,"bold"),
                              relief="ridge",bg='orange',fg='white',width=14)
    instruction_button.place(x=300,y=320)

    leaderboard_button=Button(root,text="  Leaderboard ",command=leader,font=("Helvetica",20,"bold"),
                              relief="ridge",bg='brown',fg='white',width=14)
    leaderboard_button.place(x=300,y=400)

    exit_button=Button(root,text="       EXIT        ",command=escape,font=("Helvetica",20,"bold"),
                       relief="ridge",bg='black',fg='white',width=14)
    exit_button.place(x=300,y=480)

    root.mainloop()









