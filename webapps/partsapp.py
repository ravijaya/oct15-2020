from flask import Flask, render_template, request, redirect
from basics.db import Database

app = Flask(__name__)


@app.route('/delete/<int:part_id>')
def delete_part(part_id):
    db = Database('../basics/store.db')
    db.remove(part_id)
    return redirect('/')


@app.route('/add', methods=['GET', 'POST'])
def add_part():
    if request.method == "POST":
        part = request.form['part']
        retailer = request.form['retailer']
        customer = request.form['customer']
        price = request.form['price']
        db = Database('../basics/store.db')
        db.insert(part, customer, retailer, price)
        return redirect('/')

    else:
        return render_template('partform.html', title='adding part')


@app.route('/')
def list_parts():
    db = Database('../basics/store.db')
    rows = db.fetch()
    return render_template('listparts.html', rows=rows)


if __name__ == '__main__':
    app.run(debug=True)

    # @ 4: 35 PM
