from machine import Pin
import time
 
ldr = machine.ADC(27)
led = Pin(25, Pin.OUT)
 
while True:
     print(ldr.read_u16())
     if ldr.read_u16() >= 15000:
         led.high()
         time.sleep(0.5)
     else:
        led.low()
        time.sleep(0.5)