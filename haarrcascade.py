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
             
