import time
from flask import Flask, render_template, request, redirect, url_for
from adafruit_pca9685 import PCA9685
from board import SCL, SDA
import busio
import signal

# Initialize I2C bus and PCA9685
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50  # Set frequency to 50 Hz for standard servos

# Define PCA9685 channels for each motor
SERVO_CHANNELS = [1, 2, 3, 4]  # Channels for four MG996R motors

# Function to set servo angle on PCA9685
def set_angle(channel, angle):
    min_pulse = 1000  # Min pulse length in microseconds
    max_pulse = 2000  # Max pulse length in microseconds
    pulse_width = min_pulse + (angle / 180) * (max_pulse - min_pulse)
    duty_cycle = int(pulse_width / 20000 * 0xFFFF)  # Convert to 16-bit duty cycle
    pca.channels[channel].duty_cycle = duty_cycle

# Function to move all servos forward
def move_forward():
    for channel in SERVO_CHANNELS:
        set_angle(channel, 0)  # Move all motors to 0 degrees for forward
    time.sleep(1)

# Function to move all servos backward
def move_backward():
    for channel in SERVO_CHANNELS:
        set_angle(channel, 180)  # Move all motors to 180 degrees for backward
    time.sleep(1)

# Function to turn left (one side forward, one side backward)
def turn_left():
    set_angle(SERVO_CHANNELS[0], 180)  # Left wheel 1 backward
    set_angle(SERVO_CHANNELS[1], 180)  # Left wheel 2 backward
    set_angle(SERVO_CHANNELS[2], 0)    # Right wheel 1 forward
    set_angle(SERVO_CHANNELS[3], 0)    # Right wheel 2 forward
    time.sleep(1)

# Function to turn right (one side backward, one side forward)
def turn_right():
    set_angle(SERVO_CHANNELS[0], 0)    # Left wheel 1 forward
    set_angle(SERVO_CHANNELS[1], 0)    # Left wheel 2 forward
    set_angle(SERVO_CHANNELS[2], 180)  # Right wheel 1 backward
    set_angle(SERVO_CHANNELS[3], 180)  # Right wheel 2 backward
    time.sleep(1)

# Function to stop all servos
def stop():
    for channel in SERVO_CHANNELS:
        pca.channels[channel].duty_cycle = 0

# Flask app setup
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    action = request.form['action']
    if action == 'forward':
        move_forward()
    elif action == 'backward':
        move_backward()
    elif action == 'left':
        turn_left()
    elif action == 'right':
        turn_right()
    elif action == 'stop':
        stop()
    return redirect(url_for('index'))

# Cleanup on exit
def cleanup(signal, frame):
    stop()  # Stop any movement
    pca.deinit()  # Deinitialize PCA9685

# Bind the cleanup function to exit signals
signal.signal(signal.SIGINT, cleanup)
signal.signal(signal.SIGTERM, cleanup)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    finally:
        cleanup(None, None)
