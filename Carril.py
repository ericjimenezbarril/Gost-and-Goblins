#Zombies always have their feet on the lane they're on (z.y+z.h = self.y)
from PIL import Image, ImageTk
import os     
   



class Escala:
    """
    Represents a ladder in a game, allowing characters to climb between different levels or heights.

    This class manages the visual representation of ladders and their placement within the game environment.

    Attributes:
        x (int): The x-coordinate of the ladder on the game canvas.
        w (int, optional): The width of the ladder image. Defaults to 50.
        h (int, optional): The height of the ladder image. Defaults to 200.
        nivell (int, optional): The level of detail for the ladder's image based on the game level. Defaults to 0.
    """
        
    def __init__(self, x, w=50, h=200, nivell=0):
        """
        Initializes a new ladder instance with specified attributes and loads the appropriate ladder image.

        The ladder's image is selected based on the game level and adjusted based on its specified height.

        Args:
            x (int): The x-coordinate where the ladder will be drawn.
            w (int, optional): The width of the ladder image. Defaults to 50.
            h (int, optional): The height of the ladder image. Defaults to 200.
            nivell (int, optional): The level of the game which determines the ladder image. Defaults to 0.
        """
        self.x,self.w,self.h, self.nivell = x,w,h,nivell
        escales = ["Escala0.png","Escala2.png", "Escala3.png","Escala4.png","Escala5.png"]
        
        if self.nivell==0:
            self.img = os.path.join("Escales", escales[self.nivell])
        elif self.nivell!=1:
            if self.h < 250:
                self.img = os.path.join("Escales", escales[self.nivell-1])
            else:
                self.img = os.path.join("Escales", escales[self.nivell])

            
        self.img = Image.open(self.img)
        self.img = self.img.resize((self.w, self.h))
        self.escala = ImageTk.PhotoImage(self.img)
    
    
    def pintar(self,w,y_c): 
        """
        Draws the ladder on the specified canvas at the specified height.

        Args:
            w (Canvas): The canvas on which to draw the ladder.
            y_c (int): The y-coordinate of the lane where the ladder should be drawn, adjusted by the ladder's height.
        """
        w.create_image(self.x, y_c - self.h, anchor="nw", image=self.escala)


class Mur():
    """
    Represents a wall in a game that may act as an obstacle for characters.

    This class manages the visual representation of walls and their positioning within the game environment.

    Attributes:
        x (int): The x-coordinate of the wall on the game canvas.
        w (int, optional): The width of the wall image. Defaults to 65.
        h (int, optional): The height of the wall image. Defaults to 110.
        nivell (int, optional): The game level which may affect the wall's appearance. Defaults to 2.
    """

    def __init__(self, x, w=65, h= 110, nivell=2):
        """
        Initializes a new wall instance with specified attributes and loads the appropriate wall image.

        The wall's image is selected based on the game level and adjusted based on its specified dimensions.

        Args:
            x (int): The x-coordinate where the wall will be drawn.
            w (int, optional): The width of the wall image. Defaults to 65.
            h (int, optional): The height of the wall image. Defaults to 110.
            nivell (int, optional): The level of the game which determines the wall image. Defaults to 2.
        """
        self.x, self.w, self.h, self.nivell= x,w,h,nivell
        self.img = None
        
        if nivell==4:
            self.img = os.path.join("Murs", "Mur2.png")
        else:
            self.img = os.path.join("Murs", "Mur.png")
        self.img = Image.open(self.img)
        self.img = self.img.resize((self.w, self.h))
        self.mur = ImageTk.PhotoImage(self.img)
    
    
    def pintar(self,w,y_c): #y_c es la altura del carril  
        """
        Draws the wall on the specified canvas at the specified height.

        Args:
            w (Canvas): The canvas on which to draw the wall.
            y_c (int): The y-coordinate of the lane where the wall should be drawn, adjusted by the wall's height.
        """    
        w.create_image(self.x, y_c - self.h, anchor="nw", image=self.mur)


