import pygame
import sys


pygame.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)


WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS

 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("❌⭕ لعبة XO - أحمد صلاح")


font = pygame.font.SysFont(None, 100)
small_font = pygame.font.SysFont(None, 50)


board = [[None]*BOARD_COLS for _ in range(BOARD_ROWS)]
current_player = "X"
game_over = False

def draw_lines():
    
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE * 2, 0), (SQUARE_SIZE * 2, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE * 2), (WIDTH, SQUARE_SIZE * 2), LINE_WIDTH)

def draw_symbols():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            symbol = board[row][col]
            if symbol == "X":
                text = font.render("X", True, RED)
                screen.blit(text, (col * SQUARE_SIZE + 60, row * SQUARE_SIZE + 40))
            elif symbol == "O":
                text = font.render("O", True, BLUE)
                screen.blit(text, (col * SQUARE_SIZE + 60, row * SQUARE_SIZE + 40))

def check_win(player):
    
    for row in range(BOARD_ROWS):
        if all(board[row][col] == player for col in range(BOARD_COLS)):
            return True
    
    for col in range(BOARD_COLS):
        if all(board[row][col] == player for row in range(BOARD_ROWS)):
            return True

    if all(board[i][i] == player for i in range(BOARD_ROWS)):
        return True
    if all(board[i][BOARD_ROWS - i - 1] == player for i in range(BOARD_ROWS)):
        return True
    return False

def restart_game():
    global board, current_player, game_over
    board = [[None]*BOARD_COLS for _ in range(BOARD_ROWS)]
    current_player = "X"
    game_over = False
    screen.fill(WHITE)
    draw_lines()

screen.fill(WHITE)
draw_lines()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] is None:
                board[clicked_row][clicked_col] = current_player

                if check_win(current_player):
                    game_over = True
                else:
                    current_player = "O" if current_player == "X" else "X"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()

    screen.fill(WHITE)
    draw_lines()
    draw_symbols()

    if game_over:
        text = small_font.render(f"{current_player} to return!enter Press R", True, BLACK)
        screen.blit(text, (30, HEIGHT // 2 - 20))

    pygame.display.update()
