#### IN THIS CODE WE DEFINE THE CLASS  "MALVAT": "ZOMBI", "GOBLIN", "OCELL", "ESCUDER" "SALTARIN"

#Zombis:
## 1: Zombi1
## 2: Zombi2
## 3: Roca1
## 4: Roca2

from PIL import Image, ImageTk
import os                           
from Arthur import *

class Malvat:
    """
    Represents a generic villain in the game, providing basic movement and behavior methods.

    This class is intended to be a superclass for more specific types of villain characters, handling
    common attributes like position, movement direction, and firing mechanisms.

    Attributes:
        malvat (int): Type identifier for the villain.
        x (float): The x-coordinate of the villain on the game canvas.
        auxiliar (int): A helper variable for miscellaneous uses, such as timing or state transitions.
        transposar (bool): Indicates whether the villain's image should be flipped (used for changing direction visually).
        turn (bool): Indicates whether the villain can turn around on reaching canvas boundaries.
        tirador (bool): Indicates whether the villain can shoot.
        auxiliar_tir (int): A counter used to manage shooting timing or frequency.
        v (float): Current velocity (speed and direction) of the villain.
        w (int): Width of the villain's image.
        h (int): Height of the villain's image.
        a (float): Acceleration factor for speeding up the villain.
    """
    def __init__(self, malvat, x):
        """
        Initializes a new villain with the specified type and initial position.

        Args:
            malvat (int): The type identifier for the villain.
            x (float): Initial x-coordinate of the villain.
        """
        self.malvat, self.x = malvat, x
        self.auxiliar=0
        self.transposar = False                  
        self.turn = False
        self.tirador = False
        self.auxiliar_tir = 0

    def moure(self):
        """
        Moves the villain based on its current velocity and position settings.

        Handles boundary interactions where the villain may need to turn around or reset its position to
        the opposite side of the canvas, depending on the 'turn' attribute.
        """
        self.x+=self.v

        if self.turn == False:
            # for those who go in a positive direction
            if(self.v > 0 and self.x>1000): 
                self.x = -self.w
            # for those who go in a negative direction
            elif(self.v<0 and self.x<-self.w):  
                self.x = 1000   
        else:
            # for those who go in a positive direction
            if(self.v > 0 and self.x+self.w>1000): 
                self.v = -self.v
                self.transposar = False
            # for those who go in a negative direction   
            elif(self.v<0 and -10<self.x<5):  
                self.v = -self.v
                self.transposar = True

            
    def accelerar(self):
        """
        Increases the villain's velocity by its acceleration factor.
        """
        self.v +=self.a
    
    
    def image(self, tipus_malvat, img_pth):
        """
        Loads and returns the appropriate image for the villain, flipping it if necessary.

        Args:
            tipus_malvat (Malvat): The specific villain instance for which the image is needed.
            img_pth (str): The path to the image file.

        Returns:
            ImageTk.PhotoImage: The image object of the villain to be displayed.
        """
        img = Image.open(img_pth)

        if (tipus_malvat.transposar==True):
            img = img.transpose(Image.FLIP_LEFT_RIGHT)

        img = img.resize((tipus_malvat.w, tipus_malvat.h))
        img = ImageTk.PhotoImage(img)

        return img


class Zombi(Malvat):
    """
    Represents a zombie enemy in the game, inheriting from the generic villain class 'Malvat'.
    This class manages zombie-specific attributes such as width, height, velocity, and health,
    along with methods for rendering the zombie's movement on the game canvas.

    Attributes:
        w (int): Width of the zombie image.
        h (int): Height of the zombie image.
        v (int): Velocity of the zombie. Negative values indicate leftward movement.
        a (int, optional): Acceleration factor for the zombie. Defaults to None.
        vides (int): Health points of the zombie, indicating how many hits it can take before being defeated.
    """

    def __init__(self, x, w=50, h=50, v=-3, a=None):
        """
        Initializes a new zombie instance with specified characteristics including position, size, velocity,
        and optional acceleration.

        Args:
            x (int): Initial x-coordinate of the zombie.
            w (int, optional): Width of the zombie image. Defaults to 50.
            h (int, optional): Height of the zombie image. Defaults to 50.
            v (int, optional): Velocity of the zombie. Negative values indicate leftward movement. Defaults to -3.
            a (int, optional): Acceleration factor for the zombie. Defaults to None.
        """
        super().__init__(0, x)
        self.w, self.h, self.v, self.a = w, h, v, a
        self.vides = 1  # Zombies start with one health point


    def zombi_img(self):
        """
        Selects and returns the appropriate zombie image based on the zombie's auxiliary counter,
        which creates an animation effect by cycling through images.

        Returns:
            ImageTk.PhotoImage: The image object of the zombie to be displayed.
        """
        zombi1 = "Zombi1.png"
        zombi2 = "Zombi2.png"
        self.auxiliar += 1  # Increment to change images and simulate movement
        
        if self.auxiliar < 3:
            img = os.path.join("Zombis", zombi1)
        else:
            img = os.path.join("Zombis", zombi2)
            if self.auxiliar == 6:
                self.auxiliar = -1  # Reset the counter for continuous animation

        self.img = super().image(self, img)
        
        return self.img


    def pintar(self, w, y_c):
        """
        Draws the zombie on the specified canvas at a given y-coordinate adjusted by the zombie's height.

        Args:
            w (Canvas): The canvas on which to draw the zombie.
            y_c (int): The y-coordinate of the lane where the zombie should be drawn, adjusted by the zombie's height.
        """
        w.create_image(self.x, y_c - self.h, anchor="nw", image=self.zombi_img())


