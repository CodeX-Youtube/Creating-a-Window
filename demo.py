import pygame
import math

WIDTH, HEIGHT = 720, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

run = True
dt = 0
images = {}
images['Player'] = pygame.image.load('Player.png')
scroll = [0, 0]
particles = []
#[[x,y], color, size, velocity]

class Player:
	def __init__(self):
		self.size = 64
		self.speed = 4
		self.angle = 0
		self.hitbox = 8
		self.image = pygame.transform.scale(images['Player'], (self.size, self.size))
		self.vel = [0, 0]
		self.pos = [100, 100]

	def update(self):
		self.move()
		self.point()

	def move(self):
		keys = pygame.key.get_pressed()
		vx, vy = 0, 0
		if keys[pygame.K_a]: vx -= 1 
		if keys[pygame.K_d]: vx += 1 
		if keys[pygame.K_w]: vy -= 1 
		if keys[pygame.K_s]: vy += 1
		if vx != 0 and vy != 0:
			vx *= 0.7071 
			vy *= 0.7071

		self.vel[0] += (vx*self.speed-self.vel[0]) * 0.1 * dt
		self.vel[1] += (vy*self.speed-self.vel[1]) * 0.1 * dt

		self.pos[0] += self.vel[0] * dt
		self.pos[1] += self.vel[1] * dt
		print(self.vel)

	def point(self):
		mouseangle = math.atan2(pygame.mouse.get_pos()[1]-self.pos[1], pygame.mouse.get_pos()[0]-self.pos[0])
		self.angle = -mouseangle / math.pi * 180

	def draw(self):
		img = pygame.transform.rotate(self.image,self.angle)
		screen.blit(img, (self.pos[0]-img.get_width()/2, self.pos[1]-img.get_height()/2))

player = Player()

while run:
	clock.tick(60)
	fps = clock.get_fps()
	pygame.display.set_caption('DEMO - {:.2f}FPS'.format(fps))
	if fps > 0:
		dt = 60/fps
	else:
		dt = 0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	player.update()

	screen.fill((0, 0, 50))
	player.draw()

	pygame.display.update()

pygame.quit()