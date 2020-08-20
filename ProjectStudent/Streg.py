from tkinter import *
import mysql.connector as connector
import requests  
import json





student = Tk()
student.title("Student Register")

#welcome messages
welcome = Label(student,text="Welcome to Student Register",font=("calibri",36,"bold"))
welcome2 = Label(student,text="please choose the action you want to perform \n ",font=("calibri",10,"bold"))
welcome.pack()
welcome2.pack()

#declaring the fuction buttons
start1 = Button(student,text='Student Registration',padx =10,relief= RAISED,bg="orange",command=lambda:start1com())
start2 = Button(student,text='Fetcher',padx =10,relief= RAISED,bg="orange",command=lambda:start2com())
start1.pack(fill=X)
start2.pack(fill=X)

#ceating the frames associated with the buttons
frame1 = Frame()
frame2 = Frame()
#creating all the global variable that might be needed
N = ""
C = ""
M = ""
A = ""
s = ""
res = ""

searchresult = ""

#creating the string variables that might be needed
namein = StringVar()
classin = StringVar()
mobin = StringVar()
addin = StringVar()
searchin = StringVar()
resultout = StringVar()
resultshow = StringVar()

#declaring the first button command
def start1com():
    
    global frame1
    global frame2
    global N
    global M
    global C
    global A
    

    frame1 = Frame()
    
    label1 = Label(master=frame1,text="Enter the student details as following \n")
    label1.pack()

    #place for name entry
    labelname = Label(master=frame1,text ="Enter the name of the student")
    labelname.pack()

    entryname = Entry(master= frame1,textvariable= namein,width=60)
    entryname.pack()
    

    #place for class entry
    labelclass= Label(master=frame1,text ="Enter the class of the Student")
    labelclass.pack()
    

    entryclass = Entry(master= frame1,textvariable= classin,width=60)
    entryclass.pack()
    
    #place for mobile entry
    labelmobile = Label(master = frame1,text="Enter the mobile number of the student")
    labelmobile.pack()

    entrymobile = Entry(master = frame1 ,textvariable= mobin, width = 60)
    entrymobile.pack()
    
    #place for address entry
    labeladd = Label(master = frame1 ,text="Enter the address of the student")
    labeladd.pack()

    entryadd = Entry(master = frame1 ,textvariable= addin,width=60)
    entryadd.pack()
    
    
    #button to register the input to the database
    buttregister = Button(master = frame1 , text="REGISTER" ,font=("calibri",15,"bold"),padx =10,relief= RAISED,bg="orange"
                        ,command=lambda:[h.dataentry(),sendsms(mobin.get())])
                    
    buttregister.pack()


  
    #deesigned in a way so that the other frme is destroyed when another one is called
    frame1.pack()
    frame2.destroy()
    

#declaring the second button fuction
def start2com():
    
    global frame1
    global frame2
    global res
    global searchresult

    frame2 = Frame()
    label2 = Label(master=frame2,text="Fetch ",font=("futura",35,"bold"),fg="red")
    label2.pack()
    label3 = Label(master=frame2,text="Enter the keyword you want to search by \n ",font=("futura",10,"bold"))
    label3.pack()
    

    searchenter = Entry(master = frame2, textvariable = searchin ,width = 60 )
    searchenter.pack()

    photo = PhotoImage(file = "X:\Search.png" )
    photoimage = photo.subsample(5)
    

    #option = Menubutton(master = frame2 ,text = "test")
    #option.pack()

    
    #button that fecth the data from the database
    searchbutt = Button(master = frame2 , text = "search", image = photoimage , command = lambda:h.datafetcher() )
    searchbutt.image = photoimage
    searchbutt.pack()

    #place to show the search result
    searchresult = Text(master = frame2 , height = 10 , width = 30)
    searchresult.pack(fill = X)
    
    #similar function as of the frame 1
    frame2.pack()
    frame1.destroy()

    
#creating the class for managing the mysql database
class DBhelper:
    def __init__(self):
        self.connect = connector.connect(host="localhost", port="3306", user= "root", password= "IlTd7084@",database="Studentsdata")
        print("Connected")
        query = "create table if not exists student(name varchar(30),class varchar(2), mobile varchar(13),address varchar(300))"
        cur = self.connect.cursor()
        cur.execute(query)
        print("Table created succefully")
        
    #method to carry out the data entry process on button press
    def dataentry(self):
        
        global M
        global C
        global N
        global A
        
        

        

        N = namein.get()
        C = classin.get()
        M = mobin.get()
        A = addin.get()

        

        query= "insert into student(name,class,mobile,address) values('{}','{}','{}','{}')".format(N.casefold(),C,M,A)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("Updated")
        

    #method to fecth data from database and show it on button call
    def datafetcher(self):
        global s
        global res
        global searchresult
        
        s = searchin.get()

        

        query = "select * from Studentsdata.student"
        cur = self.connect.cursor()
        cur.execute(query)
        for row in cur:
            if row[0] == s.casefold():
                res = ( "Name:" +row[0] + "\n" + "Class:" + row[1] + "\n" + "Mobile:" + row[2] + "\n" + "Address:" + row[3] )
                resultshow.set(res)
                
                searchresult.destroy()

                #basically created similar searchresult Text by destroying the previous one as it seems the previous one was updated
                searchresult = Text(master = frame2 , height = 10 , width = 30)
                searchresult.pack(fill = X)
                searchresult.insert(END,res)
                #"Name : " , row[0]
                #"Class : " , row[1]
                #"Mobile : ", row[2]
                #"Address :", row[3]"
    

#function tosend SMS
def sendsms(number):
    url="https://api.textlocal.in/send/?"
    para= {
        "apikey":"bQZAEIOH1JE-3Ix4AsojqibCuw8iKPmL084D4kH6Aj",
        "sender":"TXTLCL",
        "message":"Your registration has been succesfully completed with EDN institute",
        #"language":"english",
        #"route":"p",
        "numbers":number
        
    }
    response = requests.get(url,params=para)
    dic = response.json()
    print(dic)


h = DBhelper()



student.mainloop()


