from flask import Flask, render_template, request, Markup, redirect, url_for, session
import os

import login_module
import p_management
import warehouse_management
import move_product


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('home'))
    return render_template("index.html")


@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        un = request.form['user']
        pa = request.form['pass']

        l = login_module.login()

        c = l.check(un, pa)
        if c == 1:
            session['user'] = 'admin'
            return redirect(url_for('home'))
        else:
            return render_template("index.html", f=1)
    if 'user' in session:
        return redirect(url_for('home'))


@app.route('/add_product', methods=['POST'])
def add_product():
    if 'user' in session:
        if request.method == 'POST':
            p_name = request.form['p_name']
            p_type = request.form['type']
            p_weight = request.form['weight']


            a = p_management.product()
            f = a.p_add(p_name, p_type, p_weight)

            m = move_product.Move()
            loc = m.get_location()
            pro = m.get_product()
            return render_template("home.html", lc=loc, po=pro, flag=f)
    else:
        return redirect(url_for('index'))

@app.route('/show')
def show():
    if 'user' in session:
        m = move_product.Move()
        loc = m.get_location()
        pro = m.get_product()
        a = p_management.product()
        s = a.p_show()
        value = Markup(s)
        return render_template("pshow.html", str=value, lc=loc, po=pro)
    else:
        return redirect(url_for('index'))

@app.route('/home')
def home():
    if 'user' in session:
        m = move_product.Move()
        loc = m.get_location()
        pro = m.get_product()
        return render_template("home.html", lc=loc, po=pro)
    else:
        return redirect(url_for('index'))


@app.route('/update_product', methods=['POST'])
def update_product():
    if 'user' in session:
        if request.method == 'POST':
            p_id = request.form['id']
            p_name = request.form['p_name']
            p_type = request.form['type']
            p_weight = request.form['weight']
            print p_id

            m = p_management.product()
            m.p_update(p_id, p_name, p_type, p_weight)

            return redirect(url_for('show'))
    else:
        return redirect(url_for('index'))

@app.route('/add_location', methods=['POST'])
def add_location():
    if 'user' in session:
        if request.method == 'POST':
            p_name = request.form['l_name']
            p_type = request.form['add']
            p_weight = request.form['city']


            a = warehouse_management.location()
            f = a.l_add(p_name, p_type, p_weight)

            m = move_product.Move()
            loc = m.get_location()
            pro = m.get_product()
            return render_template("home.html", lc=loc, po=pro, flag=f)
    else:
        return redirect(url_for('index'))

@app.route('/location_show')
def location_show():
    if 'user' in session:
        m = move_product.Move()
        loc = m.get_location()
        pro = m.get_product()
        a = warehouse_management.location()
        s = a.l_show()
        value = Markup(s)
        return render_template("lshow.html", str=value, lc=loc, po=pro)
    else:
        return redirect(url_for('index'))

@app.route('/update_location', methods=['POST'])
def update_location():
    if 'user' in session:
        if request.method == 'POST':
            p_id = request.form['id']
            p_name = request.form['p_name']
            p_type = request.form['type']
            p_weight = request.form['weight']


            m = warehouse_management.location()
            m.l_update(p_id, p_name, p_type, p_weight)

            return redirect(url_for('location_show'))
    else:
        return redirect(url_for('index'))

@app.route('/add_movement', methods=['POST'])
def add_movement():
    if 'user' in session:
        if request.method == 'POST':
            f = request.form['from']
            t = request.form['to']
            pro = request.form['pro']
            q = request.form['qty']
            m = move_product.Move()
            f = m.insert(f, t, pro, q)
            m = move_product.Move()
            loc = m.get_location()
            pro = m.get_product()
            return render_template("home.html", lc=loc, po=pro, flag=f)
    else:
        return redirect(url_for('index'))

@app.route('/view_report')
def view_report():
    if 'user' in session:
        m = move_product.Move()
        loc = m.get_location()
        pro = m.get_product()
        m = move_product.Move()
        r = m.view_record()

        return render_template("view_report.html", report = r, lc=loc, po=pro)
    else:
        return redirect(url_for('index'))

@app.route('/view_move')
def view_move():
    if 'user' in session:
        m = move_product.Move()
        loc = m.get_location()
        pro = m.get_product()
        m = move_product.Move()
        r = m.view_movement()
        value = Markup(r)

        return render_template("view_move.html", report =value, lc=loc, po=pro )
    else:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user', None)

    return redirect(url_for('index'))


@app.route('/update_movement',  methods=['POST'])
def update_movement():
    if 'user' in session:
        if request.method == 'POST':
            f = request.form['from']
            t = request.form['to']
            mid = request.form['mid']
            q = request.form['qty']

            m = move_product.Move()
            r = m.update_movement(f, t, q, mid)

        return redirect(url_for('view_move'))
    else:
        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run()
