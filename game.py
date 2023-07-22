import pygame
import random
import sys
from objects import Player, Enemy, Bullet
from factories import PlayerFactory, EnemyFactory, BulletFactory
from config import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_SPAWN_RATE, PLAYER_SIZE, WHITE, RED, GREEN

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Square Shooter")
font = pygame.font.Font(None, 36)

player_factory = PlayerFactory()
player = player_factory.create_object(
    SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_SIZE * 2)

bullets = []
bullet_factory = BulletFactory()

enemies = []
enemy_factory = EnemyFactory()

running = True
clock = pygame.time.Clock()
score = 0


def start_screen():
    screen.fill((0, 0, 0))
    fight_text = font.render("FIGHTER !", 1, RED)
    start_text = font.render("Press any key to start", 1, WHITE)
    screen.blit(fight_text, (SCREEN_WIDTH//2 - fight_text.get_width() //
                2, SCREEN_HEIGHT//2 - fight_text.get_height()))
    screen.blit(start_text, (SCREEN_WIDTH//2 - start_text.get_width() //
                2, SCREEN_HEIGHT//2 + start_text.get_height()))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return


def game_over_screen():
    screen.fill((0, 0, 0))
    game_over_text = font.render("Game Over !", 1, RED)
    score_text = font.render("Score : " + str(score), 1, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width() //
                2, SCREEN_HEIGHT//2 - game_over_text.get_height()))
    screen.blit(score_text, (SCREEN_WIDTH//2 - score_text.get_width() //
                2, SCREEN_HEIGHT//2 + score_text.get_height()))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return


start_screen()

while running:
    clock.tick(60)  # 60 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = bullet_factory.create_object(
                    player.rect.x + PLAYER_SIZE//2, player.rect.y)
                bullets.append(bullet)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        player.move(5, 0)

    if random.randint(0, ENEMY_SPAWN_RATE) < 1:
        enemies.append(enemy_factory.create_object(1 + score // 10))

    for bullet in bullets:
        bullet.move()
        if bullet.rect.top < 0:
            bullets.remove(bullet)

    for enemy in enemies:
        enemy.move()
        if enemy.rect.top > SCREEN_HEIGHT:
            enemies.remove(enemy)
        # vérifier si l'ennemi a dépassé le joueur
        if enemy.rect.top > player.rect.bottom:
            game_over_screen()
            pygame.quit()
            sys.exit()
        if player.rect.colliderect(enemy.rect):
            game_over_screen()
            pygame.quit()
            sys.exit()

    for bullet in bullets:
        for enemy in enemies:
            if bullet.rect.colliderect(enemy.rect):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 1

    screen.fill((0, 0, 0))

    for bullet in bullets:
        bullet.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    player.draw(screen)

    score_text = font.render("Score : {0}".format(score), 1, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
