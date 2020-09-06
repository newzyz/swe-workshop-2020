from flask import Flask, render_template, request
from app.utility.validator import validate_name, validate_id, validate_phone_number

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    first_name = data['first_name']
    last_name = data['last_name']
    id = data['id']
    tel = data['tel']

    error_message = ""
    if validate_name(first_name) is not True:
        error_message = 'กรุณากรอกชื่อให้ถูกต้อง'
        return render_template('error.html', message=error_message)

    if validate_name(last_name) is not True:
        error_message = 'กรุณากรอกนามสกุลให้ถูกต้อง'
        return render_template('error.html', message=error_message)

    if validate_id(id) is not True:
        error_message = 'กรุณากรอกบัตรประชาชนให้ถูกต้อง'
        return render_template('error.html', message=error_message)
    return render_template('success.html',
                           first_name=first_name,
                           last_name=last_name,
                           id=id,
                           tel=tel)


def init_app():
    return app
