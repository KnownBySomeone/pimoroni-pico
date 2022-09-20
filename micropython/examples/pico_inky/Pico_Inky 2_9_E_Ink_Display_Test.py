# Pico Inky 2.9 E-Ink Display Demo/Test
# By Known By Someone / Jeremiah B.

# Using code from Gadgetoid in https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/examples/pico_inky/button_test.py


# This code requires the following SDK or similar to be loaded on to the the Raspberry Pi Pico:
# https://github.com/pimoroni/pimoroni-pico/releases/download/v1.19.6/pimoroni-badger2040-v1.19.6-micropython.uf2


import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_INKY_PACK

# This tells the library which of the Pimoroni displays is in use.
# Do not forget to call "DISPLAY_INKY_PACK" from the library above as well.
display = PicoGraphics(display=DISPLAY_INKY_PACK)

# Not sure what this does.
# I believe it sets the speed of the screen refresh
# or it sets the earliest time after "display.update()" it can be refreshed again.
display.set_update_speed(2)



# This does the same thing as "clear()", except that "display.rectangle(0,0,w,h)"
#      can be modified to clear only a portion of the screen, reducing time required to refresh the screen.
w, h = display.get_bounds()
display.rectangle(0, 0, w, h)

# I assume this creatres a "clear()" function to erase the screen to white.
# You should be able to use "display.set_pen(0)" instead of "display.set_pen(15)" to clear the screen to black.
def clear():
    display.set_pen(15)
    display.clear()
    
# I question if this can be a native command or if it has to be defined.  I am not sure.
clear()

# Sets the display color for following display commands.  "set_pen(0)" for black and "set_pen(15)" is for white
display.set_pen(0)

# I do not know how to discribe it for now, just move some numbers around.
# Each cordinate is a point on the side of the polygon.
# The command will close the final gap, so there is no need to yourself.
display.polygon([
  (0, 10),
  (20, 10),
  (20, 0),
  (30, 15),
  (20, 30),
  (20, 20),
  (0, 20),
])

# display.pixel(x, y)
display.pixel(5, 0)

# display.line(x1, y1, x2, y2)
display.line(2, 7, 17, 3)

# display.triangle(x1, y1, x2, y2, x3, y3)
display.triangle(0, 35, 5, 25, 10, 35)

# display.circle(x, y, r)
display.circle(20, 35, 5)

# display.rectangle(x, y, w, h)
display.rectangle(0, 40, 15, 20)



display.set_pen(0)

display.set_font("bitmap8")
display.text("ABCabc", 35, 0, 200, 2)

display.set_font("bitmap6")
display.text("ABCabc", 110, 0, 200, 2)

display.set_font("bitmap14_outline")
display.text("ABCabc", 190, 0, 200, 1)

display.set_font("sans")
display.text("ABCabc", 35, 30, 200, 1)

display.set_font("gothic")
display.text("ABCabc", 170, 40, 200, 2)

display.set_font("cursive")
display.text("ABCabc", 35, 55, 200, 1)

display.set_font("serif_italic")
display.text("ABab", 165,  85, 250, 2)

display.set_font("serif")
display.text("ABab", 0, 100, 200, 2)

# posts the recent "display" commands to the screen
display.update()



display.set_pen(0)

display.set_font("bitmap8")
display.text("Button:", 190, 110, 200, 2)



display.update()


# This next part, while modified, is almost entirly from:
# https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/examples/pico_inky/button_test.py


# Setup the buttons to variables.
button_a = Button(12)
button_b = Button(13)
button_c = Button(14)


while True:
    if button_a.read():                                   # if a button press is detected then...
        display.set_pen(15)                               # change the pen colour to white
        display.rectangle(260, 107, 296, 128)             # clear the corner only
        display.set_pen(0)                                # change the pen colour to black
        display.text("A", 270, 110, 240, 2)               # display some text on the screen
        display.update()                                  # update the display
        time.sleep(0.5)
    elif button_b.read():
        display.set_pen(15)                        
        display.rectangle(260, 107, 296, 128)     
        display.set_pen(0)                           
        display.text("B", 270, 110, 240, 2)
        display.update()                     
        time.sleep(0.5)
    elif button_c.read():
        display.set_pen(15)                     
        display.rectangle(260, 107, 296, 128)          
        display.set_pen(0)                       
        display.text("C", 270, 110, 240, 2) 
        display.update()   
        time.sleep(0.5)
    time.sleep(0.1)  # this number is how frequently the Pico checks for button presses
