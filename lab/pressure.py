import time
import board
import adafruit_bmp280

i2c = board.I2C()

sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)

sensor.sea_level_pressure = 1013.25

print("BMP280 Sensor Initialized Successfully!")
print("---------------------------------------")

while True:
    try:
        temp = sensor.temperature
        press = sensor.pressure
        alt = sensor.altitude
        
        print(f"Temperature: {temp:.2f} °C")
        print(f"Pressure:    {press:.2f} hPa")
        print(f"Altitude:    {alt:.2f} meters")
        print("---------------------------------------")
        
    except Exception as e:
        print(f"Sensor Error: {e}")
        
    time.sleep(2)

# pip3 install adafruit-circuitpython-bmp280
# pip3 install adafruit-blinka

# SCL -> GPIO 2
# SDA -> GPIO 3


# Before installing anything, you must enable the hardware ports. Without this, your code will crash even if the libraries are perfect.

# Run sudo raspi-config.

# Go to Interface Options.

# Enable I2C (for LCD and Pressure sensors).

# Enable Serial Port (for the Fingerprint sensor).

# Select No for "Login shell over serial" and Yes for "Hardware serial port".