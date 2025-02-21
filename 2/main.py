import pygame

class Game:
    def __init__(self):
        # pygame'i yükle
        pygame.init()

        # ekranı oluştur(genişlik, yükseklik)
        self.screen = pygame.display.set_mode([640, 480])

        # zamanlayıcı(fps'i 60 a sabitlemek için)
        self.clock = pygame.time.Clock()

        # oyuncunun sprite'ı(görseli)
        self.player_surface = pygame.image.load("player.png")
        self.player_pos = [100, 300]  # karakterin konumu(x, y)

        # çarpışma(collision) için alan
        self.collision_area = pygame.Rect(50, 50, 200, 100)

    def run(self):
        # ana uygulama döngüsü
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit

            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                self.player_pos[1] -= 200 * dt
            elif keys[pygame.K_DOWN]:
                self.player_pos[1] += 200 * dt
            
            if keys[pygame.K_RIGHT]:
                self.player_pos[0] += 200 * dt
            elif keys[pygame.K_LEFT]:
                self.player_pos[0] -= 200 * dt
            
            # (x,y, genişlik, yükseklik)
            player_rect = pygame.Rect(
                *self.player_pos,
                *self.player_surface.size)

            area_color = (219, 107, 42)

            if player_rect.colliderect(self.collision_area):
                area_color = (214, 57, 23)
            
            self.screen.fill((42, 157, 219))

            pygame.draw.rect(
                self.screen, area_color, self.collision_area
            )

            self.screen.blit(self.player_surface, self.player_pos)

            # ekranı yenile
            pygame.display.flip()

            # 60 fps'e sabitle
            dt = self.clock.tick(60) / 1000

game = Game()
game.run()
