###  IN THIS CODE WE DEFINE THE CLASS"ARMA"
import keyboard
import time
from tkinter import *
from PIL import Image, ImageTk
from Carril import *
import os   


class Arma:
    def __init__(self, personatge, arma, x, y, sentit, v=15, d=1):
        """
        Initializes a new weapon instance with specified attributes and loads the weapon image.

        The weapon's trajectory and other visual properties like width, height, and image
        are set based on the character and type of the weapon.

        Args:
            personatge (str): The name of the character who uses the weapon.
            arma (int): Type of the weapon.
            x (int): Initial x-coordinate of the weapon.
            y (int): Initial y-coordinate of the weapon.
            sentit (int): Direction of the weapon's movement.
            v (int, optional): Speed of the weapon. Defaults to 15.
            d (int, optional): Damage caused by the weapon. Defaults to 1.
        """
        self.personatge, self.arma, self.x, self.y, self.sentit, self.v, self.d = personatge, arma, x, y, sentit, v, d
        self.trajectoria = 1
        self.h, self.w, self.img = None, None, None

        # Define weapon details for each character and weapon type
        if self.personatge == "Arthur":
            detalls_arma = {
                0: ("Arma_1.png", 50, 5, d),
                1: ("Arma_2.png", 30, 10, d),
                2: ("Arma_3.png", 20, 20, 2),
                3: ("Arma_4.png", 20, 20, 3),
                4: ("Arma_5.png", 30, 30, 4),
            }
        elif self.personatge == "Escuder":
            detalls_arma = {
                0: ("Escut.png", 50, 5, d),
                1: ("Trident.png", 30, 10, d),
                2: ("Falc.png", 20, 40, d),
                3: ("Bident.png", 40, 6, d),
            }

        img_file, self.w, self.h, self.d = detalls_arma.get(self.arma, (None, None, None, self.d))
        if img_file:
            img_path = os.path.join("Armes", img_file)
            self.img = Image.open(img_path)
            if self.sentit == -1:
                self.x -= 2 * self.w
                self.img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
            self.img = self.img.resize((self.w, self.h))
            self.arma_img = ImageTk.PhotoImage(self.img)

    def moure(self):
        """
        Moves the weapon based on its speed and trajectory. Adjusts position and handles special trajectory for certain weapons.
        """
        self.x += self.sentit * self.v
        if self.personatge == "Arthur" and self.arma in [2, 3, 4]:
            if self.trajectoria < 5:
                self.y -= self.v // self.trajectoria
                self.trajectoria += 1
            else:
                self.y += self.v // max(10 - self.trajectoria, 1)
                self.trajectoria += 1

    def pintar(self, w):
        """
        Draws the weapon on the canvas at its current position.

        Args:
            w (Canvas): The canvas on which to draw the weapon.
        """
        w.create_image(self.x, self.y, anchor="nw", image=self.arma_img)
