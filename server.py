from flask import Flask, session, render_template, redirect, request
from random import randint

app = Flask(__name__)
app.secret_key='thegreatnumberis2'

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = randint(1, 100)
    print(session['number'])
    return render_template ('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['number_guessed'])
    if session['guess'] == session['number']:
        print('You got it!')
    elif session['guess'] < session['number']:
        print('Too Low!')
    else: 
        print('Too high!')
    return render_template ('index.html')

@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect ('/')

if __name__=='__main__':
    app.run(debug=True)



