#the objective of this project is to make a gui for students registry and as soon as they make the registry , they wil get a sms regarding that
import mysql.connector as connector
class DBHelper:
    def __init__(self):
        self.con = connector.connect(host="localhost",port="3306",user="root",password="IlTd7084@",database="registry")
        query = 'create table student(studentname varchar(20),class varchar(2), mobile varchar(12), address varchar(200))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    def Insert(self,studentname,mobile,address):
        query="insert into student(studentname,class,mobile,address) values('{}','{}','{}','{}')".format(studentname, mobile, address)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("done")
        

    def fetch(self):
        query = " select * from registry.student"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)

helper= DBHelper()
#helper.Insert(3,"8444851127","Agarpara,Kolkata-700109")
helper.fetch()
