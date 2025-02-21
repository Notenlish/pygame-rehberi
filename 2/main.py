import pygame


class Game:
    def __init__(self) -> None:
        # pygame'i yükle
        pygame.init()

        # ekranı oluştur(genişlik, yükseklik)
        self.screen = pygame.display.set_mode([640, 480])

        # zamanlayıcı(fps'i 60 a sabitlemek için)
        self.clock = pygame.time.Clock()

        # karakterin görseli
        self.surface = pygame.image.load("player.png").convert_alpha()
        self.pos: list[float] = [100, 300]  # karakter konumu(x, y)

        # çarpışma(collision) için alan
        self.collision_area = pygame.Rect(50, 50, 200, 100)

    def run(self):
        dt = 0

        # ana uygulama döngüsü
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise SystemExit

            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                self.pos[1] -= 200 * dt
            elif keys[pygame.K_DOWN]:
                self.pos[1] += 200 * dt

            if keys[pygame.K_LEFT]:
                self.pos[0] -= 200 * dt
            elif keys[pygame.K_RIGHT]:
                self.pos[0] += 200 * dt

            player_rect = pygame.Rect(*self.pos, *self.surface.size)  # type:ignore

            area_color = (219, 107, 42)
            if player_rect.colliderect(self.collision_area):
                area_color = (214, 59, 23)

            # ekranı maviye boya
            # RGB, hex veya ingilizce kelime
            self.screen.fill((42, 157, 219))

            # alanı çiz
            pygame.draw.rect(self.screen, area_color, self.collision_area)

            # karakteri çiz
            self.screen.blit(self.surface, self.pos)

            # ekranı yenile
            pygame.display.flip()

            # 144 fps'e sabitle
            dt = self.clock.tick(144) / 1000


game = Game()
game.run()
