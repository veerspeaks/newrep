from tkinter import *

cal = Tk()
cal.title("Calculator")
op = ""
textinput = StringVar()
textresult = StringVar()
x = "powder blue"
y = "black"
textDisplay = Entry(cal, font=('ariel', 20, 'bold'), textvariable=textinput, bd=30, insertwidth=4, bg='white',
                    justify='right').grid(columnspan=4)

resultdisplay = Entry(cal,font=('ariel', 20, 'bold'), textvariable =textresult, bd = 5, insertwidth=2,bg= x ,fg= y,justify= 'right').grid(columnspan=3)


def butt(a, r, c):
    buta = Button(cal, padx=20, bd=8,height=1, fg=y, font=('arial', 20, 'bold'), text=a, bg=x,
                  command=lambda: buttclick(a)).grid(row=int(r),
                                                     column=int(
                                                         c))

butt(7, 2, 0)
butt(8, 2, 1)
butt(9, 2, 2)
butt('/', 2, 3)

butt(4, 3, 0)
butt(5, 3, 1)
butt(6, 3, 2)
butt('*', 3, 3)

butt(1, 4, 0)
butt(2, 4, 1)
butt(3, 4, 2)
butt('-', 4, 3)


butt(0, 5, 1)
butt('+', 5, 3)
buttClear = Button(cal, padx=16, bd=8,height=1, fg=y, font=('arial', 20, 'bold'), text="C", bg=x,command = lambda:buttC()).grid(row=int(5),
                                                     column=int(
                                                         0))
buttequal = Button(cal, padx=16, bd=8,height=1, fg=y, font=('arial', 20, 'bold'), text="=",  bg=x,command = lambda:buttEq()).grid(row=int(5),
                                                     column=int(
                                                         2))

def buttclick(num):
    global op
    op += str(num)
    textinput.set(op)


def buttC():
    global op
    op = ""
    textinput.set(op)
    
    textresult.set(op)

def buttEq() :
    global op
    result = str(eval(op))
    textresult.set(result)
    op = ""

butttheme = Button(cal, padx=1,height=1, bd=5, fg='white', font=('arial', 20, 'bold'), text="D",  bg='black',command = lambda:darkmode()).grid(row=int(1),
                                                     column=int(
                                                         3))


cal.mainloop()
