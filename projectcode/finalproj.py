from tkinter import *
import tkinter.messagebox
import sqlite3
conn=sqlite3.connect("test5.db")
print("CONNECT")
def create_table():
    signup_query=str("CREATE TABLE IF NOT EXISTS details(ID INTEGER PRIMARY KEY AUTOINCREMENT,"+
                     "details_name VARCHAR,"+
                     "details_score INTEGER)")
    conn.execute(signup_query)
    print("created score table")


def reprint(lst, x, y, sf, f):
    num=lst[x][y]
    merge(lst, x, y ,num)
    lst[x][y]=num+1
    generate_numbers(lst)
    sf.destroy()
    f.destroy()
    buttons(lst)

def generate_numbers(lst):
    zeros=obtain_Zeros(lst)
    for i in zeros:
        lst[i[0]][i[1]]=lst[i[0]-1][i[1]]


                

def nomoves(lst):
    length = len(lst)
    for i in range(0, length):
        for j in range(0, length):
            if (i - 1 >= 0 and i < 4 and j >= 0 and j < 4):
                if (lst[i - 1][j] == lst[i][j]):
                    return False
            if (i >= 0 and i + 1 < 4 and j >= 0 and j < 4):
                if (lst[i + 1][j] == lst[i][j]):
                    return False
            if (i >= 0 and i < 4 and j - 1 >= 0 and j < 4):
                if (lst[i][j - 1] == lst[i][j]):
                    return False
            if (i >= 0 and i < 4 and j >= 0 and j + 1 < 4):
                if (lst[i][j + 1] == lst[i][j]):
                    return False
    return True


def merge(lst, x, y,num):
    flag=0
    if (x >= 0 and y < 5) :
        nxt_row = x + 1
        nxt_col = y + 1
        prev_row = x - 1
        prev_col = y - 1
        if (nxt_col < 4):
            if (lst[x][nxt_col] == num):
                lst[x][nxt_col] = 0
                flag=1
                merge(lst, x, nxt_col,num)
        if (prev_col >= 0):
            if (lst[x][prev_col] == num):
                lst[x][prev_col] = 0
                flag=1
                merge(lst, x, prev_col,num)
        if (nxt_row < 4):
            if (lst[nxt_row][y] == num):
                lst[nxt_row][y] = 0
                flag=1
                merge(lst, nxt_row, y,num)
        if (prev_row >= 0):
            if (lst[prev_row][y] == num):
                lst[prev_row][y] = 0
                flag=1
                merge(lst, prev_row, y,num)
        if(flag==1):
            lst[x][y]=0

def score(lst):
    score = 0
    for i in lst:
        for j in i:
            score = score + 5 * j
    return score


def drop(lst):
    for i in lst:
        for j in i:
            if (j == 0):
                x = i.index(j)
                i.insert(0, 0)
                i.pop(x + 1)


def switch(x):
    if (x == 1):
        return "cyan"
    elif (x == 2):
        return "pink"
    elif (x == 3):
        return "green"
    elif (x == 4):
        return "red"
    elif (x == 5):
        return "blue"
    elif (x == 6):
        return "brown"
    elif (x == 7):
        return "orange"
    elif (x == 8):
        return "pink"
    elif (x == 9):
        return "magenta"
    elif (x == 10):
        return "gray"
    elif (x == 11):
        return "lightblue"
    elif (x == 12):
        return "lightgray"
    elif (x == 13):
        return "red"


def max_number(lst):  # function to find maximum number
    length = len(lst)  # provides length of single matrix
    max_lst = []
    for i in lst:
        max_lst.append(max(i))
    max_number = max(max_lst)
    return (max_number)  # returns maximam of a 2D list


def exit(event):
    root.quit()


def quit(self):
    self.quit()


def destroy(f1, lst):
    f1.destroy()
    buttons(lst)


def menu(lst ,f, sf):
    f.destroy()
    sf.destroy()
    startup(lst)


def final():
    f1 = Frame(root, width=660, height=600, bg="yellow")
    f1.propagate(0)
    f1.pack()
    lb = Label(f1, text="MAKE IT 13!", font=('Showcard Gothic', 50, 'bold'), fg="purple", bg="yellow", bd=10)
    lb.pack()
    lb = Label(f1, text="NAME", font=('rockwell extra bold', 40, 'bold'), fg="red", bd=10, bg="yellow")
    lb.place(x=0, y=150)
    e1 = Entry(f1, fg="blue", bd=15, bg="white", width=40)
    e1.place(x=240, y=170)
    lb = Label(f1, text="SCORE", font=('rockwell extra bold', 40, 'bold'), fg="red", bd=10, bg="yellow")
    lb.place(x=0, y=250)
    e1 = Entry(f1, fg="blue", bd=15, bg="white", width=40)
    e1.place(x=240, y=270)
    lb = Label(f1, text="TO SHOWCASE YOUR SKILLS AGAIN", font=('rockwell extra bold', 20, 'bold'), fg="BLUE", bd=10,
               bg="yellow")
    lb.place(x=20, y=370)
    b = Button(f1, text="REPLAY", padx=7, pady=7, bd=6, fg="blue", font=('rockwell extra bold', 30, 'bold'),
               command=lambda: destroy(f1))
    b.place(x=170, y=430)


