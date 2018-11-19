x = 0

def setup():
    size(640, 360)
    noStroke()
    
def draw():
    global x

    if x >= 640:
        x = 0
    x += 2
    
    background(102, 158, 249)
    
    drawCloud(x+60, 100)
    drawCloud(x+200, 320)
    drawCloud(x+500, 200)
        
def drawCloud(x, y):
    ellipse(x, y, 50, 50)
    ellipse(x+30, y, 50, 50)
    ellipse(x+10, y-20, 50, 50)
