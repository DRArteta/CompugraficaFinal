import configparser
import pygame
import math
import random

Ancho = 1000
Alto = 600
NEGRO=[0,0,0]
BLANCO=[255,255,255]

def empe():
    balas.empty()
    rivales.empty()
    rivales2.empty()
    rivales3.empty()
    rivales4.empty()
    paquetesv.empty()
    doublets.empty()
    Boses.empty()
    VidaBoses.empty()
    balas_r.empty()
    Guis.empty()
    Puntos.empty()
    Asteroids.empty()

def inicio():


    segundo = 0
    animy = 0
    men = 1
    Mx = 0
    My = 0
    BossCan = True
    CanVertical = False
    CanHorizontal2 = False
    CanHorizontal1 = True
    asteroides = True
    rival = True
    ttt = True
    rival2 = True
    rival3 = True
    baalasr = True
    Colision = True
    segundol = False
    pos_fila = 0
    an_corte=32
    end = False
    printf = 0
    printc = 0
    canFire = True
    cont_cuadros=0
    tasa_cuadros=60
    ticon = 0
    stein = 0
    NR = 2
    NR3 = 1
    NR4 = 1
    lim = 180
    j1.vidas = 3
    j1.puntos = 0


    gui = Gui(G)
    Guis.add(gui)
    sound.play()

    if rival == True:
        for i in range(NR3):
            e=Rival3([0,0])
            e.rect.x = random.randrange(Ancho - e.rect.width)
            e.rect.y = random.randrange(400)
            rivales3.add(e)

        for i in range(NR4):
            h=Rival4([0,0])
            h.rect.x = random.randrange(Ancho - h.rect.width)
            h.rect.y = random.randrange(400)
            rivales4.add(h)

        for i in range(NR):
        	e = Rival([20,20],enemy)
        	e2 = Rival2([20,20])
        	e.rect.x = random.randrange(Ancho - e.rect.width)
        	e.rect.y = random.randrange(400)
        	rivales.add(e)
        	e2.rect.x = random.randrange(Ancho - e2.rect.width)
        	e2.rect.y = random.randrange(400)
        	rivales2.add(e2)

        for i in range(10):
            aster = Asteroid([250,250],E)
            aster.rect.x = random.randrange(Ancho)
            aster.rect.y = random.randrange(300)
            prob_v = random.randrange(3)
            if prob_v == 1:
                aster.velx=aster.velx*-1
                aster.vely=aster.velx*-1
            Asteroids.add(aster)

def expl(j):
    exp = [pygame.image.load('png/exp/31.png'),pygame.image.load('png/exp/32.png'),pygame.image.load('png/exp/33.png'),pygame.image.load('png/exp/34.png'),pygame.image.load('png/exp/35.png'),pygame.image.load('png/exp/36.png'),pygame.image.load('png/exp/37.png'),pygame.image.load('png/exp/38.png')]
    for i in range (0,8):
        pantalla.blit(exp[i],j)


class Torreta(pygame.sprite.Sprite): #Torre
    def __init__(self,p):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('png/Torreta.png')
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx = -1
        self.temp = 100
        self.vida = 2
    def update(self):
        self.rect.x += self.velx
        if self.temp > 0:
            self.temp -= 1


class Bouse(pygame.sprite.Sprite): #Torre
    def __init__(self,p):
        pygame.sprite.Sprite.__init__(self)
        self.i = 0
        self.im=[pygame.image.load('png/Boss2/0.png'),pygame.image.load('png/Boss2/1.png'),pygame.image.load('png/Boss2/2.png'),pygame.image.load('png/Boss2/3.png'),pygame.image.load('png/Boss2/4.png')]
        self.image = self.im[self.i]
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx = -1
        self.vely = 1
        self.vida = 100
        self.temp = 100

    def update(self):

        self.i+=1
        if self.i > 4:
            self.i=0
        self.image=self.im[self.i]
        if self.temp > 0:
            self.temp -= 1
        self.rect.x += self.velx
        self.rect.y += self.vely
        if self.rect.x < 700:
            self.velx=0
        if self.rect.y < 20:
            self.vely= 3
        if self.rect.y > 300:
            self.vely=-3

        if self.vida > 0:
            pygame.draw.rect(pantalla, [200,0,0],[300,20, self.vida*3, 2])
        else:
            pygame.draw.rect(pantalla, [200,0,0],[300,20, -self.vida*3, 2])


class Final(pygame.sprite.Sprite): #Torre
    def __init__(self,p):
        pygame.sprite.Sprite.__init__(self)
        self.i = 0
        self.im=[pygame.image.load('png/Boss2/0.png'),pygame.image.load('png/Boss2/1.png'),pygame.image.load('png/Boss2/2.png'),pygame.image.load('png/Boss2/3.png'),pygame.image.load('png/Boss2/4.png')]
        self.image = self.im[self.i]
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx = -1
        self.vely = 1
        self.vida = 100
        self.temp = 100

    def update(self):

        self.i+=1
        if self.i > 4:
            self.i=0
        self.image=self.im[self.i]
        if self.temp > 0:
            self.temp -= 1
        self.rect.x += self.velx
        self.rect.y += self.vely
        if self.rect.x < 700:
            self.velx=0
        if self.rect.y < 20:
            self.vely= 3
        if self.rect.y > 300:
            self.vely=-3

        if self.vida > 0:
            pygame.draw.rect(pantalla, [200,0,0],[300,20, self.vida*3, 2])
        else:
            pygame.draw.rect(pantalla, [200,0,0],[300,20, -self.vida*3, 2])


class Rival4(pygame.sprite.Sprite): #Rival morado de Nivel 2 con bala apuntadora
    def __init__(self,p):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('png/ship6.png')
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=-2
        self.vely=0
        self.temp = 100
        self.vida = 2

    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        #para limitar el movimiento solo dentro de la pantalla
        if(self.rect.x > Ancho):
            self.velx = -1*self.velx
        if(self.rect.x < 0):
            self.velx = -1*self.velx
        if self.temp > 0:
            self.temp -= 1
        if(self.rect.y < 0):
            self.vely = -1*self.vely
        if(self.rect.y > Alto - 130):
            self.vely = -1*self.vely