class Carril:
    """
    Represents a lane in the game environment that may contain various obstacles, enemies, and items.

    This class manages entities like zombies, goblins, birds, jumpers, shield bearers, ladders, walls, weapons, and armors
    within a single lane, and handles their interactions and movements.

    Attributes:
        x (int): The x-coordinate of the lane.
        y (int): The y-coordinate of the lane, representing its vertical starting point.
        w (int): The width of the lane.
        h (int): The height of the lane.
        a (int): The vertical extension upwards from the base height, varies by level.
        nivell (int): The current game level affecting the lane's characteristics.
        zombis (list): A list of zombie objects within the lane.
        goblins (list): A list of goblin objects within the lane.
        ocells (list): A list of bird objects within the lane.
        saltarins (list): A list of jumper objects within the lane.
        escuders (list): A list of shield bearer objects within the lane.
        escales (list): A list of ladder objects within the lane.
        murs (list): A list of wall objects within the lane.
        armes (list): A list of weapon objects within the lane.
        armadures (list): A list of armor objects within the lane.
    """
    def __init__(self,x,y,w,h,a,nivell,zombis=[], goblins=[] ,ocells=[], saltarins=[],escuders=[],escales=[],murs=[],armes=[], armadures=[]):
        """
        Initializes a new lane with specified attributes and optional entities.

        Args:
            x (int): The x-coordinate of the lane.
            y (int): The y-coordinate of the lane.
            w (int): The width of the lane.
            h (int): The height of the lane.
            a (int): The vertical extension upwards from the base height.
            nivell (int): The current level which may affect the entities and their behavior in the lane.
            zombis (list, optional): List of zombies in the lane.
            goblins (list, optional): List of goblins in the lane.
            ocells (list, optional): List of birds in the lane.
            saltarins (list, optional): List of jumpers in the lane.
            escuders (list, optional): List of shield bearers in the lane.
            escales (list, optional): List of ladders in the lane.
            murs (list, optional): List of walls in the lane.
            armes (list, optional): List of weapons in the lane.
            armadures (list, optional): List of armors in the lane.
        """
        self.x,self.y,self.w,self.h,self.a,self.nivell,self.zombis,self.goblins, self.ocells = x, y, w, h,a,nivell,zombis, goblins, ocells 
        self.saltarins, self.escuders,self.escales, self.murs,self.armes,self.armadures= saltarins, escuders, escales, murs, armes, armadures
        
        carrils1=["Carril1.png", "Carril2.png", "Carril3.png", "Carril4.png","Carril5.png"]
        carrils2=["Carril11.png", "Carril22.png", "Carril33.png","Carril44.png","Carril55.png"]
        if(self.h< 40):
            img = os.path.join("Carrils", carrils1[self.nivell])
        else:
            img = os.path.join("Carrils", carrils2[self.nivell])
        self.img = Image.open(img)
        self.img = self.img.resize((self.w, self.h))
        self.carril = ImageTk.PhotoImage(self.img)


    def pintar(self, w):
        """
        Draws the lane and all contained entities on the specified canvas.

        Args:
            w (Canvas): The canvas on which to draw the lane and its entities.
        """
        w.create_image(self.x, self.y , anchor="nw", image=self.carril)
        for e in self.escales:
            e.pintar(w, self.y)
        for z in self.zombis + self.goblins:
            z.pintar(w, self.y)
        altres_objectes = self.ocells + self.saltarins + self.escuders + self.armes + self.armadures
        for o in altres_objectes:
            o.pintar(w)
        for m in self.murs:
            m.pintar(w,self.y)


    def moure_zombis(self):
        """
        Moves all movable entities within the lane including zombies, goblins, birds, jumpers, and shield bearers.
        Also handles collision with walls to prevent certain entities from passing through them.
        """
        objectes_movils = self.zombis + self.goblins + self.ocells + self.saltarins + self.escuders

        # Code to move entities and handle collisions
        for a in self.armes:
            a.moure()

        for o in objectes_movils:
            from Zombi import Escuder
            colisio_mur_left = False
            colisio_mur_right = False
            
            if isinstance(o, Escuder) and o.tipus == 1:
                    if self.nivell==4:
                        for mur in self.murs:
                            if mur.x-5<=o.x + o.w <= mur.x+5 and self.y - mur.h <= o.y + o.h <= self.y:
                                colisio_mur_left=True
                            if mur.x+mur.w -5<= o.x <= mur.x + mur.w +5 and self.y - mur.h <= o.y + o.h <= self.y:
                                colisio_mur_right=True 
                    if colisio_mur_left:
                        o.v = -o.v
                        o.transposar = False
                    elif colisio_mur_right:
                        o.v= -o.v
                        o.transposar = True
            o.moure()

        objectes_voladors = self.ocells + self.escuders

        for v in objectes_voladors:                
            if v.vuela==True:
                if v.is_up==True:
                    v.y-=3
                else:
                    v.y+=3

                if v.y + v.h>=self.y:
                    v.is_up=True
                elif v.y <= self.y + self.h - self.a:
                    v.is_up=False

        for s in self.saltarins:
            s.saltar()
        
        for e in self.escuders:
            if e.tirador==True:
                e.auxiliar_tir+=1
                if e.auxiliar_tir%10== 0:
                        from Arma import Arma   
                        llenca_arma = Arma("Escuder", e.tipus, e.x, e.y,e.v/abs(e.v)) 
                        self.armes.append(llenca_arma)
                if e.auxiliar_tir==10*(7-e.vides):
                    e.tirador=False
                    e.auxiliar_tir=0


    def detectar_colisions(self, objecte): 
        """
        Detects collisions between a given object and entities within the lane. Updates the state of the
        entities based on the type of collision (e.g., damage taken, changes in behavior).

        Args:
            objecte (Object): The object with which to check for collisions against entities in the lane.
        
        Returns:
            Object: The entity that collided with the given object, if any.
        """
        from Zombi import Zombi
        from Zombi import Goblin
        from Arma import Arma   

        # Code to detect collisions and update entity states
        for z in self.zombis + self.goblins:
            if (
                z.x <= (objecte.x + objecte.w)    
                and (z.x + z.w) >= objecte.x 
                and self.y >= objecte.y           
                and (self.y - z.h) <= (objecte.y + objecte.h)
            ):  
                if isinstance(objecte, Arma):
                    z.vides-=objecte.d
                else:
                    z.vides = 0       

                if(z.vides<=0):
                    if isinstance(z, Zombi):
                        self.zombis.append(Zombi(1000 + z.x))
                        self.zombis.remove(z)
                    elif isinstance(z, Goblin):
                        self.goblins.append(Goblin(1000+z.x))
                        self.goblins.remove(z)
                elif isinstance(z, Goblin):       
                    z.h -=z.h//(z.vides +1)
                    z.w -=z.w//(z.vides +1)
                    
                return z
            
        for o in self.ocells:   
            if (
                o.x <= (objecte.x + objecte.w)      
                and (o.x + o.w) >= objecte.x 
                and o.y  + o.h >= objecte.y           
                and o.y <= (objecte.y + objecte.h)
            ):
                if isinstance(objecte, Arma):
                    o.vides-=objecte.d
                else:
                    o.vides = 0                                 
                if(o.vides<=0):
                    from Zombi import Ocell
                    self.ocells.append(Ocell(o.malvat, 1000+ o.x, o.y, o.w, o.h, o.v, o.a, o.boles, o.cadencia))
                    self.ocells.remove(o)
                return o
            
        for s in self.saltarins:
            if (
                s.x <= objecte.x + objecte.w      
                and s.x + s.w >= objecte.x 
                and s.y+s.h >= objecte.y           
                and s.y <= objecte.y + objecte.h
            ):
                if isinstance(objecte, Arma):
                    s.vides-=objecte.d
                else:
                    s.vides = 0
                if(s.vides<=0):
                    from Zombi import Saltarin
                    self.saltarins.append(Saltarin(1000+s.x, s.y))
                    self.saltarins.remove(s)
                    return s
                
        for e in self.escuders:
            if (
                e.x <= objecte.x + objecte.w     
                and e.x + e.w >= objecte.x 
                and e.y+e.h >= objecte.y           
                and e.y <= objecte.y + objecte.h
            ):
                if isinstance(objecte, Arma):
                    e.vides-=objecte.d
                else:
                    e.vides = 0

                if e.tipus == 3:
                    e.tirador=True

                if e.vides ==2:
                    if e.tipus == 0:
                        e.escut = False
                        img_pth = os.path.join("Armes", "Escut.png")
                        img = Image.open(img_pth)
                        img = img.resize((15, 15))
                        e.escut_img=ImageTk.PhotoImage(img)
                        e.x_moment = e.x
                    else:
                        llenca_arma = Arma("Escuder", e.tipus, e.x, e.y, e.v//abs(e.v), v=5)
                        self.armes.append(llenca_arma)
                elif e.vides<=0:
                    from Zombi import Escuder
                    self.escuders.append(Escuder(e.tipus, 1000+e.x, e.y, e.w, e.h, e.v))
                    self.escuders.remove(e)
                return e
            
        for a in self.armes:
            if a.personatge!="Arthur" and isinstance(objecte, Arma)==False:
                if (
                    a.x <= objecte.x + objecte.w      
                    and a.x + a.w >= objecte.x 
                    and a.y+a.h >= objecte.y           
                    and a.y <= objecte.y + objecte.h
                ):
                    self.armes.remove(a)
                    return a
        return None
        
    
    def canvi_arma(self, arthur):
        """
        Checks for and handles the event where Arthur picks up a weapon in the lane. Updates Arthur's current weapon.

        Args:
            arthur (Arthur): The game's main character who might pick up a weapon.
        """
        # Code to allow Arthur to change weapons
        for a in self.armes:
                if(
                a.personatge=="Arthur"
                and arthur.x <= (a.x + a.w)      
                and (arthur.x + arthur.w) >= a.x 
                and (arthur.y+arthur.h) >= a.y           
                and arthur.y <= (a.y + a.h)
            ):
                    arthur.arma_actual = a.arma
                    self.armes.remove(a)
    
    def armadura(self, arthur):
        """
        Checks for and handles the event where Arthur picks up an armor. Updates Arthur's armor status.

        Args:
            arthur (Arthur): The game's main character who might pick up an armor.
        """
        # Code to allow Arthur to pick up armor
        for a in self.armadures:
            if (
                arthur.x <= (a.x + a.w)    
                and (arthur.x + arthur.w) >= a.x 
                and (arthur.y+arthur.h) >= a.y           
                and arthur.y <= (a.y + a.h)
            ):
                arthur.vides=1
                self.armadures.remove(a)
                    