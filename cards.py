import pygame
import time
pygame.init()
width=600
height=400
screen=pygame.display.set_mode((width,height))
#loading images
img1=pygame.image.load("diwali_bg1.jpg")
img2=pygame.image.load("diwali_bg2.jpg")
img3=pygame.image.load("diwali_bg3.jpeg")
img4=pygame.image.load("diwali_bg4.jpeg")
# resizing img
img1=pygame.transform.scale(img1,(width,height))
img2=pygame.transform.scale(img2,(width,height))
img3=pygame.transform.scale(img3,(width,height))
img4=pygame.transform.scale(img4,(width,height))
#loading font
font=pygame.font.SysFont("lobster",45)


run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    screen.blit(img1,(0,0))
    text1=font.render("Keep calm and eat sweets, it’s Diwali!",True,"white")
    screen.blit(text1,(30,100))
    pygame.display.update()
    time.sleep(2)
    screen.blit(img2,(0,0))
    text2=font.render("When in doubt, add more lights!",True,"white")
    screen.blit(text2,(40,100))
    pygame.display.update() 
    time.sleep(2)
    screen.blit(img3,(0,0))
    text3=font.render("Sugar,shine,and shenanigans!",True,"white")
    screen.blit(text3,(40,100))
    pygame.display.update()
    time.sleep(2)
    screen.blit(img4,(0,0))
    text4=font.render("Glow goals achieved",True,"white")
    screen.blit(text4,(40,100))
    pygame.display.update()
    time.sleep(2)
    
    pygame.display.update()
pygame.quit()
    
    
    pygame.display.update()
pygame.quit()
