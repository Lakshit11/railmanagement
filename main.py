from datetime import *
import mysql.connector as m
conn=m.connect(user='root',passwd='root',database='rail')
cursor=conn.cursor()
def create_new_account():
    fname=input("Enter your name:")
    password=input("Enter the password:")
    age=int(input("Enter your age:"))
    login_query="INSERT INTO LOG(USER_NAME,PASSWD,AGE) VALUES (%s,%s,%s);"
    try:
        cursor.execute(login_query,(fname,password,age))
        print("Account Created!")
        conn.commit()
    except:
        print("Server Error")
def delete_account():
    fname = input("Enter your username:")
    paswd = input("Enter the password:")
    delete_query="DELETE FROM LOG WHERE USER_NAME = (%s) AND PASSWD=(%s);"
    try:
        cursor.execute(delete_query,(fname,paswd))
        print("Account Deleted Successfully")
        conn.commit()
    except Exception as arg:
        print("Unable to delete",arg)
        conn.rollback()
def book_ticket():
    count_query = "SELECT COUNT(*) FROM TICKET_INFO;"
    cursor.execute(count_query)
    c = cursor.fetchone()
    for x in c:
        if(x>=10):
            print("Sorry!! The train your are booking in is FULL NOW")
        else:
            print("Please Provide Following Details Carefully : ")
            name = input("Enter your Name : ")
            age = int(input("Enter your Age :"))
            source = input("Enter the Departure Station : ")
            dest = input("Enter the Destination Station : ")
            book_date = date.today()
            travel_date = input("Enter the travel date (YYYY-MM-DD) : ")
            q_book = """ INSERT INTO TICKET_INFO(NAME,AGE,SOURCE,DEST,BOOKING_DATE,TRAVEL_DATE) VALUES(%s,%s,%s,%s,%s,%s);"""
            try:
                cursor.execute(q_book,(name,age,source,dest,book_date,travel_date))
                print("Ticket Booked Successfully")
                conn.commit()
            except:
                print("Error while booking the ticket")
                conn.rollback()
    print("The following the your Ticket ID, Please NOTE IT SOMEWHERE : ")
    tick = "SELECT MAX(TICKET_ID) FROM TICKET_INFO;"
    cursor.execute(tick)
    x=cursor.fetchone()
    for i in x:
        print(i)
def update_ticket(t_id):
      choice= int(input("What do you want to update? \nPress 1 for Name, \nPress 2 for Age, \nPress 3 for Source Station, \nPress 4 for Destination Station, \nPress 5 for Travel Date : "))
      if(choice == 1):
            name=input("Enter the Correct Name:")
            que="UPDATE TICKET_INFO SET NAME = (%s) WHERE TICKET_ID = (%s)"
            try:
                cursor.execute(que,(name,t_id))
                print("Name Updated Successfully")
                conn.commit()
            except Exception as arg:
                    print("Error While Updation",arg)
                    conn.rollback()
      elif(choice == 2):
          age=int(input("Enter Your Correct Age : "))
          que = " UPDATE TICKET_INFO SET AGE = (%s) WHERE TICKET_ID = (%s)"
          try:
              cursor.execute(que,(age,t_id))
              print("Age Updated Successfully")
              conn.commit()
          except:
              print("Error While Updating Date")
              conn.rollback()
      elif(choice == 3):
          source=input("Enter the Changed  Source of Journey : ")
          que="UPDATE TICKET_INFO SET SOURCE = (%s) WHERE TICKET_ID = (%s)"
          try:
              cursor.execute(que,(source,t_id))
              print("Source Changed Successfully")
              conn.commit()
          except:
              print("Error while updating Source")
              conn.rollback()
      elif(choice == 4):
         dest=input("Enter the correct Destination : ")
         que="UPDATE TICKET_INFO SET DEST = (%s) WHERE TICKET_ID = (%s)"
         try:
             cursor.execute(que,(dest,t_id))
             print("Destination Updated Successfully ")
             conn.commit()
         except:
             print("Error while Changing the destination")
             conn.rollback()
      elif(choice == 5):
          travel_date=input("Enter new Travel Date (YYYY-MM-DD) : ")
          que="UPDATE TICKET_INFO SET TRAVEL_DATE = (%s) WHERE TICKET_ID = (%s)"
          try:
              cursor.execute(que,(travel_date,t_id))
              print("Travel Date Updated Successfully")
              conn.commit()
          except:
              print("Error while updating Travel Date ")
              conn.rollback()
      else:
          print("Choose From Given Choices Only")
          update_ticket(t_id)

