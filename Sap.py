import pygame
from pygame.locals import *

import sys
from pygame.rect import Rect
import numpy as np

pygame.init()
x = (384)
y = (288)
NBx = 210
NBy = 302
ZBx =48*9+12
ZBy = 48*8+12
NBx1 = 485
NBy1 = 500

white = (255, 255, 255, 255)
OKNOGRY = pygame.display.set_mode((816, 624), 0, 32)
pygame.display.set_caption('SAPER')
robotImg = pygame.image.load('robot.png')
mapImg = pygame.image.load('mapaSaper.png')
map2Img = pygame.image.load('budynek1.png')
map3Img = pygame.image.load('budynek2.png')
CzB = pygame.image.load('CzB.png')
NB = pygame.image.load('NB.png')
ZB = pygame.image.load('ZB.png')
mapa=0
mapaNB=0
pole = 110
NBpole = 106
mapaZB = 3
ZBpole = 145
change_map = mapImg
przewoz=0
mapa=0



# 0- puste (może przejechać), 1- zajęte ( nie może przejechać), 2- budynek(może wjechać do środka),
#3 - wej�cie do budynku;4,6 - bomba 9#wyjście z map3,5-woda,66-tablica,77-hehe my
map = np.array([1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0,
       5, 5, 0, 1, 3, 3, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0,
       0, 5, 5, 5, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0,
       0, 1, 1, 5, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 2, 2, 0,
       0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0,
       0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1,
       0, 0, 0, 1, 4, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1,
       1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
       1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0,
       0, 0, 0, 66, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1,
       5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 0, 0, 5, 5, 5, 1, 1,
       0, 0, 0, 5, 0, 5, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0,
       1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 5, 5, 5, 1, 1, 0])

map2 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1,
        1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1,
        0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 8, 8, 8, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 8, 8, 8, 1, 1])

map3 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 77, 1,
       0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1,
       1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1,
       1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 0, 6, 0, 0, 0, 0, 0, 0, 0,
       1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 9, 0, 0])

map_general = map


def krata():
    for i in range(0,13):
        for j in range(0,17):

            pygame.draw.rect(OKNOGRY, (0,0,0), Rect((j*48,i*48),(48,48)), 1)


def szukanieBomby():
    for i in range(0,17):
        for j in range(0,13):

            pole = i*17+j
            x = j*48+24 #środek pola
            y = i*48+24 #środek pola
def robot(x, y):
	OKNOGRY.blit(robotImg, (x, y))
def fNB(NBx,NBy):
    if mapaNB==mapa:
        OKNOGRY.blit(NB, (NBx+6, NBy+6))
def fZB(ZBx,ZBy):
    if mapaZB==mapa:
        OKNOGRY.blit(ZB, (ZBx+6, ZBy+6))
        
