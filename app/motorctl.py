# print('motorctl')
# from flask import request, render_template, flash, redirect
# from app import app
# from app.forms import GoForm, GoFormInt
#from app.Alphademo import Alphademo
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, GoForm, GoFormInt
from app.Alphademo import Alphademo

car = Alphademo()

print('done imports in motorctl.py')

# @app.route('/setmotor/')
# @app.route('/setmotor/<string:left>/')
# @app.route('/setmotor/<string:left>/<string:right>')
# def setmotor(left="0",right="0"):
#     msg = ('left =' + left + "  right = " + right)
#     car.setmotor(int(left),int(right))
#     return '<h1> motor was set ' + msg + '</h1>'

# NOT BEING USED
@app.route('/setmotorstr', methods=['GET','POST'])
def setmotorstr():
    form = GoForm()
    if form.validate_on_submit():
        left = form.left.data
        right = form.right.data
        msg = ('left =' + left + "  right = " + right)
        flash('motor was set ' + msg )
        car.setMotor(int(left),int(right))
        return redirect('/index')
    return render_template('setmotor.html',form=form)


@app.route('/setmotor', methods=['GET','POST'])
def setmotor():
    form = GoFormInt()
    if form.validate_on_submit():
        left = form.left.data
        right = form.right.data
        msg = ('left =' + str(left) + "  right = " + str(right))
        flash('motor was set ' + msg )
        car.setMotor(int(left),int(right))
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
    # reset GPIOs to all output
    car.set_output_mode()

    return ( msg + '<h2> Gpio init = ' + gpio_init + '</h2>' +
            '<h2> Gpio stopped = ' + gpio_stopped + '</h2>' + 
            '<h2> Gpio forward = ' + gpio_forward + '</h2>' +
            '<h2> Gpio diabled = ' + gpio_disabled + '</h2>' )

@app.route('/setmotortest')
def setmotortest():
        left = '43'
        right = '22'
        msg = ('left =' + left + "  right = " + right)
        flash('motor was set ' + msg )
        print('motor was set ' + msg )
        car.setMotor(int(left),int(right))
        #return redirect('/index')
        return '<h1> did it work </h1>'

