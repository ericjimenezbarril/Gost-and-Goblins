from Zombi import *
from Arthur import *
from Arma import * 
from Carril import *
from Puerta import *

class Partida:
    """
    Manages the game session, including level setup, character initialization, and placement of game elements like lanes,
    enemies, and items.

    This class initializes all components required for the game level, including the player character 'Arthur', enemies,
    weapons, armor, keys, and gates.

    Attributes:
        nivell (int): The current game level.
        arma (int): The initial weapon Arthur starts with.
        llista_carrils (list): A list of lists, each containing 'Carril' instances for different game levels.
        llista_claus (list): A list of lists, each containing 'Clau' (Key) instances for unlocking parts of each level.
        llista_portes (list): A list of 'Porta' (Gate) instances that serve as goals or checkpoints within levels.
        inicis_y (list): A list of y-coordinates at which Arthur starts in each level.
        arthur (Arthur): The player's character, initialized based on the level and starting weapon.
    """
    
    def __init__(self, nivell, arma):
        """
        Initializes the game session with the specified level and Arthur's initial weapon.

        Sets up the game environment based on the level, including lanes, enemies, items, keys, gates,
        and the starting position and weapon of the player character.

        Args:
            nivell (int): The current game level.
            arma (int): The initial weapon index Arthur starts with.
        """
        self.nivell, self.arma = nivell, arma

        # Initialize lanes for different levels
        carrils_1=[Carril(0,500, 1000, 100, 200,0,zombis=[Zombi(300),Zombi(330), Zombi(920),Zombi(980),Zombi(1000)], saltarins=[Saltarin(500, 475), Saltarin(900, 475)],
                        armes=[Arma("Arthur",2,700,470,1,v=0)],escales=[Escala(200), Escala(800)], armadures=[Armadura(120, 270)]),
                    Carril(100,300, 300,20, 200, 0, escuders=[Escuder(3,900, 250, w=50,h=20), Escuder (3,1500, 250, w=50,h=20),
                            Escuder (3,2200, 250, w=50,h=20)], escales=[Escala(300)]),
                    Carril(600, 300, 300, 20, 200, 0),
                    Carril(175,100,200, 20, 200, 0,escuders=[Escuder(0, 1800, 50,v=-7),Escuder(0, 1500, 50,v=-7),Escuder(0, 1200, 50,v=-7)],armes=[Arma("Arthur",1,170,70,0,v=0)]),
                    Carril(475, 100, 50, 20, 200, 0),
                    Carril(625, 100, 200, 20, 200, 0)]  

        carrils_2 = [Carril(0,550,1000,60, 95, 1),
                    Carril(40,455,160, 20, 62, 1),   
                    Carril(200,393,600, 20, 92, 1, ocells=[Ocell(1,500, 330, v=-5), Ocell(1,750, 330, v=-5), Ocell(1,1000, 330, v=-5)],
                            armes=[Arma("Arthur",3,400,370,1,v=0)]),  
                    Carril(805,455,160, 20, 62, 1, armadures=[Armadura(880, 415)]),  
                    Carril(400,301,200, 20, 93, 1),   
                    Carril(430,208,140, 20, 93, 1,ocells=[Ocell(4,485, 208-93//2), Ocell(4,100, 208-93//2), Ocell(4,870, 208-93//2)]),   
                    Carril(173,208,160, 20, 93, 1),   
                    Carril(668,208,160, 20, 93, 1, armes=[Arma("Arthur",0,725,190,1,v=0)]),   
                    Carril(65,115,100, 20, 100, 1),  
                    Carril(838,115,100, 20, 100, 1)]   
        carrils_3 = [Carril(0, 550, 1000,50, 140, 2, escales=[Escala(50, h=140, nivell=2),Escala(627, h=140, nivell=2),Escala(915, h=140, nivell=2)],
                                                    murs=[Mur(460)], goblins=[Goblin(1000), Goblin(460), Goblin(30000)]),
                    Carril(0, 410, 1000, 25, 140, 2, escales=[Escala(250, h=140, nivell=2),Escala(535, h=140, nivell=2),
                                                            Escala(915, h=140, nivell=2),Escala(715, h=140, nivell=2)],murs=[Mur(433), Mur(810)], goblins=[Goblin(1500)],
                                                            saltarins=[Saltarin(700, 385), Saltarin(1000, 385), Saltarin(1300, 385)]),
                    Carril(0, 270, 1000, 25, 140, 2,escales=[Escala(150, h=140, nivell=2),Escala(715, h=140, nivell=2)],
                                                    murs=[Mur(305, h=125), Mur(615, h=125)], 
                                                    ocells=[Ocell(3, 300, 210,w=40, h=20), Ocell(3, 1700, 210,w=40, h=20),Ocell(3, 3800, 210,w=40, h=20)],
                                                    saltarins=[Saltarin(2700, 385), Saltarin(3000, 385), Saltarin(3300, 385)],
                                                    armes=[Arma("Arthur",4, 830, 230,0,v=0)]),
                    Carril(0, 130, 1000, 20, 100, 2, goblins=[Goblin(900), Goblin(2300), Goblin(20000)],
                            ocells=[Ocell(3, 1000, 70,w=40, h=20),Ocell(3, 2700, 70,w=40, h=20)])] 

        carrils_4 = [Carril(0, 550, 1000,50, 100, 3, escales=[Escala(675, h=100, nivell=3)],
                            escuders=[Escuder(2, 700, 500, w=40 ,h=50),Escuder(2, 1300, 500, w=40 ,h=50)]), 
                    Carril(600, 450, 200, 20, 100, 3, armes=[Arma("Arthur", 2, 600, 410, 1, v=0)], escales=[Escala(740, h=100, nivell=3)]),
                    Carril(100, 350, 300, 20, 100, 3, escales=[Escala(340, h=100, nivell=3)]),
                    Carril(580, 350, 100, 20, 100, 3, escales=[Escala(590, h=100, nivell=3)]),
                    Carril(740, 350, 100, 20, 100, 3, ocells=[Ocell(0, 730,323,w=15,h=15),Ocell(0, 530,300,w=15,h=15),Ocell(0, 130,312,w=15,h=15)]),
                    Carril(890, 350, 100, 20, 100, 3),
                    Carril(330, 250, 150, 20, 100, 3, escales=[Escala(420, h=100,nivell=3)]),
                    Carril(550, 250, 150, 20, 100, 3, ocells=[Ocell(0, 550,190,w=15,h=15),Ocell(0, 1125,201,w=15,h=15),Ocell(0, 1325,187,w=15,h=15)]),
                    Carril(750, 250, 200, 20, 100, 3, escales=[Escala(800, h=100,nivell=3)], armes=[Arma("Arthur", 0, 650, 230, 1, 0)]),
                    Carril(330, 150, 150, 20, 100, 3),
                    Carril(250, 120, 50, 20, 100, 3),
                    Carril(170, 90, 50, 20, 100, 3),
                    Carril(50, 120, 70, 20, 100, 3, armadures=[Armadura(60, 90)]),
                    Carril(800, 150, 200, 20, 150, 3, ocells=[Ocell(0, 730,1123,w=15,h=15),Ocell(0, 1560,100,w=15,h=15),Ocell(0, 1030,112,w=15,h=15)])]
        carrils_5 = [Carril(0, 550, 1000, 50, 100, 4, escales=[Escala(240, h=100, nivell=4), Escala(750,h=160,nivell=4)],
                            murs=[Mur(318, 58, 385, 4),Mur(632, 58, 385, 4)],
                            escuders=[Escuder(1, 900, 500,w=50, h=50,v=-5), Escuder(1, 1300, 500,w=50, h=50,v=-5),
                                        Escuder(1, 400, 500,w=50, h=50,v=-5)],
                                        armadures=[Armadura(390, 520)], armes=[Arma("Arthur", 4, 570, 515, 1, v=0)]),
                    Carril(200, 450, 100, 20, 120, 4, escales=[Escala(205, h=120, nivell=4)]),
                    Carril(55, 330, 200, 20, 120, 4, escales=[Escala(70, h=120, nivell=4), Escala(200,h=120,nivell=4)],
                            murs=[Mur(145, w=30, h=120, nivell=4)],
                            ocells=[Ocell(2, 800, 260, w=40, v=-15),Ocell(2, 850, 260, w=40, v=-15),
                            Ocell(2, 900, 260, w=40, v=-15), Ocell(2, 1300, 260, w=40, v=-15),Ocell(2, 1350, 260, w=40, v=-15),
                            Ocell(2, 1400, 260, w=40, v=-15)]),
                    Carril(30, 210, 220, 20, 100, 4),  
                    Carril(305, 145, 80, 20, 100, 4, armes=[Arma("Arthur", 2, 330, 120, 1, v=0)]),             
                    Carril(620, 145, 80, 20, 100, 4),              
                    Carril(446, 480, 105, 20, 100, 4, escales=[Escala(473.5, h=280, nivell=4)]),
                    Carril(446, 200, 105, 20, 100, 4, ocells=[Ocell(2, 500, 160, w=40, v=-15),Ocell(2, 550, 160, w=40, v=-15),
                            Ocell(2, 1300, 160, w=40, v=-15),Ocell(2, 1350, 160, w=40, v=-15)]),            
                    Carril(690, 390, 310,20, 150, 4, escales=[Escala(820, h=160, nivell=4)], armadures=[Armadura(910, 360)]),
                    Carril(800, 230, 80, 20, 180, 4)]
        self.llista_carrils = [carrils_1, carrils_2, carrils_3, carrils_4, carrils_5]
        
        # Initialize keys
        self.llista_claus= [[Clau(700,250, 0, 0)],                                                            #LEVEL 1
                        [Clau(105,75, 1, 0), Clau(242,170, 1,1), Clau(415,260, 1,2),                          #LEVEL 2
                        Clau(565,260, 1,3), Clau(880,75, 1,4)],                                 
                        [Clau(415, 500,2,0),Clau(378, 200,2,1),Clau(738, 350,2,2),Clau(600, 500,2,3)],        #LEVEL 3
                        [Clau(110, 320,3,0),Clau(900, 310,3,1),Clau(920, 220,3,2)],                           #LEVEL 4
                        [Clau(493, 155, 4, 0), Clau(125, 290, 4, 1), Clau(490, 510, 4, 2)]]                   #LEVEL 5
        
        # Initialize doors
        self.llista_portes= [Porta(675, 20,100,80, 0),Porta(470, 150, 60,60,1), Porta(248, 465, 66,85,2), Porta(850, 50,100,105, 3),Porta(880, 470,80,80, 4)]

        # Initialize y values
        self.inicis_y = [450, 405, 500, 500,500]
        
        # Initialize Arthur
        self.arthur=Arthur(30,self.inicis_y[self.nivell],40,50, self.nivell, arma_actual=self.arma)     
        
