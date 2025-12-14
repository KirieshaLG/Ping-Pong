import pygame

class Sprite:
    def __init__(self, center, image):
        self.image = image
        self.rect = image.get_frect()
        self.rect.center = center
    def render(self, surface):
        surface.blit(self.image, self.rect)
        
     
class Player(Sprite):
    def __init__(self, center, image, speed):
        super().__init__(center, image)
        self.speed = speed
        self.move_up = False
        self.move_down = False

    def update(self):
        if self.move_up != self.move_down:
            if self.move_up:
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed
                    





window = pygame.Window('Ping  Pong', (800, 600), pygame.WINDOWPOS_CENTERED)
surface = window.get_surface()
clock = pygame.Clock()

image = pygame.Surface( (40, 100) )
image.fill('red')

left_player = Player( (40, 300), image, 10 )
right_player = Player( (760, 300), image, 10)

running = True
while running:
    # оБРАБОТА СОБЫИЯ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # При нажатии нв клавишу
        elif event.type == pygame.KEYDOWN:
            # 
            if event.key == pygame.K_w:
                left_player.move_up = True
            elif event.key == pygame.K_s:
                left_player.move_down = True

            # 
            elif event.key == pygame.K_UP:
                right_player.move_up = True
            elif event.key == pygame.K_DOWN:
                right_player.move_down = True
        # При отпусаии клавы
        elif event.type == pygame.KEYUP:
            # left
            if event.key == pygame.K_w:
                left_player.move_up = False
            elif event.key == pygame.K_s:
                left_player.move_down = False
                #right
            elif event.key == pygame.K_UP:
                right_player.move_up = False
            elif event.key == pygame.K_DOWN:
                right_player.move_down = False
           


    # обновление обьектов
    left_player.update()
    right_player.update()


    # Отрисовка
    surface.fill('white')
    left_player.render(surface)
    right_player.render(surface)
    window.flip()
    clock.tick(60)
    window.title = 'FPS: ' + str(round(clock.get_fps()))
