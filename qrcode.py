import pyqrcode
import png
import cv2
#data
data = 'qr3'
#create qrcode
url = pyqrcode.create(data)
url.png('qr3.png', scale=6)
#read qrcode
img = cv2.imread('qr3.png')
det = cv2.QRCodeDetector()
val, pts, st_code = det.detectAndDecode(img)
print(val)