class Rival3(pygame.sprite.Sprite):
    def __init__(self,p):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('png/Enemypro.png')
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=-2
        self.vely=0
        self.temp = 100
        self.vida = 2
        self.tb= 0
    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.tb+=1
        if self.tb > 3:
            self.tb=0
        if(self.rect.x > Ancho):
            self.velx = -1*self.velx
        if(self.rect.x < 0):
            self.velx = -1*self.velx
        if self.temp > 0:
            self.temp -= 1
        if(self.rect.y < 0):
            self.vely = -1*self.vely
        if(self.rect.y > Alto - 130):
            self.vely = -1*self.vely
        pantalla.blit(turbob[1][self.tb],[self.rect.x-30,self.rect.y+19])

class Rival2(pygame.sprite.Sprite):
    def __init__(self,p):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('png/nave2p.png')
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=0
        self.vely=1
        self.temp = 100
        self.vida = 2
    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        if(self.rect.x > Ancho): # linita al rival
            self.velx = -1*self.velx
        if(self.rect.x < 0):
            self.velx = -1*self.velx
        if self.temp > 0:
            self.temp -= 1
        if(self.rect.y < 0):
            self.vely = -1*self.vely
            self.image = pygame.image.load('png/nave2p.png') # cambia el sprite dependiendo de la direccion
        if(self.rect.y > Alto - 130):
            self.vely = -1*self.vely
            self.image = pygame.image.load('png/nave2.png')

class Rival(pygame.sprite.Sprite):
    def __init__(self,p,i):
        pygame.sprite.Sprite.__init__(self)
        self.image = i
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=1
        self.vely=2
        self.temp = 100
    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        if(self.rect.x > (Ancho - random.randint(1,50))): # linita al rival
            self.velx = -1*self.velx
        if(self.rect.x < 0):
            self.velx = -1*self.velx
        if(self.rect.y < 0):
            self.vely = -1*self.vely
        if(self.rect.y > Alto - 130):
            self.vely = -1*self.vely
        if self.temp > 0:
            self.temp -= 1

class Asteroid(pygame.sprite.Sprite):
    def __init__(self,p,i):
        pygame.sprite.Sprite.__init__(self)
        self.anim = 0
        self.image = Cut(0,self.anim,1,4,i,32,32) #recorta la imagen
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=2
        self.vely=-2
    def update(self):
        self.rect.x += self.velx
        self.rect.y += self.vely
        self.image = Cut(0,self.anim,1,4,E,32,32)
        if cont_cuadros%4 == 0: #para relentizar el cambio de sprites
            self.anim += 1
        if(self.rect.x > (Ancho + 100)):
            self.velx = -1*self.velx
        if(self.rect.x < -100):
            self.velx = -1*self.velx
        if(self.rect.y < -100):
            self.vely = -1*self.vely
        if(self.rect.y > Alto + 100):
            self.vely = -1*self.vely
        if self.anim > 3:
            self.anim = 0

class Bala(pygame.sprite.Sprite):
    def __init__(self,p,i):
        pygame.sprite.Sprite.__init__(self)
        self.image = i
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=1
        self.vely=1
        self.posj = j1.rect
        self.posm = posMause
        self.m = Direct(posMause,self.posj,15) #Retorna la posicion en x y y para en viar la vala
        self.ang = DirectAng(posMause,self.posj) #Retorna el angulo
    def update(self):
        self.rect.x += self.m[0]#usa la pendiente para enviar la bala
        self.rect.y += self.m[1]

class Gui(pygame.sprite.Sprite):
    def __init__(self,i):
        pygame.sprite.Sprite.__init__(self)
        self.m = 0
        self.image = i
        self.rect = self.image.get_rect()
        self.rect.x=0
        self.rect.y=Alto - 100

class BalaR(pygame.sprite.Sprite):
    def __init__(self,p):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('png/balar.png')
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=0
        self.vely=15

    def update(self):
        self.rect.y += self.vely
        self.rect.x += self.velx

class BalaB(pygame.sprite.Sprite):
    def __init__(self,p):
        pygame.sprite.Sprite.__init__(self)
        self.anim=0
        self.balab = [pygame.image.load('png/Boss2/bb1.png'),pygame.image.load('png/Boss2/bb2.png'),pygame.image.load('png/Boss2/bb3.png')]
        self.image = self.balab[self.anim]
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=0
        self.vely=0

    def update(self):
        self.anim+=1
        if self.anim > 2:
            self.anim=0
        self.image = self.balab[self.anim]

        self.rect.y += self.vely
        self.rect.x += self.velx

class PaqueteVida(pygame.sprite.Sprite):
    def __init__(self,p):
        pygame.sprite.Sprite.__init__(self)
        self.image = vida1
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=1
        self.vely=5
        self.g = 0.001
    def update(self):
        if self.rect.y < Alto - 125:
            self.rect.y += self.vely
            self.vely += self.g

class DobleDisparo(pygame.sprite.Sprite):
    def __init__(self,p):
        pygame.sprite.Sprite.__init__(self)
        self.image = doublet
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=1
        self.vely=5
        self.g = 0.001
    def update(self):
        if self.rect.y < Alto - 125:
            self.rect.y += self.vely
            self.vely += self.g

def Direct(pj, pr, vel):
    ang= math.atan2((pj[1]-pr[1]),(pj[0]-pr[0]))# se usa atan para simplificar y evitar error con la pendiente y la division sobre 0
    x=int(vel*math.cos(ang))#se pasa el coseno del angulo para hallar x
    y=int(vel*math.sin(ang))
    return ([x,y])

def DirectAng(pj, pr):
    ang= 95-1*math.degrees(math.atan2((pj[1]-pr[1]),(pj[0]-pr[0])))# se le resta 95 el angulo para evitar que halla un desface del angulo
    return (ang)

