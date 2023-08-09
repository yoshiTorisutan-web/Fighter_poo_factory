import unittest
from objects import Player, Bullet, Enemy
from factories import PlayerFactory, BulletFactory, EnemyFactory


class TestPlayerFactory(unittest.TestCase):

    def test_create_player(self):
        player_factory = PlayerFactory()
        player = player_factory.create_object(100, 200)

        self.assertEqual(player.rect.x, 100)
        self.assertEqual(player.rect.y, 200)


class TestBulletFactory(unittest.TestCase):

    def test_create_bullet(self):
        bullet_factory = BulletFactory()
        bullet = bullet_factory.create_object(150, 250)

        self.assertEqual(bullet.rect.x, 150)
        self.assertEqual(bullet.rect.y, 250)


class TestCollisionDetection(unittest.TestCase):

    def test_bullet_enemy_collision(self):
        bullet = Bullet(50, 50)    # Create a test bullet at coordinates (50, 50)
        enemy = Enemy(50, 50, 5)  # Assuming a speed of 5, adjust accordingly
        collided = bullet.rect.colliderect(enemy.rect)
        self.assertTrue(collided)


if __name__ == '__main__':
    unittest.main()
