# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""Driving four servos on an Adafruit Feather rp2040"""

# System imports
import board
import digitalio
import pwmio
import time

# 3rd Party imports
from adafruit_motor import servo



# create a PWMOut object on Pin SDA.
pwms = []
pwms.append(pwmio.PWMOut(board.SDA, duty_cycle=2 ** 15, frequency=50))
pwms.append(pwmio.PWMOut(board.D4, duty_cycle=2 ** 15, frequency=50))
pwms.append(pwmio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50))
pwms.append(pwmio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50))

# Create servo objects
servos = []
for i in range(0, len(pwms)):
    servos.append(servo.Servo(pwms[i], min_pulse = 750, max_pulse = 2000))

pir = digitalio.DigitalInOut(board.RX)
pir.direction = digitalio.Direction.INPUT

def back():
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        for i in range(0, len(servos)):
            servos[i].angle = angle
        time.sleep(0.05)

def forth():
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        for i in range(0, len(servos)):
            servos[i].angle = angle
        time.sleep(0.05)

print("Hello World!")

while True:
    if (pir.value):
        print("PIR active!")
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
    else:
        print("PIR not active")
        time.sleep(2)