class Jugador(pygame.sprite.Sprite):
    def __init__(self,id,p,i):
        pygame.sprite.Sprite.__init__(self)
        self.id=id
        self.n=0
        self.im=i
        self.image = self.im[self.n]
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.velx=0
        self.vely=0
        self.super=False
        self.tb=0
        self.doblet=False
        self.vidas = 3
        self.ac=0.1
        self.lim=3
        self.sonido = pygame.mixer.Sound('ogg/exp.ogg')
        self.puntos = 0
        self.est=0 #en que direccion va a ir la nave

    def acelx(self,vel,ac,ban,lim): #aceleracion en x

        if vel > 0: #si la variable vel vale mas de 0 se acelera hacia la izquierda

            if self.velx < lim: #se pone una velocidad maxima de 5
                self.velx+=ac

        if vel < 0: #si la variable vel vale menos de 0 se acelera hacia la derecha

            if self.velx > -lim: #se pone una velocidad maxima de -5
                self.velx-=ac

        if vel == 0 and ban==True:
            self.velx=0

        if vel == 0 and ban==False: #si el jugador suelta los botones, se desacelera hasta llegar a 0

            if self.velx > 0: #si la velocidad esta por encima del 0, se le resta hasta llegar a cero
                self.velx-=ac

            if self.velx < 0: # si la velocidad esta por debajo del 0, se le suma hasta llegar a cero
                self.velx+=ac


    def acely(self,vel,ac,ban,lim): #aceleracion en y

        if vel > 0: #si la variable vel vale mas de 0 se acelera hacia arriba

            if self.vely < lim: #se pone una velocidad maxima de 5
                self.vely+=ac

        if vel < 0: #si la variable vel vale menos de 0 se acelera hacia abajo

            if self.vely > -lim: #se pone una velocidad maxima de -5
                self.vely-=ac

        if vel == 0 and ban==True:
            self.vely=0

        if vel == 0 and ban==False: #si el jugador suelta los botones, se desacelera hasta llegar a 0

            if self.vely > 0: #si la velocidad esta por encima del 0, se le resta hasta llegar a cero
                self.vely-=ac

            if self.vely < 0: # si la velocidad esta por debajo del 0, se le suma hasta llegar a cero
                self.vely+=ac

            if -1 < self.vely < 1:
                self.vely=0

    def update(self):
        self.tb+=1
        if self.super==True:
            self.n=1
            self.image=self.im[1]
            self.ac=0.3
            self.lim=6

        if self.vidas > 3 and self.super == False:
            self.vidas-=1
        if self.vidas > 6 and self.super == True:
            self.vidas-=1
        if self.tb > 3:
            self.tb=0

        if self.est == 1: #estado 1: la nave se va a dirigir hacia arriba
            self.acely(0.5,self.ac,self.super,self.lim)
            self.acelx(0,self.ac,self.super,self.lim)

        if self.est == 2: #estado 2: la nave se va a dirigir hacia arriba y derecha
            self.acely(0.5,self.ac,self.super,self.lim)
            self.acelx(0.5,self.ac,self.super,self.lim)

        if self.est == 3: #estado 3: la nave se va a dirigir hacia la derecha
            self.acelx(0.5,self.ac,self.super,self.lim)
            self.acely(0,self.ac,self.super,self.lim)

        if self.est == 4: #estado 4: la nave se va a dirigir hacia la derecha y abajo
            self.acelx(0.5,self.ac,self.super,self.lim)
            self.acely(-0.5,self.ac,self.super,self.lim)

        if self.est == 5: #estado 5: la nave se va a dirigir hacia abajo
            self.acely(-0.5,self.ac,self.super,self.lim)
            self.acelx(0,self.ac,self.super,self.lim)

        if self.est == 6: #estado 6: la nave se va a dirigir hacia abajo e izquierda
            self.acely(-0.5,self.ac,self.super,self.lim)
            self.acelx(-0.5,self.ac,self.super,self.lim)

        if self.est == 7: #estado 7: la nave se va a dirigir hacia la izquierda
            self.acelx(-0.5,self.ac,self.super,self.lim)
            self.acely(0,self.ac,self.super,self.lim)

        if self.est == 8: #estado 8: la nave se va a dirigir hacia la izquierda y arriba
            self.acelx(-0.5,self.ac,self.super,self.lim)
            self.acely(0.5,self.ac,self.super,self.lim)

        if self.est == 0: #estado 0: la nave va a desacelerar hasta quedarse quieta
            self.acelx(0,self.ac,self.super,self.lim)
            self.acely(0,self.ac,self.super,self.lim)

        self.rect.x += self.velx
        self.rect.y -= self.vely
        if (self.rect.x > (Ancho )):
            self.rect.x = Ancho
            self.velx=0
            self.vely=0
        if (self.rect.x < 0):
            self.rect.x = 0
            self.velx=0
            self.vely=0
        if (self.rect.y > (Alto - 150 )):
            self.rect.y = Alto - 150
            self.velx=0
            self.vely=0
        if (self.rect.y < -20):
            self.rect.y = -20
            self.velx=0
            self.vely=0
        pantalla.blit(turbob[0][self.tb],[self.rect.x-5,self.rect.y+19])

def Cut(F,C,Tx,Ty,img,tamx,tamy):
    """
    	F: Fila a cortar
		C: Columna a cortar
		Tx: Tamanio de columnas de imagen
		Ty: Tamanio de filas de imagen
		img: Imagen a cortar
		tam:tamanioo de recorte 32 x 32 o 64 x 64
    """
    Mat=[]
    for h in range (Tx):
        ls = []
        for i in range (Ty):
            cuadro = img.subsurface(tamx*h,tamy*i,tamx,tamy)
            ls.append(cuadro)
        Mat.append(ls)
    cuadro = Mat[F][C]
    return cuadro

def ShowMenu(men):
    if men == 1:
        fondo1 = pygame.image.load('png/1.png')
        fondo2 = pygame.image.load('png/4.png')
        playf = pygame.image.load('png/playunp.png')
        playn = pygame.image.load('png/playp.png')
        quitf = pygame.image.load('png/quitunp.png')
        quitn = pygame.image.load('png/quitp.png')
        mouse = pygame.mouse.get_pos()
        pantalla.blit(fondo1,[0,0])
        if 100+183 > mouse[0] > 100 and 300+93 > mouse[1] > 300:
            pantalla.blit(playn,[100,300])
        else:
            pantalla.blit(playf,[100,300])

        if 300+192 > mouse[0] > 300 and 305+102 > mouse[1] > 305:
            pantalla.blit(quitn,[300,305])
        else:
            pantalla.blit(quitf,[300,305])


        men = 0

class Punto(pygame.sprite.Sprite):#La clase del recolectable para aumentar puntos
    def __init__(self,p):
        pygame.sprite.Sprite.__init__(self)
        C = [0,255,0]
        self.image = pygame.image.load('png/puntos.png')
        self.rect = self.image.get_rect()
        self.rect.x=p[0]
        self.rect.y=p[1]
        self.vely = 1
        self.g = 0.001
    def update(self):
        if self.rect.y < Alto - 125:
            self.rect.y += self.vely
            self.vely += self.g
        if self.rect.y >= (Alto - self.rect.height):
            self.rect.y = Alto - self.rect.height

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])
    segundo = 0
    animy = 0
    men = 1
    Mx = 0
    My = 0
    BossCan = True
    CanVertical = False
    CanHorizontal2 = False
    CanHorizontal1 = True
    asteroides = True
    rival = True
    ttt = True
    rival2 = True
    rival3 = True
    baalasr = True
    Colision = False
    segundol = False

