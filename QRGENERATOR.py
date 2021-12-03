#QRGENERATOR
#Filip Rokita
#www.filiprokita.com

import qrcode
import PIL

qrInput = input("INPUT: ")

qrImage = qrcode.make(qrInput)
qrImage.save("qrcode.png")