
import mysql.connector


class product:
    def p_add(self, pn, pt, pw):
        cnx = mysql.connector.connect(user='root', database='inventory', charset='utf8')
        cursor = cnx.cursor()


        add = ('INSERT INTO product '
                        '(p_name, p_type, p_weight)'
                        'VALUES (%s, %s, %s)')

        data = (pn, pt, pw)

        # Insert new employee
        cursor.execute(add, data)

        # Make sure data is committed to the database
        cnx.commit()

        cursor.close()
        cnx.close()
        return 1


    def p_show(self):
        cnx = mysql.connector.connect(user='root', database='inventory', charset='utf8')
        cursor = cnx.cursor()
        s=''
        query = ("SELECT * FROM product"
                 )

        cursor.execute(query)

        s=''


        for (pid, p_name, p_type, p_weight) in cursor:
            s += "<tr><td> "
            s += str(pid)
            s += " </td> "
            s += " <td> "
            s += p_name
            s += " </td> "
            s += " <td> "
            s += p_type
            s += " </td> "
            s += " <td> "
            s += str(p_weight)
            s += """ </td><td><button class='btn btn-success' data-toggle='modal' data-target='#myModal28' onclick='fun(\""""
            s += str(pid)
            s += """\",\""""
            s += p_name
            s += """\",\""""
            s += p_type
            s += """\",\""""
            s += str(p_weight)
            s += """\")'>Update</button></td></tr> """



        return s

    def p_update(self, i, pn, pt, pw):
        cnx = mysql.connector.connect(user='root', database='inventory', charset='utf8')
        cursor = cnx.cursor()

        add = ('update product set p_name=%s, p_type=%s, p_weight=%s where pid=%s'
               )


        data = (pn, pt, pw, i)

        cursor.execute(add, data)

        cnx.commit()

        cursor.close()
        cnx.close()
        return 1

