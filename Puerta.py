### IN THIS CODE WE DEFINE THE CLASSES "KEY" AND "DOOR"
from PIL import Image, ImageTk
import os

class Porta:
    """
    Represents a gate or door in the game environment, which can either be open or closed depending on game conditions.

    This class manages the visual representation of a door at a specific level and location within the game,
    and controls its open or closed state.

    Attributes:
        x (int): The x-coordinate of the door on the game canvas.
        y (int): The y-coordinate of the door on the game canvas.
        w (int): The width of the door image.
        h (int): The height of the door image.
        nivell (int): The level of the game at which the door appears.
        oberta (bool): A boolean indicating whether the door is open (True) or closed (False).
        porta (ImageTk.PhotoImage): The current image of the door, adjusted based on its state.
    """

    def __init__(self, x, y, w,h, nivell):
        """
        Initializes a new door instance with specified attributes.

        Sets the location, size, and level of the door, and initializes it as closed.

        Args:
            x (int): The x-coordinate where the door will be drawn.
            y (int): The y-coordinate where the door will be drawn.
            w (int): The width of the door.
            h (int): The height of the door.
            nivell (int): The level at which the door is located.
        """
        self.x, self.y, self.w, self.h, self.nivell = x,y,w,h,nivell
        self.oberta = False
        self.imag = None 

        # Doors
        self.portes = ["Porta1.png", "Porta2.png", "Porta3.png", "Porta4.png","Porta5.png"]         #clau[self.posicio][self.nivell]
        self.portes_obertes = ["Porta11.png", "Porta22.png","Porta33.png","Porta44.png", "Porta55.png"]
    
    
    def porta_img(self):   
        """
        Loads and returns the appropriate door image based on its current state (open or closed).

        Returns:
            ImageTk.PhotoImage: The image object of the door to be displayed.
        """
        if self.oberta == False:
            img = os.path.join("Portes", self.portes[self.nivell])
        else: 
            img = os.path.join("Portes", self.portes_obertes[self.nivell])
        
        self.img = Image.open(img) # Arthur de pie derecha    
        self.img = self.img.resize((self.w, self.h))
        self.porta = ImageTk.PhotoImage(self.img)
        
        return self.porta
        

    def pintar(self,w):
        """
        Draws the door on the specified canvas.

        Args:
            w (Canvas): The canvas on which to draw the door.
        """
        w.create_image(self.x, self.y, anchor="nw", image=self.porta_img())


class Clau:
    """
    Represents a key in the game, used for unlocking certain areas or elements within the levels.

    This class manages the visual representation of a key and provides methods for rendering it at specific locations
    within the game environment.

    Attributes:
        x (int): The x-coordinate of the key on the game canvas.
        y (int): The y-coordinate of the key on the game canvas.
        nivell (int): The level of the game at which the key appears.
        clau (int): The specific type of key within the level.
        w (int): The width of the key image.
        h (int): The height of the key image.
        clau_img (ImageTk.PhotoImage): The current image of the key, adjusted for display.
    """
    def __init__(self, x, y, nivell, clau): 
        """
        Initializes a new key instance with specified attributes.

        Sets the location, size, level, and type of the key, and adjusts its dimensions based on the level.

        Args:
            x (int): The x-coordinate where the key will be drawn.
            y (int): The y-coordinate where the key will be drawn.
            nivell (int): The level at which the key is used.
            clau (int): The type index of the key within the level.
        """
        self.x, self.y, self.nivell, self.clau = x, y, nivell, clau
        self.imag = None 
        self.w = 15
        self.h=40
        self.claus = [["Clau1.png"], ["Clau21.png", "Clau22.png", "Clau23.png","Clau24.png","Clau25.png"],
                      ["Clau31.png", "Clau32.png", "Clau33.png","Clau34.png"], ["Clau41.png", "Clau41.png", "Clau42.png"],
                      ["Clau5.png", "Clau5.png", "Clau5.png"]]        #clau[self.posicio][self.nivell]
        
        # Adjust size based on level-specific settings
        if nivell ==0:
            self.w=40
        elif nivell==3:
            self.h=20
            self.w=20 


    def claus_img(self):
        """
        Loads and returns the appropriate key image based on its level and type.

        Returns:
            ImageTk.PhotoImage: The image object of the key to be displayed.
        """
        img_path = os.path.join("Claus", self.claus[self.nivell][self.clau])
        
        self.img = Image.open(img_path)
        self.img = self.img.resize((self.w, self.h))
        self.clau_img = ImageTk.PhotoImage(self.img)
        
        return self.clau_img
    

    def pintar(self,w):
        """
        Draws the key on the specified canvas.

        Args:
            w (Canvas): The canvas on which to draw the key.
        """

        w.create_image(self.x, self.y, anchor="nw", image=self.claus_img())

         