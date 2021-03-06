import os

import pygame

from src import constants
from src import globalvars


class ObjSpriteSheet:
    """A sprite sheet object class for processing the individual sprites.

    Loads sprite sheet files and grab relevant portions of the file for making animation sequence
    lists or simply still image sprites. Will also have scaling functionality (to 32 x 32).

    Attributes
    ----------
    sprite_sheet : pygame.Surface
        The sprite sheet that is loaded from `file_dir` and `file_name`.
    tileDict : dict
        Maps alphabetical letters to columns of the sprite sheet.

    """

    def __init__(self, file_dir, file_name):
        self.sprite_sheet = pygame.image.load(
            os.path.join('data', 'graphics', file_dir, file_name)).convert()
        self.tileDict = {
            'A': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
            'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
            's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'a1': 27,
            'b1': 28, 'c1': 29, 'd1': 30, 'e1': 31, 'f1': 32, 'g1': 33
        }

    def get_image(self, col, row, w=constants.CELL_WIDTH, h=constants.CELL_HEIGHT, scale=None):
        """Returns a list with a single sprite entry.

        Parameters
        ----------
        col : str
            A letter from `tileDict` corresponding to the column coordinate of the desired image.
        row : int
            The row coordinate number (counting from 0) of the desired image.
        w : int, optional
            The width of the sprite in pixels. Usually 16 or 32. Default 32 to match tile size.
        h : int, optional
            The height of the sprite in pixels. Usually 16 or 32. Default 32 to match tile size.
        scale : tuple, optional
            The (width, height) in pixels for the desired image to be scaled to.

        Returns
        -------
        list
            A list containing a single sprite image from the sprite sheet.
        """
        image_list = []

        image_surface = pygame.Surface([w, h]).convert()
        image_surface.blit(self.sprite_sheet, (0, 0), (self.tileDict[col] * w, row * h, w, h))

        if scale is not None:
            image_surface = pygame.transform.scale(image_surface, scale)

        image_list.append(image_surface)
        return image_list

    def get_animation(self, col, row, num_sprites, w=constants.CELL_WIDTH, h=constants.CELL_HEIGHT,
                      scale=None):
        """Returns a list with a sequence of sprites that make up an animation

        Parameters
        ----------
        col : str
            A letter from `tileDict` corresponding to the column coordinate of the desired image.
        row : int
            The row coordinate number (counting from 0) of the desired image.
        num_sprites : int
            The number of sequential sprites in a row (counting the first one specified by
            `row` and `col`) in the particular animation sequence.
        w : int, optional
            The width of the sprite in pixels. Usually 16 or 32. Default 32 to match tile size.
        h : int, optional
            The height of the sprite in pixels. Usually 16 or 32. Default 32 to match tile size.
        scale : tuple, optional
            The (width, height) in pixels for the desired image to be scaled to.

        Returns
        -------
        list
            A list containing a sequence of sprites from the sprite sheet.
        """
        animation_list = []

        for i in range(num_sprites):
            # create blank surface
            sprite_surface = pygame.Surface([w, h]).convert()

            # copy sprite from sprite sheet onto blank surface
            sprite_surface.blit(self.sprite_sheet, (0, 0), (self.tileDict[col] * w + (w * i), row * h, w, h))

            if scale:
                sprite_surface = pygame.transform.scale(sprite_surface, scale)

            animation_list.append(sprite_surface)

        return animation_list


