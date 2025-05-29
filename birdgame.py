from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame,sys
import time
pygame.init()
fsize = 40
scrn = pygame.display.set_mode((590,702))
font = pygame.font.SysFont('none',fsize)
mainbg = pygame.image.load('mainbg.png')

class Button():
    def __init__(self,text,width,height,pos):
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = (100,100,100)
        self.text_color = (225,225,225)

        self.text_surf = font.render(text,True,self.text_color)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
    def draw(self):
        pygame.draw.rect(scrn,self.top_color,self.top_rect,border_radius = 12)
        scrn.blit(self.text_surf,self.text_rect)
        self.hoverBtn()
    def hoverBtn(self):
        pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(pos):
            self.top_color = (15,225,225)
        else:
            self.top_color = (100,100,100)
            

def play():
    pygame.mixer.init()
    click = pygame.mixer.Sound('buttonclick.mp3')
    click.play()
    pos = pygame.mouse.get_pos()
    if playbutton.top_rect.collidepoint(pos):
        scrn.fill(playbutton.top_color)
        print('Hello the [player]')
        #image source
        screen = pygame.display.set_mode((590,702))
        backgound = pygame.image.load('background.png')
        bird = pygame.image.load('fuppy.png')
        villan = pygame.image.load('pipe.png')

        #variables
        run = True
        birdy = 150
        villanx = 450
        score = 0
        font = pygame.font.Font('freesansbold.ttf',32)
        gameover = pygame.font.Font('freesansbold.ttf',100)

        while run:
            
            scoredisplay = font.render(str(score), True,(225,225,225))

        #brid movements
            
            if birdy < 585:
                birdy = birdy+1     
            else:
                birdy = 585

        #villan attack

            if villanx >100 and villanx < 150:
                if birdy <300 or birdy >476:
                    #restart button
                    screen.blit(backgound,(0,0))
                    pygame.display.update()
                    run = False
        #villan movement            
            if villanx > -50:
                
                villanx = villanx - 1.5
            else:
                villanx = 570
                score += 1                           
            screen.blit(backgound,(0,0))
            screen.blit(bird,(100,birdy))
            screen.blit(scoredisplay,(10,10))
            if villanx > -50:
                screen.blit(villan,(villanx,-350))
                pass
            else:
                screen.blit(villan,(villanx,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        birdy = birdy - 45
            pygame.display.update()
def Exit():
    pygame.mixer.init()
    click = pygame.mixer.Sound('buttonclick.mp3')
    click.play()
    pygame.mixer.music.set_volume(0.4)
    pos = pygame.mouse.get_pos()
    if exitbutton.top_rect.collidepoint(pos):
        print()
        print(''"""""""""""""""""""""""""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' ")
        print("This not an error. This mean Game is Quit")
        print(''"""""""""""""""""""""""""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''' ")
        print()
        time.sleep(0.5 )
        pygame.quit()

playbutton = Button('Start',140,40,(260,350))
exitbutton = Button('Exit',120,40,(270,400))
Run = True

while Run:
    pygame.mixer.init()
    pygame.mixer.music.load('bird.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.queue('bird.mp3')
    pygame.mixer.music.set_volume(0.4)
    scrn.blit(mainbg,(0,0))
    playbutton.draw()
    exitbutton.draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            play()
            Exit()
    pygame.display.update()
pygame.quit()
