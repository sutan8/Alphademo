from flask import Flask
from Alphademo import Alphademo

app = Flask(__name__)

car = Alphademo()

@app.route('/')
def index():
    return 'Hello World'

@app.route('
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

