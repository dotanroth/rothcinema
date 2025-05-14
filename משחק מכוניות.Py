import pygame
import random
import sys

# אתחול pygame
pygame.init()

# הגדרות חלון
WIDTH, HEIGHT = 500, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("מרוץ מכוניות")

# צבעים
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# מכונית שחקן
player_width, player_height = 50, 100
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# מכוניות אויב
enemy_width, enemy_height = 50, 100
enemy_speed = 4
enemy_list = []

# שלב
level = 1
score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

def draw_window(player_rect, enemies, level, score):
    win.fill(WHITE)
    pygame.draw.rect(win, BLACK, player_rect)

    for enemy in enemies:
        pygame.draw.rect(win, RED, enemy)

    # הצגת שלב וניקוד
    level_text = font.render(f'שלב: {level}', True, BLACK)
    score_text = font.render(f'ניקוד: {score}', True, BLACK)
    win.blit(level_text, (10, 10))
    win.blit(score_text, (10, 50))

    pygame.display.update()

def reset_game():
    global player_x, player_y, enemy_list, enemy_speed, level, score
    player_x = WIDTH // 2 - player_width // 2
    player_y = HEIGHT - player_height - 10
    enemy_list = []
    enemy_speed = 4
    level = 1
    score = 0

def main():
    global player_x, enemy_speed, level, score
    run = True
    spawn_timer = 0

    while run:
        clock.tick(60)
        spawn_timer += 1
        score += 1

        if spawn_timer > 60:
            enemy_x = random.randint(0, WIDTH - enemy_width)
            enemy_list.append(pygame.Rect(enemy_x, -enemy_height, enemy_width, enemy_height))
            spawn_timer = 0

        # עדכון אויבים
        for enemy in enemy_list:
            enemy.y += enemy_speed

        # הסרת אויבים שירדו מהמסך
        enemy_list[:] = [enemy for enemy in enemy_list if enemy.y < HEIGHT]

        # שלבים - כל 500 נקודות מעלים שלב ומגבירים מהירות
        if score % 500 == 0:
            level += 1
            enemy_speed += 1

        # קלט שחקן
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x - player_speed > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x + player_speed + player_width < WIDTH:
            player_x += player_speed

        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

        # בדיקת התנגשות
        for enemy in enemy_list:
            if player_rect.colliderect(enemy):
                reset_game()

        draw_window(player_rect, enemy_list, level, score)

        # אירועים
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
