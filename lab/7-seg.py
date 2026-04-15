from gpiozero import LED
from time import sleep

# Define segments
a = LED(17)
b = LED(18)
c = LED(27)
d = LED(22)
e = LED(23)
f = LED(24)
g = LED(25)

# Digit mapping using actual segment objects
digits = {
    0: [a, b, c, d, e, f],
    1: [b, c],
    2: [a, b, d, e, g],
    3: [a, b, c, d, g],
    4: [b, c, f, g],
    5: [a, c, d, f, g],
    6: [a, c, d, e, f, g],
    7: [a, b, c],
    8: [a, b, c, d, e, f, g],
    9: [a, b, c, d, f, g]
}

# All segments list
all_segments = [a, b, c, d, e, f, g]

def display(num):
    # Turn OFF all
    for seg in all_segments:
        seg.off()

    # Turn ON required
    for seg in digits[num]:
        seg.on()

try:
    while True:
        for i in range(10):
            print("Displaying:", i)
            display(i)
            sleep(1)

except KeyboardInterrupt:
    print("Stopped")