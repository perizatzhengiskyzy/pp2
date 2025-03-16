import pygame
import os

pygame.init()

playlist = []
music_folder = "C:\\pp22\\pp2\\lab7\\musics"
allmusic = os.listdir(music_folder)

for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Straykids")
clock = pygame.time.Clock()

background = pygame.image.load("C:\\pp22\\pp2\\lab7\\music-elements\\background1.png")

bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))

font2 = pygame.font.SysFont(None, 30)

playb = pygame.image.load("C:\\pp22\\pp2\\lab7\\music-elements\\play.png")
pausb = pygame.image.load("C:\\pp22\\pp2\\lab7\\music-elements\\pause.png")
nextb = pygame.image.load("C:\\pp22\\pp2\\lab7\\music-elements\\next.png")
prevb = pygame.image.load("C:\\pp22\\pp2\\lab7\\music-elements\\back.png")

btn_size = (60, 60)
playb = pygame.transform.scale(playb, btn_size)
pausb = pygame.transform.scale(pausb, btn_size)
nextb = pygame.transform.scale(nextb, btn_size)
prevb = pygame.transform.scale(prevb, btn_size)

index = 0
aplay = False

pygame.mixer.music.load(playlist[index]) 
pygame.mixer.music.play(1)
aplay = True 

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()
            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

    max_length = 30
    song_name = os.path.basename(playlist[index])
    if len(song_name) > max_length:
        song_name = song_name[:max_length] + "..."
    text2 = font2.render(song_name, True, (20, 20, 50))
    
    screen.blit(background, (-50, 0))
    screen.blit(bg, (150, 550))
    screen.blit(text2, (400 - text2.get_width() // 2, 520))
    screen.blit(pausb if aplay else playb, (370, 600))
    screen.blit(nextb, (460, 600))
    screen.blit(prevb, (280, 600))

    clock.tick(24)
    pygame.display.update()
