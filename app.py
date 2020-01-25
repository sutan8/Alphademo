from flask import Flask, request, render_template, flash, redirect
from Alphademo import Alphademo
from forms import  Config

app = Flask(__name__)
app.config.from_object(Config)
import motorctl


print('car instance')
car = Alphademo()

@app.route('/')
@app.route('/index')
def index():
     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


