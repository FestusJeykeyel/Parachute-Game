import pygame
import random
from settings import*


#klasse Boat Erzeugen 
class Boat(pygame.sprite.Sprite):
    def __init__(self, boat_width, boat_height,picture_path, boat_velocity):
        super().__init__()
        self.pos_left= (0,700)
        self.pos_right= (SCREEN_WIDTH, 700)
        self.image= pygame.image.load(picture_path)
        self.image= pygame.transform.scale(self.image,(boat_width,boat_height))
        self.rect= self.image.get_rect()
        self.boat_velocity= boat_velocity
        self.hitbox = (self.rect.x,self.rect.y, 64,64)


    def draw(self):
        self.hitbox = (self.rect.x+ 30,self.rect.y+80, 150,30)
        pygame.draw.rect(screen,(255,0,0),(self.rect),2)

    def update(self):
        self.draw()
        #Steuerung Links und Rechts
        keystate= pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            self.rect.x += self.boat_velocity

        if keystate[pygame.K_LEFT]:
            self.rect.x -= self.boat_velocity
            
        '''
        # Einfache Kollision
        if  self.rect.colliderect(parachute1.rect):
            self.kill()
        '''
        #kollision mit wand
        if self.rect.topleft <=  self.pos_left:
            self.rect.topleft = self.pos_left

        if self.rect.topright  >= self.pos_right:
            self.rect.topright = self.pos_right

boat1 = Boat(200,100,'game_pictures/boot_holz.png',8)
boat_single_group = pygame.sprite.GroupSingle()
boat_single_group.add(boat1)


# Klasse Wasser erzeugt
class Water(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image= pygame.image.load('game_pictures/liquidWaterTop.png')
        self.rect= self.image.get_rect()
        self.image= pygame.transform.scale(self.image,(SCREEN_WIDTH,200))
        self.rect.topleft = (0,692)

water=Water()
water_group= pygame.sprite.Group()
water_group.add(water) 

# Wolke Erzeugt
class Wolken(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x,pos_y):
        super().__init__()
        self.cloud_pos_1 = (SCREEN_WIDTH,50)
        self.cloud_pos_2 = (0,(50))
        self.cloud_height = 0
        self.image= pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (150,150))
        self.rect.center = (pos_x ,pos_y)
        self.velocity = 0.5

    def update(self):
        
        self.rect.centerx += self.velocity
        if self.rect.topleft >= self.cloud_pos_1:
            self.rect.topleft = self.cloud_pos_2 
        
wolken_group = pygame.sprite.Group()

for wolke in range(8):
    new_clouds= Wolken('game_pictures/wolken.png', random.randrange(0,SCREEN_WIDTH), random.randint(100,200))
    wolken_group.add(new_clouds)
    
# Baumkonstruktor
class   Tree_Constructor(pygame.sprite.Sprite):
    def __init__(self,picture_path,poas_x,pos_y):
        super().__init__() 
        self.image = pygame.image.load(picture_path)
        self.rect= self.image.get_rect()
        self.rect.center= [poas_x,pos_y]
     
# Einzelne Bäume mit Konstruktor
long_tree_group = pygame.sprite.Group()
for i in range(5):
    new_long_tree = Tree_Constructor('game_pictures/treeLong.png',random.randint(10,SCREEN_WIDTH),580)
    long_tree_group.add(new_long_tree)

normal_tree_group = pygame.sprite.Group()
for i in range(5):
    new_tree = Tree_Constructor('game_pictures/tree.png', random.randrange(0,SCREEN_WIDTH), random.randint(500,590))
    normal_tree_group.add(new_tree)

    
class Boat_Parachute_Collision:
    def __init__(self):
        super().__init__()
        pass

    def update(self):
        #Kolision mit Fallschirm 
        # sprite colllision detection advanced with Group
        pygame.sprite.spritecollide(boat1, parachutes_group, True)

        
class Score(pygame.sprite.Sprite):
    def __init__(self,score_value):
        super().__init__()
        self.score_value = score_value
        self.font = pygame.font.SysFont('arial',20)
    
    def update(self):
        if pygame.sprite.spritecollide(boat1, parachutes_group, True):
            self.score_value += 1
        schrift = self.font.render("Score :" + str(self.score_value), True, (0,0,0,),(255,0,0))
        screen.blit(schrift,(10,100))
    
score_single_group = pygame.sprite.GroupSingle()
score_single_group.add(Score(0))

###################################### Ab hier kommen Maiwands Klassen ############################################################

class Helicopter (pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pygame.image.load(os.path.join('game_pictures/helicopter.png'))
        self.rect = self.image.get_rect()
        #Hier hat Festus das Bild skaliert
        self.image = pygame.transform.scale(self.image,(200,100))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.draw(screen)
        self.x += self.speed
        if self.x >= SCREEN_WIDTH - self.width-150:
            self.speed = -self.speed
            self.image = pygame.transform.flip(self.image, True, False)
        if self.x <= 0:
            self.speed = -self.speed
            self.image = pygame.transform.flip(self.image, True, False)

helicopter_1 = Helicopter(0,25,40,50,2)
helicopter_group = pygame.sprite.GroupSingle()
helicopter_group.add(helicopter_1)

class Parachutist(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, speed):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pygame.image.load('game_pictures/parachute.png')
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        if self.rect.y == 120:
            self.speed = 0
            self.image = pygame.image.load('game_pictures/water_splash1.png')
            #water_splash_image = pygame.transform.scale(water_splash_image, (self.width, self.height))
            self.rect = self.image.get_rect()
            self.rect.y = self.y
            #water_splash_sound.play()

class ParachutistHeart(Parachutist):
    def init(self, x, y, width, height, speed):
        super().__init__(x, y, width, height, speed)
        self.image = pygame.image.load('game_pictures/parachute_heart.png')
        self.rect = self.image.get_rect()


class ParachutistDamaged(Parachutist):
    def init(self, x, y, width, height, speed):
        super().__init__(x, y, width, height,speed+1)
        self.image = pygame.image.load('game_pictures/parachute_damaged.png')
        self.rect = self.image.get_rect()

class ParachutistLightning(Parachutist):
    def init(self, x, y, width, height, speed):
        super().__init__(x, y, width, height, speed)
        self.image = pygame.image.load('game_pictures/parachute_lightning.png')
        self.rect = self.image.get_rect()

parachutes_group = pygame.sprite.Group()
