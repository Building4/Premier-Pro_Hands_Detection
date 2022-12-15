import pyautogui as pg
pos = 1
def rightLeftMovement(a=0):
  b=0
  while True:
   if(a>0 and b<a):
      pg.hotkey("right")
      b=b+1
   if(a<0 and b>a):
     pg.hotkey("left")
     b=b-1
def CordMovement(a=0):
  global pos
  
  if(a>0 and pos<a):
    pg.hotkey("right")
    pos += 1
  if(a<0 and pos>a):
    pg.hotkey("left")
    pos -= 1

  
    
  
