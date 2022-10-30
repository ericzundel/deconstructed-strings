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

pirs =[]
pirs.append(digitalio.DigitalInOut(board.D13))
pirs.append(digitalio.DigitalInOut(board.RX))

for pir in pirs:
  pir.direction = digitalio.Direction.INPUT

def setAll(angle):
    for servo in servos:
            servo.angle = angle
def back():
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        for servo in servos:
            servo.angle = angle
        time.sleep(0.05)

def forth():
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        for servo in servos:
            servo.angle = angle
        time.sleep(0.05)

print("Hello World!")
setAll(0)

while True:
    if (pirs[0].value and  pirs[1].value):
        print("Both PIRs active!")
        for servo in servos:
            servo = 45
        time.sleep(.5)
        for servo in servos:
            servo = 135
        time.sleep(.5)
    if (pirs[0].value):
        print("PIR 0 active!")
        servos[0].angle = 0
        servos[1].angle = 180
        servos[2].angle = 45
        servos[3].angle = 90
        time.sleep(2)
        servos[0].angle = 180
        servos[1].angle = 0
        servos[2].angle = 90
        servos[3].angle = 45
        time.sleep(2)
    elif (pirs[1].value):
        print("PIR 1 active!")
        print("back")
        back()
        print("forth")
        forth()
    else:
        print("PIRs not active")
        time.sleep(2)
