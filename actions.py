import pyautogui as pg
def rightLeftMovement(a=0):
  b=0
  while True:
   if(a>0 and b<a):
      pg.hotkey("right")
      b=b+1
   if(a<0 and b>a):
     pg.hotkey("left")
     b=b-1

  
    
  
