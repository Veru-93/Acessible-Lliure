from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/tadah')
def tadah():
    return render_template('tadah.html')

if __name__ == '__main__':
    app.run(debug=True)