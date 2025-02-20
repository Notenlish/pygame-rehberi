import pygame

# pygame'i yükle
pygame.init()

# ekranı oluştur(genişlik, yükseklik)
screen = pygame.display.set_mode([640, 480])


# zamanlayıcı(fps'i 60 a sabitlemek için)
clock = pygame.time.Clock()


# ana uygulama döngüsü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

    # ekranı maviye boya
    # RGB, hex veya ingilizce kelime
    screen.fill("blue")

    # ekranı yenile
    pygame.display.flip()

    # 60 fps'e sabitle
    clock.tick(60)
