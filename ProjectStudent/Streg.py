from tkinter import *
import mysql.connector as connector
import requests  
import json




class streg():
    def __init__(self):
        self.student = Tk()
        self.student.title("Student Register")

        #welcome messages
        self.welcome = Label(self.student,text="Welcome to Student Register",font=("calibri",36,"bold"))
        self.welcome2 = Label(self.student,text="please choose the action you want to perform \n ",font=("calibri",10,"bold"))
        self.welcome.pack()
        self.welcome2.pack()

        #declaring the fuction buttons
        self.start1 = Button(self.student,text='Student Registration',padx =10,relief= RAISED,bg="orange",command=lambda:self.start1com())
        self.start2 = Button(self.student,text='Fetcher',padx =10,relief= RAISED,bg="orange",command=lambda:self.start2com())
        self.start1.pack(fill=X)
        self.start2.pack(fill=X)

        #ceating the frames associated with the buttons
        self.frame1 = Frame()
        self.frame2 = Frame()
        #creating all the global variable that might be needed
        
        self.s = ""
        self.res = ""

        self.searchresult = ""

        #creating the string variables that might be needed
        
        self.namein = StringVar()
        self.classin = StringVar()
        self.mobin = StringVar()
        self.addin = StringVar()
        self.searchin = StringVar()
        self.resultout = StringVar()
        self.resultshow = StringVar()

        self.h = DBhelper()
        self.student.mainloop()

        #declaring the first button command
    def start1com(self):
        
        global frame1
        global frame2
        global N
        global M
        global C
        global A
        

        self.frame1 = Frame()
        
        self.label1 = Label(master=self.frame1,text="Enter the student details as following \n")
        self.label1.pack()

        #place for name entry
        self.labelname = Label(master=self.frame1,text ="Enter the name of the student")
        self.labelname.pack()

        self.entryname = Entry(master= self.frame1,textvariable= self.namein,width=60)
        self.entryname.pack()
        

        #place for class entry
        self.labelclass= Label(master=self.frame1,text ="Enter the class of the Student")
        self.labelclass.pack()
        

        self.entryclass = Entry(master= self.frame1,textvariable= self.classin,width=60)
        self.entryclass.pack()
        
        #place for mobile entry
        self.labelmobile = Label(master = self.frame1,text="Enter the mobile number of the student")
        self.labelmobile.pack()

        self.entrymobile = Entry(master = self.frame1 ,textvariable= self.mobin, width = 60)
        self.entrymobile.pack()
        
        #place for address entry
        self.labeladd = Label(master = self.frame1 ,text="Enter the address of the student")
        self.labeladd.pack()

        self.entryadd = Entry(master = self.frame1 ,textvariable= self.addin,width=60)
        self.entryadd.pack()
        
        
        #button to register the input to the database
        self.buttregister = Button(master = self.frame1 , text="REGISTER" ,font=("calibri",15,"bold"),padx =10,relief= RAISED,bg="orange"
                            ,command=lambda:[self.h.dataentry(),self.sendsms(self.mobin.get())])
                        
        self.buttregister.pack()


    
        #deesigned in a way so that the other frme is destroyed when another one is called
        self.N = self.namein.get()
        C = self.classin.get()
        M = self.mobin.get()
        A = self.addin.get()
        self.frame1.pack()
        self.frame2.destroy()
        

    #declaring the second button fuction
    def start2com(self):
        
        global frame1
        global frame2
        global res
        global searchresult

        self.frame2 = Frame()
        self.label2 = Label(master=self.frame2,text="Fetch ",font=("futura",35,"bold"),fg="red")
        self.label2.pack()
        self.label3 = Label(master=self.frame2,text="Enter the keyword you want to search by \n ",font=("futura",10,"bold"))
        self.label3.pack()
        

        self.searchenter = Entry(master = self.frame2, textvariable = self.searchin ,width = 60 )
        self.searchenter.pack()

        self.photo = PhotoImage(file = "X:\Search.png" )
        self.photoimage = self.photo.subsample(5)
        

        #option = Menubutton(master = frame2 ,text = "test")
        #option.pack()

        
        #button that fecth the data from the database
        self.searchbutt = Button(master = self.frame2 , text = "search", image = self.photoimage , command = lambda:self.datafetcher() )
        self.searchbutt.image = self.photoimage
        self.searchbutt.pack()

        #place to show the search result
        self.searchresult = Text(master = self.frame2 , height = 10 , width = 30)
        self.searchresult.pack(fill = X)
        
        #similar function as of the frame 1
        self.frame2.pack()
        self.frame1.destroy()


        #function tosend SMS
    def sendsms(self,number):
        self.url="https://api.textlocal.in/send/?"
        self.para= {
            "apikey":"xxxxxxx",
            "sender":"TXTLCL",
            "message":"Your registration has been succesfully completed with EDN institute",
            #"language":"english",
            #"route":"p",
            "numbers":number
            
        }
        self.response = requests.get(self.url,params=self.para)
        self.dic = self.response.json()
        print(dic)

    


#creating the class for managing the mysql database
class DBhelper(streg):
    def __init__(self):
<<<<<<< HEAD
        self.connect = connector.connect(host="localhost", port="3306", user= "root", password= "xxxxx",database="Studentsdata")
=======
        self.connect = connector.connect(host="localhost", port="3306", user= "root", password= "password",database="Studentsdata")
>>>>>>> 765c3452bf58afab545943bcfc16e07d87a81347
        print("Connected")
        query = "create table if not exists student(name varchar(30),class varchar(2), mobile varchar(13),address varchar(300))"
        cur = self.connect.cursor()
        cur.execute(query)
        print("Table created succefully")
        
        
    #method to carry out the data entry process on button press
    
    def dataentry(self):
        
      
        
        

        
        
    

        

        query= "insert into student(name,class,mobile,address) values('{}','{}','{}','{}')".format(self.N.casefold(),self.C,self.M,self.A)
        cur = self.connect.cursor()
        cur.execute(query)
        self.connect.commit()
        print("Updated")
        

    #method to fecth data from database and show it on button call
    
    def datafetcher(self):
        global s
        global res
        global searchresult
        
        self.s = streg.searchin.get()

        

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

<<<<<<< HEAD
stu = streg()






=======
#function tosend SMS
def sendsms(number):
    url="https://api.textlocal.in/send/?"
    para= {
        "apikey":"your api key",
        "sender":"TXTLCL",
        "message":"Your registration has been succesfully completed with EDN institute",
        #"language":"english",
        #"route":"p",
        "numbers":number
        
    }
    response = requests.get(url,params=para)
    dic = response.json()
    print(dic)
>>>>>>> 765c3452bf58afab545943bcfc16e07d87a81347







