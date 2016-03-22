from ftplib import FTP
add_library('minim')

def setup():
    size(300, 300)
    global minim, input, recorder
    global nom
    
    minim = Minim(this)
    input = minim.getLineIn()
    nom = str(day()) + str(month()) + str(hour()) + str(minute()) + ".wav"
    recorder = minim.createRecorder(input, nom)
    
def draw():
    background(0)
    if recorder.isRecording():
        fill(0, 255, 0)
        println("enregistrement…")
    else:
        fill(255)
        
    ellipse(width/2, height/2, 30, 30)
    envoi()
    delay(500)

def envoi():
    nom = str(day()) + str(month()) + str(hour()) + str(minute()) + str(second()) + ".png"
        
def keyReleased():
    if key == 'r':
        if recorder.isRecording():
            recorder.endRecord()
        else:
            recorder.beginRecord()
    if key == 's':
        recorder.endRecord()
        recorder.save()
        println("sauve")
        execfile('envoi.py')
        println("envoyeee")