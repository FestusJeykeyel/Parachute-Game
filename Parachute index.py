import pygame
from settings import*
from sprites import*

#Instanzierung
#Wahrscheinlichkeiten festsetzen für die versachiedenen Fallschirmspringer 
parachutist_spawnrate = 0.5
parachutist_damaged_spawnrate = 0.28
parachutist_lightning_spawnrate = 0.2
parachutist_heart_spawnrate = 0.02  #if hearts <=2


spawn_timer = 0
spawn_interval = random.randint(80, 300)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
            print("Spiel wurde beendet")
  #Maiwand
    if spawn_timer >= spawn_interval:
        parachute_x = helicopter_1.x  # Calculate x-coordinate based on helicopter's position
        parachute_y = helicopter_1.y + 90 

        RandomSpawnNumber = random.random()
        if RandomSpawnNumber < parachutist_spawnrate:
            parachute = Parachutist(parachute_x, parachute_y, 80, 20, 2)
        elif RandomSpawnNumber < parachutist_spawnrate + parachutist_damaged_spawnrate:
            parachute = ParachutistDamaged(parachute_x, parachute_y, 80, 20, 2)
        elif RandomSpawnNumber < parachutist_spawnrate + parachutist_damaged_spawnrate + parachutist_lightning_spawnrate:
            parachute = ParachutistLightning(parachute_x, parachute_y, 80, 20, 2)
        else:
            parachute = ParachutistHeart(parachute_x, parachute_y, 80, 20, 2)
#parachute = Parachutist(parachute_x, parachute_y, helicopter1.x, helicopter1.y, 2)
        #parachute.x = parachute_x
        parachutes_group.add(parachute) 

        spawn_timer = 0
        spawn_interval = random.randint(80, 300)
    else:
        spawn_timer +=1


    #Render
    screen.blit(image_background,(0,0))
    
    normal_tree_group.draw(screen)# - Festus
    long_tree_group.draw(screen)
    wolken_group.draw(screen)
    player_group.draw(screen)
    water_group.draw(screen) # - F

    parachutes_group.draw(screen)  # - M
  
    boat_single_group.draw(screen) # F

    #Update
    boat_single_group.update() # - Festus
    score_single_group.update()
    player_group.update()# - F
    wolken_group.update() # - Festus
    
    parachutes_group.update() # - M
    helicopter_group.update() # - Maiwand
      
    pygame.display.flip()
    

pygame.quit()
