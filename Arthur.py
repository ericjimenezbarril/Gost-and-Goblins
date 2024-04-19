#### IN THIS CODE WE DEFINE THE CLASS "ARTHUR".
### IMPORTANT: FOR THE FUNCTION TO GO DOWN STAIRS, IF WE WANT TO ADD A NEW LEVEL WHERE IT BOTHERS, 
### PUT IT EXPLICITLY IN THE FUNCTION
 
 
import keyboard
import time
from tkinter import *
from PIL import Image, ImageTk
from Carril import *
import os


# To import photos from a directory
# Posicions: 0: mirant dreta de peu, 1: mirant esquerra de peu, 
#            2: mirant dreta saltant,3: mirant essquerra saltant
#            4: mirant dreta disparant, 5:mirant esquerra disparant
 
 
class Armadura:
    """
    Represents an armor in a game, typically worn by a character.

    This class manages the armor's visual representation and positioning on the game screen.

    Attributes:
        x (int): The x-coordinate where the armor is drawn on the canvas.
        y (int): The y-coordinate where the armor is drawn on the canvas.
        w (int, optional): The width of the armor image. Defaults to 50.
        h (int, optional): The height of the armor image. Defaults to 30.
    """

    def __init__(self, x, y, w=50, h=30):
        """
        Initializes a new armor instance with specified attributes and loads the armor image.

        The armor image is resized based on the provided width and height.

        Args:
            x (int): The x-coordinate where the armor will be drawn.
            y (int): The y-coordinate where the armor will be drawn.
            w (int, optional): The width of the armor image. Defaults to 50.
            h (int, optional): The height of the armor image. Defaults to 30.
        """
        self.x, self.y, self.w, self.h = x, y, w, h
        img_path = os.path.join("Arthur", "Armadura.png")
        self.img = Image.open(img_path)    
        self.img = self.img.resize((self.w, self.h))
        self.img = ImageTk.PhotoImage(self.img)
        
    def pintar(self, w):
        """
        Draws the armor on the specified canvas.

        Args:
            w (Canvas): The canvas on which to draw the armor.
        """
        w.create_image(self.x, self.y, anchor="nw", image=self.img)


