import pygame

class Field:
    def __init__(self):
        self.walls = [pygame.Rect(0,0,700,1),pygame.Rect(0,499,700,1)]
        self.goals= [pygame.Rect(0,0,1,500),pygame.Rect(699,0,1,500)]
        self.score = [0,0]
    def draw(self,win):
        for wall in self.walls:
            pygame.draw.rect(win, (0,0,0), wall)
        for goal in self.goals:
            pygame.draw.rect(win, (0,0,0), goal)
        

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 340
        self.y = 240
        self.color = (0,0,0)
        self.rect = pygame.Rect(self.x, self.y, 20,20)
        self.xvel = 2
        self.yvel = 2
        self.started = False
    
    def check_colision(self, players,field):
        for wall in field.walls:
            if self.rect.colliderect(wall):
                self.yvel *= -1
                self.y += self.yvel*2
                print("wall")
        for player in players:
            if self.rect.colliderect(player.box):
                self.xvel *= -1
                self.x += self.xvel*2
                print("player")
        if self.rect.colliderect(field.goals[0]):
            field.score[1] +=1
            self.center()
            print("goal")
        if self.rect.colliderect(field.goals[1]):
            field.score[0] += 1
            self.center()
            print("goal")
            
    
    def move(self,players, field):
        if self.started:
            self.x += self.xvel
            self.y += self.yvel
            self.check_colision(players, field)
            self.update()
            
    def center(self):
        self.started =False
        self.x = 340
        self.y = 240
        self.update()
        
    def start(self):
        self.started = True
        
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)