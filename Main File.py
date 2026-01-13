try:
    from tabulate import tabulate
except:
    print("Install 'tabulate' module using command = pip install tabulate in command prompt")
    exit()
try:
    import mysql.connector as sq
    p=sq.connect(host="localhost",user="root",password="",database="library")
    if p.is_connected()==False:
        print("Error..")
    else:
        myc=p.cursor()
except:
    print("ERROR")
def Add_book():
    try:
        Bid=int(input("Enter book id:"))
        book=input("Enter book name:")
        au=input("Enter Author name:")
        pr=float(input("Enter price:"))
        copies=int(input("Enter number of copies:"))
        qr="INSERT INTO book VALUES({},'{}','{}',{},{},{})".format(Bid,book,au,pr,copies,copies)
        myc.execute(qr)
        p.commit()
        print("Book was added successfully")
    except:
        print("ERROR")
def Edit_book():
    try:
        Id=int(input("Enter book id:"))
        qry="SELECT* FROM book WHERE Bookid={}".format(Id)
        myc.execute(qry)
        R=myc.fetchone()
        if R:
            npr=float(input("Enter new price of book:"))
            q="UPDATE book SET Price={} WHERE Bookid={}".format(npr,Id)
            myc.execute(q)
            p.commit()
            print("The price was edited successfully")
        else:
            print("You have entered wrong book id")
    except:
        print("ERROR")
def Delete_book():
    try:
        Id=int(input("Enter book id:"))
        qry="SELECT* FROM book WHERE Bookid={}".format(Id)
        myc.execute(qry)
        R=myc.fetchone()
        if R:
            q="DELETE FROM book WHERE Bookid={}".format(Id)
            myc.execute(q)
            p.commit()
            print("The book was deleted successfully")
        else:
            print("You have entered wrong book id")
    except:
        print("ERROR")
def Add_member():
    try:
        Mid=int(input("Enter member id:"))
        name=input("Enter member name:")
        add=input("Enter member's address:")
        contact=int(input("Enter phone number:"))
        qry="INSERT INTO member VALUES({},'{}','{}',{})".format(Mid,name,add,contact)
        myc.execute(qry)
        p.commit()
        print("Member was added successfully")
    except:
        print("ERROR")
def Edit_member():
    try:
        Id=int(input("Enter member id:"))
        qry="SELECT* FROM member WHERE Memberid={}".format(Id)
        myc.execute(qry)
        R=myc.fetchone()
        if R:
            ch=int(input("What do you want to change? 1.Phone number\n2.Address\n3.Both\n"))
            if ch==1:
                newno=int(input("Enter new phone number:"))
                q="UPDATE member SET ContactNumber={} WHERE Memberid={}".format(newno,Id)
                myc.execute(q)
                p.commit()
                print("Edited successfully")
            elif ch==2:
                newadd=input("Enter new address of member:")
                q="UPDATE member SET Maddress='{}' WHERE Memberid={}".format(newadd,Id)
                myc.execute(q)
                p.commit()
                print("Edited successfully")
            elif ch==3:
                newno=int(input("Enter new phone number:"))
                newadd=input("Enter new address of member:")
                q="UPDATE member SET Maddress='{}',ContactNumber={} WHERE Memberid={}".format(newadd,newno,Id)
                myc.execute(q)
                p.commit()
                print("Edited successfully")
            else:
                print("Such option does'nt exist")
        else:
            print("You have entered wrong member id")
    except:
        print("ERROR")
def Delete_member():
    try:
        Id=int(input("Enter member id:"))
        qry="SELECT* FROM member WHERE Memberid={}".format(Id)
        myc.execute(qry)
        R=myc.fetchone()
        if R:
            q="DELETE FROM member WHERE Memberid={}".format(Id)
            myc.execute(q)
            p.commit()
            print("The member was deleted successfully")
        else:
            print("You have entered wrong member id")
    except:
        print("ERROR")
def Issue_book():
    try:
        q="SELECT MAX(issueid)FROM issue"
        myc.execute(q)
        r=myc.fetchone()[0]
        if r:
            issueid=r+1
        else:
            issueid=1
        x=int(input("Enter Member ID"))
        q1="SELECT*FROM member WHERE Memberid={}".format(x)
        myc.execute(q1)
        r=myc.fetchone()
        if r:
            y=int(input("Enter book ID"))
            q2="SELECT Bookid,RemainingCopies FROM book WHERE Bookid={}".format(y)
            myc.execute(q2)
            r=myc.fetchone()
            if r:
                if r[1]>0:
                    issuedt=input("Enter issue date")
                    copies=int(input("Enter no of copies"))
                    remcopies=r[1]-copies
                    q3="INSERT INTO issue VALUES({},'{}',{},{},{})".format(issueid,issuedt,x,y,copies)
                    myc.execute(q3)
                    q4="UPDATE book SET RemainingCopies={} WHERE Bookid={}".format(remcopies,y)
                    myc.execute(q4)
                    p.commit()
                    print("Book issued")
                else:
                    ("Book is not available")
            else:
                print("You have entered wrong book id")
        else:
            print("You have entered wrong member id")
    except:
        print("ERROR")
