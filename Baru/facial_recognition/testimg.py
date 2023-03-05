import pyrebase

config = {
  "apiKey": "AIzaSyD3Ir3Jd-IFcYPrgypbOiKhBSccDaYAPRM",
  "authDomain": "special-myway.firebaseapp.com",
  "databaseURL": "https://special-myway-default-rtdb.firebaseio.com",
  "projectId": "special-myway",
  "storageBucket": "special-myway.appspot.com",
  "messagingSenderId": "754576402722",
  "appId": "1:754576402722:web:972b23c4b312bde0aadd7b"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_cloud = "images/img.png"
path_local = "test.png"

storage.child (path_cloud).put(path_local)