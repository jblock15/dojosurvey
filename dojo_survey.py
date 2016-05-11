from flask import Flask, render_template, request, redirect, flash
app = Flask (__name__)
app.secret_key = "effyousecretkey"

@app.route('/')
def index():
 return render_template('main.html')

@app.route('/survey' , methods = ['POST', 'GET'])
def create_user():


 error_count = 0

 if len(request.form['name']) < 1:
  flash('Name cannot be empty!')

 elif len(request.form['comments']) > 120:
  error_count += 1

 if len(request.form['comments']) > 120:
  flash('Comments must be less than 120 characters')
  error_count += 1

 if error_count > 0:
  return redirect('/')

 else:
  flash('Success!')

 return render_template('results.html',
 name = request.form['name'],
 dojo = request.form['dojo'],
 language = request.form['language'],
 comments = request.form['comments'])
 # name = request.form['name']
 # dojo = request.form['dojo']
 # language = request.form['language']
 # comments = request.form['comments']
 return render_template('results.html',
 name = request.form['name'],
 dojo = request.form['dojo'],
 language = request.form['language'],
 comments = request.form['comments'])

app.run(debug=True)