class ObjAssets:
    """A class which functions like a struct and contains all the assets used in the game.

    Loads sprite sheets using the ObjSpriteSheet class and creates individual sprite images and
    animations from the ObjActor class. Music and sound effects are included as assets.
    """

    def __init__(self):

        # ========================== SPRITE SHEETS ========================== #

        # ---> Character folder
        self.player = ObjSpriteSheet("Characters", "Player.png")
        self.slime = ObjSpriteSheet("Characters", "Slime.png")
        self.death = ObjSpriteSheet("Characters", "Death.png")

        # ---> Items folder
        self.weapon = ObjSpriteSheet("Items", "Weapon.png")
        self.defence = ObjSpriteSheet("Items", "Defence.png")
        self.scroll = ObjSpriteSheet("Items", "Scroll.png")
        self.special = ObjSpriteSheet("Items", "Special.png")
        self.money = ObjSpriteSheet("Items", "Money.png")

        # ---> Objects folder
        self.wall = ObjSpriteSheet("Objects", "Wall.png")
        self.floor = ObjSpriteSheet("Objects", "Floor.png")
        self.tile = ObjSpriteSheet("Objects", "Tile.png")
        self.door = ObjSpriteSheet("Objects", "Door.png")
        self.dungeonTiles = ObjSpriteSheet("Objects", "Dungeon_Tileset2.png")

        # ---> Menu folder
        self.menugui = ObjSpriteSheet("menu", "menugui.png")

        # ============================ SPRITES ============================= #

        #                        ||| Animations |||

        # ---> Player
        self.A_PLAYER_LEFT = self.player.get_animation('A', 5, 4)
        self.A_PLAYER_RIGHT = self.player.get_animation('A', 4, 4)
        self.S_PLAYER_PFP = pygame.image.load(
            os.path.join("data", "graphics", "menu", "pfp.png")).convert()
        self.S_PLAYER_LVL = pygame.image.load(
            os.path.join("data", "graphics", "menu", "player_level.png")).convert()

        # ---> Enemy creatures
        self.A_DUNGO = self.slime.get_animation('A', 1, 2)
        self.A_DARKSOOT = self.slime.get_animation('A', 2, 2)
        self.A_BLAZEO = self.slime.get_animation('e', 0, 2)
        self.A_KELPCLOPSE = self.slime.get_animation('e', 1, 2)
        self.A_SHELK = self.slime.get_animation('e', 2, 2)

        # friendly mobs
        self.A_ICESLIME = self.slime.get_animation('A', 0, 2)

        # Soul sprites
        self.A_DEATH_RED = self.death.get_animation('A', 0, 9)
        self.A_DEATH_BLUE = self.death.get_animation('A', 1, 9)

        #                        ||| Still Sprites |||

        # ---> Dungeon structures
        self.S_WALL = self.wall.get_image('d', 7, 16, 16, (32, 32))[0]
        self.S_WALL_EXPLORED = self.wall.get_image('d', 13, 16, 16, (32, 32))[0]

        self.S_WALL_0 = self.dungeonTiles.get_image('a', 0, 16, 16, (32, 32))[0]
        self.S_WALL_1 = self.dungeonTiles.get_image('c', 0, 16, 16, (32, 32))[0]
        self.S_WALL_2 = self.dungeonTiles.get_image('b', 0, 16, 16, (32, 32))[0]  # need wall piece
        self.S_WALL_3 = self.dungeonTiles.get_image('A', 4, 16, 16, (32, 32))[0]  # corner bot-left
        self.S_WALL_4 = self.dungeonTiles.get_image('e', 2, 16, 16, (32, 32))[0]  # need wall piece
        self.S_WALL_5 = self.dungeonTiles.get_image('e', 1, 16, 16, (32, 32))[0]
        self.S_WALL_6 = self.dungeonTiles.get_image('A', 0, 16, 16, (32, 32))[0]  # corner top-left
        self.S_WALL_7 = self.dungeonTiles.get_image('e', 3, 16, 16, (32, 32))[0]  # right (and left) side
        self.S_WALL_8 = self.dungeonTiles.get_image('a', 0, 16, 16, (32, 32))[0]  # need wall piece
        self.S_WALL_9 = self.dungeonTiles.get_image('e', 4, 16, 16, (32, 32))[0]  # corner bot-right
        self.S_WALL_10 = self.dungeonTiles.get_image('b', 0, 16, 16, (32, 32))[0]  # need wall piece
        self.S_WALL_11 = self.dungeonTiles.get_image('a', 0, 16, 16, (32, 32))[0]  # top side
        self.S_WALL_12 = self.dungeonTiles.get_image('e', 0, 16, 16, (32, 32))[0]  # corner top-right
        self.S_WALL_13 = self.dungeonTiles.get_image('A', 1, 16, 16, (32, 32))[0]  # left side
        self.S_WALL_14 = self.dungeonTiles.get_image('a', 4, 16, 16, (32, 32))[0]  # bot side
        self.S_WALL_15 = self.dungeonTiles.get_image('a', 4, 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_22 = self.dungeonTiles.get_image('e', 4, 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_33 = self.dungeonTiles.get_image('A', 4, 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_44 = self.dungeonTiles.get_image('e', 0, 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_55 = self.dungeonTiles.get_image('A', 0, 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_66 = self.dungeonTiles.get_image('c', 5, 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_77 = self.dungeonTiles.get_image('d', 5, 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_88 = self.dungeonTiles.get_image('e', 5, 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_99 = self.dungeonTiles.get_image('f', 0, 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_100 = self.dungeonTiles.get_image('f', 1, 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_111 = self.dungeonTiles.get_image('f', 3, 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_122 = self.dungeonTiles.get_image('f', 2, 16, 16, (32, 32))[0]  # room corner

        self.S_WALL_EXPLORED_0 = self.dungeonTiles.get_image('a', (0 + 10), 16, 16, (32, 32))[0]
        self.S_WALL_EXPLORED_1 = self.dungeonTiles.get_image('c', (0 + 10), 16, 16, (32, 32))[0]
        self.S_WALL_EXPLORED_2 = self.dungeonTiles.get_image('b', (0 + 10), 16, 16, (32, 32))[0]  # need wall piece
        self.S_WALL_EXPLORED_3 = self.dungeonTiles.get_image('A', (4 + 10), 16, 16, (32, 32))[0]  # corner bot-left
        self.S_WALL_EXPLORED_4 = self.dungeonTiles.get_image('e', (2 + 10), 16, 16, (32, 32))[0]  # need wall piece
        self.S_WALL_EXPLORED_5 = self.dungeonTiles.get_image('e', (1 + 10), 16, 16, (32, 32))[0]
        self.S_WALL_EXPLORED_6 = self.dungeonTiles.get_image('A', (0 + 10), 16, 16, (32, 32))[0]  # corner top-left
        self.S_WALL_EXPLORED_7 = self.dungeonTiles.get_image('e', (3 + 10), 16, 16, (32, 32))[0]  # right (and left) side
        self.S_WALL_EXPLORED_8 = self.dungeonTiles.get_image('a', (0 + 10), 16, 16, (32, 32))[0]  # need wall piece
        self.S_WALL_EXPLORED_9 = self.dungeonTiles.get_image('e', (4 + 10), 16, 16, (32, 32))[0]  # corner bot-right
        self.S_WALL_EXPLORED_10 = self.dungeonTiles.get_image('b', (0 + 10), 16, 16, (32, 32))[0]  # need wall piece
        self.S_WALL_EXPLORED_11 = self.dungeonTiles.get_image('a', (0 + 10), 16, 16, (32, 32))[0]  # top side
        self.S_WALL_EXPLORED_12 = self.dungeonTiles.get_image('e', (0 + 10), 16, 16, (32, 32))[0]  # corner top-right
        self.S_WALL_EXPLORED_13 = self.dungeonTiles.get_image('A', (1 + 10), 16, 16, (32, 32))[0]  # left side
        self.S_WALL_EXPLORED_14 = self.dungeonTiles.get_image('a', (4 + 10), 16, 16, (32, 32))[0]  # bot side
        self.S_WALL_EXPLORED_15 = self.dungeonTiles.get_image('a', (4 + 10), 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_EXPLORED_22 = self.dungeonTiles.get_image('e', (4 + 10), 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_EXPLORED_33 = self.dungeonTiles.get_image('A', (4 + 10), 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_EXPLORED_44 = self.dungeonTiles.get_image('e', (0 + 10), 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_EXPLORED_55 = self.dungeonTiles.get_image('A', (0 + 10), 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_EXPLORED_66 = self.dungeonTiles.get_image('c', (5 + 10), 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_EXPLORED_77 = self.dungeonTiles.get_image('d', (5 + 10), 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_EXPLORED_88 = self.dungeonTiles.get_image('e', (5 + 10), 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_EXPLORED_99 = self.dungeonTiles.get_image('f', (0 + 10), 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_EXPLORED_100 = self.dungeonTiles.get_image('f', (1 + 10), 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_EXPLORED_111 = self.dungeonTiles.get_image('f', (3 + 10), 16, 16, (32, 32))[0]  # room corner
        self.S_WALL_EXPLORED_122 = self.dungeonTiles.get_image('f', (2 + 10), 16, 16, (32, 32))[0]  # room corner

        self.S_FLOOR_0_f6 = self.dungeonTiles.get_image('f', 6, 16, 16, (32, 32))[0]
        self.S_FLOOR_0_f7 = self.dungeonTiles.get_image('f', 7, 16, 16, (32, 32))[0]
        self.S_FLOOR_0_f8 = self.dungeonTiles.get_image('f', 8, 16, 16, (32, 32))[0]
        self.S_FLOOR_0_g6 = self.dungeonTiles.get_image('g', 6, 16, 16, (32, 32))[0]
        self.S_FLOOR_0_g7 = self.dungeonTiles.get_image('g', 7, 16, 16, (32, 32))[0]
        self.S_FLOOR_0_g8 = self.dungeonTiles.get_image('g', 8, 16, 16, (32, 32))[0]
        self.S_FLOOR_0_h6 = self.dungeonTiles.get_image('h', 6, 16, 16, (32, 32))[0]
        self.S_FLOOR_0_h7 = self.dungeonTiles.get_image('h', 7, 16, 16, (32, 32))[0]
        self.S_FLOOR_0_h8 = self.dungeonTiles.get_image('h', 8, 16, 16, (32, 32))[0]
        self.S_FLOOR_0_i6 = self.dungeonTiles.get_image('i', 6, 16, 16, (32, 32))[0]
        self.S_FLOOR_0_i7 = self.dungeonTiles.get_image('i', 7, 16, 16, (32, 32))[0]
        self.S_FLOOR_0_i8 = self.dungeonTiles.get_image('i', 8, 16, 16, (32, 32))[0]

        self.S_FLOOR_1_a1 = self.dungeonTiles.get_image('a', 6, 16, 16, (32, 32))[0]
        self.S_FLOOR_1_b1 = self.dungeonTiles.get_image('b', 6, 16, 16, (32, 32))[0]
        self.S_FLOOR_1_c1 = self.dungeonTiles.get_image('c', 6, 16, 16, (32, 32))[0]
        self.S_FLOOR_1_d1 = self.dungeonTiles.get_image('d', 6, 16, 16, (32, 32))[0]

        self.S_FLOOR_2_e6 = self.dungeonTiles.get_image('e', 6, 16, 16, (32, 32))[0]
        self.S_FLOOR_2_e7 = self.dungeonTiles.get_image('e', 7, 16, 16, (32, 32))[0]
        self.S_FLOOR_2_e8 = self.dungeonTiles.get_image('e', 8, 16, 16, (32, 32))[0]

        self.S_FLOOR_3 = self.dungeonTiles.get_image('d', 1, 16, 16, (32, 32))[0]
        self.S_FLOOR_4_a3 = self.dungeonTiles.get_image('a', 7, 16, 16, (32, 32))[0]
        self.S_FLOOR_4_b3 = self.dungeonTiles.get_image('b', 7, 16, 16, (32, 32))[0]
        self.S_FLOOR_4_c3 = self.dungeonTiles.get_image('c', 7, 16, 16, (32, 32))[0]
        self.S_FLOOR_4_d3 = self.dungeonTiles.get_image('d', 7, 16, 16, (32, 32))[0]


        self.S_FLOOR_5 = self.dungeonTiles.get_image('b', 1, 16, 16, (32, 32))[0]
        self.S_FLOOR_6 = self.dungeonTiles.get_image('d', 3, 16, 16, (32, 32))[0]
        self.S_FLOOR_7 = self.dungeonTiles.get_image('d', 1, 16, 16, (32, 32))[0]
        self.S_FLOOR_8_A6 = self.dungeonTiles.get_image('A', 6, 16, 16, (32, 32))[0]
        self.S_FLOOR_8_A7 = self.dungeonTiles.get_image('A', 7, 16, 16, (32, 32))[0]
        self.S_FLOOR_8_A8 = self.dungeonTiles.get_image('A', 8, 16, 16, (32, 32))[0]

        self.S_FLOOR_9 = self.dungeonTiles.get_image('a', 1, 16, 16, (32, 32))[0]
        self.S_FLOOR_10 = self.dungeonTiles.get_image('a', 2, 16, 16, (32, 32))[0]
        self.S_FLOOR_11 = self.dungeonTiles.get_image('a', 1, 16, 16, (32, 32))[0]
        self.S_FLOOR_12 = self.dungeonTiles.get_image('a', 3, 16, 16, (32, 32))[0]
        self.S_FLOOR_13 = self.dungeonTiles.get_image('a', 1, 16, 16, (32, 32))[0]
        self.S_FLOOR_14 = self.dungeonTiles.get_image('a', 3, 16, 16, (32, 32))[0]
        self.S_FLOOR_15 = self.dungeonTiles.get_image('c', 2, 16, 16, (32, 32))[0]

        self.S_FLOOR_EXPLORED_0_f6 = self.dungeonTiles.get_image('f', (6 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_0_f7 = self.dungeonTiles.get_image('f', (7 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_0_f8 = self.dungeonTiles.get_image('f', (8 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_0_g6 = self.dungeonTiles.get_image('g', (6 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_0_g7 = self.dungeonTiles.get_image('g', (7 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_0_g8 = self.dungeonTiles.get_image('g', (8 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_0_h6 = self.dungeonTiles.get_image('h', (6 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_0_h7 = self.dungeonTiles.get_image('h', (7 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_0_h8 = self.dungeonTiles.get_image('h', (8 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_0_i6 = self.dungeonTiles.get_image('i', (6 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_0_i7 = self.dungeonTiles.get_image('i', (7 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_0_i8 = self.dungeonTiles.get_image('i', (8 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_1_a1 = self.dungeonTiles.get_image('a', (6 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_1_b1 = self.dungeonTiles.get_image('b', (6 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_1_c1 = self.dungeonTiles.get_image('c', (6 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_1_d1 = self.dungeonTiles.get_image('d', (6 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_2_e6 = self.dungeonTiles.get_image('e', (6 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_2_e7 = self.dungeonTiles.get_image('e', (7 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_2_e8 = self.dungeonTiles.get_image('e', (8 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_3 = self.dungeonTiles.get_image('d', (1 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_4_a3 = self.dungeonTiles.get_image('a', (7 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_4_b3 = self.dungeonTiles.get_image('b', (7 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_4_c3 = self.dungeonTiles.get_image('c', (7 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_4_d3 = self.dungeonTiles.get_image('d', (7 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_5 = self.dungeonTiles.get_image('b', (1 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_6 = self.dungeonTiles.get_image('d', (3 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_7 = self.dungeonTiles.get_image('d', (1 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_8_A6 = self.dungeonTiles.get_image('A', (6 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_8_A7 = self.dungeonTiles.get_image('A', (7 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_8_A8 = self.dungeonTiles.get_image('A', (8 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_9 = self.dungeonTiles.get_image('a', (1 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_10 = self.dungeonTiles.get_image('a', (2 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_11 = self.dungeonTiles.get_image('a', (1 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_12 = self.dungeonTiles.get_image('a', (3 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_13 = self.dungeonTiles.get_image('a', (1 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_14 = self.dungeonTiles.get_image('a', (3 + 10), 16, 16, (32, 32))[0]
        self.S_FLOOR_EXPLORED_15 = self.dungeonTiles.get_image('c', (2 + 10), 16, 16, (32, 32))[0]

        # ---> Items
        self.S_SCROLL_YELLOW = self.scroll.get_image('A', 0)
        self.S_SCROLL_GREEN = self.scroll.get_image('a', 0)
        self.S_SCROLL_RED = self.scroll.get_image('b', 0)
        self.S_SCROLL_BLUE = self.scroll.get_image('c', 0)
        self.S_SCROLL_BROWN = self.scroll.get_image('d', 0)
        self.S_SCROLL_WHITE = self.scroll.get_image('A', 1)
        self.S_SCROLL_GRAY = self.scroll.get_image('a', 1)
        self.S_SCROLL_MULTI = self.scroll.get_image('b', 1)
        self.S_GOLD = self.money.get_image('A', 0)

        # ---> Equipment
        self.S_SWORD_BRONZE = self.weapon.get_image('A', 0)
        self.S_SWORD_IRON = self.weapon.get_image('a', 0)
        self.S_SWORD_STEEL = self.weapon.get_image('b', 0)
        self.S_SWORD_BLACK = self.weapon.get_image('c', 0)
        self.S_SWORD_RUNE = self.weapon.get_image('d', 0)
        self.S_SPEAR_BRONZE = self.weapon.get_image('A', 1)
        self.S_SPEAR_IRON = self.weapon.get_image('a', 1)
        self.S_SPEAR_STEEL = self.weapon.get_image('b', 1)
        self.S_SPEAR_BLACK = self.weapon.get_image('c', 1)
        self.S_SPEAR_RUNE = self.weapon.get_image('d', 1)

        self.S_SHIELD_WOODEN = self.defence.get_image('A', 1)
        self.S_SHIELD_BRONZE = self.defence.get_image('A', 0)
        self.S_SHIELD_IRON = self.defence.get_image('a', 0)
        self.S_SHIELD_STEEL = self.defence.get_image('b', 0)
        self.S_SHIELD_BLACK = self.defence.get_image('c', 0)
        self.S_SHIELD_RUNE = self.defence.get_image('d', 0)

        # ---> Special
        self.S_STAIRS_UP = self.tile.get_image('a', 2, 16, 16, (32, 32))
        self.S_STAIRS_DOWN = self.tile.get_image('b', 2, 16, 16, (32, 32))

        self.S_MAIN_MENU = pygame.image.load(os.path.join("data", "graphics", "landscape.png")).convert()
        self.S_MAIN_MENU = pygame.transform.scale(self.S_MAIN_MENU, (constants.CAMERA_WIDTH, constants.CAMERA_HEIGHT))

        self.S_INVENTORY = pygame.image.load(os.path.join("data", "graphics", "menu", "inventory.png")).convert()
        self.S_INVENTORY_SELECT = \
            pygame.image.load(os.path.join("data", "graphics", "menu", "inventory_selected.png")).convert()
        self.S_GRAY_POPUP = pygame.image.load(os.path.join("data", "graphics", "menu", "gray_popup.png")).convert()

        self.S_MINI_WALL = pygame.Surface((2, 2))
        self.S_MINI_WALL.fill(pygame.Color("#d6871a"))
        self.S_MINI_WALL_EXPLORED = pygame.Surface((2, 2))
        self.S_MINI_WALL_EXPLORED.fill(pygame.Color("#6e4b1f"))

        self.S_MINI_FLOOR = pygame.Surface((2, 2))
        self.S_MINI_FLOOR.fill(pygame.Color("#fffef5"))
        self.S_MINI_FLOOR_EXPLORED = pygame.Surface((2, 2))
        self.S_MINI_FLOOR_EXPLORED.fill(pygame.Color("#abaa9f"))

        self.S_MINI_STAIRS = pygame.Surface((2, 2))
        self.S_MINI_STAIRS.fill(constants.COLOR_GREEN)
        self.S_MINI_PORTAL = pygame.Surface((2, 2))
        self.S_MINI_PORTAL.fill(pygame.Color("#64c4ed"))

        self.S_TOP_L_MENU_LIGHT = self.menugui.get_image('b1', 8, 16, 16, (32, 32))[0]
        self.S_TOP_R_MENU_LIGHT = self.menugui.get_image('e1', 8, 16, 16, (32, 32))[0]
        self.S_TOP_MENU_LIGHT = self.menugui.get_image('c1', 8, 16, 16, (32, 32))[0]
        self.S_BOT_L_MENU_LIGHT = self.menugui.get_image('b1', 10, 16, 16, (32, 32))[0]
        self.S_BOT_R_MENU_LIGHT = self.menugui.get_image('e1', 10, 16, 16, (32, 32))[0]
        self.S_BOT_MENU_LIGHT = self.menugui.get_image('c1', 10, 16, 16, (32, 32))[0]
        self.S_SIDE_L_MENU_LIGHT = self.menugui.get_image('b1', 9, 16, 16, (32, 32))[0]
        self.S_SIDE_R_MENU_LIGHT = self.menugui.get_image('e1', 9, 16, 16, (32, 32))[0]
        self.S_MID_MENU_LIGHT = self.menugui.get_image('c1', 9, 16, 16, (32, 32))[0]

        self.S_TOP_L_MENU_BROWN = self.menugui.get_image('b1', 14, 16, 16, (32, 32))[0]
        self.S_TOP_R_MENU_BROWN = self.menugui.get_image('e1', 14, 16, 16, (32, 32))[0]
        self.S_TOP_MENU_BROWN = self.menugui.get_image('c1', 14, 16, 16, (32, 32))[0]
        self.S_BOT_L_MENU_BROWN = self.menugui.get_image('b1', 16, 16, 16, (32, 32))[0]
        self.S_BOT_R_MENU_BROWN = self.menugui.get_image('e1', 16, 16, 16, (32, 32))[0]
        self.S_BOT_MENU_BROWN = self.menugui.get_image('c1', 16, 16, 16, (32, 32))[0]
        self.S_SIDE_L_MENU_BROWN = self.menugui.get_image('b1', 15, 16, 16, (32, 32))[0]
        self.S_SIDE_R_MENU_BROWN = self.menugui.get_image('e1', 15, 16, 16, (32, 32))[0]
        self.S_MID_MENU_BROWN = self.menugui.get_image('c1', 15, 16, 16, (32, 32))[0]

        self.S_SIDE_L_BUTTON_BLUE = self.menugui.get_image('c1', 1, 16, 16, (32, 32))[0]
        self.S_SIDE_R_BUTTON_BLUE = self.menugui.get_image('e1', 1, 16, 16, (32, 32))[0]
        self.S_MID_BUTTON_BLUE = self.menugui.get_image('d1', 1, 16, 16, (32, 32))[0]

        self.S_SIDE_L_BUTTON_BLUE_HOVER = self.menugui.get_image('y', 1, 16, 16, (32, 32))[0]
        self.S_SIDE_R_BUTTON_BLUE_HOVER = self.menugui.get_image('a1', 1, 16, 16, (32, 32))[0]
        self.S_MID_BUTTON_BLUE_HOVER = self.menugui.get_image('z', 1, 16, 16, (32, 32))[0]

        self.S_MAGIC_ROCK = self.special.get_image('a', 0)
        self.A_PORTAL_OPEN = self.door.get_animation('c', 6, 2, 16, 16, (32, 32))
        self.S_PORTAL_CLOSED = self.door.get_image('b', 6, 16, 16, (32, 32))

        self.S_TARGET_MARK = self.menugui.get_image('c1', 2, 16, 16, (32, 32))[0]

        # ---> GUI
        self.slider_button_size = (26, 20)
        self.slider_btn_path = os.path.join(
            "data", "graphics", "GUI", "buttons", "BTN_SLIDER_SM_(1).png")
        self.S_SLIDER_BUTTON = pygame.image.load(self.slider_btn_path).convert()
        self.S_SLIDER_BUTTON = pygame.transform.scale(self.S_SLIDER_BUTTON, self.slider_button_size)

        self.animation_dict = {
            "A_PLAYER_LEFT": self.A_PLAYER_LEFT,
            "A_PLAYER_RIGHT": self.A_PLAYER_RIGHT,
            "A_DUNGO": self.A_DUNGO,
            "A_DARKSOOT": self.A_DARKSOOT,
            "A_BLAZEO": self.A_BLAZEO,
            "A_KELPCLOPSE": self.A_KELPCLOPSE,
            "A_SHELK": self.A_SHELK,
            "A_ICESLIME": self.A_ICESLIME,
            "A_DEATH_RED": self.A_DEATH_RED,
            "A_DEATH_BLUE": self.A_DEATH_BLUE,
            "S_SCROLL_YELLOW": self.S_SCROLL_YELLOW,
            "S_SCROLL_GREEN": self.S_SCROLL_GREEN,
            "S_SCROLL_RED": self.S_SCROLL_RED,
            "S_SCROLL_BLUE": self.S_SCROLL_BLUE,
            "S_SCROLL_BROWN": self.S_SCROLL_BROWN,
            "S_SCROLL_WHITE": self.S_SCROLL_WHITE,
            "S_SCROLL_GRAY": self.S_SCROLL_GRAY,
            "S_SCROLL_MULTI": self.S_SCROLL_MULTI,
            "S_GOLD": self.S_GOLD,
            "S_SWORD_BRONZE": self.S_SWORD_BRONZE,
            "S_SWORD_IRON": self.S_SWORD_IRON,
            "S_SWORD_STEEL": self.S_SWORD_STEEL,
            "S_SWORD_BLACK": self.S_SWORD_BLACK,
            "S_SWORD_RUNE": self.S_SWORD_RUNE,
            "S_SPEAR_BRONZE": self.S_SPEAR_BRONZE,
            "S_SPEAR_IRON": self.S_SPEAR_IRON,
            "S_SPEAR_STEEL": self.S_SPEAR_STEEL,
            "S_SPEAR_BLACK": self.S_SPEAR_BLACK,
            "S_SPEAR_RUNE": self.S_SPEAR_RUNE,
            "S_SHIELD_WOODEN": self.S_SHIELD_WOODEN,
            "S_SHIELD_BRONZE": self.S_SHIELD_BRONZE,
            "S_SHIELD_IRON": self.S_SHIELD_IRON,
            "S_SHIELD_STEEL": self.S_SHIELD_STEEL,
            "S_SHIELD_BLACK": self.S_SHIELD_BLACK,
            "S_SHIELD_RUNE": self.S_SHIELD_RUNE,
            "S_STAIRS_UP": self.S_STAIRS_UP,
            "S_STAIRS_DOWN": self.S_STAIRS_DOWN,
            "S_MAGIC_ROCK": self.S_MAGIC_ROCK,
            "A_PORTAL_OPEN": self.A_PORTAL_OPEN,
            "S_PORTAL_CLOSED": self.S_PORTAL_CLOSED
        }

        self.wall_dict = {
            0: self.S_WALL_0,
            1: self.S_WALL_1,
            2: self.S_WALL_2,
            3: self.S_WALL_3,
            4: self.S_WALL_4,
            5: self.S_WALL_5,
            6: self.S_WALL_6,
            7: self.S_WALL_7,
            8: self.S_WALL_8,
            9: self.S_WALL_9,
            10: self.S_WALL_10,
            11: self.S_WALL_11,
            12: self.S_WALL_12,
            13: self.S_WALL_13,
            14: self.S_WALL_14,
            15: self.S_WALL_15,
            22: self.S_WALL_22,
            33: self.S_WALL_33,
            44: self.S_WALL_44,
            55: self.S_WALL_55,
            66: self.S_WALL_66,
            77: self.S_WALL_77,
            88: self.S_WALL_88,
            99: self.S_WALL_99,
            100: self.S_WALL_100,
            111: self.S_WALL_111,
            122: self.S_WALL_122,

        }

        self.wall_explored_dict = {
            0: self.S_WALL_EXPLORED_0,
            1: self.S_WALL_EXPLORED_1,
            2: self.S_WALL_EXPLORED_2,
            3: self.S_WALL_EXPLORED_3,
            4: self.S_WALL_EXPLORED_4,
            5: self.S_WALL_EXPLORED_5,
            6: self.S_WALL_EXPLORED_6,
            7: self.S_WALL_EXPLORED_7,
            8: self.S_WALL_EXPLORED_8,
            9: self.S_WALL_EXPLORED_9,
            10: self.S_WALL_EXPLORED_10,
            11: self.S_WALL_EXPLORED_11,
            12: self.S_WALL_EXPLORED_12,
            13: self.S_WALL_EXPLORED_13,
            14: self.S_WALL_EXPLORED_14,
            15: self.S_WALL_EXPLORED_15,
            22: self.S_WALL_EXPLORED_22,
            33: self.S_WALL_EXPLORED_33,
            44: self.S_WALL_EXPLORED_44,
            55: self.S_WALL_EXPLORED_55,
            66: self.S_WALL_EXPLORED_66,
            77: self.S_WALL_EXPLORED_77,
            88: self.S_WALL_EXPLORED_88,
            99: self.S_WALL_EXPLORED_99,
            100: self.S_WALL_EXPLORED_100,
            111: self.S_WALL_EXPLORED_111,
            122: self.S_WALL_EXPLORED_122,

        }

        self.floor_dict = {
            0: (self.S_FLOOR_0_f6, self.S_FLOOR_0_f7, self.S_FLOOR_0_f8,
                self.S_FLOOR_0_g6, self.S_FLOOR_0_g7, self.S_FLOOR_0_g8,
                self.S_FLOOR_0_h6, self.S_FLOOR_0_h7, self.S_FLOOR_0_h8,
                self.S_FLOOR_0_i6, self.S_FLOOR_0_i7, self.S_FLOOR_0_i8),

            1: (self.S_FLOOR_1_a1, self.S_FLOOR_1_b1, self.S_FLOOR_1_c1, self.S_FLOOR_1_d1,),
            2: (self.S_FLOOR_2_e6, self.S_FLOOR_2_e7, self.S_FLOOR_2_e8),
            3: self.S_FLOOR_3,
            4: (self.S_FLOOR_4_a3, self.S_FLOOR_4_b3, self.S_FLOOR_4_c3, self.S_FLOOR_4_d3),
            5: self.S_FLOOR_5,
            6: self.S_FLOOR_6,
            7: self.S_FLOOR_7,
            8: (self.S_FLOOR_8_A6, self.S_FLOOR_8_A7, self.S_FLOOR_8_A8),
            9: self.S_FLOOR_9,
            10: self.S_FLOOR_10,
            11: self.S_FLOOR_11,
            12: self.S_FLOOR_12,
            13: self.S_FLOOR_13,
            14: self.S_FLOOR_14,
            15: self.S_FLOOR_15,
        }

        self.floor_explored_dict = {
            0: (self.S_FLOOR_EXPLORED_0_f6, self.S_FLOOR_EXPLORED_0_f7, self.S_FLOOR_EXPLORED_0_f8,
                self.S_FLOOR_EXPLORED_0_g6, self.S_FLOOR_EXPLORED_0_g7, self.S_FLOOR_EXPLORED_0_g8,
                self.S_FLOOR_EXPLORED_0_h6, self.S_FLOOR_EXPLORED_0_h7, self.S_FLOOR_EXPLORED_0_h8,
                self.S_FLOOR_EXPLORED_0_i6, self.S_FLOOR_EXPLORED_0_i7, self.S_FLOOR_EXPLORED_0_i8),
            1: (self.S_FLOOR_EXPLORED_1_a1, self.S_FLOOR_EXPLORED_1_b1,
                self.S_FLOOR_EXPLORED_1_c1, self.S_FLOOR_EXPLORED_1_d1),
            2: (self.S_FLOOR_EXPLORED_2_e6, self.S_FLOOR_EXPLORED_2_e7, self.S_FLOOR_EXPLORED_2_e8),
            3: self.S_FLOOR_EXPLORED_3,
            4: (self.S_FLOOR_EXPLORED_4_a3, self.S_FLOOR_EXPLORED_4_b3,
                self.S_FLOOR_EXPLORED_4_c3, self.S_FLOOR_EXPLORED_4_d3),
            5: self.S_FLOOR_EXPLORED_5,
            6: self.S_FLOOR_EXPLORED_6,
            7: self.S_FLOOR_EXPLORED_7,
            8: (self.S_FLOOR_EXPLORED_8_A6, self.S_FLOOR_EXPLORED_8_A7, self.S_FLOOR_EXPLORED_8_A8),
            9: self.S_FLOOR_EXPLORED_9,
            10: self.S_FLOOR_EXPLORED_10,
            11: self.S_FLOOR_EXPLORED_11,
            12: self.S_FLOOR_EXPLORED_12,
            13: self.S_FLOOR_EXPLORED_13,
            14: self.S_FLOOR_EXPLORED_14,
            15: self.S_FLOOR_EXPLORED_15,
        }

        # =============================== AUDIO ================================== #

        #                             ||| Music |||

        self.main_menu_music = os.path.join("data", "audio", "music", "RPG-Blues_Looping.ogg")
        self.ingame_music = os.path.join(
            "data", "audio", "music", "Bog-Creatures-On-the-Move_Looping.ogg")

        #                          ||| Sound Effects |||
        self.sfx_list = []

        self.sfx_hit_punch1 = self.sfx_add("hit_punch_1.wav")
        self.sfx_hit_punch2 = self.sfx_add("hit_punch_2.wav")
        self.sfx_hit_punch3 = self.sfx_add("hit_punch_3.wav")
        self.sfx_hit_punch4 = self.sfx_add("hit_punch_4.wav")
        self.sfx_hit_punch5 = self.sfx_add("hit_punch_5.wav")

        self.sfx_click1 = self.sfx_add("click3.wav")
        self.sfx_rollover = self.sfx_add("rollover1.wav")
        self.sfx_coin_pickup = self.sfx_add("coin_pickup.wav")
        self.sfx_soul_consume = self.sfx_add("soul_consume.wav")
        self.sfx_pure_soul_consume = self.sfx_add("pure_soul_consume.wav")
        self.sfx_item_pickup = self.sfx_add("item_pickup.wav")
        self.sfx_level_up = self.sfx_add("glassbell_levelup.wav")

        # sfx list for hitting creature
        self.sfx_hit_punch_list = [self.sfx_hit_punch1,
                                   self.sfx_hit_punch2,
                                   self.sfx_hit_punch3,
                                   self.sfx_hit_punch4,
                                   self.sfx_hit_punch5]

        # adjust volume according to previous or default setting when first initialized
        self.volume_adjust()

    def sfx_add(self, file_name):
        """Loads a new sound effect and adds it to the master sfx list.

        Parameters
        ----------
        file_name : str
            The name of the desired sound effect's file.

        Returns
        -------
        pygame Sound obj
            The sound effect that was loaded in as a pygame Sound object.
        """
        new_sfx = pygame.mixer.Sound(os.path.join("data", "audio", "sfx", file_name))
        self.sfx_list.append(new_sfx)

        return new_sfx

    def volume_adjust(self):
        """Changes volume of all sfx audio and the music volume according to the settings.

        Returns
        -------
        None
        """
        for sfx in self.sfx_list:
            sfx.set_volume(globalvars.PREFERENCES.sfx_volume_val)

        pygame.mixer.music.set_volume(globalvars.PREFERENCES.music_volume_val)
