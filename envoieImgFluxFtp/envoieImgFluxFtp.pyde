from ftplib import FTP
add_library('minim')
add_library('video')

nom = 0

def setup():
    size(640, 480)
    global cam
    cams = Capture.list()
    cam = Capture(this, cams[0])
    cam.start()
    
def draw():
    global nom
    nom = str(day()) + str(month()) + str(hour()) + str(minute()) + str(second()) + ".jpg"
    
    if cam.available():
        cam.read() 
    image(cam, 0, 0)
    
    if minute() % 5 == 0 and second() < 2 or mousePressed:
        println("DESSIN…")
        saveFrame(nom)
        delay(1000)
        execfile('envoi.py')
        
def mouseReleased():
    saveFrame(nom)
    delay(1000)
    execfile('envoi.py')