from tkinter import *

 
ttt = Tk()

ttt.title("Tic Tac Toe")
userinput1 = StringVar()
userinput2 = StringVar()
butt1 = Button(ttt)
result= StringVar()


ttt.config(bg='#624120')
op = ""
x = ""
y = ""

#name input of player 1
intro1 = Label(ttt,font=("ariel",10),fg="white",bg='#624120',text= "Enter name of player 1").grid(row=0)


plyr1name = Entry(ttt,font=("ariel",10),textvariable=userinput1)
plyr1name.grid(row=0,column=1)
plyr1name.focus_set()
buttu1 = Button(ttt,font=("ariel",10,"bold"),bg="white",fg="blue",text="X",command=lambda:getus1())
buttu1.grid(row=0, column= 2)

def getus1():
    global userinput1
    global x
    x += userinput1.get()
    return x



#name input of player 2
intro2 = Label(ttt,font=("ariel",10),fg="white",bg='#624120',text= "Enter name of player 2").grid(row=2)

plyr2name = Entry(ttt,font=("ariel",10),textvariable=userinput2).grid(row=2,column=1)

buttu2 = Button(ttt,font=("ariel",10,"bold"),bg="white",fg="red",text="O",command=lambda:getus2())
buttu2.grid(row=2, column= 2)


def getus2():
    global userinput2
    global y
    y += userinput2.get()
    return y


#result display 
tDisplay = Entry(ttt,font = ("Bradley Hand ITC", 20 ,'bold'),justify='center',bg="#322111",fg= "white",textvariable=result,relief= RAISED,bd=20)
tDisplay.grid(columnspan=3)

#creating the buttons

butt1 = Button(ttt,font=("Bradley Hand ITC",60,'bold'),bd=5,bg='#edd1b0',fg="black",anchor=CENTER,text="   ",command = lambda:buttclick1())
butt1.grid(row= 6,column =0)

butt2 = Button(ttt,font=("Bradley Hand ITC",60,'bold'),bd=5,bg='#edd1b0',fg="black",anchor=CENTER,text="   ",command = lambda:buttclick2())
butt2.grid(row= 6,column =1)

butt3 = Button(ttt,font=("Bradley Hand ITC",60,'bold'),bd=5,bg='#edd1b0',fg="black",anchor=CENTER,text="   ",command = lambda:buttclick3())
butt3.grid(row= 6,column =2)

butt4 = Button(ttt,font=("Bradley Hand ITC",60,'bold'),bd=5,bg='#edd1b0',fg="black",anchor=CENTER,text="   ",command = lambda:buttclick4())
butt4.grid(row= 7,column =0)

butt5 = Button(ttt,font=("Bradley Hand ITC",60,'bold'),bd=5,bg='#edd1b0',fg="black",anchor=CENTER,text="   ",command = lambda:buttclick5())
butt5.grid(row= 7,column =1)

butt6 = Button(ttt,font=("Bradley Hand ITC",60,'bold'),bd=5,bg='#edd1b0',fg="black",anchor=CENTER,text="   ",command = lambda:buttclick6())
butt6.grid(row= 7,column =2)

butt7 = Button(ttt,font=("Bradley Hand ITC",60,'bold'),bd=5,bg='#edd1b0',fg="black",anchor=CENTER,text="   ",command = lambda:buttclick7())
butt7.grid(row= 8,column =0)

butt8 = Button(ttt,font=("Bradley Hand ITC",60,'bold'),bd=5,bg='#edd1b0',fg="black",anchor=CENTER,text="   ",command = lambda:buttclick8())
butt8.grid(row= 8,column =1)

butt9 = Button(ttt,font=("Bradley Hand ITC",60,'bold'),bd=5,bg='#edd1b0',fg="black",anchor=CENTER,text="   ",command = lambda:buttclick9())
butt9.grid(row= 8,column =2)





inputs = ["O"]


#defining how the buttons will function on click

def buttclick1():
    global inputs

    if len(inputs)%2==1:

        butt1.config(text="X",fg="blue")
    
        inputs.append("X")

    else:

        butt1.config(text="O",fg="red")
        
        inputs.append("O")
    
    buttcheck()