##################################################Zona Preparacion Nivel 1##########################################################################################

    mapa = configparser.ConfigParser()
    mapa.read('mapa.map')
    cad_map=mapa.get('info','mapa')
    ls_mapa = cad_map.split('\n')
    pos_fila = 0
    an_corte=32
    end = False
    printf = 0
    printc = 0
    canFire = True
    cont_cuadros=0
    tasa_cuadros=60

    turbob = [[pygame.image.load('png/turbo/21.png'),pygame.image.load('png/turbo/22.png'),pygame.image.load('png/turbo/23.png'),pygame.image.load('png/turbo/24.png')],[pygame.image.load('png/turbo/11.png'),pygame.image.load('png/turbo/12.png'),pygame.image.load('png/turbo/13.png'),pygame.image.load('png/turbo/14.png')]]
    niv1 = pygame.image.load('png/nivel1.png')
    niv2 = pygame.image.load('png/nivel2.png')
    gov = pygame.image.load('png/gov.png')
    vida1 = pygame.image.load('png/vida.png')
    balar = pygame.image.load('png/balab.png')
    playf = pygame.image.load('png/playunp.png')
    playn = pygame.image.load('png/playp.png')
    tienda = [pygame.image.load('png/store/tienda.png'),pygame.image.load('png/store/buyu.png'),pygame.image.load('png/store/buyp.png'), [pygame.image.load('png/store/1s.png'),pygame.image.load('png/store/3s.png'),pygame.image.load('png/store/4s.png'),pygame.image.load('png/store/5s.png'),pygame.image.load('png/store/6s.png'), pygame.image.load('png/store/7s.png'),pygame.image.load('png/store/8s.png'),pygame.image.load('png/store/9s.png'),pygame.image.load('png/store/10s.png'),pygame.image.load('png/store/11s.png'),pygame.image.load('png/store/12s.png'),pygame.image.load('png/store/13s.png'),pygame.image.load('png/store/14s.png')]]

    ticon = 0
    stein = 0


    sound = pygame.mixer.Sound('ogg/musica.ogg')
    sound2 = pygame.mixer.Sound('ogg/Space.ogg')
    Points = pygame.mixer.Sound('ogg/coin.ogg')
    crash = pygame.mixer.Sound('ogg/crash.ogg')

    balas = pygame.sprite.Group()
    rivales = pygame.sprite.Group()
    rivales2 = pygame.sprite.Group()
    rivales3 = pygame.sprite.Group()
    rivales4 = pygame.sprite.Group()
    torretas = pygame.sprite.Group()
    paquetesv = pygame.sprite.Group()
    doublets = pygame.sprite.Group()

    Torret = pygame.sprite.Group()
    Boses = pygame.sprite.Group()
    VidaBoses = pygame.sprite.Group()

    balas_r = pygame.sprite.Group()
    balas_b = pygame.sprite.Group()
    jugadores = pygame.sprite.Group()
    Guis = pygame.sprite.Group()
    Puntos = pygame.sprite.Group()
    Asteroids = pygame.sprite.Group()

    doublet = pygame.image.load('png/DT.png')
    player = [pygame.image.load('png/Nave.png'),pygame.image.load('png/Nave22.png')]
    enemy = pygame.image.load('png/nave1.png')
    enemy2 = pygame.image.load('png/nave2p.png')
    enemy3 = pygame.image.load('png/Enemypro.png')
    enemy4 = pygame.image.load('png/ship6.png')
    fondo1 = pygame.image.load('png/Back.png')
    fondo2 = pygame.image.load('png/BackVert.png')
    fondo3 = pygame.image.load('png/final.png')
    #fondo1 = pygame.transform.scale(fondo1,[Ancho*3,Alto*3])
    #fondo2 = pygame.transform.scale(fondo2,[Ancho*3,510])


    G = pygame.image.load('png/tablero.png')
    E = pygame.image.load('png/asteroid.png')

    reloj = pygame.time.Clock()
    j1 = Jugador(1,[20,Alto/2],player)

    jugadores.add(j1)
    gui = Gui(G)
    Guis.add(gui)
    sound.play()

    NR = 2
    NR3 = 1
    NR4 = 1

    lim = 120
    fuente = pygame.font.Font(None,32)

############################################ Crea enemigos y esteroides ###################################################################


     #Boss PAra Testear Al inicio
    #B=Bouse([1000,100])
    #Boses.add(B)






#############################################################################################################################################
    while not end:
        segundo = cont_cuadros // tasa_cuadros
        seg_actual = lim - segundo
        #print(segundo)
        for (event) in pygame.event.get():
            if event.type == pygame.QUIT:
                end=True
            if event.type == pygame.MOUSEBUTTONUP:
                canFire = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                    posMause = event.pos
                    b = Bala([j1.rect.x-10,j1.rect.y-5],balar)
                    img = pygame.transform.rotate(balar,b.ang)
                    b.image = img
                    balas.add(b)
                    if j1.doblet == True:
                        b = Bala([j1.rect.x-30,j1.rect.y-15],balar)
                        img = pygame.transform.rotate(balar,b.ang)
                        b.image = img
                        balas.add(b)
            if event.type == pygame.KEYUP: #se revisa el evento de levantar las teclas
                keys = pygame.key.get_pressed() #se genera una variable keys para que guarde que teclas se presionaron del teclado
                if keys.count(1) == 1: #se revisa el numero de teclas pulsadas
                    j1.est=0 #se cambia al estado 0 para dejar quieto al jugador


            #if event.type == pygame.KEYDOWN: #se revisa el evento de presionar una tecla

            keys = pygame.key.get_pressed() #se genera una variable keys para que guarde las teclase que presiona en el teclado
            if keys.count(1) == 3: #se revisa si hay dos teclas presionadas

                if keys[pygame.K_w] and keys[pygame.K_d]: #se revisa si se presiona hacia arriba y derecha
                    j1.est=2 #pasa al estado 2 para acelerar hacia arriba y derecha

                if keys[pygame.K_d] and keys[pygame.K_s]: #se revisa si se presiona hacia abajo y derecha
                    j1.est=4 #pasa al estado 4 para acelerar hacia abajo y derecha

                if keys[pygame.K_s] and keys[pygame.K_a]: #se revisa si se presiona hacia abajo e izquierda
                    j1.est=6 #pasa al estado 6 para acelerar hacia abajo e izquierda

                if keys[pygame.K_w] and keys[pygame.K_a]: #se revisa si se presiona hacia arriba e izquierda
                    j1.est=8 #pasa al estado 8 para acelerar hacia arriba e izquierda

            if keys.count(1) == 2: #se revisa si se presiona una tecla nada mas

                if keys[pygame.K_w]:#se revisa si se presiona hacia arriba
                    j1.est=1 #se pasa al estado 1 para acelerar hacia arriba

                if keys[pygame.K_s]:#se revisa si se presiona hacia abajo
                    j1.est=5 #se pasa al estado 5 que es acelerar hacia abajo

                if keys[pygame.K_d]:#se revisa si se presiona hacia la derecha
                    j1.est=3 #se pasa al estado 3 que es acelerar hacia la derecha

                if keys[pygame.K_a]:#se revisa si se presiona hacia la izquierda
                    j1.est=7 #se pasa al estado 7 que es acelerar hacia la izquierda
        if event.type == pygame.K_SPACE:
            men += 1




