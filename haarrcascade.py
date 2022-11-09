from imutils.video import videoStream
from imutils.video import FPS
import face_recognition
import argparse
import imutils
import pickle
import time
import CV2
from firebase import firebase
firebase=firebase.FirebaseApplication('https://mqtt-raspberry.firebase.com/')

parse=argparse.ArgumentParser()
parser.add_argument("-c","--cascade,required=True,
                    help"path to where the face cascade)
parser.add_argument("-e","--encodings,required=True,
                    help"path to sterialized dbof facial encodings")
                    args=vars(parser.parse_args())
             
detector.cv2.classifier(args["cascade"])
data=pickle.load(open(args["encodings"],"rb").read())
#intitialize the video stream
print("strting the video stream")
vs=videoStream(src=0).start()
time.sleep(2.0)
#Start the Fbs counter(:le nombre  d'image afiché par seconde)
fps=FPS().start()
#loop over frames from the video file stream
while True:
#resize the frame from video
                    
   frame=vs.read()
    #to 500 px
   frame=imutils.resize(frame,width=500)
   #convert the input frame BGR from grayscale for face detection
   # from BGR to RGB (for face recognition)
   gray=cv2.cvtcolor(frame,cv2.COLOR_ BGR2GRAY)    
   gray=cv2.cvtcolor(frame,cv2.COLOR_ BGR2RGB)     
   #detect faces in the gray scale frame
   rects=detector.detectMultiscale(gray,scaleFactor=1.1,minsize=(30,30))
   boxes=[(y,x+w,y+w,x)for(x,y,w;h)in rects]
   #compute the facial recognition for each facebounding box
   encodings=face_recognition.face_encodings(rgb,boxes)
   names=[]
   #loop over the facial
   for encoding in encodings:
     trueface=face_recognition.compare(data["encodings"],encoding)
     name="Unknown"  
     #check if we have a match
      if true in truefaces:
      #find the indexes of all matches
      matched=[i for (i,b)in enumerate (matches) if b]
      counts={}
      for i in matched:
          name=data["names"][i]
          counts[name]=counts.get(name,0)+1
           #determine the recognized face with a largest number of votes
           name=max(counts,key=counts.get)
      names.append(name)
      if name=="unknown":
            firebase.put('mqtt-raspberry','light',unknown)
      else:
         firebase.put('mqtt-raspberry','light',names)    
      #loop over the recognized face
   for                  
                    
                    
                    
                    
    
    
  
                    
                    
                    
       
                    
                    
