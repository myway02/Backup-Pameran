import cv2
import pyrebase

##Firebase setup
config = {
    "apiKey": "AIzaSyC41ntynimqPmk4_3oWSfmXpJ0C3wgGr7I",
    "authDomain": "myway2023-790a8.firebaseapp.com",
    "databaseURL": "https://myway2023-790a8-default-rtdb.firebaseio.com",
    "projectId": "myway2023-790a8",
    "storageBucket": "myway2023-790a8.appspot.com",
    "messagingSenderId": "68073473672",
    "appId": "1:68073473672:web:d0c86be90a802d2265013d",
    "measurementId": "G-31T6CG2PDK"
};

#initializing database
firebase = pyrebase.initialize_app(config)

name = 'Nabilla' #replace with your name

cam = cv2.VideoCapture(0)

cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 500, 300)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    
    cv2.imshow("press space to take a photo", frame)

    k = cv2.waitKey(1)
    
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
     
    elif k%256 == 32:
        # SPACE pressed
        img_name = "dataset/"+ name +"/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        
        #Firebase storage setup
        storage = firebase.storage()
        database = firebase.database()
        
        path_cloud = (f"{img_name}")
        path_local = (f"{img_name}")
    
        storage.child(path_cloud).put(path_local)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

cam.release()
cv2.destroyAllWindows()