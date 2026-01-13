import mysql.connector
def database_creation():
    conn=mysql.connector.connect(host='localhost',user='root',password='')
    if conn.is_connected==False:
        print("ERROR")
    else:
        cursor=conn.cursor()
    try:
        q="CREATE DATABASE IF NOT EXISTS LIBRARY"
        cursor.execute(q)
        conn.commit()
        conn.close()
        print("Database Created")
    except:
        print("ERROR")
def table_creation():
    conn=mysql.connector.connect(host='localhost',user='root',password='',database="library")
    if conn.is_connected==False:
        print("ERROR")
    else:
        cursor=conn.cursor()
    try:
        t1="CREATE TABLE book(Bookid int primary key,Bookname varchar(30),Author varchar(30),Price float,Copies int,RemainingCopies int)"
        cursor.execute(t1)
        t2="CREATE TABLE Member(Memberid int primary key,Mname varchar(30),Maddress varchar(60),ContactNumber char(10))"
        cursor.execute(t2)
        t3="CREATE TABLE issue(issueid int primary key,issuedate date,Memberid int,Bookid int,Copies int,Foreign key(Bookid) references book(Bookid),Foreign key(Memberid) references member(Memberid))"
        cursor.execute(t3)
        t4="CREATE TABLE returning (returnid int primary key,returndate date,Memberid int,Bookid int,Copies int,Foreign key(Bookid) references book(Bookid),Foreign key(Memberid) references member(Memberid))"
        cursor.execute(t4)
        conn.commit()
        conn.close()
        print("All Tables Created .\n Now you can run main file.")
    except:
        print("ERROR")
try:
    database_creation()
    table_creation()
except:
    print("There is an error")
