from tkinter import *
import time
import keyboard
from Zombi import *
from Arthur import *
from Arma import * 
from Carril import *
from Puerta import *
from Crear_Partida import Partida
from PIL import Image, ImageTk

### PRINCESA
#img = Image.open("Princesa.png")
#img = img.resize((50, 50))
#princesa = ImageTk.PhotoImage(img)

# Birds
# Bat --> Ocell(0, x,y, w=15, h=15)
# Blue --> Ocell(1, x, y, v=-20)
# Red --> Ocell(2, x, y, w=40, v=-15)
# MayFly --> Ocell(3, x, y,w=40, h=20)
# Petite --> Ocell(4,x,y)

# WEAPONS_ARTHUR
# Arma 0 (Lanza) : Arma("Arthur", 0, x,y, 50, 5, sentit,v=)
# Arma 1 (Espasa): Arma("Arthur", 1, x,y, 30, 10, sentit,v=)
# Arma 2 (Foc)   : Arma("Arthur", 2, x,y, 20, 20, sentit,v=)
# Arma 3 (Hacha) : Arma("Arthur", 3, x,y, 20, 20, sentit,v=)
# Arma 4 (Nose)  : Arma("Arthur", 4, x,y, 30, 30, sentit,v=)
 
# ESCUDERS
# Esuder 0 (Escuder):Escuder(0, x, y,v=-7)
# Escuder 1 (Cerdo) : Escuder(1, x, y,w=50, h=50,v=-5)
# Escuder 2 (Mort)  : 
# Escuder 3  (Woody) : Escuder (3,x,y, w=50,h=20) 

#Inicialitcem el nivell
fotos_nivells=["Fons1.png", "Fons2.png", "Fons3.png","Fons4.png", "Fons5.png"]

def foto_nivell(nivell):
    img_path = os.path.join("Fons",fotos_nivells[nivell])
    img = Image.open(img_path)
    img = img.resize((1000, 600))
    fons_img = ImageTk.PhotoImage(img)
    return fons_img

tk = Tk()  # Creo un objeto Tkinter
w = Canvas(tk, width=1000, height=600, bg="black")
w.pack()

coin = 1 

