import pygame, random, math, socket

# Initialize Pygame
pygame.init()

# Initialisation de la connexion
HOST = 'localhost'
PORT = 5000

# Set the screen size
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Dominos")

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# Set the font
font = pygame.font.SysFont('Calibri', 25, True, False)

# Function to create the initial set of tiles
def create_tiles():
    tiles = []
    for i in range(7):
        for j in range(i, 7):
            tiles.append((i, j))
    return tiles

# Function to shuffle the tiles
def shuffle_tiles(tiles):
    random.shuffle(tiles)
    return tiles

# Create the tiles and shuffle them

tiles = create_tiles()
tiles = shuffle_tiles(tiles)

# Deal the tiles to the players
player1_tiles = []
player2_tiles = []
player3_tiles = []
player4_tiles = [] 
computer_tiles = []

# Set up the board tiles
board_tiles = []

# Set up the players' scores
player1_score = 0
player2_score = 0
player3_score = 0
player4_score = 0
computer_score = 0

turn=0

menu_done = False

# Function to draw the game menu
def draw_menu():
    # Clear the screen
    screen.fill(WHITE)
    # Draw the board

    pygame.draw.rect(screen, BLACK, (500, 0, 500, 1000))

    pygame.draw.circle(screen, BLACK, (250, 200), 150)
    pygame.draw.circle(screen, WHITE, (750, 600), 150)

    text1 = font.render("Héberger une partie", True, WHITE)
    text2 = font.render("Rejoindre une partie", True, BLACK)

    screen.blit(text1, (140, 175))
    screen.blit(text2, (640, 575))

    pygame.display.update()

def choose_menu():
    choose_made = False
    while not choose_made:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                sqx1 = (pos[0] - 250)**2
                sqy1 = (pos[1] - 200)**2
                sqx2 = (pos[0] - 750)**2
                sqy2 = (pos[1] - 600)**2
                if math.sqrt(sqx1 + sqy1) < 150: 
                    draw_host_menu()
                    return choose_number_players()
                elif math.sqrt(sqx2 + sqy2) < 150:
                    choose_made = True

def draw_host_menu():
    # Clear the screen
    screen.fill(WHITE)
    # Draw the board

    pygame.draw.rect(screen, BLACK, (500, 0, 500, 1000))

    pygame.draw.circle(screen, WHITE, (750, 200), 30)
    pygame.draw.circle(screen, WHITE, (750, 300), 30)
    pygame.draw.circle(screen, WHITE, (750, 400), 30)
    pygame.draw.circle(screen, WHITE, (750, 500), 30)

    text1 = font.render("Choix du nombre de joueurs", True, BLACK)
    text2 = font.render("1", True, BLACK)
    text3 = font.render("2", True, BLACK)
    text4 = font.render("3", True, BLACK)
    text5 = font.render("4", True, BLACK)

    screen.blit(text1, (100, 350))
    screen.blit(text2, (745, 185))
    screen.blit(text3, (745, 285))
    screen.blit(text4, (745, 385))
    screen.blit(text5, (745, 485))
    
    pygame.display.update()

def choose_number_players():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                sqx1 = (pos[0] - 750)**2
                sqy1 = (pos[1] - 200)**2
                sqx2 = (pos[0] - 750)**2
                sqy2 = (pos[1] - 400)**2
                sqx3 = (pos[0] - 750)**2
                sqy3 = (pos[1] - 600)**2
                sqx4 = (pos[0] - 750)**2
                sqy4 = (pos[1] - 800)**2
                if math.sqrt(sqx1 + sqy1) < 30: 
                    deal_tiles(1)
                    return 1
                # elif math.sqrt(sqx2 + sqy2) < 30:
                #     connexion(2)
                #     deal_tiles(2)
                #     return 2
                # elif math.sqrt(sqx3 + sqy3) < 30:
                #     connexion(3)
                #     deal_tiles(3)
                #     return 3
                # elif math.sqrt(sqx4 + sqy4) < 30:
                #     connexion(4)
                #     deal_tiles(4)
                #     return 4

# def connexion(nb_joueurs):
#     waiting_screen()
#     # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # server_socket.bind((HOST, PORT))
#     # server_socket.listen()
#     # print('Attente de connexion des joueurs...')
#     # player1, address1 = server_socket.accept()
#     # print('Joueur 1 connecté:', address1)
#     # player1.send('Vous êtes le joueur 1'.encode())

#     # player2, address2 = server_socket.accept()
#     # print('Joueur 2 connecté:', address2)
#     # player2.send('Vous êtes le joueur 2'.encode())

# def waiting_screen():
#     screen.fill(WHITE)
#     # Draw the board