class Goblin(Malvat):
    """
    Represents a goblin enemy in the game, inheriting from the generic villain class 'Malvat'.
    This class manages goblin-specific attributes such as width, height, velocity, health, and turning behavior,
    along with methods for rendering the goblin's movement on the game canvas.

    Attributes:
        w (int): Width of the goblin image.
        h (int): Height of the goblin image.
        v (int): Velocity of the goblin. Negative values indicate leftward movement.
        a (int, optional): Acceleration factor for the goblin. Defaults to None.
        vides (int): Health points of the goblin, indicating how many hits it can take before being defeated.
        turn (bool): Indicates whether the goblin can turn around upon reaching the boundaries of the game canvas.
    """

    def __init__(self, x, w=100, h=100, v=-5, a=None):
        """
        Initializes a new goblin instance with specified characteristics including position, size, velocity,
        and optional acceleration.

        Args:
            x (int): Initial x-coordinate of the goblin.
            w (int, optional): Width of the goblin image. Defaults to 100.
            h (int, optional): Height of the goblin image. Defaults to 100.
            v (int, optional): Velocity of the goblin. Negative values indicate leftward movement. Defaults to -5.
            a (int, optional): Acceleration factor for the goblin. Defaults to None.
        """
        super().__init__(0, x)
        self.w, self.h, self.v, self.a = w, h, v, a
        self.vides = 5  # Goblins start with five health points
        self.turn = True  # Goblins can turn at canvas boundaries


    def goblin_img(self):
        """
        Selects and returns the appropriate goblin image based on the goblin's auxiliary counter,
        which creates an animation effect by cycling through images.

        Returns:
            ImageTk.PhotoImage: The image object of the goblin to be displayed.
        """
        goblin1 = "Goblin1.png"
        goblin2 = "Goblin2.png"
        # Increment to change images and simulate movement
        self.auxiliar += 1  

        if self.auxiliar < 2:
            img = os.path.join("Goblins", goblin1)
        else:
            img = os.path.join("Goblins", goblin2)
            # Reset the counter for continuous animation
            if self.auxiliar == 4:
                self.auxiliar = -1  

        self.img = super().image(self, img)
        return self.img


    def pintar(self, w, y_c):
        """
        Draws the goblin on the specified canvas at a given y-coordinate adjusted by the goblin's height.

        Args:
            w (Canvas): The canvas on which to draw the goblin.
            y_c (int): The y-coordinate of the lane where the goblin should be drawn, adjusted by the goblin's height.
        """
        w.create_image(self.x, y_c - self.h, anchor="nw", image=self.goblin_img())


