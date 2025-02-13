from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/sad')
def sad():
    return render_template('sad.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)