from flask import Flask, render_template, request, flash

app = Flask(__name__)
logged_in = False
user_name = ""
app.secret_key = b'th46zszf786'


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/home.html')
def home():
    return render_template('home.html')


@app.route('/register.html', methods=['GET', "POST"])
def register():
    user_data_error = ""
    email_data_error = "lol"
    if request.method == 'POST':
        user = request.form['username']
        psw = request.form['psw']
        mail = request.form['email']
        fname = request.form['fname']
        lname = request.form['lname']
        gender = request.form['gender']
        return home()
    return render_template('register.html', userDataError=user_data_error, emailDataError=email_data_error)


@app.route('/resume.html')
def resume():
    return render_template('resume.html')


@app.route('/quot.html')
def quot():
    return render_template('quot.html')


@app.route('/hobby.html')
def hobby():
    return render_template('hobby.html')


if __name__ == "__main__":
    app.run(debug=True)
