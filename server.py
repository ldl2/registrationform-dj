from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = "sosecret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result/pre', methods=['POST'])
def button():
    #checks password length
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters")
        return redirect('/')
    else:
        pass
    #checks passwords match
    if request.form['password'] != request.form['confirmpassword']:
        flash("Your passwords must match")
        return redirect('/')
    else:
        pass
    #no num char in first name well should have used str.isalpha() in retrospect but it works
    for x in request.form['first_name']:
        try:
            i = int(x)
            flash("First name cannot have numbers") 
            return redirect('/')
        except ValueError:
            pass
        #names need this added as the other rules can leave only these empty
    if len(request.form['first_name']) > 1:
        print("hi")
    else:
        flash("First name cannot be empty!")
        return redirect('/')
    #no num char in last name
    for x in request.form['last_name']:
        try:
            i = int(x)
            flash("Last name cannot have numbers") 
            return redirect('/')
        except ValueError:
            pass
    if len(request.form['last_name']) > 0:
        pass
    else:
        flash("Last name cannot be empty!")
        return redirect('/')
    #email wrong format
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    else:
        pass
    return redirect('/result')

@app.route('/result')

def realresult():
    return render_template('/result.html')

app.run(debug=True)
