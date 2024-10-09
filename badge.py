from machine import Pin
from time import sleep
import random
import rp2
from rp2 import PIO
import ujson as json


LEDPin28=28
LEDPin27=27
LEDPin26=26

LEDPin22=22
LEDPin21=21
LEDPin20=20

LEDPin19=19
LEDPin18=18
LEDPin17=17

LEDPin0=0
LEDPin1=1
LEDPin2=2

LEDPin3=3
LEDPin4=4
LEDPin5=5

LEDPin6=6
LEDPin7=7
LEDPin8=8

myLED1_R=Pin(LEDPin28,Pin.OUT)
myLED1_G=Pin(LEDPin27,Pin.OUT)
myLED1_B=Pin(LEDPin26,Pin.OUT)

myLED2_R=Pin(LEDPin22,Pin.OUT)
myLED2_G=Pin(LEDPin21,Pin.OUT)
myLED2_B=Pin(LEDPin20,Pin.OUT)

myLED3_R=Pin(LEDPin6,Pin.OUT) 
myLED3_G=Pin(LEDPin7,Pin.OUT)
myLED3_B=Pin(LEDPin8,Pin.OUT)

myLED4_R=Pin(LEDPin0,Pin.OUT)
myLED4_G=Pin(LEDPin1,Pin.OUT)
myLED4_B=Pin(LEDPin2,Pin.OUT)

myLED5_R=Pin(LEDPin3,Pin.OUT)
myLED5_G=Pin(LEDPin4,Pin.OUT)
myLED5_B=Pin(LEDPin5,Pin.OUT)

myLED6_R=Pin(LEDPin19,Pin.OUT)
myLED6_G=Pin(LEDPin18,Pin.OUT)
myLED6_B=Pin(LEDPin17,Pin.OUT)

myLED1_R.value(1)
myLED1_G.value(1)
myLED1_B.value(1)

myLED2_R.value(1)
myLED2_G.value(1)
myLED2_B.value(1)

myLED3_R.value(1)
myLED3_G.value(1)
myLED3_B.value(1)

myLED4_R.value(1)
myLED4_G.value(1)
myLED4_B.value(1)

myLED5_R.value(1)
myLED5_G.value(1)
myLED5_B.value(1)

myLED6_R.value(1)
myLED6_G.value(1)
myLED6_B.value(1)

butPin=9
myButton=Pin(butPin,Pin.IN,Pin.PULL_UP)
butPinr=16
myButtonr=Pin(butPinr,Pin.IN,Pin.PULL_UP)
butStateNow=1
butStateOld=1
LEDState=False

# how fast the lights are moving initially
delayTime = 0.07
# range for how fast the light will move from LED to LED
# Using random function to make it harder for the user
# to time the button press
delayTimeMin = 0.03
delayTimeMax = 0.12

# variables to track interrupt activation and time for debouncing
interrupt_flag = 0
debounce_time = 0

# interrupt function
def button_handler(myButton):
    global interrupt_flag, debounce_time
    if (utime.ticks_ms()-debounce_time) > 300:
        interrupt_flag = 1
        debounce_time=utime.ticks_ms()

def button_handler2(myButtonr):
    global interrupt_flag, debounce_time
    if (utime.ticks_ms()-debounce_time) > 300:
        interrupt_flag = 2
        debounce_time=utime.ticks_ms()


# interrupt request
myButton.irq(trigger=Pin.IRQ_RISING, handler=button_handler)
myButtonr.irq(trigger=Pin.IRQ_RISING, handler=button_handler2)

import utime

import machine
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd


I2C_ADDR     = 0x27  
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

print("Running test_main")
i2c = I2C(1, sda=machine.Pin(14), scl=machine.Pin(15), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)    
#lcd.putstr("It Works!")
#utime.sleep(2)
    
#open JSON file and load LED state
try:
    with open('savedata.json', 'r') as f:
        data = json.load(f)
        led_state= data["stateKey"]
except:
    led_state= False
    print("LED state variable not found. Starting with all as OFF.")
    
jsonData = {"stateKey": led_state}

# Save LED state to JSON file
def save_led_state(state):
    jsonData["stateKey"]=state
    try:
        with open('savedata.json', 'w') as f:
            json.dump(jsonData, f)
    except:
        print("Could not save the ctf state variable.")