def delete_booking(t_id):
    que="DELETE FROM TICKET_INFO WHERE TICKET_ID = (%s)"
    try:
        cursor.execute(que,(t_id,))
        print("Ticket Deleted Successfully")
        conn.commit()
    except:
        print("Error While Deleting the Ticket")
        conn.rollback()
def view_ticket(t_id):
    que="SELECT * FROM TICKET_INFO WHERE TICKET_ID = (%s)"
    try:
        cursor.execute(que,(t_id,))
        x = cursor.fetchall()
        for i in x:
            tid = i[0]
            name= i[1]
            age = i[2]
            source = i[3]
            dest = i[4]
            bdate = i[5]
            tdate = i[6]
        print("Ticket ID : ",tid)
        print("Name on Ticket : ",name)
        print("Age of Traveller : ",age)
        print("Source of Journey : ",source)
        print("Destination of Journey : ",dest)
        print("Booking Date of Ticket : ",bdate)
        print("Travel Date : ",tdate)
    except:
        print("Error While Fetching The Ticket")
def save_ticket(t_id):
    que="SELECT * FROM TICKET_INFO WHERE TICKET_ID = (%s)"
    try:
        cursor.execute(que,(t_id,))
        x = cursor.fetchall()
        for i in x:
            tid = i[0]
            name= i[1]
            age = i[2]
            source = i[3]
            dest = i[4]
            bdate = i[5]
            tdate = i[6]
        f=open("ticket.txt","w")
        f.write("**************************************************************************************\n")
        f.write("Ticket id : ")
        f.write(str(tid))
        f.write("\n")
        f.write("Passenger's Name : ")
        f.write(name)
        f.write("\n")
        f.write("Passenger's Age : ")
        f.write(str(age))
        f.write("\n")
        f.write("Source : ")
        f.write(source)
        f.write("\n")
        f.write("Destination : ")
        f.write(dest)
        f.write("\n")
        f.write("Booking Date : ")
        f.write(str(bdate))
        f.write("\n")
        f.write("Travel Date : ")
        f.write(str(tdate))
        f.write("\n")
        f.write("**************************************************************************************")
        f.close()
        print("TICKET SAVED !!")
    except:
        print("Error While Saving The Ticket ")
def main():
    print("Welcome To Train Ticket Management Program Using Python And MySQL")
    x=int(input("\n Press 1 to Manage your account \n Press 2 to Book or Manage Ticket :"))
    if(x==1):
        c = int(input("\nPress 1 to Create New Account \nPress 2 to Delete Existing Account \nHow May I Help You?"))
        if(c==1):
          create_new_account()
        elif(c==2):
            delete_account()
        elif(x==2):
            ch=int(input("\nPress 1 to Book new Ticket \nPress 2 to Update Ticket Details \nPress 3 to Delete Ticket \nPress 4 to View the Ticket \nPress 5 to Save the Ticeket \nEnter your Choice : "))
        if(ch==1):
            book_ticket()
        elif(ch==2):
            t_id=int(input("Enter your Ticket ID:"))
            update_ticket(t_id)
        elif(ch==3):
            t_id=int(input("Enter your Ticket ID:"))
            delete_booking(t_id)
        elif(ch==4):
            t_id=int(input("Enter your Ticket ID:"))
            view_ticket(t_id)
        elif(ch==5):
            t_id=int(input("Enter your Ticket ID:"))
            save_ticket(t_id)
        

main()
print("Thank You For Giving Your Time!! HAVE A GOOD DAY!!")
