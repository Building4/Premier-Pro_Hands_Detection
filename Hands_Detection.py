import time
import cv2

import mediapipe as mp
import numpy as np 



mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)


with mp_hands.Hands(min_detection_confidence=0.6, min_tracking_confidence=0.5, max_num_hands=2) as hands: 
    
  while cap.isOpened():
    ret, frame = cap.read()
    
    
    #BRG 2 RGB
    image= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    #Set Flag
    image.flags.writeable = False
    
    #Set results
    results = hands.process(image)
    
    #Set Flag To True
    image.flags.writeable = True
    
    #RGB 2 BRG
    image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    #print results
    print(results)
    
    if results.multi_hand_landmarks:
      for num, hand in enumerate(results.multi_hand_landmarks):
          mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )
    
    
    cv2.imshow('Hand Tracking', image)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
      break
    
  
cap.release()
cv2.destroyAllWindows()