class Ocell(Malvat):
    """
    Represents a bird-like enemy in the game, inheriting from the generic villain class 'Malvat'.
    This class manages bird-specific attributes such as flying behavior, shooting projectiles,
    and animated movement.

    Attributes:
        y (int): The y-coordinate of the bird on the game canvas.
        w (int): Width of the bird image.
        h (int): Height of the bird image.
        v (int): Velocity of the bird. Negative values indicate leftward movement.
        a (int, optional): Acceleration factor for the bird. Defaults to None.
        boles (list): List of projectiles the bird may shoot.
        cadencia (int): Rate at which the bird shoots projectiles.
        vides (int): Health points of the bird, indicating how many hits it can take before being defeated.
        is_throwing (bool): Indicates whether the bird is currently throwing/shooting.
        vuela (bool): Determines if the bird has flying behavior (up and down movement).
        is_up (bool): Indicates if the bird is moving upward in its flight pattern.
        vuelo (int): Counter to manage how much the bird has flown, related to its flying behavior.
        ocells1 (list): List of filenames for the bird's first animation state images.
        ocells2 (list): List of filenames for the bird's second animation state images.
    """

    def __init__(self, ocell, x, y, w=30, h=20, v=-10, a=None, boles=[], cadencia=2):
        """
        Initializes a new bird instance with specified characteristics including position, size, velocity,
        optional acceleration, projectiles, and shooting cadence.

        Args:
            ocell (int): The type identifier for the bird.
            x (int): Initial x-coordinate of the bird.
            y (int): Initial y-coordinate of the bird.
            w (int, optional): Width of the bird image. Defaults to 30.
            h (int, optional): Height of the bird image. Defaults to 20.
            v (int, optional): Velocity of the bird. Negative values indicate leftward movement. Defaults to -10.
            a (int, optional): Acceleration factor for the bird. Defaults to None.
            boles (list, optional): List of projectiles the bird may shoot.
            cadencia (int, optional): Rate at which the bird shoots projectiles. Defaults to 2.
        """
        super().__init__(ocell, x)
        self.y, self.w, self.h, self.v, self.a = y, w, h, v, a
        self.boles, self.cadencia = boles, cadencia
        self.vides = ocell + 1  # Health is based on bird type
        self.is_throwing = False
        self.vuela = False
        self.is_up = False
        self.vuelo = 0
        self.auxiliar = 0

        if ocell in [0, 1]:  # Specific bird types have flying behavior
            self.vuela = True
        if ocell == 0:
            self.turn = True  # Allows turning at screen edges for certain bird types

        self.ocells1 = ["Bat1.png", "Blue1.png", "Red1.png", "MayFly1.png", "Petite1.png"]
        self.ocells2 = ["Bat2.png", "Blue2.png", "Red2.png", "MayFly2.png", "Petite2.png"]

    def ocell_img(self):
        """
        Selects and returns the appropriate bird image based on an auxiliary counter,
        creating an animation effect by cycling through two sets of images.

        Returns:
            ImageTk.PhotoImage: The image object of the bird to be displayed.
        """
        if self.auxiliar < 3:
            img = os.path.join("Ocells", self.ocells1[self.malvat])
            self.auxiliar += 1
        else:
            img = os.path.join("Ocells", self.ocells2[self.malvat])
            if self.auxiliar == 5:
                self.auxiliar = 0  # Reset counter for continuous animation
            self.auxiliar += 1

        self.img = super().image(self, img)

        return self.img

    def pintar(self, w):
        """
        Draws the bird on the specified canvas at its current coordinates.

        Args:
            w (Canvas): The canvas on which to draw the bird.
        """
        w.create_image(self.x, self.y, anchor="nw", image=self.ocell_img())
 

class Escuder(Ocell):
    """
    Represents a shield-bearing enemy in the game, inheriting from the bird-like enemy class 'Ocell'.
    This class manages specific attributes such as shield status, type of shield bearer, and provides methods
    for rendering the shield bearer's movement and shield status on the game canvas.

    Attributes:
        tipus (int): Type identifier for the shield bearer, which affects its appearance and behavior.
        vides (int): Health points of the shield bearer, indicating how many hits it can take before being defeated.
        escut (bool): Indicates whether the shield is currently active.
        aux_escut (int): Auxiliary counter used to manage the animation of the shield falling off.
        x_moment (int): X-coordinate for the falling shield animation.
    """

    def __init__(self, tipus, x, y, w=30, h=40, v=-10, a=None):
        """
        Initializes a new shield bearer instance with specified characteristics including position, size, velocity,
        type, and optional acceleration.

        Args:
            tipus (int): Type of the shield bearer, influencing appearance and specific behaviors.
            x (int): Initial x-coordinate of the shield bearer.
            y (int): Initial y-coordinate of the shield bearer.
            w (int, optional): Width of the shield bearer image. Defaults to 30.
            h (int, optional): Height of the shield bearer image. Defaults to 40.
            v (int, optional): Velocity of the shield bearer. Negative values indicate leftward movement. Defaults to -10.
            a (int, optional): Acceleration factor for the shield bearer. Defaults to None.
        """
        # Defined as malvat=0 initially
        super().__init__(0, x, y, w, h, v, cadencia=0)  
        self.tipus = tipus
        self.vides = 4 if tipus != 3 else 2  
        self.escut = True
        self.aux_escut = 0
        self.turn = tipus in [1, 2, 3]  
        self.vuela = tipus == 3  


    def escuder_img(self):
        """
        Selects and returns the appropriate shield bearer image based on the type and current health status,
        creating an animation effect by cycling through images.

        Returns:
            ImageTk.PhotoImage: The image object of the shield bearer to be displayed.
        """
        # Image selection based on type and health
        if self.vides < 3:
            self.malvat = 1
        imatges = {
            0: (["Escuder1.png", "Escuder2.png"], ["Escuder11.png", "Escuder22.png"]),
            1: (["Cerdo1.png", "Cerdo2.png"], ["Cerdo11.png", "Cerdo22.png"]),
            2: (["Mort1.png", "Mort2.png"], ["Mort11.png", "Mort22.png"]),
            3: (["Woody1.png", "Woody1.png"], ["Woody2.png", "Woody1.png"])
        }
        imgs = imatges[self.tipus]
        current_imgs = imgs[0] if self.malvat == 0 else imgs[1]

        if self.auxiliar < 2:
            img = os.path.join("Escuder", current_imgs[0])
            self.auxiliar += 1
        else:
            img = os.path.join("Escuder", current_imgs[1])
            self.auxiliar += 1
            if self.auxiliar == 4:
                # Reset for continuous animation
                self.auxiliar = 0  

        self.img = super().image(self, img)

        return self.img


    def pintar(self, w):
        """
        Draws the shield bearer on the specified canvas at its current coordinates.
        Also manages the animation of the shield falling off if the shield is deactivated.

        Args:
            w (Canvas): The canvas on which to draw the shield bearer.
        """
        w.create_image(self.x, self.y, anchor="nw", image=self.escuder_img())
        if not self.escut and self.aux_escut < 5:
            # Draw falling shield animation
            w.create_image(self.x_moment, self.y + 10 * self.aux_escut, anchor="nw", image=self.escut_img)
            self.aux_escut+=1
                

