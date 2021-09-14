from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hellow():
    return 'Hello Leela Sai Krishna'

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/contacts')
def contacts():
    return 'welcome to contacts'
if __name__ == '__main__':
    app.run()
