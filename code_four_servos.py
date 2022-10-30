# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo


# create a PWMOut object on Pin SDA.
pwms = []
pwms.append(pwmio.PWMOut(board.SDA, duty_cycle=2 ** 15, frequency=50))
pwms.append(pwmio.PWMOut(board.D4, duty_cycle=2 ** 15, frequency=50))
pwms.append(pwmio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50))
pwms.append(pwmio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50))

num_servos = len(pwms)

# Create a servo object
servos = []
for i in range(0, num_servos):
    servos.append(servo.Servo(pwms[i], min_pulse = 750, max_pulse = 2000))

def back():
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        for i in range(0,num_servos):
            servos[i].angle = angle
        time.sleep(0.05)

def forth():
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        for i in range(0,num_servos):
            servos[i].angle = angle
        time.sleep(0.05)

print("Hello World!")

while True:
    print("back")
    back()
    print("forth")
    forth()

    print("Sweep one way")
    servos[0].angle = 0
    servos[1].angle = 180
    servos[2].angle = 45
    servos[3].angle = 90
    time.sleep(2)

    print("Sweep the other way")
    servos[0].angle = 180
    servos[1].angle = 0
    servos[2].angle = 90
    servos[3].angle = 45
    time.sleep(2)
