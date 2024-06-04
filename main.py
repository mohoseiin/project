import sqlite3

conn = sqlite3.connect('expenses.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         DATE           TEXT    NOT NULL,
         TYPEPAY        TEXT     NOT NULL,
         MONEY          INT     NOT NULL,
         DOCS           CHAR(200));''')

print ("Table created successfully")

print('1 => add pay')
print('2 => show all pay')
print('3 => update a pay')
print('4 => delete a pay')
print('5 => exit application')
while True:
    last_id = 0
    a = input('type work:')

    if int(a) == 1:
        b = input('date of payment:')
        c = input('Cost type:')
        d = input('amount spent:')
        e = input('Description:')

        last_id += 1
        conn.execute(f''' INSERT OR IGNORE INTO COMPANY(ID,DATE,TYPEPAY,MONEY,DOCS)
        VALUES({last_id}, '{b}', '{c}', {int(d)}, '{e}')''')

        conn.commit()
        print ('added data\n')

    elif int(a) == 2:
        mycursor = conn.cursor()

        data = mycursor.execute("SELECT * FROM COMPANY")
        rows = mycursor.fetchall()
        for record in rows:
            print ('ID : '+str(record[0]))
            print ('DATE : '+str(record[1]))
            print ('TYPEPAY : '+str(record[2]))
            print ('MONEY : '+str(record[3]))
            print ('DOCS : '+str(record[4])+'\n')

    elif int(a) == 3:
        x = input('id pay:')
        b = input('date of payment:')
        c = input('Cost type:')
        d = input('amount spent:')
        e = input('Description:')

        conn.execute(f''' UPDATE COMPANY set DATE='{b}', TYPEPAY='{c}', MONEY={int(d)}, DOCS='{e}' WHERE ID = {int(x)} ''')

        conn.commit()

        print ('updated pay')

    elif int(a) == 4:
        x = input('id pay:')
        conn.execute(f''' DELETE from COMPANY WHERE ID = {int(x)} ''')
        conn.commit()
        print ('Deleted pay')


    elif int(a) == 5:
        conn.close()
        break