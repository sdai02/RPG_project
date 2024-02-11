from random import randint
class Attack:
  def __init__(self,name,damage,crit,miss):
    self.name = name
    self.damage = damage
    self.crit = crit
    self.miss = miss

  def calculate_damage(self):
    r = randint(0,100)
    if r < self.crit:
      return self.damage * 2
    r = randint(0,100)
    if r < self.miss:
      return 0

    return self.damage

class Item :
  def __init__(self,name):
    self.name = name

  def use(self, Entity):
    print("Vous utilisez :", self.name)

class Potion(Item) :
  def __init__(self,name,effect,power):
    super().__init__(name)
    self.effect = effect
    self.power = power

  def use(self, player):
    if self.effect == "Soin":
      player.hp += self.power
    elif self.effect == "Def":
      player.Def += self.power

class Weapon(Item) :
  def __init__(self,name,atk):
    super().__init__(name)
    self.atk = atk

  def use(self,player):
    player.atks.append(self.atk)

from random import randint
class Entity():
  def __init__(self,name, atks, Def, hp ):
    self.name = name
    self.atks = atks
    self.Def = Def
    self.hp = hp

  def attack(self):
    pass

class PlayerRPG(Entity):
  def __init__(self,Role):
    if Role == "Warrior":
      super().__init__(Role,[Attack("Epee",1,5,5),Attack("Hache",10,5,5)],5,20)
      self.inventory = [Potion("Potion de vie","Soin",15)]
    elif Role == "Mage":
      super().__init__(Role,[Attack("Boule de feu",40,5,30),Attack("Eclair",20,20,40)],3,15)
      self.inventory =[Potion("Potion de Soin","Soin",20),Weapon("Baton",Attack("Boule de feu",5,20,0)),Potion("Potion de Defense","Defense",10),Potion("Potion de Defense","Defense",10)]

  def use_inventory(self):
    self.open_inventory()
    choose = int(input())
    p = self.inventory[choose]
    p.use(self)
    self.inventory.remove(p)

  def attack(self):
    for element in self.atks:
      print(element.name)
    choose = int(input())
    return self.atks[choose].calculate_damage()

  def open_inventory (self):
    for item in self.inventory:
      print(item.name)
      
  def move (self):   
    self.liste = [ Place('néant',' le noir le plus complet'),
                    Place('jungle','un paysage avec des arbres géant et des liannes'),
                    Place('foret en neiger','une foret avec plein de neige'),
                    Place('desert','un paysage avec du sable et des squelets d\'animaux mort') ] 
    while self.hp > 0:
      r = randint(0,len(self.liste)-1)
      path = input("gauche ou droit")
    
      if path == "gauche" or "droite":   
        print("Vous êtes en " + str(self.liste[r].name) + " dans " + str(self.liste[r].details))
        event(self)
      
      
    
    

class monster(Entity) :
  def __init__(self, name, atks, Def, hp, loot):
    super().__init__(name,atks,Def,hp)
    self.loot = loot

  def attack(self):
    r = randint(0,len(self.atks)-1)
    atk = self.atks[r]
    return atk.calculate_damage()


def Fight(Player,Monster):
  while Player.hp > 0 and Monster.hp > 0:
    choose = input("Atk or item")
    if choose == "Atk":
        Monster.hp -= Player.attack()
        Monster.hp*-1
        print("Le pv du " + str(Monster.name) + " il est de " + str(Monster.hp))
      
    elif len(Player.inventory) > 0:
      Player.use_inventory()
      
    elif Monster.hp < 0:
      Player.inventory.append(Monster.loot)
      
    Player.hp -= Monster.attack()
    
    
    


      

class Place:
  def __init__(self,name,details):
    self.name = name
    self.details = details


def event (self):
    r = randint(0,2)
    
    if r == 0:
      gobelin = monster("gobelin",[Attack("Morsure",1,5,1)],1,10,"dents") 
      print('un ' + str(gobelin.name) + " apparait")
      Fight(self,gobelin)
    elif r == 1:
      print('vous trouvez un coffre, vous l\'ouvrez et ça ajoute un potion de soin dans l\'inventaire')
      self.inventory.append(Potion("potion de soin", 'soin',10))
    elif r == 2:
      print("Enigme : Dans un royaume lointain, vous vous retrouvez face à deux portes gardées par deux gardiens. "
            +"L'un des gardiens ne dit que la vérité, et l'autre ne dit que des mensonges." 
            +"Vous ne savez pas lequel est lequel. Chaque porte mène à un destin différent: l'une vers la liberté et l'autre vers un dragon. "
            +"Vous avez le droit de poser une seule question à l'un des gardiens pour déterminer quelle porte choisir."
            )
      print("1. Si je demandais à l'autre gardien quelle porte mène à la liberté, que me dirait-il ? "
            +"2.Quelle porte choisirais-tu ?")
      choose = int(input())
      
      if choose == 1:
          self.atks.append(Weapon("épée enflamé",Attack("coupe enflamé",30,40,50)))
          print("bravo, épée enflamé est dans votre inventaire")
      elif choose == 2:
        print("perdue") 
        
    
     


            
        
       

    
Pl = PlayerRPG("Warrior")
M1 = monster("Gobelin",[Attack("Morsure",1,1,1)],1,10,None)

Pl.move()



