sun = 330
press = 0  
keyboard = 0 
speed = 1.5 

def setup():
    global sat_img 
    global back_img
    global sat_img2

    size(800, 450) # size has to be the same size of the background 
    sat_img = loadImage("sun2 copy 2.png") #smaller image 
    back_img = loadImage("beach.png") #background image 
    sat_img2 = loadImage("whale.png") 
    sat_img3 = loadImage("beachball.png")

def draw():
    global sun 
    global i 
    global press
    global speed  
    
    background(back_img)
    
    if keyboard == 1:
        if sun >= 600 or sun <= 320 :
            speed *= (-1) 
        sun += speed 
    image(sat_img, sun , 40, 100, 100)
    
    if press == 1:
        image(sat_img2, 160, 300, 75, 75)
     
    stroke(0,0,0)       
    fill("#ad3408") 
    quad(580, 325, 610, 325, 620, 315, 570, 315)
    fill("#e5b15e")
    triangle(580, 315, 595, 295, 610, 315)
    line(595, 295, 595, 315)

    noStroke()
    fill("#ffffff")
    ellipse(360, 50, 50, 50)
    ellipse(340, 75, 50, 50)
    ellipse(380, 75, 50, 50)
    
    textSize(24)
    fill("#447c46")
    text("Beach Day", 80,100)

def mousePressed():
    global press
    press += 1
    if press == 2:
        press = 0
    
def keyPressed(): 
    global keyboard   
    keyboard += 1 
    if keyboard == 2:
        keyboard = 0 
        

#quad(trx, try, tlx, tly, blx, bly, brx, bry)
