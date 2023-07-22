import random
from objects import Player, Enemy, Bullet
from config import SCREEN_WIDTH

class GameObjectFactory:
    def create_object(self):
        pass


class PlayerFactory(GameObjectFactory):
    def create_object(self, x, y):
        return Player(x, y)


class EnemyFactory(GameObjectFactory):
    def create_object(self, speed):
        return Enemy(random.randint(0, SCREEN_WIDTH), 0, speed)


class BulletFactory(GameObjectFactory):
    def create_object(self, x, y):
        return Bullet(x, y)
