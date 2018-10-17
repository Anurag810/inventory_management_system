import mysql.connector

class Move:

    def get_location(self):

        cnx = mysql.connector.connect(user='root', database='inventory', charset='utf8')
        cursor = cnx.cursor()

        query = ("SELECT * FROM location"
                 )

        cursor.execute(query)

        loc = []

        for (lid, l_name, l_add, l_city) in cursor:
            l = [lid, l_name]
            loc.append(l)


        return loc

    def get_product(self):
        cnx = mysql.connector.connect(user='root', database='inventory', charset='utf8')
        cursor = cnx.cursor()

        query = ("SELECT * FROM product"
                 )

        cursor.execute(query)

        pro = []

        for (pid, p_name, p_type, p_weight) in cursor:
            p = [pid,p_name]
            pro.append(p)
        return pro


    def insert(self, f, to, pid, qty):

        c=self.get_avail(f, qty, pid)
        flag = 0
        if ( (c==1)or (f == "--") ):

             c=3

             cnx = mysql.connector.connect(user='root', database='inventory', charset='utf8')
             cursor = cnx.cursor()

             add = ('INSERT INTO movement '
               '(l_from, l_to, pid, qty)'
               'VALUES (%s, %s, %s,%s)')

             data = (f, to, pid, qty)

        # Insert new employee
             cursor.execute(add, data)

             if to != '--':

                 i=self.check(to, pid)

                 if i == 1:
                     query = ('update quantity set qty=qty+%s where lid=%s and pid=%s'
                     )

                     info = (qty, to, pid)
                 else:
                     query= ('INSERT INTO quantity '
                         '(lid, pid, qty)'
                         'VALUES (%s, %s, %s)')

                     info = (to, pid, qty)

                 cursor.execute(query, info)

             if f != '--':




                 query = ('update quantity set qty=qty-%s where lid=%s and pid=%s'
                              )

                 info = (qty, f, pid)




                 cursor.execute(query, info)


             cnx.commit()

             cursor.close()
             cnx.close()
             return c

        return flag


    def check(self, un, pa):
        cnx = mysql.connector.connect(user='root', database='inventory', charset='utf8')
        cursor = cnx.cursor()

        query = ("SELECT * FROM quantity WHERE lid=%s and pid=%s"
                 )

        add_data = (un, pa)

        cursor.execute(query, add_data)

        for (lid) in cursor:
            return 1

        cursor.close()
        cnx.close()


    def get_avail(self, f, qty, pid):
        cnx = mysql.connector.connect(user='root', database='inventory', charset='utf8')
        cursor = cnx.cursor()
        c = 0
        print c
        query = ("SELECT * FROM quantity WHERE lid=%s and pid=%s and qty>=%s"
                 )

        add_data = (f, pid, qty)

        cursor.execute(query, add_data)

        for (lid) in cursor:
            c = 1

        return c
        cursor.close()
        cnx.close()


    def view_record(self):
        cnx = mysql.connector.connect(user='root', database='inventory', charset='utf8')
        cursor = cnx.cursor()
        s = []
        query = ("SELECT location.l_name,product.p_name,quantity.qty"
                 " FROM quantity "
                 "INNER JOIN location ON location.lid=quantity.lid "
                 "INNER JOIN product ON product.pid=quantity.pid ORDER BY "
                 "location.lid"
                 )
        cursor.execute(query)
        for (l_name, p_name, qty) in cursor:
            l=[l_name, p_name, qty]
            s.append(l)

        return s


    def view_movement(self):
        cnx = mysql.connector.connect(user='root', database='inventory', charset='utf8')
        cursor = cnx.cursor()
        s = ''
        query = ("""SELECT DISTINCT m.mid, m.time, p.p_name AS product_name, m.l_from, l2.l_name AS from_location, 
            l.l_name as to_location, m.l_to, m.qty 
            FROM movement m 
            LEFT OUTER JOIN product p ON p.pid = m.pid 
            LEFT OUTER JOIN location l on l.lid = m.l_to 
            LEFT OUTER JOIN location l2 ON l2.lid = m.l_from 
            ORDER BY m.mid""")

        cursor.execute(query)
        for (mid, time, product_name, l_from, from_location, l_to, to_location, qty) in cursor:
            s += "<tr><td> "
            s += str(mid)
            s += " </td> "
            s += " <td> "
            s += str(time)
            s += " </td> "
            s += " <td> "
            s += product_name
            s += " </td> "
            s += " <td> "

            s += " </td> "
            s += " <td> "
            s += str(from_location)
            s += " </td> "
            s += " <td> "

            s += " </td> "
            s += " <td> "
            s += str(l_to)
            s += " </td> "
            s += " <td> "
            s += str(qty)
            s += """ </td><td><button class='btn btn-success' data-toggle='modal' data-target='#myModal28' onclick='fun(\""""
            s += str(mid)
            s += """\",\""""
            s += str(from_location)
            s += """\",\""""
            s += str(to_location)
            s += """\",\""""
            s += str(qty)
            s += """\")'>Update</button></td></tr> """




        return s


    def update_movement(self, f, t, qty, mid):
        cnx = mysql.connector.connect(user='root', database='inventory', charset='utf8')
        cursor = cnx.cursor()


        add = ('update movement set l_from=%s, l_to=%s, qty=%s where mid=%s'
               )

        data = (f, t, qty, mid)

        cursor.execute(add, data)

        cnx.commit()

        cursor.close()
        cnx.close()
        return 1