#     pygame.draw.rect(screen, BLACK, (500, 0, 500, 1000))

#     text1 = font.render("Choix du nombre de joueurs", True, BLACK)

#     screen.blit(text1, (340, 400))
    
#     pygame.display.update()

def deal_tiles(nb_players):
    global player1_tiles, computer_tiles, tiles
    
    if nb_players == 1:
        player1_tiles = tiles[:7]
        computer_tiles = tiles[7:14]
        tiles = tiles[14:]
        # return player1_tiles, computer_tiles, tiles
    elif nb_players == 2:
        player1_tiles = tiles[:7]
        player2_tiles = tiles[7:14]
        tiles = tiles[14:]
        # return player1_tiles, player2_tiles, tiles
    elif nb_players == 3:
        player1_tiles = tiles[:7]
        player2_tiles = tiles[7:14]
        player3_tiles = tiles[14:21]
        tiles = tiles[21:]
        # return player1_tiles, player2_tiles, player3_tiles, tiles
    elif nb_players == 4:
        player1_tiles = tiles[:7]
        player2_tiles = tiles[7:14]
        player3_tiles = tiles[14:21]
        player3_tiles = tiles[21:28]
        tiles = tiles[28:]
        # return player1_tiles, player2_tiles, player3_tiles, player4_tiles, tiles

# Function to draw the board and tiles
def draw_board(player1_tiles, player2_tiles, board_tiles):
    # Clear the screen
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (0, 660, 1000, 5))

    # Draw the tiles on the board
    for i, tile in enumerate(board_tiles):
        if i > 15:
            pygame.draw.rect(screen, BLACK, (30+(i-16)*60, 370, 50, 100), 2)
            text = font.render(str(tile[0])+'-'+str(tile[1]), True, BLACK)
            screen.blit(text, (31+(i-16)*60, 385))
        elif i > 30:
            pygame.draw.rect(screen, BLACK, (30+(i-31)*60, 480, 50, 100), 2)
            text = font.render(str(tile[0])+'-'+str(tile[1]), True, BLACK)
            screen.blit(text, (31+(i-31)*60, 495))
        else:
            pygame.draw.rect(screen, BLACK, (30+i*60, 260, 50, 100), 2)
            text = font.render(str(tile[0])+'-'+str(tile[1]), True, BLACK)
            screen.blit(text, (31+i*60, 275))
    
    # Draw the player 1's tiles
    for i, tile in enumerate(player1_tiles):
        pygame.draw.rect(screen, BLACK, (15+i*60, 680, 50, 100), 2)
        text = font.render(str(tile[0])+'-'+str(tile[1]), True, BLACK)
        screen.blit(text, (20+i*60, 695))
            

    # Draw the player 2's tiles
    for i, tile in enumerate(player2_tiles):
        pygame.draw.rect(screen, BLACK, (15+i*60, 15, 50, 100))

    # Update the screen
    pygame.display.update()
    
    



# Function to determine the winner
def determine_winner(player1_tiles, player2_tiles):
    player1_score = sum([tile[0]+tile[1] for tile in player1_tiles])
    player2_score = sum([tile[0]+tile[1] for tile in player2_tiles])
    if player1_score < player2_score:
        return "Player 1 wins!"
    elif player2_score < player1_score:
        return "Player 2 wins!"
    else:
        return "It's a tie!"

# Function to check if a move is valid
def is_valid_move(tile, board_tiles):
    if len(board_tiles) == 0:
        return True
    else:
        left_value = board_tiles[0][0]
        right_value = board_tiles[-1][1]
        return tile[0] == left_value or tile[1] == left_value or tile[0] == right_value or tile[1] == right_value

def get_valid_moves(tiles, board_tiles):
    valid_moves = []
    for tile in tiles:
        if tile[0] == board_tiles[0][0] or tile[1] == board_tiles[0][0]:
            valid_moves.append(tile)
        if tile[0] == board_tiles[-1][1] or tile[1] == board_tiles[-1][1]:
            valid_moves.append(tile)
    return valid_moves
    
