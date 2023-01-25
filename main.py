#Troy Tural
#GR:404
#EXCERSICE POO#2

import random
import math

def lancer():
   lancer1 = random.randint(1,6)
   lancer2 = random.randint(1,6)
   lancer3 = random.randint(1,6)
   lancer4 = random.randint(1,6)
   if lancer1 < lancer2 and lancer1 < lancer3 and lancer1 < lancer4:
       lancer = lancer2 + lancer3 + lancer4
       return lancer

   if lancer2 < lancer1 and lancer2 < lancer3 and lancer2 < lancer4:
       lancer = lancer1 + lancer3 + lancer4
       return lancer

   if lancer3 < lancer1 and lancer3 < lancer2 and lancer3 < lancer4:
       lancer = lancer1 + lancer2 + lancer4
       return lancer

   if lancer4 < lancer1 and lancer4 < lancer2 and lancer4 < lancer3:
       lancer = lancer1 + lancer2 + lancer3
       return lancer



class NPC:
    def __init__(self,name):
       self.ATK = lancer()
       self.AGI = lancer()
       self.CONS = lancer()
       self.INT = lancer()
       self.SAGE = lancer()
       self.CARI = lancer()
       self.DEF = random.randint(1,12)
       self.NAME = ('Eddie')
       self.RACE = ('Human')
       self.HP = (20)
       self.JOB = ('Geomancer')

    def afficherNPC(self):
        print()

class Kobold(NPC):
    def attack(self,cible):
        return random.randint(1, 6) + self.ATK

    def damage_taken(self,dmg):
        self.HP -= dmg - self.DEF

class HERO(NPC):
    def attack(self,cible):
        return random.randint(1,6) + self.ATK

    def damage_taken(self,dmg):
        self.HP -= dmg - self.DEF