#Turn LED on/off depending on the state read from JSON file.
#led.value(led_state)
        
if led_state == 1:
    print ("ctf 1 complete ")   
    myLED1_R.value(0)
    myLED1_G.value(0)
    myLED1_B.value(0)
    myLED6_R.value(0)
    myLED6_G.value(0)
    myLED6_B.value(0)
    
if led_state == 2:
    print ("ctf 2 complete ")   
    myLED1_R.value(0)
    myLED1_G.value(0)
    myLED1_B.value(0)
    myLED6_R.value(0)
    myLED6_G.value(0)
    myLED6_B.value(0)
    myLED2_R.value(1)
    myLED2_G.value(0)
    myLED2_B.value(1)
    myLED5_R.value(1)
    myLED5_G.value(0)
    myLED5_B.value(1)

if led_state == 3:
    print ("ctf 3 complete ")   
    myLED1_R.value(0)
    myLED1_G.value(0)
    myLED1_B.value(0)
    myLED6_R.value(0)
    myLED6_G.value(0)
    myLED6_B.value(0)
    myLED2_R.value(1)
    myLED2_G.value(0)
    myLED2_B.value(1)
    myLED5_R.value(1)
    myLED5_G.value(0)
    myLED5_B.value(1)
    myLED3_R.value(1)
    myLED3_G.value(1)
    myLED3_B.value(0)
    myLED4_R.value(1)
    myLED4_G.value(1)
    myLED4_B.value(0)


lcd.clear()
lcd.custom_char(0,bytearray([
    0x00,
    0x0A,
    0x1F,
    0x0A,
    0x02,
    0x04,
    0x08,
    0x00]))
lcd.custom_char(1,bytearray([
    0x01,
    0x02,
    0x0C,
    0x14,
    0x04,
    0x04,
    0x04,
    0x00
    ]))
lcd.custom_char(2,bytearray([
    0x00,
  0x1F,
  0x01,
  0x01,
  0x01,
  0x01,
  0x1F,
  0x00
    ]))
lcd.custom_char(3,bytearray([
    0x00,
  0x04,
  0x1F,
  0x11,
  0x01,
  0x02,
  0x04,
  0x00
    ]))
lcd.custom_char(4,bytearray([
   0x00,
  0x00,
  0x00,
  0x00,
  0x1F,
  0x00,
  0x00,
  0x00 
    ]))
lcd.move_to(6,0)
lcd.putchar(chr(0))
lcd.move_to(7,0)
lcd.putchar(chr(1))
lcd.move_to(8,0)
lcd.putchar(chr(2))
lcd.move_to(9,0)
lcd.putchar(chr(3))
#lcd.move_to(9,0)
#lcd.putchar(chr(4))
lcd.move_to(0,1)
lcd.putstr("<Game      LEDs>")
utime.sleep(2)

          
import select
import sys

# setup poll to read USB port
poll_object = select.poll()
poll_object.register(sys.stdin,1)

#while True:
    # check usb input
    
       
