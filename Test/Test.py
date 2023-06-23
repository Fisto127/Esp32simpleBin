import firebase_admin
import subprocess
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db


# Replace with your actual service account credentials
service_account_credentials = {
  "type": "service_account",
  "project_id": "mrhandy-8d8aa",
  "private_key_id": "9783ce97425540e7dab71b9b40cb40f6719d0623",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCtMh/waxWuZBlL\noKJ6KjCy2Uvs5gFaFrHsFc4DoSz3Xv3ZOnz6EO39Z1vn6PJWzhTi/vxj1pFhaPIa\nfRvdjHjimll9OpeC/QAMPmHu0GYeGaGu7e6jMNLPNDfe+maXwcH0ZPHKl7/hx1d+\nn5hObcVii3EPCgNluoYD7OuXvVac9jIfwsEruo+YKtXquNRzehKymP5LeOfqCz11\nAKYXMg+cwfJw5EgTRKnyW1jNnZTfHvuf/uYXx76onSip7m4a3h6XqZvbJ3pgJmRG\n7UDdbH1yqaMYaOuuwzkm5176cavwnHBZlKPnAKmQOJd+HWOBLSEETQ7+OhkXL/XW\nCnobXfapAgMBAAECggEAIHQykPH3+5gtN0Mv/vVV78WRGSCWY0O6blM9qedzTh1C\nMwjnL1KpzeCm06OOeZ6fQlPmhmzIDDlGmJkV9iNi6Y9jsngeuQBgmGq+Hip14DEM\nX4OdQn4dGo+d4o4IWGqJxhp+Rmi+H3gjmIoeV5/xK0CW3GsTbOYRQ74K/YGQr9OR\nXnqojKPW8PT26AVrSRTqEGsD1cTkdE67HzdltKt9qNJysvuYwNjs7gcVTwAvowGN\nprJfEHsooPtTQuzZn7D/rQ+eVlKzl0v9O/xepWLjEc5yiPfL2TBJzQ2zXrYFBGje\naFVGkNhtENFgyASgjRDrevYofT9A0aaWxFngWKtC4wKBgQDcARAk9Z4AUHre8mWc\nhy0LkoZ1ANqxHjOI+SduWZhcfIvUhmbbW39+ttT1fVb/MGxSmG6U15awbmU7bK+4\npaMG2lviJQXDtrviwRDWsziBsjf5uOuHcgNOSycwYicNs2SHKVRsE5ZB9HdKshGC\nHs8qnCFrCz8O6e2F2biddgVcCwKBgQDJiHr+CSN1QgpAeThKFHeSVAznD8EjD7FR\nh1WTlkKBFA5PlUkzTG4cJsBn6zbSfIHN4/1OOIFU2dZyC1OlzTrbE4GfsmDrqbTK\nTAgoS+ERstdyH07t9QP64cPHkKoD7XwPen2B8QRoJTRo66lO8nShs5FZb9fsVnFd\nFwVE9Wc0mwKBgQDDPW5GXnLJdKKWGCd0scGX84C/dPKfHF4/wFzt4TUFXsH46Q1+\nvcR3f2meMo1yClcXNY9tJ6XjDRVplxqakuQKwN2p45EqDpDOuudmocYT00U5qJHc\nsaGdabRti618yyb7jAIPp5JBFeKHt18ySoUvGz/M7z4WziKsFntvwb0f4QKBgCMf\ntD/eG93t2peOCO9wTb6lA3Kp3kFcFM1ext1oDMMuWagpHo7gPTiO0G3MIsvgg0b8\n+0LMuk2tgaBytOtqr11LMwZAMoAgHbA8PBe50coh30a2ii0SzNTG0DZR0i/JDhws\nfv9MoDX+dfnrSKDHxOgBwc1SntFD55IP1w1Dr+8NAoGAX0HHMw+g5f6vOvfoWccs\n2HS9nwQbKBCqHW1KJaFgc/0gF/wf9rBJN6w4COgXxN6ekz98rcYpfwoA6xHZ4cVi\nPn7EU5HKuQ67G6YnaYcDug5YfxfDT6CsB59U98duVimPD7wqJ5ACjtLyKG7eZmWx\nkitEq3zLxqc7wTjMKum9nTU=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-w0wnt@mrhandy-8d8aa.iam.gserviceaccount.com",
  "client_id": "110214433717431043021",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-w0wnt%40mrhandy-8d8aa.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

# Initialize Firebase credentials
cred = credentials.Certificate(service_account_credentials)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mrhandy-8d8aa-default-rtdb.europe-west1.firebasedatabase.app/'
})

# Get a reference to the 'OTA' node
refota = db.reference('OTA')

# Read the values of 'test1' and 'test2'
upload = refota.child('UPL').get()
code = refota.child('CDE').get()

# Check if 'test1' is true and run script based on 'test2' value


def callback(event):
    if upload :
        if code == 1:
            print("Running ota with Blink red")
            subprocess.call(['Esp32simpleBin/Test/script1.sh'])
            db.reference('OTA').update ({
                'Current': 1,
                'UPD': False
            })
        elif code == 2:
            print("Running ota with blink blue")
            subprocess.call(['Esp32simpleBin/Test/script2.sh'])
            db.reference('OTA').update ({
                'Current': 2,
                'UPD': False
            })
        elif code == 3:
            print("Running ota with blink red blue")
            subprocess.call(['Esp32simpleBin/Test/script3.sh'])
            db.reference('OTA').update ({
                'Current': 3,
                'UPD': False
            })
        else:
            print("Error")
            db.reference('OTA').update ({
                'UPD': False
            })
    
# Set up the listener
refota.listen(callback)

# Keep the script running indefinitely
while True:
    pass