from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='root', database='employees', charset='utf8')
cursor = cnx.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)

add_employee = ('delete from employees where first_name="Geert"'
                )


cursor.execute(add_employee)
print("done")
# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()