class Saltarin(Malvat):
    """
    Represents a jumping enemy (Saltarin) in the game, inheriting from the generic villain class 'Malvat'.
    This class manages specific attributes such as jump mechanics, standing, bending, and provides methods
    for rendering the Saltarin's various states on the game canvas.

    Attributes:
        y (int): The y-coordinate of the Saltarin on the game canvas.
        w (int): Width of the Saltarin image.
        h (int): Height of the Saltarin image.
        v (int): Velocity of the Saltarin. Negative values indicate leftward movement.
        a (int, optional): Acceleration factor for the Saltarin. Defaults to None.
        vides (int): Health points of the Saltarin, indicating how many hits it can take before being defeated.
        turn (bool): Indicates whether the Saltarin can turn around upon reaching the boundaries of the game canvas.
        salt (int): Counter to manage the jumping mechanics.
        pos (int): Position state of the Saltarin: 0 (bending), 1 (standing), 2 (jumping).
        is_jumping (bool): Indicates if the Saltarin is in the jumping phase.
        is_bending (bool): Indicates if the Saltarin is in the bending phase.
    """

    def __init__(self, x, y, w=20, h=25, v=-5, a=None):
        """
        Initializes a new Saltarin instance with specified characteristics including position, size, velocity,
        and optional acceleration.

        Args:
            x (int): Initial x-coordinate of the Saltarin.
            y (int): Initial y-coordinate of the Saltarin.
            w (int, optional): Width of the Saltarin image. Defaults to 20.
            h (int, optional): Height of the Saltarin image. Defaults to 25.
            v (int, optional): Velocity of the Saltarin. Negative values indicate leftward movement. Defaults to -5.
            a (int, optional): Acceleration factor for the Saltarin. Defaults to None.
        """
        super().__init__(None, x)
        self.y, self.w, self.h, self.v, self.a = y, w, h, v, a
        self.vides = 2
        self.turn = True  # Saltarines turn at screen edges
        self.salt = 0
        self.pos = 1  # Initial position is standing
        self.is_jumping = False
        self.is_bending = False


    def saltarin_img(self):
        """
        Selects and returns the appropriate Saltarin image based on the current position state,
        which includes different images for standing, bending, and jumping phases.

        Returns:
            ImageTk.PhotoImage: The image object of the Saltarin to be displayed.
        """
        saltarin_images = ["Saltarin1.png", "Saltarin2.png"]
        img_path = os.path.join("Saltarin", saltarin_images[self.pos])
        self.img = super().image(self, img_path)

        return self.img

    def pintar(self, w):
        """
        Draws the Saltarin on the specified canvas at its current coordinates.

        Args:
            w (Canvas): The canvas on which to draw the Saltarin.
        """
        w.create_image(self.x, self.y, anchor="nw", image=self.saltarin_img())


    def saltar(self):
        """
        Manages the Saltarin's jumping and bending mechanics by adjusting its vertical position and height
        based on its current state and progression within the jump cycle.
        """
        if self.salt == 0:  # Control speed of the animation
            if self.pos == 0:  # From bending to standing
                self.h = 5 * self.h
                self.y = self.y - self.h + self.h // 5
                self.pos = 1
            elif self.pos == 1 and not self.is_jumping and not self.is_bending:  # From standing to jumping
                self.y -= 2 * self.h
                self.is_jumping = True
            elif self.pos == 1 and self.is_jumping:  # From jumping to standing
                self.y += 2 * self.h
                self.is_bending = True
                self.is_jumping = False
            else:  # From standing to bending
                self.y = self.y + self.h - self.h // 5
                self.h = self.h // 5
                self.pos = 0
                self.is_bending = False
            self.salt += 1
        else:
            self.salt+=1
            if self.salt==3:
                self.salt=0 
            
    

