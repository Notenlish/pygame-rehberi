import pygame

# pygame'i yükle
pygame.init()

# ekranı oluştur(genişlik, yükseklik)
screen = pygame.display.set_mode([640, 480])

surf = pygame.Surface((100, 100)).convert_alpha()
# pygame.draw.circle(surf, pygame.Color(255, 0, 0, 125), (50, 50), 50)
surf.fill(pygame.Color(255,0,0,125))

# zamanlayıcı(fps'i 60 a sabitlemek için)
clock = pygame.time.Clock()


# ana uygulama döngüsü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

    # ekranı maviye boya
    # RGB, hex veya ingilizce kelime
    screen.fill("black")

    screen.blit(surf, (50, 50))

    # ekranı yenile
    pygame.display.flip()

    # 60 fps'e sabitle
    clock.tick(60)
