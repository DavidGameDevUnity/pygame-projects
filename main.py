import pygame

def draw_rect(screen, color, x, y, width, height):
	pygame.draw.rect(screen, color, (x, y, width, height))

pygame.init()

sc = pygame.display.set_mode((600, 400))
sc.fill((33,33,33))
pygame.display.flip()

x = 10
y = 10
rect_width = 100
rect_height = 100
clock = pygame.time.Clock()

font = pygame.font.Font(None, 74)
text = font.render('Привет, Pygame!', True, (171,219,227))

while True:
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			pygame.quit()
			exit()


	keys = pygame.key.get_pressed()
	if keys[pygame.K_DOWN] and y + rect_height < 400:
		y+=10
		print(y)
	if keys[pygame.K_UP] and y > 0:
		y-=10
		print(y)
	if keys[pygame.K_LEFT] and x > 0:
		x-=10
		print(x)
	if keys[pygame.K_RIGHT] and x + rect_width < 600:
		x+=10
		print(x)
	sc.fill((33, 33, 33))
	draw_rect(sc, (0,0,255), x, y, 100, 100)
	sc.blit(text, (100, 200))
	pygame.display.flip()
	clock.tick(60)
	print(clock.get_fps())
