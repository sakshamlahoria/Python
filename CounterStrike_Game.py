from pygame import mixer
mixer.init()
class cs():
    life=100
    ammo=100
    sm=0
    gren=0
    missile=0
    shoot=0
    healthkit=0
    medikit=0
    shotgun=0
    head=0
    def __init__(self):
        mixer.music.load(r"C:\Users\saksham\Desktop\theme.mp3")

        mixer.music.play()
        print('hello i am counter terrorist')
    def shoot1(self):
        if self.ammo > 0 and self.life > 0:
            mifrom pygame import mixer
mixer.init()
class cs():
    life=100
    ammo=100
    sm=0
    gren=0
    missile=0
    shoot=0
    healthkit=0
    medikit=0
    shotgun=0
    head=0
    def __init__(self):
        mixer.music.load(r"C:\Users\saksham\Desktop\theme.mp3")

        mixer.music.play()
        print('hello i am counter terrorist')
    def shoot1(self):
        if self.ammo > 0 and self.life > 0:
            mixer.music.load(r"C:\Users\saksham\Desktop\cs.mp3")
            mixer.music.play()
            self.ammo-=1
            self.life-=1
            print('ammo')
            print(self.ammo)
        else:
            print('dead')
            mixer.music.stop()

    def health(self):
        print(self.life)

    def gun(self):
        if self.life>0:
            self.ammo=100

    def medikit1(self):
        if self.life>0 and self.life<80 :
            self.life+=20
        else:
            a=100-self.life
            self.life+=a
            print('medikit1')
            print(self.life)

    def missile1(self):
        if self.life>0:
           self.missile+=1
           print('missile')
           print(self.missile)
        else:
            print('dead')

    def grenade(self):
        if self.life>0:
            self.gren+=1
            print('grenade')
            print(self.gren)
        else:
            print('dead')
    def shootmisile(self):
        mixer.music.load(r'C:\Users\saksham\Desktop\missile.mp3')
        mixer.music.play()
        if self.life>0:
            self.life-=80
            print('life')
            print(self.life)
        else:
            print('dead')
            mixer.music.stop()
    def shootgrenade(self):
        mixer.music.load(r"C:\Users\saksham\Desktop\bomb.mp3")
        mixer.music.play()
        if self.life>0:
            self.life-=80
            print('grenade')
            print(self.life)
        else:
            print('dead')
            mixer.music.stop()
    def amunation(self):
        print('life' + str(self.life))
        print('ammo' + str(self.ammo))
        print('missile' + str(self.missile))
        print('grenade' + str(self.gren))
    def head1(self):
        mixer.music.load(r'C:\Users\saksham\Desktop\headshot.mp3')
        mixer.music.play()
        if self.life>0:
            self.life=0
            print('headshot')
            print(self.life)
    def shotg(self):
        mixer.music.load(r'C:\Users\saksham\Desktop\shotgun.mp3')
        mixer.music.play()
        if self.life>0:
            self.life-=85
            print('shotgun')
            print(self.life)
        else:
            print('dead')
            mixer.music.stop()
a=cs()
while 3:
    b=input('enter operation')
    if b=='s':

        a.shoot1()
    elif b=='h':
        a.health()
    elif b=='m':
        a.missile1()
    elif b=='g':
        a.grenade()
    elif b=='k':
        a.shootmisile()
    elif b=='r':
        a.shootgrenade()
    elif b=='l':
        a.medikit1()
    elif b=='w':
        a.amunation()
    elif b=='sg':

        a.shotg()
    elif b=='hs':
        a.head1()

    else:
        print('please enter correct operation')
xer.music.load(r"C:\Users\saksham\Desktop\cs.mp3")
            mixer.music.play()
            self.ammo-=1
            self.life-=1
            print('ammo')
            print(self.ammo)
        else:
            print('dead')
            mixer.music.stop()

    def health(self):
        print(self.life)

    def gun(self):
        if self.life>0:
            self.ammo=100

    def medikit1(self):
        if self.life>0 and self.life<80 :
            self.life+=20
        else:
            a=100-self.life
            self.life+=a
            print('medikit1')
            print(self.life)

    def missile1(self):
        if self.life>0:
           self.missile+=1
           print('missile')
           print(self.missile)
        else:
            print('dead')

    def grenade(self):
        if self.life>0:
            self.gren+=1
            print('grenade')
            print(self.gren)
        else:
            print('dead')
    def shootmisile(self):
        mixer.music.load(r'C:\Users\saksham\Desktop\missile.mp3')
        mixer.music.play()
        if self.life>0:
            self.life-=80
            print('life')
            print(self.life)
        else:
            print('dead')
            mixer.music.stop()
    def shootgrenade(self):
        mixer.music.load(r"C:\Users\saksham\Desktop\bomb.mp3")
        mixer.music.play()
        if self.life>0:
            self.life-=80
            print('grenade')
            print(self.life)
        else:
            print('dead')
            mixer.music.stop()
    def amunation(self):
        print('life' + str(self.life))
        print('ammo' + str(self.ammo))
        print('missile' + str(self.missile))
        print('grenade' + str(self.gren))
    def head1(self):
        mixer.music.load(r'C:\Users\saksham\Desktop\headshot.mp3')
        mixer.music.play()
        if self.life>0:
            self.life=0
            print('headshot')
            print(self.life)
    def shotg(self):
        mixer.music.load(r'C:\Users\saksham\Desktop\shotgun.mp3')
        mixer.music.play()
        if self.life>0:
            self.life-=85
            print('shotgun')
            print(self.life)
        else:
            print('dead')
            mixer.music.stop()
a=cs()
while 3:
    b=input('enter operation')
    if b=='s':

        a.shoot1()
    elif b=='h':
        a.health()
    elif b=='m':
        a.missile1()
    elif b=='g':
        a.grenade()
    elif b=='k':
        a.shootmisile()
    elif b=='r':
        a.shootgrenade()
    elif b=='l':
        a.medikit1()
    elif b=='w':
        a.amunation()
    elif b=='sg':

        a.shotg()
    elif b=='hs':
        a.head1()

    else:
        print('please enter correct operation')
