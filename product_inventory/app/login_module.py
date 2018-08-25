import mysql.connector


class login:
    def check(self, un, pa):
         cnx = mysql.connector.connect(user='root', database='inventory', charset='utf8')
         cursor = cnx.cursor()

         query = ("SELECT * FROM user WHERE u_name=%s and pass=%s"
                  )

         add_data = (un, pa)

         cursor.execute(query, add_data)

         for (name) in cursor:
             return 1

         cursor.close()
         cnx.close()
