from microbit import *
import random
import radio

flash = [] # a list. do you remember the boats?
for x in range(9, -1, -1):
    empty_img = Image()
    fully_lit_img = 
    multiplied_brightness = 
    
    # add it into flash
    flash.append(multiplied_brightness)

radio.on()

while True:
    if button_a.was_pressed(): # IMPORTANT: we use was_pressed() here to make sure we don't spam the radio.
        radio.send('flash')
    
    # receive the message
    incoming = 
    if incoming == 'flash':
        procrastination = random.randint(50, 350) # I'll do it - in a minute.
        # when you procrastinate, what do you do?
        display.show(flash, delay=100, wait=False)
        
        # roll a dice and if you land on 2, send another signal!
        if # generate a random number and check its value.
            sleep(500) # wait a little while before sending the signal
            # send the signal!