while coin > 0:
    seleccion=0
    inici_partida = False
    
    while not keyboard.is_pressed("enter"):
        if keyboard.is_pressed("+"):
            seleccion = (1-seleccion)        
        fotos_inici=["Inici.png","Instruccions.png"]
        def foto_inici(seleccion):
            img_path = os.path.join("Inicis",fotos_inici[seleccion])
            img = Image.open(img_path)
            img = img.resize((1000, 600))
            fons_img = ImageTk.PhotoImage(img)
            return fons_img
        fons_img = foto_inici(seleccion)
        w.create_image(0, 0, anchor="nw", image=fons_img)   
        
        w.update()  
            
        time.sleep(50/1000)

    # Initialization of the game
    jocs = 3                   
    joc_en_curs = True

    # Initialization of the level
    nivell_auxiliar= 0        
    nivell_actual  = 0
    auxiliar = 0                
    arma_actual= 0              
    auxiliar_vides = 0          

    while joc_en_curs:
        partida_en_curs = True
        partida = Partida(nivell_actual, arma_actual)
        llista_carrils  = partida.llista_carrils
        llista_claus = partida.llista_claus
        llista_portes = partida.llista_portes
        inicis_y = partida.inicis_y
        arthur = partida.arthur
        
        nivell_auxiliar = nivell_actual
        
        # The game starts
        while partida_en_curs:          
            w.delete("all")
            if (nivell_auxiliar != nivell_actual):
                arthur=Arthur(30,inicis_y[nivell_actual],40,50, nivell_actual, vides=arthur.vides,arma_actual=arthur.arma_actual)

            nivell_auxiliar = nivell_actual

            ## Print the background
            fons_img = foto_nivell(nivell_actual)
            w.create_image(0, 0, anchor="nw", image=fons_img)   

            if keyboard.is_pressed("q"):
                break

            if nivell_actual==1 and arthur.y + arthur.h >= 550:
                partida_en_curs=False                             

            # LETS DEFINE THE MAIN OBJECTS
            porta = llista_portes[nivell_actual]
            claus = llista_claus[nivell_actual]
            carrils = llista_carrils[nivell_actual]
            
            # ACTIONS
            porta.pintar(w)
            
            #PART1.1: MOVE ARTHUR
            arthur.moure(carrils)  
            
            #PART1.2: MOVE THE ELEMENTS OF THE GAME
            for carril in carrils:
                # zombis
                carril.moure_zombis()  
                if arthur.auxiliar_vides ==True:
                    colisio_zombi = carril.detectar_colisions(arthur) 
                    if colisio_zombi is not None:
                        arthur.vides -=1
                        arthur.auxiliar_vides=False
                else:
                    if arthur.contador_aux_vides > 0:
                        arthur.contador_aux_vides -=1
                    else:
                        if arthur.vides < 0:
                            partida_en_curs = False
                        arthur.auxiliar_vides = True
                        arthur.contador_aux_vides = 30
                carril.canvi_arma(arthur)
                carril.armadura(arthur)

            # Detect weapons hitting zombies or walls
            colisio_mur_left = False
            colisio_mur_right = False 
                          
            for arma in arthur.armas:
                # If they hit a wall they are removed
                for carril in carrils:    
                    for mur in carril.murs:
                        if mur.x-5<=arma.x + arma.w <= mur.x+5 and carril.y - mur.h <= arma.y + arma.h <= carril.y:
                            colisio_mur_left=True
                        if mur.x+mur.w -5<= arma.x <= mur.x + mur.w +5 and carril.y - mur.h <= arma.y + arma.h <= carril.y:
                            colisio_mur_right=True 
                
                # If it goes off the map, we delete it
                if arma.x < 0 or arma.x>1000 or colisio_mur_left==True or colisio_mur_right==True: 
                    arthur.armas.remove(arma)
                for carril in carrils:
                    colisio_zombi = carril.detectar_colisions(arma) 
                    if colisio_zombi is not None:
                        if arma in arthur.armas:
                            arthur.armas.remove(arma)                  

            #PART3: REPRINT SCREEN: Print zombis, carrils, Arthur, etc.
            for carril in carrils:
                carril.pintar(w)
            for clau in claus:
                clau.pintar(w)
            arthur.pintar(w)

            # Let's see if the key is caught
            for clau in claus:
                if (clau.x < arthur.x + arthur.w
                    and clau.x + clau.w > arthur.x
                    and clau.y < arthur.y + arthur.h
                    and clau.y + clau.h > arthur.y):
                        claus.remove(clau)
                        
                        if len(claus)==0:         
                            porta.oberta=True
                        
            # Let's see if it comes in the door
            if (porta.x < arthur.x + arthur.w
                and porta.x + porta.w > arthur.x
                and porta.y < arthur.y + arthur.h
                and porta.y + porta.h > arthur.y
                and porta.oberta==True):
                nivell_actual += 1               
                arthur.nivell_actual+=1           

            # Print as many lives as we have left
            img = Image.open("Vida.png")
            img = img.resize((30, 30))
            vida_img = ImageTk.PhotoImage(img)
            mides = [10, 50, 90]
            for i in range(jocs):
                w.create_image(mides[i], 560, anchor="nw", image=vida_img)
            
            w.update()  
            # Let's stop 50 ms so the game doesn't go too fast (since we have to express it in seconds).
            time.sleep(50/1000)  
        
        jocs -=1
        arma_actual = arthur.arma_actual

        if jocs ==0:
            joc_en_curs=False 
    
    while not (keyboard.is_pressed('space') or keyboard.is_pressed('enter')):
        img_path = os.path.join("Final","Final.png")
        img = Image.open(img_path)
        img = img.resize((1000, 600))
        fons_img = ImageTk.PhotoImage(img)
        w.create_image(0, 0, anchor="nw", image=fons_img) 

        if keyboard.is_pressed('space'):
            coin = 0
        else: 
            coin=1
        w.update()  
        time.sleep(50/1000)

