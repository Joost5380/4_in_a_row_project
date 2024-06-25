# aantaal rijen
row_count = 6
# aantal kolummen
column_count = 7

# De grootte van een vakje
SQUARESIZE = 100
# De breedte van het bord
width = column_count * SQUARESIZE
# De hoogte van het bord
height = (row_count + 1) * SQUARESIZE
# De afmetingen
size = (width, height)
# De strall van de steentje
RADIUS = int(SQUARESIZE / 2 - 5)

# De kleuren
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# De scores die worden bijgehouden voor het algoritme
MINI, MAX = -1000, 1000