import pygame
import sys

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (0, 0, 255)
BLUE = (0, 128, 0)

# Set up the display
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe developed by Zia")

# Set up the grid
grid_size = 3
cell_size = WIDTH // grid_size
board = [['' for _ in range(grid_size)] for _ in range(grid_size)]

# Player turn
player = 'X'

# Game over flag
game_over = False

# Font for displaying text
font = pygame.font.SysFont(None, 50)


def draw_grid():
    """Draws the grid lines on the screen."""
    for i in range(1, grid_size):
        pygame.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, HEIGHT), 2)
        pygame.draw.line(screen, BLACK, (0, i * cell_size), (WIDTH, i * cell_size), 2)


def draw_symbols():
    """Draws the 'X' and 'O' symbols on the board."""
    for row in range(grid_size):
        for col in range(grid_size):
            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (col * cell_size + 10, row * cell_size + 10),
                                 ((col + 1) * cell_size - 10, (row + 1) * cell_size - 10), 5)
                pygame.draw.line(screen, RED, (col * cell_size + 10, (row + 1) * cell_size - 10),
                                 ((col + 1) * cell_size - 10, row * cell_size + 10), 5)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLUE, (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2),
                                  cell_size // 2 - 5, 5)


def check_win():
    """Checks for a winning condition."""
    # Check rows
    for row in board:
        if row == ['X'] * grid_size:
            return 'X'
        elif row == ['O'] * grid_size:
            return 'O'

    # Check columns
    for col in range(grid_size):
        if all(board[row][col] == 'X' for row in range(grid_size)):
            return 'X'
        elif all(board[row][col] == 'O' for row in range(grid_size)):
            return 'O'

    # Check diagonals
    if all(board[i][i] == 'X' for i in range(grid_size)):
        return 'X'
    elif all(board[i][i] == 'O' for i in range(grid_size)):
        return 'O'
    if all(board[i][grid_size - 1 - i] == 'X' for i in range(grid_size)):
        return 'X'
    elif all(board[i][grid_size - 1 - i] == 'O' for i in range(grid_size)):
        return 'O'

    # Check for a draw
    if all(cell != '' for row in board for cell in row):
        return 'Draw'

    return None


def display_message(message):
    """Displays a message on the screen."""
    text_surface = font.render(message, True, BLACK)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)

winner = None

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print(mouse_x, mouse_y)
            row = mouse_y // cell_size
            col = mouse_x // cell_size
            if board[row][col] == '':
                board[row][col] = player
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'

    screen.fill(WHITE)
    draw_grid()
    draw_symbols()
    
    if game_over == False:
        winner = check_win()
    
    if winner != None and winner != 'Draw':
        game_over = True
        display_message(f"{winner} wins!")
    elif winner == 'Draw':
        game_over = True
        display_message("It's a Draw!")
        
    pygame.display.update()
