import pygame

pygame.init()
# Colors
LIGHTBLUE = (72, 128, 247)
AZURE = (240, 255, 255)
DARK_GREY = (169, 169, 169)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (34, 177, 76)
PINK = (255, 174, 201)
PANTONE = (98, 100, 102)

WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

FPS = 240

TILESIZE = 64
TEXT_LAYER = 4
PLAYER_LAYER = 3
BLOCK_LAYER = 2
GROUND_LAYER = 1

PLAYER_SPEED = 3


# MAP  150x100xTILESIZE px

tilemap = """
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
B..............TTT.................................................................................B
B..............TTT.................................................................................B
B..............TTT...........................................................TTT...................B
B..............TTT.........................................................TTTTTTT...TTT...........B
B........e.....TTT.........................................D..............TTTD..TTT..TTTT..........B
B..............TTT............TTTTTT..TTTT............TTTTTT.............TTT.....TTTTT.TTT.........B
B..............TTT..........TTTTTTTTTTTTTTTD.........TTTTTTTTT....TTTTTTTTT......TTTTT...TTT.......B
B..............TTTD......TTTTT......TTT..TTT....TTTTTTTT...TTTTTTTTTTTTTTT.................TTT.....B
B..........a...TTT.....TTTTT..............TTT..TTTTTT.......TTTTTT.........................TTT.....B
B...............TTT...TTTT.................TTTTTT...........TTT............................DTTT....B
B................TTTTTTT.....................TTTD...........TTT............................TTT.....B
B................TTTTTT.....................................TTT...........................TTT......B
B....................TT.....................................TTT..........................TTT.......B
B....................TT.....................................TTTTTTTTT............TTT...TTTT........B
B...................TTT......P..............OOOOO............TTTTTTTTTTTT........TTTTTTTTTT........B
B.................TTTT................OOOOOOWWWWWWOOOOOOOO.........TTTTTTT.....TTTDTTTTT...........B
B...............TTTTD.........OOOOOOOOOWWWWWWWWWWWWWWWWWWOOOOOOO........TTT...TTT..................B
B..............TTT......OOOOOOWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWOOOO......TTTTTT...................B
B..............TTT..OOOOOWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWOOOOOO..TTTT....................B
B.............TTT..OWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWO..TTTOOOOOOOOOOOOOOOOOOOOB
B............TTT...OWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWOODTTTOOOOOOOOOOOOOOOOOOOOB
B...........TTT.....OOOOOOWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
B..........TTT.......OOWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWOOOTTTOOOOOOOOOOOOOOOOOOOOB
B...........TTT......OOWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWO...TTTTD.................B
B............TTT....OOWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWO...TTT...................B
B............TTT.....OOWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWOO...TTT....................B
B...........TTTD........OOWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWOOOOOOOO...TTT....................B
B..........TTT............OOOOOWWWWWWWWWWWWWWWWWWWWWWWWWWWWOOOOOOO......TTTTTT.....................B
B.........TTT.................OOOOOOOOOOOWWWWWWWWWWWWWOOOOO....TTTTTTTTTTTTTTD.....................B
B.........TTTD...........................OOOOOOOOOOOOO.......TTTTTTTTTTTTTTT.......................B
B..........TTT............................................TTTTTTD..................................B
B...........TTT.........................................TTTTT......................................B
B............TTT......................................TTTD.TT......................................B
B...........DTTT......................................TTTTTT.......................................B
B............TTT...................................DTTTTTTTT.......................................B
B.............TTT..............TTT................TTTT...TTT.......................................B
B..............TTTTD.........TTTTTTT...........TTTTTTT...TTT.......................................B
B...............TTTTT......TTTTTTTTTTD.........TTTT.......TTT......................................B
B................TTTTTTTTTTTT.....TTTTTTT......TTTD........TTTT....................................B
B...................TTTTTTTD.........TTTTTTTTTTT.............TTTT..................................B
B.......................................TTTTTTTT..............TTTTT................................B
B...........................................DTTTD................TTTT..............................B
B............................................TTTT..................TTTT............................B
B............................................TTTT....................TTT...........................B
B.............................................TTTT....................TTT..........................B
B.............................................TTTT....................TTT..........................B
B.............................................TTTT.....................TTT.........................B
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
B..................................................................................................B
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
"""
tilemap = tilemap.split()
# for i in range(len(tilemap)):
#     for j in range(len(tilemap[0])):
#         if tilemap[i][j] == "O":
#             print(f"row: {i}\ncolumn: {j}")
