import random
import math

class Game():
    def __init__(self):
        self.grid = [[" " for y in range(0,15)] for x in range(0,15)]
        for x in range(0,15):
            for y in range(0,15):
                tileseed = random.randint(1,100)
                if tileseed in range(81):
                    self.grid[x][y] = 0
                elif tileseed in range(81,98):
                    self.grid[x][y] = 1
                else:
                    self.grid[x][y] = 2
        print(self.grid)

    def get_grid(self):
        return self.grid
    

class Army():
    def __init__(self, Creator, x, y, color, unitcount=100):
        self.BaseMoveRange = 75
        self.BaseDamagePrUnit = 2
        self.BaseHealthPrUnit = 3
        self.BaseArmyRange = 75
        self.Units = unitcount
        self.MovedYet = True
        self.Ownership = Creator
        self.xCoord = x
        self.yCoord = y
        self.color = color

    def Move(self, x, y):
        MovementRange = ((x-self.xCoord)**2+(y-self.yCoord)**2)
        if MovementRange < self.BaseMoveRange**2 and MovementRange != 0:
            self.xCoord = x
            self.yCoord = y
            self.MovedYet = True
        
    def Attack_check(self, x, y, owner):
        if owner != self.Ownership:
            AttackRange = ((x-self.xCoord)**2+(y-self.yCoord)**2)
            if AttackRange > self.BaseArmyRange**2:
                return False
            else:
                return True
        else:
            return False
        
    def DamageCalculation(self, EnemyBaseDamage, EnemyUnitCount):
        CurrentHealth = self.BaseHealthPrUnit*self.Units
        EnemyDamage = EnemyBaseDamage*EnemyUnitCount
        if CurrentHealth < EnemyDamage:
            return True
        else:
            self.Units = self.Units*(EnemyDamage/CurrentHealth)
            print(self.Units)
            if self.Units < 1:
                return True
            else:
                return False
        


class Castle():
    def __init__(self):
        self.BaseRange = 6
        self.BaseDamage = 160
        self.CurrentHealth = 600

