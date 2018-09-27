from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from web.app.block import *

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        lender = request.form.get('lender')
        amount = request.form.get('amount')
        borrower = request.form.get('borrower')

        write_block(name=lender, amount=amount, to=borrower)

        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/check', methods=['GET'])
def check():
    return render_template(
        'index.html',
        check_integrity=check_integrity()
    )


if __name__ == '__main__':
    app.run(debug=True)
