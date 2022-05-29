import cv2, os
from datetime import datetime
picturePath = "./login_pictures/" 
if os.path.exists(picturePath) == False:
    os.mkdir(picturePath)

cam_port = 0
cam = cv2.VideoCapture(cam_port)

result, image = cam.read()

if result:
    ''' imgName is hh-mm-ss--DD-MMM-YYYY '''
    cv2.imwrite(picturePath + datetime.now().strftime("%H-%M-%S--%d-%b-%Y") + ".jpg", image)
else:
    print("No camera detected")
    with open(picturePath + datetime.now().strftime("%H-%M-%S--%d-%b-%Y") + ".txt", "w") as f:
        f.write("No camera detected")