def buttclick2():
    global inputs

    if len(inputs)%2==1:

        butt2.config(text="X",fg="blue")
    
        inputs.append("X")

    else:

        butt2.config(text="O",fg="red")
        
        inputs.append("O")

    buttcheck()


def buttclick3():
    global inputs

    if len(inputs)%2==1:

        butt3.config(text="X",fg="blue")
    
        inputs.append("X")

    else:

        butt3.config(text="O",fg="red")
        
        inputs.append("O")
    buttcheck()

def buttclick4():
    global inputs

    if len(inputs)%2==1:

        butt4.config(text="X",fg="blue")
    
        inputs.append("X")

    else:

        butt4.config(text="O",fg="red")
        
        inputs.append("O")

    buttcheck()
def buttclick5():
    global inputs

    if len(inputs)%2==1:

        butt5.config(text="X",fg="blue")
    
        inputs.append("X")

    else:

        butt5.config(text="O",fg="red")
        
        inputs.append("O")

    buttcheck()
def buttclick6():
    global inputs

    if len(inputs)%2==1:

        butt6.config(text="X",fg="blue")
    
        inputs.append("X")

    else:

        butt6.config(text="O",fg="red")
        
        inputs.append("O")

    buttcheck()
def buttclick7():
    global inputs

    if len(inputs)%2==1:

        butt7.config(text="X",fg="blue")
    
        inputs.append("X")

    else:

        butt7.config(text="O",fg="red")
        
        inputs.append("O")

    buttcheck()
def buttclick8():
    global inputs

    if len(inputs)%2==1:

        butt8.config(text="X",fg="blue")
    
        inputs.append("X")

    else:

        butt8.config(text="O",fg="red")
        
        inputs.append("O")

    buttcheck()
def buttclick9():
    global inputs

    if len(inputs)%2==1:

        butt9.config(text="X",fg="blue")
    
        inputs.append("X")

    else:

        butt9.config(text="O",fg="red")
        
        inputs.append("O")

    buttcheck()

#games algorithm
def buttcheck():
    global result
    global op
    global x
    global y

    #for Xs
    if butt1['text']=="X" and butt2['text']=="X" and butt3['text']=="X" :
        print(x)
        op = x + " wins"
        result.set(op)
        


    if butt4['text']=="X" and butt5['text']=="X" and butt6['text']=="X" :
        op = x + " wins"
        result.set(op)

    if butt7['text']=="X" and butt8['text']=="X" and butt9['text']=="X" :
        op = x + " wins"
        result.set(op)

    if butt1['text']=="X" and butt4['text']=="X" and butt7['text']=="X" :
        op = x + " wins"
        result.set(op)

    if butt2['text']=="X" and butt5['text']=="X" and butt8['text']=="X" :
        op = x + " wins"
        result.set(op)

    if butt3['text']=="X" and butt6['text']=="X" and butt9['text']=="X" :
        op = x + " wins"
        result.set(op)

    if butt1['text']=="X" and butt5['text']=="X" and butt9['text']=="X" :
        op = x + " wins"
        result.set(op)

    if butt3['text']=="X" and butt5['text']=="X" and butt7['text']=="X" :
        op = x + " wins"
        result.set(op)

    #for Os

    if butt1['text']=="O" and butt2['text']=="O" and butt3['text']=="O" :
        op = y + " wins"
        result.set(op)

    if butt4['text']=="O" and butt5['text']=="O" and butt6['text']=="O" :
        op = y + " wins"
        result.set(op)


    if butt7['text']=="O" and butt8['text']=="O" and butt9['text']=="O" :
        op = y + " wins"
        result.set(op)


    if butt1['text']=="O" and butt4['text']=="O" and butt7['text']=="O" :
        op = y + " wins"
        result.set(op)


    if butt2['text']=="O" and butt5['text']=="O" and butt8['text']=="O" :
        op = y + " wins"
        result.set(op)


    if butt3['text']=="O" and butt6['text']=="O" and butt9['text']=="O" :
        op = y + " wins"
        result.set(op)


    if butt1['text']=="O" and butt5['text']=="O" and butt9['text']=="O" :
        op = y + " wins"
        result.set(op)


    if butt3['text']=="O" and butt5['text']=="O" and butt7['text']=="O" :
        op = y + " wins"
        result.set(op)


    

ttt.mainloop()