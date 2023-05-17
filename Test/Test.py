import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db

# Replace with your actual service account credentials
service_account_credentials = {
  "type": "service_account",
  "project_id": "test-bd99e",
  "private_key_id": "dc19e8b3c4e3a60d060335357b222510c9721937",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDSNkfefaJKDTxA\nORq22tg1sJHCsnYH1h6LAzzi4KnbWvhkyH8qZt+rcXoQ5wuG2ml1T74NNOSpf7gB\nWvBRDGS6AlRYeOjlvRrxK3I9HFaDzvcFWzar9VzUBE5JJR2IANaVs/tEovysftjU\nBGkVaQ43bgDQpu96wCuwHAWG/KBoDbspC/ilxjNHquVCuekGnp1OvSteGbd9LyLO\n3lowgkFIwxddQNJ5vMUd5qYNL256+Lbpk+S6XlDpA0PouraNHIWf3cglQA0mTBbJ\nTx8Zc+E//dO+g0fRBAlUjX/AnV5H0vE/ol5xOSENudRaGKMdIRn17xLegH8cIeLj\n46HGZ2xdAgMBAAECggEADS44nud/PcfrK3a5KVZ7AJDP7uaMNo0TMLG1B1/BXr7r\nPLyClrjJFQGiPv2RsDSxMJkdqEvU+5jFw5X9ZAOULEKZocuBBOiw0AbinJjShuS7\nAeO4f5s8pRGZDAaO/bhZvBzDKEhU8gbpFxAou54w9UJJPEv/T5HNm3cCVLax4xw+\nM95kF6Z/M7TZsV6QV8ytavkPzrO+RlMSkuIp99cF6R/3Ptt07yJcq1B7E/uVHXJR\nuyEYLddn38qF5iGiXkhBY/LPnwXtIojE5N5EKd+wALnnsGsL//5W+eIirhGPo2SW\noiJTJXL4l8fIxCcT/O3zCcci9bQuzS90/ICWUQRsyQKBgQDr5x/SFBsVSc/aONSz\nNaXbXl+bFzqDnLxWVl6WOKnebWEANRGD7QdDhN6/yShwffN/mCbOeAT5rTRnpaI9\n/EXzkNH7vdnfLRFMqmc9T2swXtgIqM0QMpRyxwV1OjVR/+Ms2h8WMFNi1ZwHbpwF\nhMUqkKi9jPFrlWRUq8BY7mvn9QKBgQDkHtuw0oP8wh+r0TwGhlJAWUcCeBWjKzNW\npsWkedzbJWbFWsIwQFgCK7wC1PRn0OrKXHq6B8CCWPReKQ2BpqaHFN+/xIROfu2b\nL5ODJirGoITJxaDCsp1xEQFhB4FIEyfZiHMFPAPokQYjxJNUiL3ez1+sh+PNRwYv\nU1+N1S35yQKBgCO2BEIoGwV4/Acb7U8HwwjXW3+933THCFfFkWIKR+TNCA8g+XrQ\nKfZVqea8i+ujlXXuUYmV76LgTnuWPl5Fz00U0kTas52uU90YOrK0UBStduSwsQJP\ntds+N5xMaH/2TayfhG82d5kRnyIc42+Obs6HwZOYP3+6yMpsiZys0xb1AoGAd2M7\nAQi78P27y5Vev99ujqTqx/0G/fVvEeuIRrNMhhjF94WvWcdjCAfRhv3ix66MIspR\npKjH9LAPfHQp0G/ieZHQJDH6OIavXeeBYUMJYhjCRkM7BoqqYXFP8nMWEx2LXorN\n/7BQL1gvCWso3DYQgNqxLL+V1mpUb1JIERe/zxkCgYB3NtpLa06yKrpCItsQVree\nx1nY4dbbPn8NnzqTzzdwEbNp5c9vCMF23c/Xz7cwCZy3XRYITa7314yBC8lXfEmt\nTVEY3ymThs6Gie71+ulNcwW/zHrkQkX690v5pXp/fic2EQeg0pzHX4xGykpj0mhB\nqDfAuBUzYA7Aiq9CAFLBfA==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-zbzlm@test-bd99e.iam.gserviceaccount.com",
  "client_id": "103170913159097449706",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-zbzlm%40test-bd99e.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

# Initialize Firebase credentials
cred = credentials.Certificate(service_account_credentials)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-bd99e-default-rtdb.europe-west1.firebasedatabase.app/'
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
            subprocess.call(['Esp32simpleBin/Test/script1'])
        elif code == 2:
            print("Running ota with blink blue")
            subprocess.call(['Esp32simpleBin/Test/script2'])
        elif code == 3:
            print("Running ota with blink red blue")
            subprocess.call(['Esp32simpleBin/Test/script3'])
        else:
            print("Error")
    
# Set up the listener
refota.listen(callback)

# Keep the script running indefinitely
while True:
    pass