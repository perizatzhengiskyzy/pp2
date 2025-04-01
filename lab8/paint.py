import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_RED = (255, 0, 0)
C_BLUE = (0, 0, 255)
C_GREEN = (0, 255, 0)

color = C_RED
radius = 5
clock = pygame.time.Clock()

drawing = False
last_pos = None
drawing_mode = "line"  # Стартовый режим рисования - линия

# Флаги для рисования прямоугольника и круга
rect_start = None
circle_center = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
            if drawing_mode == "rectangle":
                rect_start = event.pos  # Начало рисования прямоугольника
            elif drawing_mode == "circle":
                circle_center = event.pos  # Центр круга

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None
            if drawing_mode == "rectangle":
                rect_start = None
            elif drawing_mode == "circle":
                circle_center = None
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                color = C_RED
            if event.key == pygame.K_2:
                color = C_GREEN
            if event.key == pygame.K_3:
                color = C_BLUE
            if event.key == pygame.K_0:
                color = C_WHITE
            if event.key == pygame.K_9:
                color = C_BLACK
            if event.key == pygame.K_r:
                drawing_mode = "rectangle"  # Переключиться на рисование прямоугольников
            if event.key == pygame.K_c:
                drawing_mode = "circle"  # Переключиться на рисование кругов
            if event.key == pygame.K_l:
                drawing_mode = "line"  # Переключиться на рисование линий

    # Логика рисования
    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        if drawing_mode == "line" and last_pos:
            pygame.draw.line(screen, color, last_pos, mouse_pos, radius)
        elif drawing_mode == "rectangle" and rect_start:
            rect_width = mouse_pos[0] - rect_start[0]
            rect_height = mouse_pos[1] - rect_start[1]
            pygame.draw.rect(screen, color, (rect_start[0], rect_start[1], rect_width, rect_height), 2)
        elif drawing_mode == "circle" and circle_center:
            radius = int(((mouse_pos[0] - circle_center[0]) ** 2 + (mouse_pos[1] - circle_center[1]) ** 2) ** 0.5)
            pygame.draw.circle(screen, color, circle_center, radius, 2)

        last_pos = mouse_pos

    pygame.display.update()
    clock.tick(120)

pygame.quit()