#################################################### Menu ##########################################################################################################
        if(men == 1):
            j1.doblet = False
            ShowMenu(men)
            if event.type == pygame.MOUSEBUTTONDOWN:

                p = event.pos
                if 300+192 > p[0] > 300 and 305+102 > p[1] > 305:
                    end = True

                if 100+183 > p[0] > 100 and 300+93 > p[1] > 300:
                    sound.stop()
                    inicio()
                    for p in Puntos:
                        Puntos.remove(p)
                    men = 1.5



#####################################################Nivel1########################################################################################
        if(men == 1.5):
            pantalla.fill(NEGRO)
            pantalla.blit(niv1,[500,300])
            pygame.display.flip()
            pygame.time.wait(1200)
            j1.rect.x=10
            j1.rect.y=Alto/2
            men = 2

        if(men == 2):
##################################### Probabilidad de Spawn enemigos ##############################################################

            if ttt == True:
                si_torreta = random.randrange(100)
                if si_torreta > 99:
                    e=Torreta([0,0])
                    e.rect.x = 1000
                    e.rect.y = 442
                    torretas.add(e)

            if rival == True:


                si_enemy = random.randrange(100)
                if si_enemy > 98:
                    e=Rival3([0,0])
                    e.rect.x = Ancho - random.randrange(50)
                    e.rect.y = random.randrange(400)
                    rivales3.add(e)



                si_enemy2 = random.randrange(100)
                if si_enemy2 > 98:
                    e = Rival([20,20],enemy)
                    e2 = Rival2([20,20])
                    e.rect.x = random.randrange(Ancho - e.rect.width)
                    e.rect.y = 0
                    rivales.add(e)
                    e2.rect.x = random.randrange(Ancho - e2.rect.width)
                    e2.rect.y = 0
                    rivales2.add(e2)
########################################## Fondo y parallax TIpo Z #########################################################################
            pantalla.fill([0,0,0])
            if(CanHorizontal1): # Primera parte Horizontal
                pantalla.blit(fondo1,[Mx,0])
                if Mx > -5200:
                    Mx -= 3
                if Mx < -4000:
                    CanHorizontal1 = False
                    CanVertical = True
            if(CanVertical): # Segunda Parte Vertical
                pantalla.blit(fondo1,[Mx,My])
                pantalla.blit(fondo2,[0,My])
                ttt = False
                torretas.empty()
                if My > -4600:
                    My -= 3
                if My < -4500:
                    CanVertical = False
                    CanHorizontal2 = True
                    My=0
            if(CanHorizontal2): # Tercera Parte Vertocal
                pantalla.blit(fondo3,[0,My])
                if My > -400:
                    My -= 3
                if My < -300:
                    if BossCan: # Crea el Boss DEl nivel 1
                        B = Bouse([1000,100])
                        Boses.add(B)
                        BossCan = False

########################################## balas de rivales ##########################################################################################

            ################## probabilidad de que disparen###############
            if baalasr == True:
                for r in Boses:
                    if r.temp <= 0:
                        b = BalaB([r.rect.x+100,r.rect.y+201])
                        vel=Direct(j1.rect, [r.rect.x+100,r.rect.y+201],10)
                        ang=DirectAng([r.rect.x+100,r.rect.y+201], j1.rect)
                        nimg=pygame.transform.rotate(b.image,ang)
                        b.image=nimg
                        b.velx=vel[0]
                        b.vely=vel[1]
                        balas_r.add(b)
                        r.temp=random.randrange(400)

                for r in torretas:
                    if r.temp <= 0:
                        b = BalaR([r.rect.x,r.rect.y])
                        vel=Direct(j1.rect, [r.rect.x,r.rect.y],10)
                        ang=DirectAng([r.rect.x,r.rect.y], j1.rect)
                        nimg=pygame.transform.rotate(b.image,ang)
                        b.image=nimg
                        b.velx=vel[0]
                        b.vely=vel[1]
                        balas_r.add(b)
                        r.temp=random.randrange(400)


                for r in rivales2:
                    if r.temp <= 0:
                        b = BalaR([r.rect.x,r.rect.y])
                        b.vely=2
                        balas_r.add(b)
                        r.temp=random.randrange(800)


            #si las balas del jugador colisionan con los rivales
            for b in balas:
                ls_col= pygame.sprite.spritecollide(b,rivales,True)
                ls_col2 = pygame.sprite.spritecollide(b,rivales2,True)
                ls_col3 = pygame.sprite.spritecollide(b,rivales3,False)
                ls_col4 = pygame.sprite.spritecollide(b,Boses,False)
                for i in ls_col3:
                    si_vida = random.randrange(300)
                    si_double = random.randrange(300)
                    j1.sonido.play()
                    balas.remove(b)
                    expl(b.rect)

                    if i.vida < 0:
                        rivales3.remove(i)
                        if si_vida < 30:
                            l=PaqueteVida([i.rect.x,i.rect.y]) # aparicion de paquete de vida con Probabilidad
                            paquetesv.add(l)
                        if si_double < 20:
                            d = DobleDisparo([i.rect.x,i.rect.y])#aparicion de doble tiro
                            doublets.add(d)
                    else:
                        i.vida -= 1

                for i in ls_col4:
                    si_vida = random.randrange(300)
                    si_double = random.randrange(300)
                    j1.sonido.play()
                    balas.remove(b)
                    expl(b.rect)

                    if i.vida < 0:
                        Boses.remove(i)
                        segundol=True
                        if si_vida < 30:
                            l=PaqueteVida([i.rect.x,i.rect.y]) # aparicion de paquete de vida con Probabilidad
                            paquetesv.add(l)
                        if si_double < 20:
                            d = DobleDisparo([i.rect.x,i.rect.y])#aparicion de doble tiro
                            doublets.add(d)
                    else:
                        i.vida -= 2




                for i in ls_col:
                    expl(b.rect)
                    prob_puntos = random.randrange(800)
                    if prob_puntos>200:
                        p = Punto([i.rect.x,i.rect.y])
                        Puntos.add(p)
                    balas.remove(b)
                    j1.sonido.play()
                for i in ls_col2:
                    expl(b.rect)
                    balas.remove(b)
                    j1.sonido.play()

            # colisiones con el jugador
            if Colision == True:
                for j in jugadores:
                    ls_colj = pygame.sprite.spritecollide(j,Puntos,True)
                    for i in ls_colj:
                        Points.play()
                        j1.puntos += 1
                    ls_cap2 = pygame.sprite.spritecollide(j,paquetesv,True)
                    for v in ls_cap2:
                        if j.vidas < 4:
                            j.vidas += 1
                    ls_cap22 = pygame.sprite.spritecollide(j,doublets,True)
                    for y in ls_cap22:
                        j.doblet = True
                        j.n= 1
                    ls_col4= pygame.sprite.spritecollide(j,balas_r,True)
                    for c in ls_col4:
                        j.vidas -= 1
                        crash.play()
                    ls_col5 = pygame.sprite.spritecollide(j,rivales,True)
                    for c in ls_col5:
                        j.vidas -= 1
                        crash.play()
                    ls_col6 = pygame.sprite.spritecollide(j,rivales2,True)
                    for c in ls_col6:
                        j.vidas -= 1
                        crash.play()
                    ls_col7 = pygame.sprite.spritecollide(j,rivales3,True)
                    for c in ls_col7:
                        j.vidas -= 1
                        crash.play()
                    ls_col8 = pygame.sprite.spritecollide(j,Asteroids,True)
                    for c in ls_col8:
                        j.vidas -= 1
                        crash.play()
                    ls_col9 = pygame.sprite.spritecollide(j,rivales4,True)
                    for c in ls_col9:
                        j.vidas -= 1
                        crash.play()

            ##### si las balas se salen
            for s in balas:
                if not(-100 < s.rect.x < 1000 and -100 < s.rect.y < 500):
                    balas.remove(s)
            for s in balas_r:
                if not(-100 < s.rect.x < 1000 and -100 < s.rect.y < 500):
                    balas_r.remove(s)
            for s in balas_b:
                if not(-100 < s.rect.x < 1000 and -100 < s.rect.y < 500):
                    balas_b.remove(s)
