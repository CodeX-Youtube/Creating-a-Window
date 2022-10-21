import pygame

pygame.init()

WIDTH = 720
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

run = True
while run:
	clock.tick(60)
	fps = clock.get_fps()

	pygame.display.set_caption('Tutorial - {:.2f}FPS'.format(fps))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()