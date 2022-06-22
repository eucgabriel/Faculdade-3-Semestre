class Tank:
    def __init__(self, name):
        self.name  = name
        self.alive = True
        self.ammo  = 5
        self.armor = 60
    
    def __str__(self):
        if self.alive:
            return f"{self.name} ({self.armor} armor, {self.ammo} shells)"
        else:
            return f"{self.name} (DEAD)"
    
    def fire(self, enemy):
        if self.ammo >= 1:
            self.ammo -= 1
            print(f"{self.name} fires on {enemy.name}")
            enemy.hit()
        else:
            print(f"{self.name} has no shells")

    def hit(self):
        self.armor -= 20
        print(f"{self.name} is hit!")
        if self.armor <=0:
            self.explode()
    
    def explode(self):
        self.alive = False
        print(f"{self.name} explodes!")