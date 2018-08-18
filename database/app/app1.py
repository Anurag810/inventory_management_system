
import mysql.connector

cnx = mysql.connector.connect(user='root', database='employees', charset='utf8')
cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date FROM employees"
         )



cursor.execute(query)

for (first_name, last_name, hire_date) in cursor:
  print("{}, {} was hired on {:%d %b %Y}".format(
    last_name, first_name, hire_date))

cursor.close()
cnx.close()