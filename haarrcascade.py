#xette application permet de détecter le visage et la vigilance d'un conducteur via IA et IOT
#par la méthode haarcascade
from imutils.video import videoStream
from imutils.video import FPS
from imutils import face_utils
import face_recognition
import argparse
import imutils
import pickle
import time
import CV2
import dlib
import numpy as np
from firebase import firebase
firebase=firebase.FirebaseApplication('https://mqtt-raspberry.firebase.com/')
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 16
nb= 0

parse=argparse.ArgumentParser()
parser.add_argument("-c","--cascade,required=True,
                    help"path to where the face cascade)
parser.add_argument("-e","--encodings,required=True,
                    help"path to sterialized dbof facial encodings")
ap.add_argument("-p", "--shape-predictor", required=True,help="path to facial landmark predictor")                   
                    
                    
args=vars(parser.parse_args())                 
# load OpenCV's Haar cascade for face detection    
# facial landmark predictor         
detector.cv2.classifier(args["cascade"])
predictor = dlib.shape_predictor(args["shape_predictor"])
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
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
   # loop over the face detections
	 for (x, y, w, h) in rects:
		# construct a dlib rectangle object from the Haar cascade
		# bounding box
		 rect = dlib.rectangle(int(x), int(y), int(x + w),
			int(y + h))
                    
		# determine the facial landmarks for the face region, then
		# convert the facial landmark (x, y)-coordinates to a NumPy
		# array
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)  
                # extract the left and right eye coordinates, then use the
		# coordinates to compute the eye aspect ratio for both eyes
		leftEye = shape[lStart:lEnd]
		rightEye = shape[rStart:rEnd]
		leftEAR = eye_aspect_ratio(leftEye)
		rightEAR = eye_aspect_ratio(rightEye)
		# average the eye aspect ratio together for both eyes
		ear = (leftEAR + rightEAR) / 2.0   
		# visualize each of the eyes
		leftEyeHull = cv2.convexHull(leftEye)
		rightEyeHull = cv2.convexHull(rightEye)
		cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
		cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1) 
		if ear < EYE_AR_THRESH:
			nb:nb+1
		    if nb >= EYE_AR_CONSEC_FRAMES:
		      cv2.putText(frame, "DROWSINESS ALERT!", (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
		      firebase.put('mqtt-raspberry','drawsiness:"drawsiness")
		     else:
			nb = 0
		        cv2.putText(frame, "EAR: ", (300, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
			firebase.put('mqtt-raspberry','drawsiness:"not drawsiness")	   
 
		      
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
            firebase.put('mqtt-raspberry','face detection',unknown)
      else:
         firebase.put('mqtt-raspberry','face detection',names)    
      #loop over the recognized face
    for ((top,right,bottom,left),name) in zip(boxes,names):
       #draw the predicted face name on the image
        cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0),2)
        y=top-15 if top-15>15 else top+15
        cv2.puttext(frame,name,(left,y),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,255,0),2) 
    display.imshow("frame",frame)
    if key==ord("q"):
        break
    #update the fps counter
    fps.update()
   fps.stop()
   cv2.destroyALLWindows()
   vs.stop()                
                    
                    
                    
                    
                    
                    
    
    
  
                    
                    
                    
       
                    
                    