#################################### Zona Updates #####################################################################################
            jugadores.update()
            balas.update()
            torretas.update()
            balas_r.update()
            balas_b.update()
            rivales.update()
            rivales2.update()
            rivales3.update()
            paquetesv.update()
            doublets.update()

            Boses.update()
            VidaBoses.update()

            Guis.update()
            Puntos.update()
            Asteroids.update()
##################################### Zona Draws #########################################################################################

            Boses.draw(pantalla)
            torretas.draw(pantalla)
            VidaBoses.draw(pantalla)
            balas_r.draw(pantalla)
            balas_b.draw(pantalla)
            doublets.draw(pantalla)
            Puntos.draw(pantalla)
            jugadores.draw(pantalla)

            balas.draw(pantalla)
            paquetesv.draw(pantalla)

            rivales.draw(pantalla)
            rivales2.draw(pantalla)
            rivales3.draw(pantalla)

            Asteroids.draw(pantalla)
            Guis.draw(pantalla)


#####################Dibujo de Vida en pantalla##################
            if j1.vidas > 0:
                pantalla.blit(vida1,[30,540])
            if j1.vidas > 1:
                pantalla.blit(vida1,[30,560])
            if j1.vidas > 2:
                pantalla.blit(vida1,[30,580])
            if j1.vidas > 3:
                pantalla.blit(vida1,[10,540])
            if j1.vidas > 4:
                pantalla.blit(vida1,[10,560])
            if j1.vidas > 5:
                pantalla.blit(vida1,[10,580])

############## Tecla para acceder a la tienda#############
            if keys[pygame.K_t]:
                men = 5
            if keys[pygame.K_i]:
                men = 2.5


############# Control del Game Over  ##################
            if j1.vidas < 0:
                pantalla.fill(NEGRO)
                pantalla.blit(gov,[500,300])
                pygame.display.flip()
                pygame.time.wait(1200)
                pantalla.fill(NEGRO)
                texto3 = fuente.render("Puntos",False,[255,255,255])
                pantalla.blit(texto3,[500,250])
                texto2 = fuente.render(str(j1.puntos),False,[255,255,255])
                pantalla.blit(texto2,[500,300])
                pygame.display.flip()
                pygame.time.wait(1200)
                men = 1
                empe()

            texto2 = fuente.render(str(j1.puntos),False,[255,255,255])
            pantalla.blit(texto2,[Ancho-100,Alto-70])
##################################### Zona Tiempo #############################################################################
            if seg_actual > 0:
                cont_cuadros+=1

            texto = fuente.render(str(seg_actual),False,[255,255,255])
            pantalla.blit(texto,[Ancho-100,Alto-90])

##################Paso al siguiente Nivel#########################


        if(men == 2.5 or segundol == True):

            empe()
            pantalla.fill(NEGRO)
            pantalla.blit(niv2,[500,300])
            pygame.display.flip()
            pygame.time.wait(1200)
            inicio()
            Mx = 0
            My = 0
            j1.rect.x = 50
            j1.rect.y =Alto/2
            j1.vidas = 3
            men = 3

