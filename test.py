import pygame
from pygame.locals import *
import time
import pygame.mixer
pygame.init()
fpsclock = pygame.time.Clock()
FPS = 60
Dis = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Duc Dat")
bg = pygame.image.load("background.jpg")
bg_x = 0
bg_y = 0
dino = pygame.image.load("dinosaur.png")
dinox = 20
dinoy = 220
soGiay = 20
is_jumping = False
dangNhay = True
tree = pygame.image.load("tree.png")
tree_x = 545
tree_y = 226
sound_jump = pygame.mixer.Sound("tick.wav")
point = 0
font = pygame.font.Font(None, 28)  # Tạo font chữ
gameOver = False
while True:
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                if dangNhay:
                    is_jumping = True
                    sound_jump.play()

    Dis.blit(bg, (bg_x, bg_y)) 
    s = Dis.blit(bg, (bg_x+600, bg_y))
    if bg_x == -600:
        bg_x = 0
    bg_x -= 5
    
    Dis.blit(dino, (dinox, dinoy))
    # Kiểm tra khủng long có đang nhảy hay không (bằng cách kiểm tra trục y của khủng long nếu nó thay đổi thì là đang nhảy)
    # Nếu đang nhảy thì chuyển biến dangNhay thành False để khi nhấn phím SPACE thì sẽ không vào được điều kiện
    if dinoy < 220:
        dangNhay = False
    else:
        dangNhay = True
    
    # Khủng cho khủng long nhảy lên khi nhấn phím SPACE
    if is_jumping:
        while dinoy >= 120:
            dinoy -= 3

        is_jumping = False
    

    # Khủng long trở về vị trí ban đầu 

    if dinoy < 220:
        dinoy += 2

    Dis.blit(tree, (tree_x, tree_y))
    tree_x -= 5
    if tree_x < -10:
        tree_x = 545
    
    rect_dino = dino.get_rect()
    rect_dino.x = dinox
    rect_dino.y = dinoy

    rect_tree = tree.get_rect()
    rect_tree.x = tree_x
    rect_tree.y = tree_y
    point += 0.1
    tpoint = font.render(f"Point: {int(point)}", True, (120, 120, 120))
    Dis.blit(tpoint, (500, 20))
    if rect_dino.colliderect(rect_tree):
        text = font.render("Game over", True, (120, 120, 120))
        Dis.blit(text, (220, 180))
        Dis.blit(tpoint, (220, 200))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
    pygame.display.update()
    fpsclock.tick(FPS)
    