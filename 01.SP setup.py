import pygame,random
pygame.init()

witdh=800
height=600

FPS=60
clock= pygame.time.Clock()

display_surface= pygame.display.set_mode((witdh,height))

#Game class

class Game():

    def __init__(self):
        #Inicializamos el Juego
        pass

    def update(self):
        #Actualizar el juego
        pass

    def draw(self):
        #Draw the HUD Y la informacion del display
        pass

    def shift_aliens(self):
        #shift = mover  moveremos la wave de aliens hacia abajo y cambiar la direccion
        pass
     
    def check_collision(self):
        #Check for collision between player bullet group and alien group and other collision
        pass

    def check_round_completion(self):
        #check to see if a player has completed a single round
        pass

    def start_new_round(self):
        #Empezar nueva ronda
        pass

    def check_game_status(self):
        #check if the player died
        pass

    def pause_game(self):
        #pausar el juego
        pass

    def reset_game(self):
        #Reset the game
        pass

    class Player(pygame.sprite.Sprite):
        #A class to model(crear plantilla) a spaceship the user can controll

        def __init__(self):
            #Inicializar al jugador
            pass

        def update(self):
            #Actualizar al jugador, aqui incluimos el movimiento
            pass

        def fire(self):
            #Disparar
            pass

        def reset(self):
            #Reset the player position
            pass

        #The class Alien is going to be like a IA

    class Alien(pygame.sprite.Sprite):
        #A class to model(crear plantilla) a Alien the user can control
            
        def __init__(self):
            #Inicializar al Alien
            pass

        def update(self):
            #Actualizar al Alien, aqui incluimos el movimiento
            pass

        def fire(self):
            #Disparar
            pass

        def reset(self):
            #Reset the player position
            pass

    class PlayerBullet(pygame.sprite.Sprite):
        #A class to model(crear plantilla) a bullet the user can control

        def __init__(self):
            pass

        def update(self):
            #Actualizar la bala
            pass

    class AlienBullet(pygame.sprite.Sprite):
        #A class to model(crear plantilla) a  the user can controll

        def __init__(self):
            pass

        def update(self):
            #Actualizar la bala
            pass



running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    pygame.display.update()
    clock.tick(FPS)



