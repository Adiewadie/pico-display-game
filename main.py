import picodisplay as display # comment this line out if you want to use the display2                                                  
import utime
import time
import machine  # all the libs we need for this (machine is optional)
#import picodisplay2 as display   uncomment this line if you want to use the display2
buf = bytearray(display.get_width() * display.get_height() * 2) #sets boundaries for the text
display.init(buf)
display.set_backlight(0.5)


def clear():           # sets a handy tool for clearing the screen
    display.set_pen(0, 0, 0)
    display.clear()
    display.update()
while True:
    display.set_pen(224,255,255)     
    display.text("Press A to start"10,10,240,4)
    display.update()
    if display.is_pressed(display.BUTTON_A): # just chango the button a part to b x or y to change the button
        clear()
        display.set_pen(238,44,44) # changing the pen color
        display.text("Welcome to your DOOM!"10, 10, 240, 4)
        display.update()
        utime.sleep(3) # pauses for 3 seconds
        clear()
        display.text("Oh!"10,10,240,4)
        display.update()
        utime.sleep(2)
        clear()
        display.set_pen(39,64,139)
        display.text("You scared me!"10,10,240,4)
        utime.sleep(2)
        clear()
        display.text("Well come in! Come in!"10,10,240,4)
        display.update()
        utime.sleep(2)
        clear()
        display.text("Have you come here for adventure?"10,10,240,4)
        display.update()
        sleep(2)
        clear()
        display.text("Press A for yes or X for no"10,10,240,4)
        display.update()

        if display.is_pressed(display.BUTTON_X):
            clear()
            display.text("Well then I guess I serve no purpose here"10,10,240,4)
            display.update()
            utime.sleep(2)
            clear()
            display.set_pen(220,20,60)
            display.text("GAME OVER (ಥ﹏ಥ)"10,10,240,4)    #game over 1
            display.update()
        if display.is_pressed(display.BUTTON_A):
            display.set_pen(39,64,139)
            display.text("Well then! Consider yourself lucky!"10,10,240,4)
            display.update()
            utime.sleep(3)
            clear()
            display.text("I happen to be the most famous hero around!"10,10,240,4)
            display.update()
            utime.sleep(2)
            clear()
            display.text("I once slayed a dragon"10,10,240,4)
            display.update()
            utime.sleep(2)
            clear()
            display.text("Anyway, enough talk! Let's get down to buisness"10,10,240,4)
            display.update()
            utime.sleep(2)
            clear()
            diplay.text("What kind of fighter are you?"10,10,240,4)
            display.update()
            utime.sleep(2)
            clear()
            display.text("A=Knight B=Archer X=tank Y=Wizard"10,10,240,4)
            display.update()
            if display.is_pressed(display.BUTTON_A):
                health = 150
                basic = 18
                heavy = 27
                magika = 40
                dist = 20
                accuracy = 30
                title = knight
                clear()
            if display.is_pressed(display.BUTTON_B):
                health = 100 
                basic = 20
                heavy = 8 * (accuracy / 2)
                accuracy = 35      # 1-40
                magika = 40
                dist = 60
                title = archer
                clear()
            if  display.is_pressed(display.BUTTON_X):
                health = 250
                basic = 25
                heavy = 75
                accuracy = 15
                dist = 10
                magika = 30
                title = tank
                clear()
            if display.is_pressed(display.BUTTON_Y):
                health = 85
                basic = 30
                heavy = 60
                magika = 75
                dist = 50
                title = wizard
                clear()
            display.text("I would have never guessed you were a", title,10,10,240,4)
            display.update()
            utime.sleep(2)
            clear()
            if title = knight :
                display.text("Then you should have my old sword!"10,10,240,4)
                display.update()
                utime.sleep(2)
            if title = archer :
                display.text("Then you should have my old bow!"10,10,240,4)
                display.update()
                utime.sleep(2)
            if title = tank :
                display.text("Then you should have my old armour!"10,10,240,4)
                display.update()
                utime.sleep(2)
            if title = wizard :
                display.text("You should have my old book and staff!"10,10,240,4)
                display.update()
                utime.sleep(2)
        clear()
        display.text("Wow! Your lookin' good!"10,10,240,4)
        display.update()
        utime.sleep(2)
        clear()
        display.text("Well, since it's almost nightfall we should get some sleep"10,10,240,4)
        display.update()
        utime.sleep(2)
        clear()
        display.set_backlight(0)
        display.update()
        utime.sleep(1)
        display.set_backlight(0.1)
        display.update()
        utime.sleep(1)
        display.set_backlight(0.2)
        display.update()
        utime.sleep(1)
        display.set_backlight(0.3)
        display.update()
        utime.sleep(1)
        display.set_backlight(0.4)
        display.update()
        utime.sleep(1)
        display.set_backlight(0.55)
        display.update()
        utime.sleep(1)
        display.text("Good Morning!"10,10,240,4)
        display.update()
        utime.sleep(2)
        clear()
        display.text("Not much of a Morning person eh?"10,10,240,4)
        display.update()
        utime.sleep(2)
        display.text("That's okay, we all have weaknesses"10,10,240,4)
        display.update()
        utime.sleep(2)
        clear()
        display.text("Well, anyway let's get movin!"10,10,240,4)
        
        
        
        
                
                
                
                         
                
    