def gameover(self, self1):
    self.destroy()
    self1.destroy()
    final()


def replay(lst, f):
    f.destroy()
    buttons(lst)

def about(lst,f2):
    f2.destroy()
    f1 = Frame(root, width=660, height=600, bg="yellow")
    f1.propagate(0)
    f1.pack()
    l1=Label(f1,text="ABOUT US",font=('rockwell extra bold' ,25, 'bold'),bg="yellow",fg="purple").pack()
    l2=Label(f1,text="The project is based on a popular\n game based on IOS we have used tkinter library \nto make it.\nThe name of the game is MAKE IT 13!! \n This game is about adding two numbers\n in a block form.\nAll the blocks are merged together and brought \nin one colour as the number is incremented.\n\nThis game was made by us to put in\ninterset in people and also test skills\n\n\nENJOY PLAYING!!! ",font=('lucida calligraphy', 17,"bold"),bg="yellow",fg="red").place(x=0,y=60)

def lastpage(lst, sf, f):
    def insert_table():
            name=e1.get()
            score=scorestring
            query=str("INSERT INTO details(details_name, details_score) VALUES(?,?)")
            conn.execute(query,(name,score,))
            conn.commit()
            print("adding in database is done")
            replay(lst ,f1)

    scorestring=str(score(lst))
    sf.destroy()
    f.destroy()
    f1 = Frame(root, width=660, height=600, bg="yellow")
    f1.propagate(0)
    f1.pack()
    lb = Label(f1, text="MAKE IT 13!", font=('Showcard Gothic', 50, 'bold'), fg="purple", bg="yellow", bd=10)
    lb.pack()
    lb = Label(f1, text="NAME", font=('rockwell extra bold', 40, 'bold'), fg="red", bd=10, bg="yellow")
    lb.place(x=0, y=150)
    e1 = Entry(f1, fg="blue", bd=15, bg="white", width=40)
    e1.place(x=240, y=170)
    if(e1.get()!=''):
       insert_table()
        
    lb = Label(f1, text="SCORE:", font=('rockwell extra bold', 40, 'bold'), fg="red", bd=10, bg="yellow")
    lb.place(x=0, y=250)
    e2 =Label(f1, text=scorestring ,font=('rockwell extra bold', 40 ,'bold'),fg="red",bd=10, bg="yellow")
    e2.place(x=240, y=250)
    lb = Label(f1, text="TO SHOWCASE YOUR SKILLS AGAIN", font=('rockwell extra bold', 20, 'bold'), fg="BLUE", bd=10,
               bg="yellow")
    lb.place(x=20, y=370)
    b = Button(f1, text="REPLAY", padx=7, pady=7, bd=6, fg="blue", font=('rockwell extra bold', 30, 'bold'),
               command=insert_table)
    b.place(x=170, y=430)