##################################### TIENDA #############################################

        if(men == 5):
            pantalla.blit(tienda[3][ticon],[0,0])
            stein+=1
            if (stein % 20) == 0:
                ticon +=1
            if ticon > 12:
                print(j.vidas,j.puntos)
                ticon=0
                stein=0
            pantalla.blit(tienda[0],[0,0])
            pantalla.blit(tienda[1],[560,224])
            mouse = pygame.mouse.get_pos()
            mouseb = pygame.mouse.get_pressed()

            #para comprar vida
            if 560+100 > mouse[0] > 560 and 100+62 > mouse[1] > 100:
                pantalla.blit(tienda[2],[560,100])
                if mouseb[0] == 1 and not((j1.puntos - 5) < 0):
                    if j.super == True and j.vidas < 6:
                        j1.puntos=j1.puntos-5
                        j1.vidas=j1.vidas+1
                    if j.super == False and j.vidas < 2:
                        j1.puntos=j1.puntos-5
                        j1.vidas=j1.vidas+1
                    pygame.time.wait(100)
            else:
                pantalla.blit(tienda[1],[560,100])

            #para comprar la doble bala
            if 560+100 > mouse[0] > 560 and 162+62 > mouse[1] > 162:
                pantalla.blit(tienda[2],[560,162])
                if mouseb[0] == 1:
                    j1.doblet= True
                    j1.puntos= j1.puntos - 10
                    pygame.time.wait(100)
            else:
                pantalla.blit(tienda[1],[560,162])

            #para comprar la mejora de la nave
            if 560+100 > mouse[0] > 560 and 224+62 > mouse[1] > 224:
                pantalla.blit(tienda[2],[560,224])
                if mouseb[0] == 1:
                    j1.super=True
                    j1.puntos= j1.puntos - 20
                    pygame.time.wait(100)
            else:
                pantalla.blit(tienda[1],[560,224])

            if 100+183 > mouse[0] > 100 and 500+93 > mouse[1] > 500:
                pantalla.blit(playn,[100,500])
                if mouseb[0] == 1:
                    if segundol == True:
                        men =3
                    else:
                        men=2
            else:
                pantalla.blit(playf,[100,500])

            pygame.display.flip()



###################################### Nivel 3 #######################################################################################
        if(men == 3):
##################################### Probabilidad de Spawn enemigos ##############################################################

            if ttt == True:
                si_torreta = random.randrange(100)
                if si_torreta > 98:
                    e=Torreta([0,0])
                    e.rect.x = 1000
                    e.rect.y = 442
                    torretas.add(e)

            if rival == True:

                si_enemy3 = random.randrange(800)
                if si_enemy3 > 790:
                    h=Rival4([0,0])
                    h.rect.x = Ancho - random.randrange(50)
                    h.rect.y = random.randrange(400)
                    rivales4.add(h)
                    si_enemy = random.randrange(100)

                si_enemy = random.randrange(100)
                if si_enemy > 98:
                    e=Rival3([0,0])
                    e.rect.x = Ancho - random.randrange(50)
                    e.rect.y = random.randrange(400)
                    rivales3.add(e)



                si_enemy2 = random.randrange(100)
                if si_enemy2 > 98:
                    e = Rival([20,20],enemy)
                    e2 = Rival2([20,20])
                    e.rect.x = random.randrange(Ancho - e.rect.width)
                    e.rect.y = 0
                    rivales.add(e)
                    e2.rect.x = random.randrange(Ancho - e2.rect.width)
                    e2.rect.y = 0
                    rivales2.add(e2)
########################################## Fondo y parallax TIpo Z #########################################################################
            pantalla.fill([0,0,0])
            if(CanHorizontal1): # Primera parte Horizontal
                pantalla.blit(fondo1,[Mx,0])
                if Mx > -5200:
                    Mx -= 3
                if Mx < -4000:
                    CanHorizontal1 = False
                    CanVertical = True
            if(CanVertical): # Segunda Parte Vertical
                pantalla.blit(fondo1,[Mx,My])
                pantalla.blit(fondo2,[0,My])
                ttt = False
                torretas.empty()
                if My > -4600:
                    My -= 3
                if My < -4500:
                    CanVertical = False
                    CanHorizontal2 = True
                    My=0
            if(CanHorizontal2): # Tercera Parte Vertocal
                pantalla.blit(fondo3,[0,My])
                if My > -400:
                    My -= 3
                if My < -300:
                    if BossCan: # Crea el Boss DEl nivel 1
                        B = Bouse([1000,100])
                        Boses.add(B)
                        B.vida = 200
                        BossCan = False