while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    OKNOGRY.blit(change_map, (0, 0))
    robot(x, y)
    fNB(NBx, NBy)
    fZB(ZBx, ZBy)
    #fNB(NBx1, NBy1)
    pygame.display.update()
    x_change = 0
    y_change = 0
    currentX = x
    currentY = y
    currentPole = pole
    licz=0
    
    
    robic = raw_input ('Co mam zrobi�?   ')
    if robic == ('rozbr�j') or robic == ('rozbroj'):
         if map_general[pole]==4 or map_general[pole]==46:
            NBx=1000
            NBy=1000
            fNB(NBx,NBy)
            if przewoz==1:
                przewoz=0
            print ('Bomba rozbrojona')
            if map_general[pole]==4:
                map_general[pole]=0
            else:
                map_general[pole]=6
         else:
             print ('Nie ma tu bomby')
        
    elif robic == ('jedz') or robic == ('jed�') or robic == ('idz') or robic == ('id�'):
        ile = int(raw_input('Ile pol mam jechac?  '))
        move = raw_input('W kt�r� stron� mam jecha�?    ')
        for n in range(ile):
            if move == ("w") or move == ("gora") or move == ("g�ra") or move == ("p�noc") or move == ("polnoc"):
                y_change = -48
                pole += -17
            elif move == ("s") or move == ("d�") or move == ("po�udnie") or move == ("dol") or move == ("poludnie"):
               y_change = +48
               pole += 17
            elif move == ("a") or move == ("lewo") or move == ("zachod") or move == ("zach�d"):
                x_change = -48
                pole += -1
            elif move == ("d") or move == ("prawo") or move == ("wschod") or move == ("wsch�d"):
                x_change = +48
                pole += 1

            x += x_change
            y += y_change

            if x > 816 - 48:
                x = 816 - 48
                pole = currentPole
                x= currentX
            if x < 0:
                x = 0
                x= currentX
                pole = currentPole
            if y > 624 - 48:
                y = 624 - 48
                y= currentY
                pole = currentPole
            if y < 0:
                y = 0
                y= currentY
                pole = currentPole

            if map_general[pole] == 0 :
              robot(x,y)
              if (przewoz==1):
                  if map_general[NBpole]==4:
                      map_general[NBpole]=0
                  elif map_general[NBpole]==46:
                      map_general[NBpole]=6
                  map_general[pole]=4
                  NBpole=pole
                  NBx=x+12
                  NBy=y+12
                #  fNB(NBx,NBy)
              if (przewoz==2):
                  if map_general[ZBpole]==6:
                      map_general[ZBpole]=0
                  elif map_general[ZBpole]==46:
                      map_general[ZBpole]=4
                  map_general[pole]=6
                  ZBpole=pole
                  ZBx=x-12
                  ZBy=y+12
               #   fZB(ZBx,ZBy)
            elif map_general[pole] == 4:
              if (przewoz==2):
                  map_general[ZBpole]=0
                  map_general[pole]=46
                  ZBpole=pole
                  ZBx=x-12
                  ZBy=y+12
                #  fZB(ZBx,ZBy)
            elif map_general[pole]==6:
              if (przewoz==1):
                 map_general[NBpole]=0
                 map_general[pole]=46
                 NBpole=pole
                 NBx=x+12
                 NBy=y+12
               #  fNB(NBx,NBy)
              
            elif map_general[pole] == 1:
              if licz==0:
                  licz=1
                  print("       B��D! Nie mog� wjecha� na wskazan� pozycj�.")
              robot(currentX, currentY)
              pole = currentPole
              x= currentX
              y= currentY
              if przewoz==1:
                  NBx=x+12
                  NBy=y+12
                  NBpole=pole
                 # fNB(NBx,NBy)
              elif (przewoz==2):
                  ZBx=x-12
                  ZBy=y+12
                  ZBpole=pole
               #   fZB(ZBx,ZBy)
            elif map_general[pole] == 5:
              print('       W fabryce nie nauczyli mnie p�ywa�!')
              robot(currentX, currentY)
              pole = currentPole
              x= currentX
              y= currentY
            elif map_general[pole] == 66:
              print('    Znalaz�em znak:')
              print('   "P�noc - Temeria, Zach�d - Tatooine')
              print('    Po�udnie - Shire, Wsch�d - Hogwart"')
              robot(currentX, currentY)
              pole = currentPole
              x= currentX
              y= currentY
            elif map_general[pole] == 77:
              print('   Autor�w projektu trzymamy w tej piwnicy:')
              print('       Igor Misiorny')
              print('       Bartosz Szuka�a')
              print('       Micha� �mieszek')
              print('       Gracjan Walch')
              print('       Rafa� �ebrowski')
              print("   I nie, nie wypu�cimy, mog� si� jeszcze przyda� (Gracjana ewentualnie mo�emy).")
              robot(currentX, currentY)
              pole = currentPole
              x= currentX
              y= currentY
            elif map_general[pole] == 2:
                print('     Wszed�em do budynku.')
                change_map = map2Img
                map_general = map2
                pole = 183
                OKNOGRY.blit(change_map, (0, 0))
                mapa=2       
                x = 624
                y = 480
                robot(x, y)
                if przewoz==1:
                    map_general[currentPole]=0
                    if map2[pole]==0:
                        map2[pole]=4
                    else:
                        map3[pole]=46
                    mapaNB=2
                 #   fNB(x+12,y+12)
                    map[NBpole]=0    
                    NBpole=pole
                if przewoz==2:
                    map_general[currentPole]=0
                    if map3[pole]==0:
                        map3[pole]=6
                    else:
                        map3[pole]=46
                    mapaZB=2
                  #  fZB(x-12,y+12)
                    map[ZBpole]=0    
                    ZBpole=pole
                
            elif map_general[pole] == 3:
                print("     Jestem w �rodku." )
                change_map = map3Img
                map_general = map3
                pole = 201
                OKNOGRY.blit(change_map, (0, 0))
                mapa=3 
                x = 672
                y = 528
                robot(x, y)
                if przewoz==1:
                    if map[NBpole]==4:
                       map[NBpole]=0
                       if map3[pole]==0:
                           map3[pole]=4
                       elif map3[pole]==6:
                            map3[pole]=46
                    elif map_general[currentPole]==46:
                        map_general[currentPole]=6
                        map3[pole]=4
                    mapaNB=3
                  #  fNB(x+12,y+12)    
                    NBpole=pole
                elif przewoz==2 :
                    if map_general[currentPole]==6:
                       map_general[currentPole]=0
                       if map3[202]==0:
                           map3[202]=6
                       elif map3[202]==4:
                            map3[202]=46
                    elif map2[currentPole]==46:
                        map2[currentPole]=4
                        map3[201]=6
                    mapaZB=0
                  #  fZB(x-12,y+12)  
                    ZBpole=pole

            elif map_general[pole] == 9:
                print('     Wyszed�em z budynku.')
                change_map = mapImg
                map_general = map
                pole = 39
                OKNOGRY.blit(change_map, (0, 0))
                mapa=0
                x = 240
                y = 96
                robot(x, y)
                if przewoz==1:
                    if map_general[NBpole]==4:
                       map_general[NBpole]=0
                       if map[pole]==0:
                           map[pole]=4
                       elif map[pole]==6:
                            map[pole]=46
                    elif map3[NBpole]==46:
                        map3[NBpole]=6
                        map3[40]=4
                    mapaNB=0
                 #   fNB(x+12,y+12) 
                    NBpole=pole
                if przewoz==2:
                    if map_general[currentPole]==6:
                       map_general[currentPole]=0
                       if map[pole]==0:
                           map[pole]=6
                       elif map[pole]==4:
                            map[pole]=46
                    elif map_general[ZBpole]==46:
                        map3[ZBpole]=4
                        map[pole]=6
                    mapaZB=0
                  #  fZB(x-12,y+12) 
                    ZBpole=pole
                

            elif map_general[pole] == 8:
                print('     Jestem na zewn�trz.')
                change_map = mapImg
                map_general = map
                pole = 82
                OKNOGRY.blit(change_map, (0, 0))
                mapa=0
                x = 672
                y = 192
                robot(x, y)
                if przewoz==1:
                    if map_general[NBpole]==4:
                       map_general[NBpole]=0
                       if map[pole]==0:
                           map[pole]=4
                       elif map[pole]==6:
                            map[pole]=46
                    elif map2[ZBpole]==46:
                        map2[ZBpole]=6
                        map2[pole]=4
                    mapaNB=0
                #    fNB(x+12,y+12) 
                    NBpole=pole
                if przewoz==2:
                    if map_general[ZBpole]==6:
                       map_general[ZBpole]=0
                       if map[pole]==0:
                           map[pole]=6
                       elif map[pole]==4:
                            map[pole]=46
                    elif map_general[ZBpole]==46:
                        map2[ZBpole]=4
                        map[pole]=6
                    mapaZB=0
                 #   fZB(x-12,y+12) 
                    ZBpole=pole
                
            
        
    elif robic == ('wez') or robic == ('we�') or robic == ('zabierz') or robic == ('podnies') or robic == ('podnies'):
        if map_general[pole] == 4 and przewoz == 0:
            przewoz=1
            print('     Bomba zabrana.')
        elif map_general[pole] == 6 and przewoz == 0:
            przewoz=2
            print('     Bomba zabrana.')
        elif przewoz == 2 or przewoz == 1:
            print ('    Trzymam bomb�.')
        elif map_general[pole]==46:
            co=raw_input('Bra� zielon� bomb�?       ')
            if co=='tak':
                przewoz=1
            elif co=='nie':
                przewoz=2
            else:
                print ('Odpowiedz jest prosta tak/nie    ')
        else:
            print ("    Nic tu nie ma.")
                
    elif robic == ('zostaw') or robic == ('odstaw') or robic == ('po��') or robic == ('poloz') or robic == ('odloz') or robic == ('od��'):
        if przewoz==1:
            przewoz=0
            print("     Bomba od�o�ona.")
        elif przewoz==2:
            przewoz=0
            print("     Bomba od�o�ona.")
        else:
            print("     Nie mam bomby.")
    elif robic == 'wrzuc' and map[pole]==6:
        if mapa==0:
            if przewoz==2:
                przewoz=0
            if pole==90 or pole==92 or pole==108:
                map[pole]=0
                ZBx=300
                ZBy=236
                fZB(ZBx,ZBy)
            if pole==85 or pole==87 or pole==103 or pole==69:
                map[pole]=0
                ZBx=60
                ZBy=236
                fZB(ZBx,ZBy)
            if pole==180 or pole==196 or pole==198 or pole==213:
                map[pole]=0
                ZBx=480
                ZBy=535
                fZB(ZBx,ZBy)
            print("     Bomba wrzucona do dziury.")
             
    elif robic == 'wrzuc' and map[pole]==46:
        if mapa==0:
             if przewoz==2:
                przewoz=0
             if pole==90 or pole==92 or pole==108:
                map[pole]=4
                ZBx=300
                ZBy=236
                fZB(ZBx,ZBy)
             if pole==85 or pole==87 or pole==103 or pole==69:
                map[pole]=4
                ZBx=60
                ZBy=236
                fZB(ZBx,ZBy)
             if pole==180 or pole==196 or pole==198 or pole==213:
                map[pole]=4
                ZBx=480
                ZBy=535
                fZB(ZBx,ZBy)
             print("     Bomba wrzucona do dziury.")

    elif robic == ('help') or robic == ('pomoc') or robic == ('?'):
        plik = open('plik.txt')
        try:
            tekst = plik.read()
        finally:
            plik.close()

        print tekst
            
                
    elif robic == ('przedstaw sie!') or robic == ('przedstaw sie') or robic == ('przedstaw si�!') or robic == ('przedstaw si�'):
        print("     Jestem robot ")
    elif robic == ('witam') or robic == ('czesc') or robic == ('cze��') or robic == ('siema') or robic == ('dzien dobry') or robic == ('dzie� dobry') or robic == ('hej') or robic == ('no cze��'):
        print('     Witam :)')
    elif robic ==(':(') or robic ==('xd') or robic ==('xD') or robic ==(':P') or robic ==(';)') or robic ==(':)') or robic ==(':D'):
        print('     :)')
    elif robic=='map':
        print map.reshape((13,17))
    elif robic=='map2':
        print map2.reshape((13,17))
    elif robic=='map3':
        print map3.reshape((13,17))
    elif robic=='mapa':
        print mapa, mapaNB
    elif robic=='x':
        print x, y
    elif robic=='pole':
        print pole, map_general[pole]
    elif robic == 'wyjdz':
        exit(0)
        
    else: print("      B��D! Nie rozpoznano polecenia.")
    fNB(x+12,y+12)
    fZB(x-12,y-12)
     
    pygame.display.update()

