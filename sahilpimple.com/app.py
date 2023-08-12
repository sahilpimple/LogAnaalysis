from pyexpat import model
from flask import Flask, render_template, request, jsonify
import re

from file import LoginForm, RegistrationForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ede0545ea93c735a5fb9adf67d01c053'
@app.route('/')
def index():
    if request.method == 'POST':
        model.save()
        # Failure to return a redirect or render_template
    else:
        return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    log_file = request.files['logFile']
    if log_file and log_file.filename.endswith('.log'):
        log_data = log_file.read().decode('utf-8')
        error_count = analyze_log(log_data)
        return jsonify(error_count)
    else:
        return jsonify({"error": "Invalid file format"})

def analyze_log(log_data):
    errors = re.findall(r'ERROR: (.+)', log_data)
    error_count = {}
    for error in errors:
        if error in error_count:
            error_count[error] += 1
        else:
            error_count[error] = 1
    return error_count

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/register', methods=['GET','POST'])
def register():
    form  = RegistrationForm()
    return render_template ('registration.html', title = 'register', form=form)

@app.route('/Login')
def Login():
    form  = LoginForm() 
    return render_template ('login.html',title='register' , form = form)



