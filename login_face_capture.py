import cv2, os
from datetime import datetime

def uploadFile(fName, driveFolderLink):
    folderID = driveFolderLink.split('/')[-1]
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive

    gauth = GoogleAuth()           
    drive = GoogleDrive(gauth)  

    gfile = drive.CreateFile({'parents': [{'id': folderID}]})
    
    gfile.SetContentFile(fName)
    gfile.Upload() 
    return gfile.GetLink()



def main():
    picturePath = "./login_pictures/" 
    if os.path.exists(picturePath) == False:
        os.mkdir(picturePath)

    cam_port = 0
    cam = cv2.VideoCapture(cam_port)

    result, image = cam.read()

    if result:
        ''' imgName is hh-mm-ss--DD-MMM-YYYY '''
        fName = picturePath + datetime.now().strftime("%H-%M-%S--%d-%b-%Y") + ".jpg"
        cv2.imwrite(fName, image)
        # link = uploadFile(fName, "https://drive.google.com/drive/u/1/folders/1TD-mqni916vEPCVGCRmvs3gwq9ycmjz0")
        try:
            link = uploadFile(fName, "https://drive.google.com/drive/u/1/folders/1TD-mqni916vEPCVGCRmvs3gwq9ycmjz0")
            print("Link: " + link)
        except:
            print("Error uploading file")
        
    else:
        print("No camera detected")
        with open(picturePath + datetime.now().strftime("%H-%M-%S--%d-%b-%Y") + ".txt", "w") as f:
            f.write("No camera detected")

if __name__ == "__main__":
    main()