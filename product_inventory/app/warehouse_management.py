
import mysql.connector


class location:
    def l_add(self, pn, pt, pw):
        cnx = mysql.connector.connect(user='root', database='inventory', charset='utf8')
        cursor = cnx.cursor()


        add = ('INSERT INTO location '
                        '(l_name, l_add, l_city)'
                        'VALUES (%s, %s, %s)')

        data = (pn, pt, pw)

        # Insert new employee
        cursor.execute(add, data)

        # Make sure data is committed to the database
        cnx.commit()

        cursor.close()
        cnx.close()
        return 2


    def l_show(self):

        cnx = mysql.connector.connect(user='root', database='inventory', charset='utf8')
        cursor = cnx.cursor()
        s=''
        query = ("SELECT * FROM location"
                 )

        cursor.execute(query)

        s=''


        for (lid, l_name, l_add, l_city) in cursor:

            s += "<tr><td> "
            s += str(lid)
            s += " </td> "
            s += " <td> "
            s += l_name
            s += " </td> "
            s += " <td> "
            s += l_add
            s += " </td> "
            s += " <td> "
            s += l_city
            s += """ </td><td><button class='btn btn-success' data-toggle='modal' data-target='#myModal26' onclick='fun(\""""
            s += str(lid)
            s += """\",\""""
            s += l_name
            s += """\",\""""
            s += l_add
            s += """\",\""""
            s += l_city
            s += """\")'>Update</button></td></tr> """



        return s

    def l_update(self, i, pn, pt, pw):

        cnx = mysql.connector.connect(user='root', database='inventory', charset='utf8')
        cursor = cnx.cursor()

        add = ('update location set l_name=%s, l_add=%s, l_city=%s where lid=%s'
               )
        print add

        data = (pn, pt, pw, i)

        cursor.execute(add, data)

        cnx.commit()

        cursor.close()
        cnx.close()
        return 1

