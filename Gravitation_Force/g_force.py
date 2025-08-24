import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


class Particle():
    # u - initial velocity ALL ARE IN SI UNTIS
    # m - mass
    # a - acceleration

    def __init__(self, coords, radius, u=[0, 0], a=[0, 0], m=1):
        self.coords = coords
        self.radius = radius
        self.u = u
        self.a = a
        self.m = m
    
    def render(self):
        pygame.draw.circle(screen, (255, 0, 0), tuple(self.coords), self.radius)

    def update(self):
        for i in range(len(self.coords)):
            self.u[i] += self.a[i]
            self.coords[i] += self.u[i]

    def checkBorderCollision(self):
        if (self.coords[0] - self.radius) <= 0:
            self.u[0] *= -1
        if (self.coords[0] + self.radius) >= screen.get_width():
            self.u[0] *= -1
        if (self.coords[1] - self.radius) <= 0:
            self.u[1] *= -1
        if (self.coords[1] + self.radius) >= screen.get_height():
            self.u[1] *= -1

# Scene
Ball = Particle([300, 300], 10, [1, -2], [0, 0], 1)
Ball2 = Particle([400, 300], 20, [0, 0], [0, 0], 1000)

ForceFields = {
    "GravField": {

    }
}

frames = []

class Forces():
    def gravitation(self, object1, object2):
        gForce = (6.67*pow(10, -1)*object1.m*object2.m)/(pow(math.sqrt(pow(object1.coords[0] - object2.coords[0], 2)+pow(object1.coords[1] - object2.coords[1], 2)), 2))

        obj1Pos = pygame.math.Vector2(object2.coords[0]-object1.coords[0], object2.coords[1] - object1.coords[1])
        obj1Pos = obj1Pos.normalize()
        object1.a[0] = (gForce*obj1Pos.x)/object1.m
        object1.a[1] = (gForce*obj1Pos.y)/object1.m

        obj2Pos = pygame.math.Vector2(-(object2.coords[0]-object1.coords[0]), -(object2.coords[1] - object1.coords[1]))
        obj2Pos = obj2Pos.normalize()
        object2.a[0] = (gForce*obj2Pos.x)/object2.m
        object2.a[1] = (gForce*obj2Pos.y)/object2.m

        # print(object1.a)
        # print(object2.a)

force = Forces()  

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))

    Ball.render()
    Ball.update()
    Ball2.render()
    Ball2.update()
    Ball.checkBorderCollision()
    force.gravitation(Ball, Ball2)
    

    pygame.display.flip()
    clock.tick(120)   

pygame.quit() 
    
    