class Arthur:
    """
    Represents the main character, Arthur, in a game, managing his movement, actions, and interactions.

    This class handles various actions such as walking, jumping, bending, climbing, and shooting. It also
    deals with Arthur's health and collision detection.

    Attributes:
        x (int): The x-coordinate of Arthur on the game screen.
        y (int): The y-coordinate of Arthur on the game screen.
        w (int): Width of Arthur's image.
        h (int): Height of Arthur's image.
        nivell_actual (int): Current level of the game Arthur is on.
        vides (int): Number of lives Arthur has left.
        arma_actual (int): The current weapon Arthur is using.
        pos (int): Current position in the sprite animation cycle.
        armas (list): List of weapons Arthur currently has deployed.
    """

    def __init__(self,x,y,w,h, nivell_actual,vides=0, arma_actual=0):
        """
        Initializes Arthur with specific location, size, level, and initial conditions of lives and weapon.

        Args:
            x (int): Initial x-coordinate of Arthur.
            y (int): Initial y-coordinate of Arthur.
            w (int): Width of Arthur.
            h (int): Height of Arthur.
            nivell_actual (int): Current level Arthur is in.
            vides (int, optional): Initial number of lives Arthur starts with. Defaults to 0.
            arma_actual (int, optional): Initial weapon Arthur starts with. Defaults to 0.
        """
        self.x,self.y,self.w,self.h, self.nivell_actual, self.vides, self.arma_actual=x,y,w,h, nivell_actual, vides, arma_actual
        self.pos = 0
        self.pas=0                        
        self.is_jumping = False          
        self.jump_h = 80                  

        if self.nivell_actual==1:
            self.jump_h=100

        if self.nivell_actual in [2,3]:
            self.jump_h=60

        self.salt = 0                    
        self.ajup=0                       
        self.tir = 0                      
        self.is_bending = False              
        self.is_up = False
        self.armas =[]
        self.is_shooting =False

        self.auxiliar_vides=True       
        self.contador_aux_vides = 30


    def arthur_img(self):
        """
        Selects and loads the appropriate image for Arthur based on his current state and actions.

        Returns:
            ImageTk.PhotoImage: The image object to be displayed for Arthur.
        """
         # Image selection logic based on Arthur's state
        arthurs=["Arthur_0.png", "Arthur_1.png","Arthur_2.png","Arthur_3.png", "Arthur_4.png","Arthur_5.png",
                 "Arthur_6.png","Arthur_7.png","Arthur_8.png", "Arthur_9.png","Arthur_10.png", "Arthur_11.png",
                 "Arthur_12.png","Arthur_13.png", "Arthur_14.png", "Arthur_15.png","Arthur_16.png", "Arthur_17.png",
                 "Arthur_18.png"]  
        arthurs_sin=["Arthur0.png", "Arthur1.png","Arthur2.png","Arthur3.png", "Arthur4.png","Arthur5.png",
                 "Arthur6.png","Arthur7.png","Arthur8.png", "Arthur9.png","Arthur10.png", "Arthur11.png",
                 "Arthur12.png","Arthur13.png", "Arthur14.png", "Arthur15.png","Arthur16.png", "Arthur17.png",
                 "Arthur18.png"]  
        armadura = ["armadura0.png", "armadura1.png", "mort0.png","mort1.png","mort2.png","mort3.png","mort4.png"]
        img = None
        
        if self.auxiliar_vides==True:
            if self.vides<=0:
                img = os.path.join("Arthur", arthurs_sin[self.pos])
            else:
                img = os.path.join("Arthur", arthurs[self.pos])
        elif self.vides >=0:
            if self.contador_aux_vides < 15:
                img =os.path.join("Arthur", armadura[1])
            else: 
                img=os.path.join("Arthur", armadura[0])
        else:
            i = 2
            if 25>= self.contador_aux_vides > 20:
                i = 3
            elif self.contador_aux_vides > 15:
                i=4
            elif self.contador_aux_vides > 10:
                i=5
            else:
                i=6
            img=os.path.join("Arthur", armadura[i])   

        self.img = Image.open(img) 
        self.img = self.img.resize((self.w, self.h))
        self.arthur = ImageTk.PhotoImage(self.img)
        
        return self.arthur


    def pintar(self,w):
        """
        Draws Arthur and any weapons he has on the game canvas.

        Args:
            w (Canvas): The canvas on which Arthur and his weapons will be drawn.
        """
        self.arthur_imag = w.create_image(self.x, self.y, anchor="nw", image=self.arthur_img())
        
        if(self.pos%2==0 and self.pos < 12):
            self.pos=0
        elif(self.pos%2==1 and self.pos < 12):
            self.pos=1
        for arma in self.armas:
            arma.pintar(w)


    def moure(self, carrils):
        """
        Handles movement and interaction with game environment such as jumping, bending, climbing,
        and shooting based on user input and game mechanics.

        Args:
            carrils (list): List of lanes in the game which may contain obstacles and paths for Arthur.
        """
        for arma in self.armas:
            if arma.y+arma.h <= self.y + self.h:
                arma.moure()
            else:
                self.armas.remove(arma)

        if self.is_up==False and self.is_jumping==False and self.is_bending==False:
            self.carril_actual = None
            for carril in carrils:
                if self.x  + self.h > carril.x and self.x < carril.x + carril.w and self.y + self.h == carril.y:
                    self.carril_actual= carril   
                    break         

            self.carril_sota= None
            if self.carril_actual!=None and self.nivell_actual!=1:       
                    for E in carril.escales:
                        if carril.y - E.h == self.carril_actual.y:
                            self.carril_sota= carril
                            break 
            if self.nivell_actual==1:
                for carril in carrils:
                    if self.x + self.w > carril.x and self.x < carril.x + carril.w and carril.y - carril.a <self.y + self.h < carril.y:
                        self.carril_sota = carril
                        break
            
        if self.carril_sota !=None:                   
                    for E in self.carril_sota.escales:
                        if (self.is_up==True or self.y + self.h == self.carril_actual.y):
                            if (self.x >= E.x and self.x+ self.w <= E.x + E.w):
                                if self.y + self.h > self.carril_actual.y - E.h and keyboard.is_pressed("down arrow"):  
                                    self.pujar(-1, self.carril_sota.y)  
                                elif self.y + self.h > self.carril_sota.y - E.h and keyboard.is_pressed("up arrow"):   
                                    self.pujar(1, self.carril_actual.y) 
                                          
        self.colisio_mur_left = False
        self.colisio_mur_right = False
        if self.nivell_actual==4:
            for carril in carrils:
                if carril.x==0:
                    for mur in carril.murs:
                        if mur.x-5<=self.x + self.w <= mur.x + mur.w and carril.y - mur.h <= self.y + self.h <= carril.y:
                            self.colisio_mur_left=True
                            if self.x > mur.x - self.w:               
                                self.x = mur.x - self.w
                                break
                        if mur.x<= self.x <= mur.x + mur.w +5 and carril.y - mur.h <= self.y + self.h <= carril.y:
                            self.colisio_mur_right=True          
                            if self.x < mur.x + mur.h:              
                                self.x = mur.x + mur.h
                                break
                    break

        if self.carril_actual !=None:
            for E in self.carril_actual.escales:
                if (self.is_up==True or self.y + self.h == self.carril_actual.y):
                    if (E.x<=self.x<= E.x + E.w/2) or (E.x+E.w/2 <=self.x+ self.w <= E.x + E.w):
                        if(self.y + self.h > self.carril_actual.y - E.h and keyboard.is_pressed("up arrow")):   
                            self.x=E.x + 5             
                            self.pujar(1, self.carril_actual.y - E.h)     
                        if self.y + self.h < self.carril_actual.y and keyboard.is_pressed("down arrow"):  
                            self.x=E.x +5
                            self.pujar(-1, self.carril_actual.y)
     
            if not(self.is_up):   
                    for mur in self.carril_actual.murs:
                        if mur.x-5<=self.x + self.w <= mur.x+5 and self.carril_actual.y - mur.h <= self.y + self.h <= self.carril_actual.y:
                            self.colisio_mur_left=True
                        if mur.x+mur.w -5<= self.x <= mur.x + mur.w +5 and self.carril_actual.y - mur.h <= self.y + self.h <= self.carril_actual.y:
                            self.colisio_mur_right=True  
                   
                    if keyboard.is_pressed("space"):
                            self.is_shooting= True                   
                    
                    elif not (self.is_jumping or self.is_bending): 
                        if keyboard.is_pressed("w") and self.colisio_mur_left==False and self.colisio_mur_right==False :
                            self.is_jumping = True
                        elif keyboard.is_pressed("s"):
                            self.is_bending= True
                        else:

                            if (self.x+10 <= 1000-self.w and self.colisio_mur_left==False and keyboard.is_pressed("right arrow")):
                                self.x+=10
                                self.pos=2+self.pas
                                self.pas = 2-self.pas 
                            if (0<= self.x-10 and self.colisio_mur_right==False and keyboard.is_pressed("left arrow")):
                                self.x-=10
                                self.pos=3+self.pas
                                self.pas=2-self.pas                      
            
        else:                 
            if self.nivell_actual in [0,3,4]:
                if self.y +self.h < 500:
                    self.y +=20
                    if 0<= self.x + 5*(1-2*(self.pos%2)) <= 1000-self.w and self.colisio_mur_left==False and self.colisio_mur_right==False:
                        self.x += 5*(1-2*(self.pos%2))
                else:
                    self.y = 500
            elif self.nivell_actual==1: 
                if self.carril_sota!=None and self.carril_sota.y -20<= self.y + self.h<= self.carril_sota.y + self.carril_sota.h:
                    self.y = self.carril_sota.y - self.h
                    self.carril_actual=self.carril_sota
                else:
                    self.y +=20

        if self.is_jumping:
            if self.colisio_mur_right==True or self.colisio_mur_left==True:
                self.y = self.carril_actual.y - self.h
                self.salt=20
            if self.y + self.h> 0:   
                self.saltar() 
            
            for carril in carrils:
                if carril!=self.carril_actual and self.x > carril.x -self.w//2 and self.x + self.w//2 < carril.x + carril.w and carril.y - carril.a <self.y + self.h < carril.y:
                    self.carril_actual= carril 
                    self.y = carril.y - self.h
                    self.salt = 16   
                    self.saltar()
                    break
        elif self.is_bending:
            if self.ajup > 1 and (keyboard.is_pressed("right arrow") or keyboard.is_pressed("left arrow") or keyboard.is_pressed("w")):
                self.ajup=20            
            self.ajupirse()     
        
        if self.is_shooting:
            self.disparar()    
                
    
    def saltar(self):
        """
        Manages the jumping mechanics for Arthur, updating his position based on jump height and direction.
        """
        self.pos = 6 + (self.pos%2)
        # Jumping logic
        if(self.salt==0):
            self.salt+=1
            self.y -=self.jump_h/2
            dist_salt = (1-2*(self.pos%2))*self.jump_h/3
            if 0 <= self.x + dist_salt <=1000 - self.w:
                self.x +=dist_salt                             ## si estas hacia la derecha saltas positivo y si no negativo  
        elif (self.salt<2):                                  
            self.y -= self.jump_h/2 
            dist_salt = (1-2*(self.pos%2))*self.jump_h/3
            if 0 <= self.x + dist_salt <=1000 - self.w:
                self.x +=dist_salt  
            self.salt+=1
        elif (self.salt < 10):
            dist_salt = (1-2*(self.pos%2))*self.jump_h/24
            if 0 <= self.x + dist_salt <=1000 - self.w:
                self.x +=dist_salt  
            self.salt+=1
        elif (self.salt < 15):
            self.y +=self.jump_h/5 
            dist_salt = (1-2*(self.pos%2))*self.jump_h/10
            if 0 <= self.x + dist_salt <=1000 - self.w:
                self.x +=dist_salt 
            self.salt+=1
        else:
            if (self.pos%2==0):
                self.pos=0
            else:
                self.pos=1
            self.is_jumping = False
            self.salt = 0


    def ajupirse(self):
        """
        Manages the bending mechanics for Arthur, modifying his height and position temporarily.
        """
        # Bending logic
        self.pos = 10 + (self.pos%2)
        if (self.ajup==0):
            self.h = int(self.h/2)
            self.y +=self.h              
            self.ajup+=1
        elif(self.ajup<20):
            self.ajup+=1
        else:
            self.pos = self.pos%2
            self.y -= self.h            
            self.h = 2*self.h
            self.is_bending = False
            self.ajup = 0


    def pujar(self, decisio, altura): 
        """
        Handles the climbing mechanics for Arthur, either up or down based on the given direction.

        Args:
            decisio (int): Direction of the climb (1 for up, -1 for down).
            altura (int): The height Arthur should climb to.
        """
        self.is_up=True
        self.y -= decisio*10      
        self.pos=12+(self.pas%2)        
        self.pas=1-self.pas        
        if self.y + self.h == altura:
            self.is_up = False                                       

    def disparar(self):
        """
        Handles the shooting mechanics for Arthur, creating a weapon instance and managing its deployment.
        """
        if(self.tir<1):
            if not (self.is_bending):
                self.pos= 14+(self.pos%2)             
            self.tir+=1
        elif(self.tir<2):
            if not (self.is_bending):
                self.pos= 16+(self.pos%2)            
            self.tir+=1
        else:
            from Arma import Arma
            self.armas.append(Arma("Arthur",self.arma_actual, self.x + self.w, self.y + self.h/5,(1-2*(self.pos%2))))
            self.pos = self.pos%2
            self.is_shooting=False
            self.tir=0
    
        
    