########################################## balas de rivales ##########################################################################################

            ################## probabilidad de que disparen###############


            if baalasr == True:
                for r in rivales4:
                    if r.temp <= 0:
                        b = BalaR([r.rect.x,r.rect.y])
                        vel=Direct(j1.rect, r.rect,5)
                        ang=DirectAng(r.rect, j1.rect)
                        nimg=pygame.transform.rotate(b.image,ang)
                        b.image=nimg

                        b.velx=vel[0]
                        b.vely=vel[1]
                        balas_r.add(b)
                        r.temp=random.randrange(800)

                for r in Boses:
                    if r.temp <= 0:
                        b = BalaB([r.rect.x+100,r.rect.y+201])
                        vel=Direct(j1.rect, [r.rect.x+100,r.rect.y+201],10)
                        ang=DirectAng([r.rect.x+100,r.rect.y+201], j1.rect)
                        nimg=pygame.transform.rotate(b.image,ang)
                        b.image=nimg
                        b.velx=vel[0]
                        b.vely=vel[1]
                        balas_r.add(b)
                        r.temp=random.randrange(200)

                for r in torretas:
                    if r.temp <= 0:
                        b = BalaR([r.rect.x,r.rect.y])
                        vel=Direct(j1.rect, [r.rect.x,r.rect.y],10)
                        ang=DirectAng([r.rect.x,r.rect.y], j1.rect)
                        nimg=pygame.transform.rotate(b.image,ang)
                        b.image=nimg
                        b.velx=vel[0]
                        b.vely=vel[1]
                        balas_r.add(b)
                        r.temp=random.randrange(400)


                for r in rivales2:
                    if r.temp <= 0:
                        b = BalaR([r.rect.x,r.rect.y])
                        b.vely=2
                        balas_r.add(b)
                        r.temp=random.randrange(800)


            #si las balas del jugador colisionan con los rivales
            for b in balas:
                ls_col= pygame.sprite.spritecollide(b,rivales,True)
                ls_col2 = pygame.sprite.spritecollide(b,rivales2,True)
                ls_col3 = pygame.sprite.spritecollide(b,rivales3,False)
                ls_col4 = pygame.sprite.spritecollide(b,Boses,False)
                ls_col5 = pygame.sprite.spritecollide(b,rivales4,False)
                for i in ls_col3:
                    si_vida = random.randrange(300)
                    si_double = random.randrange(300)
                    j1.sonido.play()
                    balas.remove(b)
                    expl(b.rect)

                    if i.vida < 0:
                        rivales3.remove(i)
                        if si_vida < 30:
                            l=PaqueteVida([i.rect.x,i.rect.y]) # aparicion de paquete de vida con Probabilidad
                            paquetesv.add(l)
                        if si_double < 20:
                            d = DobleDisparo([i.rect.x,i.rect.y])#aparicion de doble tiro
                            doublets.add(d)
                    else:
                        i.vida -= 1

                for i in ls_col5:
                    si_vida = random.randrange(300)
                    si_double = random.randrange(300)
                    j1.sonido.play()
                    balas.remove(b)
                    expl(b.rect)

                    if i.vida < 0:
                        rivales4.remove(i)
                        if si_vida < 30:
                            l=PaqueteVida([i.rect.x,i.rect.y]) # aparicion de paquete de vida con Probabilidad
                            paquetesv.add(l)
                        if si_double < 20:
                            d = DobleDisparo([i.rect.x,i.rect.y])#aparicion de doble tiro
                            doublets.add(d)
                    else:
                        i.vida -= 1
                for i in ls_col4:
                    si_vida = random.randrange(300)
                    si_double = random.randrange(300)
                    j1.sonido.play()
                    balas.remove(b)
                    expl(b.rect)

                    if i.vida < 0:
                        Boses.remove(i)
                        men=6
                        if si_vida < 30:
                            l=PaqueteVida([i.rect.x,i.rect.y]) # aparicion de paquete de vida con Probabilidad
                            paquetesv.add(l)
                        if si_double < 20:
                            d = DobleDisparo([i.rect.x,i.rect.y])#aparicion de doble tiro
                            doublets.add(d)
                    else:
                        i.vida -= 2




                for i in ls_col:
                    expl(b.rect)
                    prob_puntos = random.randrange(800)
                    if prob_puntos>200:
                        p = Punto([i.rect.x,i.rect.y])
                        Puntos.add(p)
                    balas.remove(b)
                    j1.sonido.play()
                for i in ls_col2:
                    expl(b.rect)
                    balas.remove(b)
                    j1.sonido.play()

            # colisiones con el jugador
            if Colision == True:
                for j in jugadores:
                    ls_colj = pygame.sprite.spritecollide(j,Puntos,True)
                    for i in ls_colj:
                        Points.play()
                        j1.puntos += 1
                    ls_cap2 = pygame.sprite.spritecollide(j,paquetesv,True)
                    for v in ls_cap2:
                        if j.vidas < 4:
                            j.vidas += 1
                    ls_cap22 = pygame.sprite.spritecollide(j,doublets,True)
                    for y in ls_cap22:
                        j.doblet = True
                        j.n= 1
                    ls_col4= pygame.sprite.spritecollide(j,balas_r,True)
                    for c in ls_col4:
                        j.vidas -= 1
                        crash.play()
                    ls_col5 = pygame.sprite.spritecollide(j,rivales,True)
                    for c in ls_col5:
                        j.vidas -= 1
                        crash.play()
                    ls_col6 = pygame.sprite.spritecollide(j,rivales2,True)
                    for c in ls_col6:
                        j.vidas -= 1
                        crash.play()
                    ls_col7 = pygame.sprite.spritecollide(j,rivales3,True)
                    for c in ls_col7:
                        j.vidas -= 1
                        crash.play()
                    ls_col8 = pygame.sprite.spritecollide(j,Asteroids,True)
                    for c in ls_col8:
                        j.vidas -= 1
                        crash.play()
                    ls_col9 = pygame.sprite.spritecollide(j,rivales4,True)
                    for c in ls_col9:
                        j.vidas -= 1
                        crash.play()

            ##### si las balas se salen
            for s in balas:
                if not(-100 < s.rect.x < 1000 and -100 < s.rect.y < 500):
                    balas.remove(s)
            for s in balas_r:
                if not(-100 < s.rect.x < 1000 and -100 < s.rect.y < 500):
                    balas_r.remove(s)
            for s in balas_b:
                if not(-100 < s.rect.x < 1000 and -100 < s.rect.y < 500):
                    balas_b.remove(s)
#################################### Zona Updates #####################################################################################
            jugadores.update()
            balas.update()
            torretas.update()
            balas_r.update()
            balas_b.update()
            rivales.update()
            rivales2.update()
            rivales3.update()
            rivales4.update()
            paquetesv.update()
            doublets.update()

            Boses.update()
            VidaBoses.update()

            Guis.update()
            Puntos.update()
            Asteroids.update()
##################################### Zona Draws #########################################################################################

            Boses.draw(pantalla)
            torretas.draw(pantalla)
            VidaBoses.draw(pantalla)
            balas_r.draw(pantalla)
            balas_b.draw(pantalla)
            doublets.draw(pantalla)
            Puntos.draw(pantalla)
            jugadores.draw(pantalla)

            balas.draw(pantalla)
            paquetesv.draw(pantalla)

            rivales.draw(pantalla)
            rivales2.draw(pantalla)
            rivales3.draw(pantalla)
            rivales4.draw(pantalla)

            Asteroids.draw(pantalla)
            Guis.draw(pantalla)


#####################Dibujo de Vida en pantalla##################
            if j1.vidas > 0:
                pantalla.blit(vida1,[30,540])
            if j1.vidas > 1:
                pantalla.blit(vida1,[30,560])
            if j1.vidas > 2:
                pantalla.blit(vida1,[30,580])
            if j1.vidas > 3:
                pantalla.blit(vida1,[10,540])
            if j1.vidas > 4:
                pantalla.blit(vida1,[10,560])
            if j1.vidas > 5:
                pantalla.blit(vida1,[10,580])

############## Tecla para acceder a la tienda#############
            if keys[pygame.K_t]:
                men = 5


############# Control del Game Over  ##################
            if j1.vidas < 0 or men==6:
                pantalla.fill(NEGRO)
                pantalla.blit(gov,[500,300])
                pygame.display.flip()
                pygame.time.wait(1200)
                pantalla.fill(NEGRO)
                texto3 = fuente.render("Puntos",False,[255,255,255])
                pantalla.blit(texto3,[500,250])
                texto2 = fuente.render(str(j1.puntos),False,[255,255,255])
                pantalla.blit(texto2,[500,300])
                pygame.display.flip()
                pygame.time.wait(1200)
                men = 1
                empe()

            texto2 = fuente.render(str(j1.puntos),False,[255,255,255])
            pantalla.blit(texto2,[Ancho-100,Alto-70])
##################################### Zona Tiempo #############################################################################
            if seg_actual > 0:
                cont_cuadros+=1

            texto = fuente.render(str(seg_actual),False,[255,255,255])
            pantalla.blit(texto,[Ancho-100,Alto-90])



        pygame.display.flip()
        reloj.tick(tasa_cuadros)
