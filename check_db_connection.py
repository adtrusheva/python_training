import pymysql.cursors

connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("select  \
                   id, \
                   firstname, \
                   lastname, \
                   middlename, \
                   photo, \
                   nickname, \
                   title, \
                   company, \
                   address, \
                   home, \
                   mobile, \
                   work, \
                   fax, email, email2, \
                   email3, homepage, bday, \
                   bmonth, byear, aday, amonth, \
                   ayear, address2, phone2,notes  \
                   from addressbook")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()