def Return_book():
    try:
        q="SELECT MAX(returnid)FROM returning"
        myc.execute(q)
        r=myc.fetchone()[0]
        if r:
            returnid=r+1
        else:
            returnid=1
        x=int(input("Enter Member ID"))
        q1="SELECT*FROM member WHERE Memberid={}".format(x)
        myc.execute(q1)
        r=myc.fetchone()
        if r:
            y=int(input("Enter book ID"))
            q2="SELECT Bookid,RemainingCopies FROM book WHERE Bookid={}".format(y)
            myc.execute(q2)
            r=myc.fetchone()
            if r:
                rdt=input("Enter return date")
                copies=int(input("Enter no of copies"))
                remcopies=r[1]+copies
                q3="INSERT INTO returning VALUES({},'{}',{},{},{})".format(returnid,rdt,x,y,copies)
                myc.execute(q3)
                q4="UPDATE book SET RemainingCopies={} WHERE Bookid={}".format(remcopies,y)
                myc.execute(q4)
                p.commit()
                print("Book returned")
            else:
                print("You have entered wrong book id")
        else:
            print("You have entered wrong member id")
    except:
        print("ERROR")
def bookdetails():
    try:
        qry="SELECT* FROM book"
        myc.execute(qry)
        R=myc.fetchall()
        H=['Bookid','Bookname','Author','Price','Copies','RemainingCopies']
        print(tabulate(R,headers=H,tablefmt='psql'))
    except:
        print("ERROR")
def memberdetails():
    try:
        qry="SELECT* FROM member"
        myc.execute(qry)
        R=myc.fetchall()
        H=['Memberid','Mname','Maddress','ContactNumber']
        print(tabulate(R,headers=H,tablefmt='psql'))
    except:
        print("ERROR")
def issuedetails():
    try:
        qry="SELECT* FROM issue"
        myc.execute(qry)
        R=myc.fetchall()
        H=['issueid','issuedate','Memberid','Bookid','Copies']
        print(tabulate(R,headers=H,tablefmt='psql'))
    except:
        print("ERROR")
def returndetails():
    try:
        qry="SELECT* FROM returning"
        myc.execute(qry)
        R=myc.fetchall()
        H=['returnid','returndatae','Memberid','Bookid','Copies']
        print(tabulate(R,headers=H,tablefmt='psql'))
    except:
        print("ERROR")
while True:
    print("="*94)
    print("\t\t\t-------LIBRARY MANAGEMENT-------")
    print("="*94)
    print("\t\t\t\tChoose an action:\n\t\t\t\t1.Book details.\n\t\t\t\t2.Member details.\n\
           \t\t\t3.Issue or return a book.\n\t\t\t\t4.Information.\n\t\t\t\t5.EXIT")
    a=int(input())
    if a==1:
        while True:
            print("\t\t\t\tChoose an action:\n\t\t\t\t1.Add book.\n\t\t\t\t2.Edit book details.\n\
        \t\t\t3.Delete a book.\n\t\t\t\t4.Back to main menu")
            ch=int(input())
            if ch==1:
                Add_book()
            elif ch==2:
                Edit_book()
            elif ch==3:
                Delete_book()
            elif ch==4:
                break
    elif a==2:
        while True:
            print("\t\t\t\tChoose an action:\n\t\t\t\t1.Add member.\n\t\t\t\t2.Edit member details\
    .\n\t\t\t\t3.Delete a member.\n\t\t\t\t4.Back to main menu")
            c=int(input())
            if c==1:
                Add_member()
            elif c==2:
                Edit_member()
            elif c==3:
                Delete_member()
            elif c==4:
                break
    elif a==3:
        while True:
            print("\t\t\t\tChoose an action:\n\t\t\t\t1.Issue book.\n\t\t\t\t2.Return book.\n\
            \t\t\t3.Back to main menu")
            h=int(input())
            if h==1:
                Issue_book()
            elif h==2:
                Return_book()
            elif h==3:
                break
    elif a==4:
        while True:
            print("\t\t\t\tChoose an action:\n\t\t\t\t1.Related to Book .\n\t\t\t\t2.Related \
   Member\n\t\t\t\t3.Issue details.\n\t\t\t\t4.Return details.\n\t\t\t\t5.Back to main menu.")
            x=int(input())
            if x==1:
                bookdetails()
            elif x==2:
                memberdetails()
            elif x==3:
                issuedetails()
            elif x==4:
                returndetails()
            elif x==5:
                break
    elif a==5:
        break
