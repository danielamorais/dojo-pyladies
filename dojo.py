import pingo
from flask import Flask
from time import sleep

app = Flask(__name__)
board = pingo.detect.MyBoard()
led_pin = board.pins[13]
led_pin.mode = pingo.OUT
led_pin.lo()

@app.route('/high')
def highLed():
    led_pin.hi()
    print('HIGH')
    return 'HIGH'
@app.route('/low')
def lowLed():
    led_pin.lo()
    print('LOW')
    return 'LOW'

def main():
    while True:
        highLed()
        sleep(1)
        lowLed()
        sleep(1)
	

if __name__ == "__main__":
    app.run()
