from flask import Flask, request, render_template, flash, redirect
from Alphademo import Alphademo
from forms import GoForm, Config

app = Flask(__name__)
app.config.from_object(Config)

car = Alphademo()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# @app.route('/setmotor/')
# @app.route('/setmotor/<string:left>/')
# @app.route('/setmotor/<string:left>/<string:right>')
# def setmotor(left="0",right="0"):
#     msg = ('left =' + left + "  right = " + right)
#     car.setmotor(int(left),int(right))
#     return '<h1> motor was set ' + msg + '</h1>'

@app.route('/setmotor', methods=['GET','POST'])
def setmotor():
    form = GoForm()
    if form.validate_on_submit():
        left = form.left.data
        right = form.right.data
        msg = ('left =' + left + "  right = " + right)
        flash('motor was set ' + msg )
        #car.setmotor(int(left),int(right))
        return redirect('/index')
    return render_template('setmotor.html',form=form)

@app.route('/gpios')
def gpio_demo():
    msg = "<h1> GPIO TEST IN1</h1>"
    gpio_init = str(car.get12())

    car.stop()
    gpio_stopped = str(car.get12())

    car.forward()
    gpio_forward = str(car.get12())

    car.disable()
    gpio_disabled = str(car.get12())

    return ( msg + '<h2> Gpio init = ' + gpio_init + '</h2>' +
            '<h2> Gpio stopped = ' + gpio_stopped + '</h2>' + 
            '<h2> Gpio forward = ' + gpio_forward + '</h2>' +
            '<h2> Gpio diabled = ' + gpio_disabled + '</h2>' )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