def buttons(lst):
    maxnumber = str(max_number(lst))
    scorestring = str(score(lst))
    drop(lst)
    sf = Frame(root, bg="yellow", width=660, height=600)
    sf.pack()
    sf.pack_propagate(0)
    la = Label(sf, text="SCORE", font=('arial,50,bold'), fg="black", bd=8, bg="yellow", padx=40, pady=20)
    la.grid(row=0, column=0, sticky=E)
    la1 = Label(sf, text="MOVES", font=('arial,30,bold'), fg="black", bd=8, bg="yellow", padx=40, pady=20)
    la1.grid(row=0, column=1, sticky=E)
    la2 = Label(sf, text="MAX", font=('arial,30,bold'), fg="black", bd=8, bg="yellow", padx=40, pady=20)
    la2.grid(row=0, column=2, sticky=E)
    l1 = Label(sf, text=scorestring, bg="yellow")
    l1.place(x=80, y=50)
    l2 = Label(sf, text="20", bg="yellow")
    l2.place(x=235, y=50)
    l3 = Label(sf, text=maxnumber, bg="yellow")
    l3.place(x=380, y=50)

    f = Frame(root, bg="yellow", width=660, height=600)
    f.pack()
    f.pack_propagate(0)
    b0 = Button(f, text="X", padx=30, pady=15, bd=10, fg="white", bg="red", command=lambda: menu(lst,f, sf))
    b0.place(x=500, y=30)
    b1 = Button(f, text=str(lst[0][0]), width=15, height=6, bg=switch(lst[0][0]),
                command=lambda: reprint(lst, 0, 0, sf, f))
    b1.place(x=100, y=120)

    b2 = Button(f, text=str(lst[1][0]), width=15, height=6, bg=switch(lst[1][0]),
                command=lambda: reprint(lst, 1, 0, sf, f))
    b2.place(x=215, y=120)

    b3 = Button(f, text=str(lst[2][0]), width=15, height=6, bg=switch(lst[2][0]),
                command=lambda: reprint(lst, 2, 0, sf, f))
    b3.place(x=330, y=120)

    b4 = Button(f, text=str(lst[3][0]), width=15, height=6, bg=switch(lst[3][0]),
                command=lambda: reprint(lst, 3, 0, sf, f))
    b4.place(x=445, y=120)

    b5 = Button(f, text=str(lst[0][1]), width=15, height=6, bg=switch(lst[0][1]),
                command=lambda: reprint(lst, 0, 1, sf, f))
    b5.place(x=100, y=221)

    b6 = Button(f, text=str(lst[1][1]), width=15, height=6, bg=switch(lst[1][1]),
                command=lambda: reprint(lst, 1, 1, sf, f))
    b6.place(x=215, y=221)

    b7 = Button(f, text=str(lst[2][1]), width=15, height=6, bg=switch(lst[2][1]),
                command=lambda: reprint(lst, 2, 1, sf, f))
    b7.place(x=330, y=221)

    b8 = Button(f, text=str(lst[3][1]), width=15, height=6, bg=switch(lst[3][1]),
                command=lambda: reprint(lst, 3, 1, sf, f))
    b8.place(x=445, y=221)

    b9 = Button(f, text=str(lst[0][2]), width=15, height=6, bg=switch(lst[0][2]),
                command=lambda: reprint(lst, 0, 2, sf, f))
    b9.place(x=100, y=322)

    b10 = Button(f, text=str(lst[1][2]), width=15, height=6, bg=switch(lst[1][2]),
                 command=lambda: reprint(lst, 1, 2, sf, f))
    b10.place( x=215, y=322)

    b11 = Button(f, text=str(lst[2][2]), width=15, height=6, bg=switch(lst[2][2]),
                 command=lambda: reprint(lst, 2, 2, sf, f))
    b11.place(x=330, y=322)

    b12 = Button(f, text=str(lst[3][2]), width=15, height=6, bg=switch(lst[3][2]),
                 command=lambda: reprint(lst, 3, 2, sf, f))
    b12.place(x=445, y=322)

    b13 = Button(f, text=str(lst[0][3]), width=15, height=6, bg=switch(lst[0][3]),
                 command=lambda: reprint(lst, 0, 3, sf, f))
    b13.place(x=100, y=423)

    b14 = Button(f, text=str(lst[1][3]), width=15, height=6, bg=switch(lst[1][3]),
                 command=lambda: reprint(lst, 1, 3, sf, f))
    b14.place(x=215, y=423)

    b15 = Button(f, text=str(lst[2][3]), width=15, height=6, bg=switch(lst[2][3]),
                 command=lambda: reprint(lst, 2, 3, sf, f))
    b15.place(x=330, y=423)

    b16 = Button(f, text=str(lst[3][3]), width=15, height=6, bg=switch(lst[3][3]),
                 command=lambda: reprint(lst, 3, 3, sf, f))
    b16.place(x=445, y=423)

    b23 = Button(f, text="MENU", padx=30, pady=5, bd=10, bg="blue", fg="white", command=lambda: menu(lst ,f, sf))
    b23.place(x=500, y=550)
    moves = nomoves(lst)
    if (moves == True):
        tkinter.messagebox.showinfo("No Moves", "No further possible moves")
        lastpage(lst, sf, f)

    
def obtain_Zeros(lst):     #returns the position of all the zeros in the list
    zero_List=[]
    for i in range(0,len(lst)):
       for j in range(0,len(lst[i])):
          if(lst[i][j]==0):
                zero_List.append([i,j])
    return zero_List

def startup(lst):
    f1 = Frame(root, bg="yellow", width=660, height=800)
    f1.pack()
    f1.pack_propagate(0)
    lb = Label(f1, text="MAKE IT 13!", font=('Showcard Gothic', 50, 'bold'), fg="purple", bg="yellow", bd=10)
    lb.pack()
    lb = Label(f1, text="Train Your Brain", font=('rockwell extra bold', 40, 'italic'), fg="red", bg="yellow", bd=10)
    lb.pack()
    b = Button(f1, text="PLAY", padx=40, pady=20, bd=8, fg="black", font=('Segoe UI Black', 30, 'bold'),
               command=lambda: destroy(f1, lst))
    b.pack()
    b = Button(f1, text="ABOUT", padx=20, pady=20, bd=8, fg="black", font=('Segoe UI Black', 30, 'bold'),
               command=lambda: about(lst,f1))
    b.pack()
    b = Button(f1, text="EXIT", padx=47, pady=20, bd=8, fg="black", font=('Segoe UI Black', 30, 'bold'),
               command=root.destroy)
    b.pack()

lst = [[10, 10, 0,0], [9, 8, 7, 6], [5, 4, 3, 2], [1, 9, 12, 3]]


create_table()

result = conn.execute("select * from details")
for i in result:
    print("id = ",i[0])

root = Tk()
root.title("MAKE IT 13!")
startup(lst)
root.mainloop()