# Function to get the player's move
def get_player_move(player_tiles, board_tiles):
    valid_moves = [tile for tile in player_tiles if is_valid_move(tile, board_tiles)]
    print("PLAYER 1 valid moves:",valid_moves)
    move_made = False
    if len(valid_moves)==0 and len(tiles) > 0:
        player1_draw(player1_tiles)
    elif len(valid_moves)>0 and len(player1_tiles) > 0:
        while not move_made:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for i, tile in enumerate(player_tiles):
                        print(i,"clic position:",pos[0],"/",pos[1],"in:", 100+i*60,"!", 150+i*60)
                        if 15+i*60 < pos[0] < 65+i*60 and 680 < pos[1] < 780 and (tile in valid_moves):
                            player_tiles.remove(tile)
                            if len(board_tiles) == 0:
                                board_tiles.append(tile)
                            else:
                                # print(board_tiles[0][0],"/",board_tiles[-1][1], "tile 0/1:",tile[0],tile[1])
                                left_value = board_tiles[0][0]
                                right_value = board_tiles[-1][1]
                                if tile[0] == left_value:
                                    board_tiles.insert(0, (tile[1], tile[0]))
                                # move_tile=1
                                elif tile[1] == right_value:
                                    board_tiles.append( (tile[1], tile[0]))
                                # move_tile=1
                                elif tile[1] == left_value:
                                    board_tiles.insert(0, tile)
                                elif tile[0] == right_value:
                                    board_tiles.append(tile)
                            move_made = True
                            break

    draw_board(player1_tiles, player2_tiles, board_tiles)


# Function to get the computer's move
def get_computer_move(computer_tiles, board_tiles):
    valid_moves = [tile for tile in computer_tiles if is_valid_move(tile, board_tiles)]
    print("PLAYER 2 valid moves:",valid_moves)
    if len(valid_moves)==0 and len(tiles) > 0:
        player2_draw(computer_tiles ,board_tiles)
    elif len(valid_moves) > 0 and len(computer_tiles) > 0:
        tile_to_play = valid_moves[0]
        computer_tiles.remove(tile_to_play)
        
        if len(board_tiles) == 0:
            board_tiles.append(tile_to_play)
        else:
            left_value = board_tiles[0][0]
            right_value = board_tiles[-1][1]
            if tile_to_play[0] == left_value:
                board_tiles.insert(0, (tile_to_play[1], tile_to_play[0]))
            elif tile_to_play[1] == right_value:
                board_tiles.append((tile_to_play[1], tile_to_play[0]))
            elif tile_to_play[1] == left_value:
                board_tiles.insert(0, tile_to_play)
            elif tile_to_play[0] == right_value:
                board_tiles.append(tile_to_play)
    draw_board(player1_tiles, player2_tiles, board_tiles)
    print("end computer turn")
    
def player1_draw(player1_tiles):
    # Player can't make a move, draw from the pile
    print("len tiles:",len(tiles))
    if len(tiles) > 0:
        pygame.draw.rect(screen, BLACK, (780, 680, 200, 100), 2)
        text = font.render("PIOCHER", True, BLACK)
        screen.blit(text, (816, 712))
        pygame.display.update()
        draw_made = False
        while not draw_made:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if 780 < pos[0] < 980 and 680 < pos[1] < 780: 
                        player1_tiles.append(tiles.pop())
                        draw_made = True

def player2_draw(player2_tiles, board_tiles):
    # Computer can't make a move, draw from the pile
    if len(get_valid_moves(player2_tiles, board_tiles)) == 0 and len(player2_tiles) > 0:
        if len(tiles) > 0:
            player2_tiles.append(tiles.pop())


def random_turn(nb_players):
    if nb_players == 1:
        return random.randint(0, 1)
    else:
        return random.randint(nb_players-nb_players+1, nb_players)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Menu
    while not menu_done:
        draw_menu()
        nb_players = choose_menu()
        turn = random_turn(nb_players)
        menu_done = True

    print(turn)
    # Player 1's turn
    if len(player1_tiles) > 0 and turn == 1:
        if nb_players == 1:
            turn = 0
        else:
            turn = 2
        draw_board(player1_tiles, computer_tiles, board_tiles)
        get_player_move(player1_tiles, board_tiles)
        if len(player1_tiles) == 0:
            player1_score = sum([tile[0]+tile[1] for tile in player1_tiles])

    # Computer's turn
    elif len(computer_tiles) > 0 and turn == 0:
        print("tour du joueur 2 ...")
        
        turn=1
        draw_board(player1_tiles, computer_tiles, board_tiles)
        pygame.time.wait(1000)
        get_computer_move(computer_tiles, board_tiles)
        if len(computer_tiles) == 0:
            computer_score = sum([tile[0]+tile[1] for tile in computer_tiles])

    # Game over
    else:
        draw_board(player1_tiles, computer_tiles, board_tiles)
        winner = determine_winner(player1_tiles, computer_tiles)
        print(winner)
        pygame.time.wait(3000)
        pygame.quit()
        exit()

    # Determine if the game is over
    if len(tiles) == 0 and len(board_tiles) == 0:
        # Game over
        draw_board(player1_tiles, computer_tiles, board_tiles)
        winner = determine_winner(player1_tiles, computer_tiles)
        print(winner)
        pygame.time.wait(5000)
        pygame.quit()
        exit()

    