while True:
    #check usb input
    if select.select([sys.stdin],[],[],0)[0]:
        ch = sys.stdin.readline()
        
        if ch[0]== '*' and ch[1]== '*' and ch[2]== '*' and ch[3]=='\\n':
            print ("Welcome to SAIKO Badge CTF!")
            print (" ")   
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr("Welcome to SAIKO")
            lcd.move_to(0,1)
            lcd.putstr("   Badge CTF.")
            utime.sleep(2)
            print ("1. Decode")   
            print (" ")   
            print ("dGhlc2Fpa29iYWRnZQ==")
            print (" ")   
            print ("Please enter your flag.")
            print (" ")
            lcd.clear()
            lcd.move_to(0,0)
            lcd.putstr("Challenge 1")
            lcd.move_to(0,1)
            lcd.putstr("SAIKO Badge CTF.")
            while True:
                if select.select([sys.stdin],[],[],0)[0]:
                    ch = sys.stdin.readline()
                    
                    if ch[0]== 't' and ch[1]== 'h' and ch[2]== 'e' and ch[3]== 's' and ch[4]== 'a' and ch[5]== 'i' and ch[6]== 'k' and ch[7]== 'o' and ch[8]== 'b' and ch[9]== 'a' and ch[10]== 'd' and ch[11]== 'g' and ch[12]== 'e' and ch[13]=='\\n':
                        print ("Challenge 1 is unlocked!")
                        print (" ")   
                        myLED1_R.value(0)
                        myLED1_G.value(0)
                        myLED1_B.value(0)
                        myLED6_R.value(0)
                        myLED6_G.value(0)
                        myLED6_B.value(0)
                        save_led_state(1)
                        print ("2. Stegano")
                        print (" ")   
                        print ("Secret hidden beneath the layers.")
                        print (" ")
                        print ("hackerware.io%2Fsri-soul.zip")
                        print (" ")   
                        print ("Please enter your flag.")
                        print (" ")
                        lcd.clear()
                        lcd.move_to(0,0)
                        lcd.putstr("Challenge 2")
                        lcd.move_to(0,1)
                        lcd.putstr("SAIKO Badge CTF.")
                        while True:
                            if select.select([sys.stdin],[],[],0)[0]:
                                ch = sys.stdin.readline()
                   
                                if ch[0]== 's' and ch[1]== '4' and ch[2]== '1' and ch[3]== 'k' and ch[4]== '0' and ch[5]=='\\n':
                                    print ("Challenge 2 is unlocked!")
                                    print (" ")   
                                    myLED2_R.value(1)
                                    myLED2_G.value(0)
                                    myLED2_B.value(1)
                                    myLED5_R.value(1)
                                    myLED5_G.value(0)
                                    myLED5_B.value(1)
                                    save_led_state(2)
                                    print ("3. Crypto")
                                    print (" ")   
                                    print ("$9$Ngd24aJDikPbsqf5Qn6M8X7NbUDk5T3ZUqf5Q9C")
                                    print (" ")   
                                    print ("Please enter your flag.")
                                    print (" ")
                                    lcd.clear()
                                    lcd.move_to(0,0)
                                    lcd.putstr("Challenge 3")
                                    lcd.move_to(0,1)
                                    lcd.putstr("SAIKO Badge CTF.")
                                    while True:
                                        if poll_object.poll(0):
                                            ch = sys.stdin.readline()
                               
                                            if ch[0]== '5' and ch[1]== 'a' and ch[2]== 'i' and ch[3]== 'k' and ch[4]== 'o' and ch[5]== '4' and ch[6]== 'w' and ch[7]== 'a' and ch[8]== 'k' and ch[9]== 'e' and ch[10]== 'n' and ch[11]== 'e' and ch[12]== 'd' and ch[13]=='\\n':
                                                print ("Congrats on completing the SAIKO BadgeCTF!")
                                                print (" ")   
                                                myLED3_R.value(1)
                                                myLED3_G.value(1)
                                                myLED3_B.value(0)
                                                myLED4_R.value(1)
                                                myLED4_G.value(1)
                                                myLED4_B.value(0)
                                                save_led_state(3)
                                                
                                                print ("       -=+++==--===++=---")
                                                print (".-----==+++==========:-===-----.")   
                                                print (":=:   .:+++==========::=-.   :=:")
                                                print (".=-     =+++========-:-=:    -=.")   
                                                print (" :=:    -+++========-:-=    :=:")
                                                print ("  :=:   .+++========-:=-   :=:")
                                                print ("   .-=:..=+*========:-=:.:=-.")
                                                print ("      .:-==++======-:-=-:.")
                                                print ("           :=+====--:")
                                                print ("             -+===-")
                                                print ("              :+=:")
                                                print ("              .+-.")
                                                print ("              -+=:")
                                                print ("            .=+==-:.")
                                                print ("         :-**+===++==-:")
                                                print ("         +#   SAIKO  #+")
                                                print ("         +# CTF NINJA +")
                                                print ("         +#*+++++++++++")
                                                print ("        :***********+++-")
                                                lcd.clear()
                                                lcd.move_to(0,0)
                                                lcd.putstr("Completed")
                                                lcd.move_to(0,1)
                                                lcd.putstr("SAIKO Badge CTF.")
                                                while True:
                                                    myLED1_R.value(0)
                                                    myLED1_G.value(0)
                                                    myLED1_B.value(0)
                                                    myLED6_R.value(0)
                                                    myLED6_G.value(0)
                                                    myLED6_B.value(0)
                                                    myLED2_R.value(1)
                                                    myLED2_G.value(1)
                                                    myLED2_B.value(1)
                                                    myLED5_R.value(1)
                                                    myLED5_G.value(1)
                                                    myLED5_B.value(1)
                                                    myLED3_R.value(1)
                                                    myLED3_G.value(1)
                                                    myLED3_B.value(1)
                                                    myLED4_R.value(1)
                                                    myLED4_G.value(1)
                                                    myLED4_B.value(1)
                                                    utime.sleep(0.2)
                                                    myLED1_R.value(1)
                                                    myLED1_G.value(1)
                                                    myLED1_B.value(1)
                                                    myLED6_R.value(1)
                                                    myLED6_G.value(1)
                                                    myLED6_B.value(1)
                                                    myLED2_R.value(1)
                                                    myLED2_G.value(0)
                                                    myLED2_B.value(1)
                                                    myLED5_R.value(1)
                                                    myLED5_G.value(0)
                                                    myLED5_B.value(1)
                                                    myLED3_R.value(1)
                                                    myLED3_G.value(1)
                                                    myLED3_B.value(1)
                                                    myLED4_R.value(1)
                                                    myLED4_G.value(1)
                                                    myLED4_B.value(1)
                                                    utime.sleep(0.2)
                                                    myLED1_R.value(1)
                                                    myLED1_G.value(1)
                                                    myLED1_B.value(1)
                                                    myLED6_R.value(1)
                                                    myLED6_G.value(1)
                                                    myLED6_B.value(1)
                                                    myLED3_R.value(1)
                                                    myLED3_G.value(1)
                                                    myLED3_B.value(0)
                                                    myLED4_R.value(1)
                                                    myLED4_G.value(1)
                                                    myLED4_B.value(0)
                                                    myLED2_R.value(1)
                                                    myLED2_G.value(1)
                                                    myLED2_B.value(1)
                                                    myLED5_R.value(1)
                                                    myLED5_G.value(1)
                                                    myLED5_B.value(1)
                                                    utime.sleep(0.2)
                                                            
                                            else:
                                                print ("Please try again. All flags are in lower caps.")   
                                                print (" ")
                                                                    
                                else:
                                    print ("Please try again. All flags are in lower caps.")   
                                    print (" ")
                                
                    else:    
                        print ("Please try again. All flags are in lower caps.")   
                        print (" ")   
                        
        if ch[0]== 'R' and ch[1]== 'E' and ch[2]== 'S' and ch[3]=='\\n':
            print ("SAIKO Badge CTF! RESET")
            save_led_state(0)
            myLED1_R.value(1)
            myLED1_G.value(1)
            myLED1_B.value(1)
            myLED6_R.value(1)
            myLED6_G.value(1)
            myLED6_B.value(1)
            myLED3_R.value(1)
            myLED3_G.value(1)
            myLED3_B.value(1)
            myLED4_R.value(1)
            myLED4_G.value(1)
            myLED4_B.value(1)
            myLED2_R.value(1)
            myLED2_G.value(1)
            myLED2_B.value(1)
            myLED5_R.value(1)
            myLED5_G.value(1)
            myLED5_B.value(1)
            #open JSON file and load LED state
            try:
                with open('savedata.json', 'r') as f:
                    data = json.load(f)
                    led_state= data["stateKey"]
            except:
                led_state= False
                print("LED state variable not found. Starting with all as OFF.")
                
            jsonData = {"stateKey": led_state}
            break
        
        else: 
            print ("Wrong input")
      # print (ch,"hello from the pico")
    
    if interrupt_flag == 2:
        interrupt_flag = 0
        myLED1_R.value(1)
        myLED1_G.value(1)
        myLED1_B.value(1)
        myLED6_R.value(1)
        myLED6_G.value(1)
        myLED6_B.value(1)
        myLED3_R.value(1)
        myLED3_G.value(1)
        myLED3_B.value(1)
        myLED4_R.value(1)
        myLED4_G.value(1)
        myLED4_B.value(1)
        myLED2_R.value(1)
        myLED2_G.value(1)
        myLED2_B.value(1)
        myLED5_R.value(1)
        myLED5_G.value(1)
        myLED5_B.value(1)
        while True:
            #white
            myLED1_R.value(0)
            myLED1_G.value(0)
            myLED1_B.value(0)
            utime.sleep(0.2)
            myLED1_R.value(1)
            myLED1_G.value(1)
            myLED1_B.value(1)
            myLED2_R.value(0)
            myLED2_G.value(0)
            myLED2_B.value(0)
            utime.sleep(0.2)
            myLED2_R.value(1)
            myLED2_G.value(1)
            myLED2_B.value(1)
            myLED3_R.value(0)
            myLED3_G.value(0)
            myLED3_B.value(0)
            utime.sleep(0.2)
            myLED3_R.value(1)
            myLED3_G.value(1)
            myLED3_B.value(1)
            myLED4_R.value(0)
            myLED4_G.value(0)
            myLED4_B.value(0)
            utime.sleep(0.2)
            myLED4_R.value(1)
            myLED4_G.value(1)
            myLED4_B.value(1)
            myLED5_R.value(0)
            myLED5_G.value(0)
            myLED5_B.value(0)
            utime.sleep(0.2)
            myLED5_R.value(1)
            myLED5_G.value(1)
            myLED5_B.value(1)
            myLED6_R.value(0)
            myLED6_G.value(0)
            myLED6_B.value(0)
            utime.sleep(0.2)
            #all off
            myLED1_R.value(1)
            myLED1_G.value(1)
            myLED1_B.value(1)
            myLED6_R.value(1)
            myLED6_G.value(1)
            myLED6_B.value(1)
            myLED3_R.value(1)
            myLED3_G.value(1)
            myLED3_B.value(1)
            myLED4_R.value(1)
            myLED4_G.value(1)
            myLED4_B.value(1)
            myLED2_R.value(1)
            myLED2_G.value(1)
            myLED2_B.value(1)
            myLED5_R.value(1)
            myLED5_G.value(1)
            myLED5_B.value(1)
            if interrupt_flag == 1:
                interrupt_flag = 0
                print("Interrupt 1 Detected")  
                break
           #yellow
            myLED1_R.value(0)
            myLED1_G.value(0)
            myLED1_B.value(1)
            utime.sleep(0.2)
            myLED1_R.value(1)
            myLED1_G.value(1)
            myLED2_R.value(0)
            myLED2_G.value(0)
            myLED2_B.value(1)
            utime.sleep(0.2)
            myLED2_R.value(1)
            myLED2_G.value(1)
            myLED3_R.value(0)
            myLED3_G.value(0)
            myLED3_B.value(1)
            utime.sleep(0.2)
            myLED3_R.value(1)
            myLED3_G.value(1)
            myLED4_R.value(0)
            myLED4_G.value(0)
            myLED4_B.value(1)
            utime.sleep(0.2)
            myLED4_R.value(1)
            myLED4_G.value(1)
            myLED5_R.value(0)
            myLED5_G.value(0)
            myLED5_B.value(1)
            utime.sleep(0.2)
            myLED5_R.value(1)
            myLED5_G.value(1)
            myLED6_R.value(0)
            myLED6_G.value(0)
            myLED6_B.value(1)
            utime.sleep(0.2)
            #all off
            myLED1_R.value(1)
            myLED1_G.value(1)
            myLED1_B.value(1)
            myLED6_R.value(1)
            myLED6_G.value(1)
            myLED6_B.value(1)
            myLED3_R.value(1)
            myLED3_G.value(1)
            myLED3_B.value(1)
            myLED4_R.value(1)
            myLED4_G.value(1)
            myLED4_B.value(1)
            myLED2_R.value(1)
            myLED2_G.value(1)
            myLED2_B.value(1)
            myLED5_R.value(1)
            myLED5_G.value(1)
            myLED5_B.value(1)
            if interrupt_flag == 1:
                interrupt_flag = 0
                print("Interrupt 1 Detected")  
                break
           #Green
            myLED1_R.value(1)
            myLED1_G.value(0)
            myLED1_B.value(1)
            utime.sleep(0.2)
            myLED1_G.value(1)
            myLED2_R.value(1)
            myLED2_G.value(0)
            myLED2_B.value(1)
            utime.sleep(0.2)
            myLED2_G.value(1)
            myLED3_R.value(1)
            myLED3_G.value(0)
            myLED3_B.value(1)
            utime.sleep(0.2)
            myLED3_G.value(1)
            myLED4_R.value(1)
            myLED4_G.value(0)
            myLED4_B.value(1)
            utime.sleep(0.2)
            myLED4_G.value(1)
            myLED5_R.value(1)
            myLED5_G.value(0)
            myLED5_B.value(1)
            utime.sleep(0.2)
            myLED5_G.value(1)
            myLED6_R.value(1)
            myLED6_G.value(0)
            myLED6_B.value(1)
            utime.sleep(0.2)
            #all off
            myLED1_R.value(1)
            myLED1_G.value(1)
            myLED1_B.value(1)
            myLED6_R.value(1)
            myLED6_G.value(1)
            myLED6_B.value(1)
            myLED3_R.value(1)
            myLED3_G.value(1)
            myLED3_B.value(1)
            myLED4_R.value(1)
            myLED4_G.value(1)
            myLED4_B.value(1)
            myLED2_R.value(1)
            myLED2_G.value(1)
            myLED2_B.value(1)
            myLED5_R.value(1)
            myLED5_G.value(1)
            myLED5_B.value(1)
            if interrupt_flag == 1:
                interrupt_flag = 0
                print("Interrupt 1 Detected")  
                break
            #Blue
            myLED1_R.value(1)
            myLED1_G.value(1)
            myLED1_B.value(0)
            utime.sleep(0.2)
            myLED1_B.value(1)
            myLED2_R.value(1)
            myLED2_G.value(1)
            myLED2_B.value(0)
            utime.sleep(0.2)
            myLED2_B.value(1)
            myLED3_R.value(1)
            myLED3_G.value(1)
            myLED3_B.value(0)
            utime.sleep(0.2)
            myLED3_B.value(1)
            myLED4_R.value(1)
            myLED4_G.value(1)
            myLED4_B.value(0)
            utime.sleep(0.2)
            myLED4_B.value(1)
            myLED5_R.value(1)
            myLED5_G.value(1)
            myLED5_B.value(0)
            utime.sleep(0.2)
            myLED5_B.value(1)
            myLED6_R.value(1)
            myLED6_G.value(1)
            myLED6_B.value(0)
            utime.sleep(0.2)
            #all off
            myLED1_R.value(1)
            myLED1_G.value(1)
            myLED1_B.value(1)
            myLED6_R.value(1)
            myLED6_G.value(1)
            myLED6_B.value(1)
            myLED3_R.value(1)
            myLED3_G.value(1)
            myLED3_B.value(1)
            myLED4_R.value(1)
            myLED4_G.value(1)
            myLED4_B.value(1)
            myLED2_R.value(1)
            myLED2_G.value(1)
            myLED2_B.value(1)
            myLED5_R.value(1)
            myLED5_G.value(1)
            myLED5_B.value(1)
            
            if interrupt_flag == 1:
                interrupt_flag = 0
                print("Interrupt 1 Detected")  
                break
    
        myLED1_R.value(1)
        myLED1_G.value(1)
        myLED1_B.value(1)
        myLED6_R.value(1)
        myLED6_G.value(1)
        myLED6_B.value(1)
        myLED3_R.value(1)
        myLED3_G.value(1)
        myLED3_B.value(1)
        myLED4_R.value(1)
        myLED4_G.value(1)
        myLED4_B.value(1)
        myLED2_R.value(1)
        myLED2_G.value(1)
        myLED2_B.value(1)
        myLED5_R.value(1)
        myLED5_G.value(1)
        myLED5_B.value(1)
        if led_state == 1:
            myLED1_R.value(0)
            myLED1_G.value(0)
            myLED1_B.value(0)
            myLED6_R.value(0)
            myLED6_G.value(0)
            myLED6_B.value(0)
            
        if led_state == 2:
            myLED1_R.value(0)
            myLED1_G.value(0)
            myLED1_B.value(0)
            myLED6_R.value(0)
            myLED6_G.value(0)
            myLED6_B.value(0)
            myLED2_R.value(1)
            myLED2_G.value(0)
            myLED2_B.value(1)
            myLED5_R.value(1)
            myLED5_G.value(0)
            myLED5_B.value(1)

        if led_state == 3:
            myLED1_R.value(0)
            myLED1_G.value(0)
            myLED1_B.value(0)
            myLED6_R.value(0)
            myLED6_G.value(0)
            myLED6_B.value(0)
            myLED2_R.value(1)
            myLED2_G.value(0)
            myLED2_B.value(1)
            myLED5_R.value(1)
            myLED5_G.value(0)
            myLED5_B.value(1)
            myLED3_R.value(1)
            myLED3_G.value(1)
            myLED3_B.value(0)
            myLED4_R.value(1)
            myLED4_G.value(1)
            myLED4_B.value(0)
    
    if interrupt_flag == 1:
        interrupt_flag = 0
        myLED1_R.value(1)
        myLED1_G.value(1)
        myLED1_B.value(1)
        myLED6_R.value(1)
        myLED6_G.value(1)
        myLED6_B.value(1)
        myLED3_R.value(1)
        myLED3_G.value(1)
        myLED3_B.value(1)
        myLED4_R.value(1)
        myLED4_G.value(1)
        myLED4_B.value(1)
        myLED2_R.value(1)
        myLED2_G.value(1)
        myLED2_B.value(1)
        myLED5_R.value(1)
        myLED5_G.value(1)
        myLED5_B.value(1)
        lcd.clear()
        print("Interrupt 1 Detected")
        lcd.move_to(0,0)
        lcd.putstr("GAME BEGINS.....")
        lcd.move_to(0,1)
        lcd.putstr("CATCH THE RED ")
        utime.sleep(2)
        
        while True:
            myLED1_B.toggle()
            myLED6_G.value(1)
            utime.sleep(delayTime)
            if interrupt_flag == 2:
                interrupt_flag = 0
                print("Interrupt 2 Detected")
                lcd.move_to(0,0)
                lcd.putstr("Too Fast        ")
                lcd.move_to(0,1)
                lcd.putstr("Restarts In 5sec")
                utime.sleep(5)
                lcd.clear()
                lcd.move_to(0,0)
                lcd.putstr("GAME BEGINS.....")
                lcd.move_to(0,1)
                lcd.putstr("CATCH THE RED ")
            if interrupt_flag == 1:
                interrupt_flag = 0
                print("Interrupt 1 Detected")  
                break
            delayTime = random.uniform(delayTimeMin, delayTimeMax)
            myLED1_B.toggle()
            myLED2_B.toggle()
            utime.sleep(delayTime)
            if interrupt_flag == 2:
                interrupt_flag = 0
                print("Interrupt 2 Detected")
                lcd.move_to(0,0)
                lcd.putstr("Too Fast        ")
                lcd.move_to(0,1)
                lcd.putstr("Restarts In 5sec")
                utime.sleep(5)
                lcd.clear()
                lcd.move_to(0,0)
                lcd.putstr("GAME BEGINS.....")
                lcd.move_to(0,1)
                lcd.putstr("CATCH THE RED ")
            if interrupt_flag == 1:
                interrupt_flag = 0
                print("Interrupt 1 Detected")  
                break
            delayTime = random.uniform(delayTimeMin, delayTimeMax)
            myLED2_B.toggle()
            myLED3_B.toggle()
            utime.sleep(delayTime)
            if interrupt_flag == 2:
                interrupt_flag = 0
                print("Interrupt 2 Detected")
                lcd.move_to(0,0)
                lcd.putstr("Too Fast        ")
                lcd.move_to(0,1)
                lcd.putstr("Restarts In 5sec")
                utime.sleep(5)
                lcd.clear()
                lcd.move_to(0,0)
                lcd.putstr("GAME BEGINS.....")
                lcd.move_to(0,1)
                lcd.putstr("CATCH THE RED ")
            if interrupt_flag == 1:
                interrupt_flag = 0
                print("Interrupt 1 Detected")  
                break
            delayTime = random.uniform(delayTimeMin, delayTimeMax)
            myLED3_B.toggle()
            myLED4_G.toggle()
            utime.sleep(delayTime)
            if interrupt_flag == 2:
                interrupt_flag = 0
                print("Interrupt 2 Detected")
                lcd.move_to(0,0)
                lcd.putstr("Too Fast        ")
                lcd.move_to(0,1)
                lcd.putstr("Restarts In 5sec")
                utime.sleep(5)
                lcd.clear()
                lcd.move_to(0,0)
                lcd.putstr("GAME BEGINS.....")
                lcd.move_to(0,1)
                lcd.putstr("CATCH THE RED ")
            if interrupt_flag == 1:
                interrupt_flag = 0
                print("Interrupt 1 Detected")  
                break
            delayTime = random.uniform(delayTimeMin, delayTimeMax)
            myLED4_G.toggle()
            myLED5_R.toggle()
            utime.sleep(delayTime)
            if interrupt_flag == 2:
                interrupt_flag = 0
                print("Interrupt 2 Detected")
                lcd.move_to(0,0)
                lcd.putstr("Bullseye        ")
                lcd.move_to(0,1)
                lcd.putstr("Restarts In 5sec")
                utime.sleep(5)
                lcd.clear()
                lcd.move_to(0,0)
                lcd.putstr("GAME BEGINS.....")
                lcd.move_to(0,1)
                lcd.putstr("CATCH THE RED ")
            if interrupt_flag == 1:
                interrupt_flag = 0
                print("Interrupt 1 Detected")  
                break
            delayTime = random.uniform(delayTimeMin, delayTimeMax)
            myLED5_R.toggle()
            myLED6_G.toggle()
            utime.sleep(delayTime)
            if interrupt_flag == 2:
                interrupt_flag = 0
                print("Interrupt 2 Detected")
                lcd.move_to(0,0)
                lcd.putstr("Too Late        ")
                lcd.move_to(0,1)
                lcd.putstr("Restarts In 5sec")
                utime.sleep(5)
                lcd.clear()
                lcd.move_to(0,0)
                lcd.putstr("GAME BEGINS.....")
                lcd.move_to(0,1)
                lcd.putstr("CATCH THE RED ")
            if interrupt_flag == 1:
                interrupt_flag = 0
                print("Interrupt 1 Detected")  
                break
        print("exit")
        myLED1_B.value(1)
        myLED2_B.value(1)  
        myLED3_B.value(1)
        myLED4_G.value(1)
        myLED5_R.value(1)
        myLED6_G.value(1)
        lcd.clear()
        lcd.move_to(6,0)
        lcd.putchar(chr(0))
        lcd.move_to(7,0)
        lcd.putchar(chr(1))
        lcd.move_to(8,0)
        lcd.putchar(chr(2))
        lcd.move_to(9,0)
        lcd.putchar(chr(3))
        lcd.move_to(0,1)
        lcd.putstr("<Game      LEDs>")
        if led_state == 1:
            myLED1_R.value(0)
            myLED1_G.value(0)
            myLED1_B.value(0)
            myLED6_R.value(0)
            myLED6_G.value(0)
            myLED6_B.value(0)
            
        if led_state == 2:
            myLED1_R.value(0)
            myLED1_G.value(0)
            myLED1_B.value(0)
            myLED6_R.value(0)
            myLED6_G.value(0)
            myLED6_B.value(0)
            myLED2_R.value(1)
            myLED2_G.value(0)
            myLED2_B.value(1)
            myLED5_R.value(1)
            myLED5_G.value(0)
            myLED5_B.value(1)

        if led_state == 3:
            myLED1_R.value(0)
            myLED1_G.value(0)
            myLED1_B.value(0)
            myLED6_R.value(0)
            myLED6_G.value(0)
            myLED6_B.value(0)
            myLED2_R.value(1)
            myLED2_G.value(0)
            myLED2_B.value(1)
            myLED5_R.value(1)
            myLED5_G.value(0)
            myLED5_B.value(1)
            myLED3_R.value(1)
            myLED3_G.value(1)
            myLED3_B.value(0)
            myLED4_R.value(1)
            myLED4_G.value(1)
            myLED4_B.value(0)

        utime.sleep(2)