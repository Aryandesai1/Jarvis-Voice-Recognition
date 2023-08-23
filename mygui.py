import pygame
import playsound
import time
class imageHandler:
  def __init__ ( self ):
    self.pics = dict()

  def loadFromFile ( self, filename, id=None ):
    if id == None: id = filename
    self.pics [ id ] = pygame.image.load ( filename ).convert()

  def loadFromSurface ( self, surface, id ):
    self.pics [ id ] = surface.convert_alpha()

  def render ( self, surface, id, position = None, clear = False, size = None ):
    if clear == True:
      surface.fill ( (5,2,23) ) #

    if position == None:
      picX = int ( surface.get_width() / 2 - self.pics [ id ].get_width() / 2 )
    else:
      picX = position [0]
      picY = position [1]

    if size == None:
      surface.blit ( self.pics [ id ], ( picX, picY ) ) #

    else:
      surface.blit ( pygame.transform.smoothscale ( self.pics [ id ], size ), ( picX, picY ) )
      
#Initialises the display-------------------------------------------------------
pygame.display.init() # Initiates the display pygame
screen = pygame.display.set_mode((600,400), pygame.RESIZABLE) #uncomment this line for smaller window
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) #allows fullscreen #comment this line out for smaller window
handler = imageHandler()
speech_button_rect = pygame.Rect(200, 350, 200, 40)

def draw_button():
    pygame.draw.rect(screen, (0, 128, 255), speech_button_rect)
    
    font = pygame.font.SysFont(None, 20)
    speech_text = font.render('Start Speech Recognition', True, (255, 255, 255))
    
    screen.blit(speech_text, (speech_button_rect.x + 10, speech_button_rect.y + 5))

def display():
    handler.loadFromFile ( "images/1.jpg", "1" ) #add your own file location here
    handler.loadFromFile ( "images/2.jpg", "2" ) #add your own file location here
    handler.loadFromFile ( "images/3.jpg", "3" ) #add your own file location here
    handler.loadFromFile ( "images/4.jpg", "4" ) #add your own file location here
    handler.loadFromFile ( "images/5.jpg", "5" ) #add your own file location here
    handler.loadFromFile ( "images/6.jpg", "6" ) #add your own file location here
    handler.loadFromFile ( "images/7.jpg", "7" ) #add your own file location here
    handler.loadFromFile ( "images/8.jpg", "8" ) #add your own file location here
    handler.loadFromFile ( "images/9.jpg", "9" )
    handler.loadFromFile ( "images/10.jpg", "10" ) #add your own file location here
    handler.loadFromFile ( "images/11.jpg", "11" )
    handler.loadFromFile ( "images/12.jpg", "12" )
    handler.loadFromFile ( "images/13.jpg", "13" )
    handler.loadFromFile ( "images/14.jpg", "14" )
    handler.loadFromFile ( "images/15.jpg", "15" )
    handler.loadFromFile ( "images/16.jpg", "16" )
    handler.loadFromFile ( "images/17.jpg", "17" )
    handler.loadFromFile ( "images/18.jpg", "18" )
    handler.loadFromFile ( "images/19.jpg", "19" )
    handler.loadFromFile ( "images/20.jpg", "20" )
    handler.loadFromFile ( "images/21.jpg", "21" )
    handler.loadFromFile ( "images/22.jpg", "22" )
    
display()

def face():
    A = 10
    B = 10
    x = 600
    y = 600
    
    handler.render ( screen, "1", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y) 
    # or replace with this line for easier coding 
    #pygame.display.update(A,B,x,y) 
    time.sleep(.1)
    handler.render ( screen, "2", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "3", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "4", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "5", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "6", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "7", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "8", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "9", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "10", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "11", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "12", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "13", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "14", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "15", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "16", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "17", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "18", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "19", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "20", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "21", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    handler.render ( screen, "22", ( A, B ), True, ( x, y ) )
    pygame.display.update(A,B,x,y)
    time.sleep(.1)
    
face()