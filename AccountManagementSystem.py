#importing package
import csv
import sqlite3
from sqlite3 import Error


#Create a Master class for menu(CRUD) functions. 
class Master:

    #funtion to create connection with database.
    @staticmethod
    def create_connection(dbfile):
            try:
                conn = sqlite3.connect(dbfile)
                return conn
            except Error as e:
                print(e)

    #function to create a table in database.
    @staticmethod
    def create_table(conn,sql1):
            try:
                cursor = conn.cursor()
                cursor.execute(sql1)
                conn.commit()
            except Error as e:
                print(e)
    
    #function to insert records in table.
    @staticmethod
    def insert_values(conn,sql2,values):
            try:
                cursor = conn.cursor()
                cursor.execute(sql2,values)
                conn.commit()
            except Error as e:
                print(e)

    #function to read or fetch the values from table.
    @staticmethod
    def read(conn,sql3):
            try:
                cursor = conn.cursor()
                cursor.execute(sql3)
                conn.commit()
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            except Error as e:
                print(e)

    #function to upadate the table.
    @staticmethod
    def update_values(conn,status,id):
            try:
                cursor = conn.cursor()
                cursor.execute('UPDATE Account SET Status = ? WHERE Account_ID = ?',(status,id))
                conn.commit()
            except Error as e:
                print(e)

    #function to delete the last row of table.
    @staticmethod
    def del_values(conn):
            try:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM Account WHERE Account_ID = (SELECT max(Account_ID) FROM Account)')
                conn.commit()
            except Error as e:
                print(e)

##########################################################################################################################

#create the object of Master class
account_table = Master()

#create a Menu for operation selection.
def menu():
    sel = int(input("Enter selection no.: ")) 
    
    #connect the database file.
    if sel == 1:
        dbfile  = r'E:\Account-Management-System\Account.db'
        conn = account_table.create_connection(dbfile)

    #create a table.
    elif sel == 2:
        dbfile  = r'E:\Account-Management-System\Account.db'
        conn = account_table.create_connection(dbfile)
        sql1 = '''
                CREATE TABLE IF NOT EXISTS Account(
                    Account_ID INTEGER,
                    Account_Name TEXT,
                    Account_Size INTEGER,
                    Account_Duration INTEGER,
                    Account_Budget INTEGER,
                    Status TEXT
                )'''
        account_table.create_table(conn,sql1)

    #insert values.
    elif sel == 3:
        dbfile  = r'E:\Account-Management-System\Account.db'
        conn = account_table.create_connection(dbfile)
        no_of_rows = int(input("Enter the no. of rows in table: "))
        sql2 = '''
                INSERT INTO Account(Account_ID,Account_Name,Account_Size,Account_Duration,Account_Budget,Status)
                            VALUES ( ?,?,?,?,?,? )
                '''
        for i in range(no_of_rows):
            Account_ID = int(input("Enter Account ID: "))
            Account_Name = input("Enter Account Name: ").title()
            Account_Size = int(input("Enter Account size: "))
            Account_Duration = int(input("Enter Account duration: "))
            Account_Budget = int(input("Enter Account budget: "))
            Status = input("Enter status: ").title()

            insert_data = (Account_ID,Account_Name,Account_Size,Account_Duration,Account_Budget,Status)
            account_table.insert_values(conn,sql2,insert_data)

    #fetch Active or Inactive accounts.
    elif sel == 4:
        dbfile  = r'E:\Account-Management-System\Account.db'
        conn = account_table.create_connection(dbfile)
        state = input("Active or Inactive: ")
        if state.lower() == 'active':
            sql3 = '''
            SELECT * FROM Account WHERE Status = "Active"
            '''
            account_table.read(conn,sql3)
        elif state.lower() == 'inactive':
            sql3 = '''
            SELECT * FROM Account WHERE Status = "Inactive"
            '''
            account_table.read(conn,sql3)

    #Update the values in table.
    elif sel == 5:
        dbfile  = r'E:\Account-Management-System\Account.db'
        conn = account_table.create_connection(dbfile)
        update_id = int(input("Enter Account ID to update: "))
        updated_status = input("Enter Status: ")
        account_table.update_values(conn,updated_status,update_id)

    #Delete the last row from table.
    elif sel == 6:
        dbfile  = r'E:\Account-Management-System\Account.db'
        conn = account_table.create_connection(dbfile)
        account_table.del_values(conn)

    #Exit 
    elif sel == 7:
        return 0
    
    return 1

while(menu()):
    pass

#create a csv file.
dbfile  = r'E:\Account-Management-System\Account.db'
conn = account_table.create_connection(dbfile)
cursor = conn.cursor()
cursor.execute("select * from Account;")
with open(r"E:\Account-Management-System\account.csv", 'w',newline='') as csv_file: 
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) 
    csv_writer.writerows(cursor)
conn.close()








