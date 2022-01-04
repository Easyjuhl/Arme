import pygame
import game

pygame.init()

screen = pygame.display.set_mode((750,750))#, pygame.FULLSCREEN
MyFont = pygame.font.SysFont("arial", 44)
clock = pygame.time.Clock()

musicstarted = False
done = False
MyGame = game.Game()

#Tile variables
TileTypes = [(0,165,0), (130,130,130), (250,250,250)]
TileSize = [50,50]

#Unit variables
UnitList = []
CurrentPlayer = "Player1"
PlayerList = ["Player1", "Player2"]

UnitList.append(game.Army("Player1", 75, 75, (0, 0, 200)))
UnitList.append(game.Army("Player2", 300, 300, (200, 0, 0)))


def playMusic():
    pygame.mixer.music.load("/home/easyjuhl/Documents/Python/Arme/Isaks_spil.mp3")
    pygame.mixer.music.play(loops=-1, start=0)

def draw_game():
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0,0,750,750))
    for i in range(0,len(MyGame.get_grid())):
        for j in range(0, len(MyGame.get_grid()[i])):
            pygame.draw.rect(screen, TileTypes[MyGame.get_grid()[i][j]], pygame.Rect(i*TileSize[0], (j)*TileSize[1], TileSize[0], TileSize[1]))
    
    for n in UnitList:
        pygame.draw.circle(screen, n.color, (n.xCoord, n.yCoord), 20 )

def draw_game_over():
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(0,0,750,750))
    text1 = MyFont.render("Game Over", True, (0,0,0))
    textRect1 = text1.get_rect()
    textRect1.center = (375, 375)
    screen.blit(text1, textRect1)
    pygame.display.update()

def pixels_to_cell(x,y):
    x1 = int(x/TileSize[0])
    y1 = int(y/TileSize[1])
    return x1,y1

def output_logic(tilstand):
    if tilstand == 1:
        draw_game()
    
    if tilstand == 2:
        draw_game_over()

tilstand = -1
Unitnumber = 0

while not done:

    if tilstand != -1:
        if musicstarted == False:
            playMusic()
            musicstarted = True

    for u in UnitList:
        Unitnumber += 1
        if u.Ownership == CurrentPlayer:
            if u.MovedYet == False:
                CurrentUnit = u
                Unitnumber = 0
                break
        if Unitnumber == len(UnitList):
            Unitnumber = 0
            if CurrentPlayer == "Player2":
                CurrentPlayer = "Player1"
            else:
                CurrentPlayer = "Player2"
            for n in UnitList:
                n.MovedYet = False
            
                


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif tilstand == -1 and (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
            tilstand = 1
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True

        
        if tilstand == 1 and event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            CurrentUnit.Move(pos[0], pos[1])
            if CurrentUnit.MovedYet == True:
                for u in UnitList:
                    if CurrentUnit.Attack_check(u.xCoord, u.yCoord, u.Ownership):
                        if u.DamageCalculation(CurrentUnit.BaseDamagePrUnit, CurrentUnit.Units):
                            UnitList.remove(u)
                        for p in PlayerList:
                            PlayerUnit = 0
                            for n in UnitList:
                                if n.Ownership == p:
                                    PlayerUnit += 1
                            
                            if PlayerUnit == 0:
                                tilstand = 2


    
    output_logic(tilstand)

    pygame.display.flip()
    clock.tick(60)

       
