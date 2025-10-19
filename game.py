
import pygame
import random

class Board:
    def __init__(self, rows, columns, square_size):
        self.rows = rows
        self.columns = columns
        self.square_size = square_size
        self.pions = [[[] for _ in range(columns)] for _ in range(rows)]

    def draw_board(self, screen):
        for col in range(9, 14):
            pygame.draw.rect(screen, 'Green', (col * self.square_size, 7 * self.square_size, self.square_size, self.square_size))
        pygame.draw.rect(screen, 'Green', (13 * self.square_size, 8 * self.square_size, self.square_size, self.square_size))
        pygame.draw.rect(screen, 'Green', (9 * self.square_size, 9 * self.square_size, 6*self.square_size, 6*self.square_size), self.square_size)
        pygame.draw.polygon(screen, 'Green', [(7.5*self.square_size, 7.5*self.square_size), (9*self.square_size, 6*self.square_size), (9*self.square_size, 9*self.square_size)])
        
        for row in range(9, 14):
            pygame.draw.rect(screen, 'Yellow', (7 * self.square_size, row * self.square_size, self.square_size, self.square_size))
        pygame.draw.rect(screen, 'Yellow', (6 * self.square_size, 13 * self.square_size, self.square_size, self.square_size))
        pygame.draw.rect(screen, 'Yellow', (0, 9 * self.square_size, 6*self.square_size, 6*self.square_size), self.square_size)
        pygame.draw.polygon(screen, 'Yellow', [(7.5*self.square_size, 7.5*self.square_size), (6*self.square_size, 9*self.square_size), (9*self.square_size, 9*self.square_size)])   
        
        for col in range(1, 6):
            pygame.draw.rect(screen, 'Blue', (col * self.square_size, 7 * self.square_size, self.square_size, self.square_size))
        pygame.draw.rect(screen, 'Blue', (1 * self.square_size, 6 * self.square_size, self.square_size, self.square_size))
        pygame.draw.rect(screen, 'Blue', (0, 0, 6*self.square_size, 6*self.square_size), self.square_size)
        pygame.draw.polygon(screen, 'Blue', [(7.5*self.square_size, 7.5*self.square_size), (6*self.square_size, 6*self.square_size), (6*self.square_size, 9*self.square_size)])
        
        for row in range(1, 6):
            pygame.draw.rect(screen, 'Red', (7 * self.square_size, row * self.square_size, self.square_size, self.square_size))
        pygame.draw.rect(screen, 'Red', (8 * self.square_size, 1 * self.square_size, self.square_size, self.square_size))
        pygame.draw.rect(screen, 'Red', (9 * self.square_size, 0, 6*self.square_size, 6*self.square_size), self.square_size)
        pygame.draw.polygon(screen, 'Red', [(7.5*self.square_size, 7.5*self.square_size), (6*self.square_size, 6*self.square_size), (9*self.square_size, 6*self.square_size)])
        
        for row in range(6, 10):
            pygame.draw.line(screen, (0, 0, 0), (9*self.square_size, row * self.square_size), (screen.get_width(), row * self.square_size))
        for col in range(9, 15):
            pygame.draw.line(screen, (0, 0, 0), (col * self.square_size, 6*self.square_size), (col * self.square_size, 9*self.square_size))
        
        for col  in range(6, 10):
            pygame.draw.line(screen, (0, 0, 0), (col * self.square_size, 9*self.square_size), (col*self.square_size, screen.get_height()))
        for row in range(9, 15):
            pygame.draw.line(screen, (0, 0, 0), (6 * self.square_size, row * self.square_size), (9 * self.square_size, row * self.square_size))

        for col in range(6, 10):
            pygame.draw.line(screen, (0, 0, 0), (col * self.square_size, 6*self.square_size), (col*self.square_size, 0))
        for row in range(0, 7):
            pygame.draw.line(screen, (0, 0, 0), (6 * self.square_size, row * self.square_size), (9 * self.square_size, row * self.square_size))

        for row in range(6, 10):
            pygame.draw.line(screen, (0, 0, 0), (0, row * self.square_size), (6 * self.square_size, row * self.square_size))
        for col in range(0, 7):
            pygame.draw.line(screen, (0, 0, 0), (col * self.square_size, 6*self.square_size), (col * self.square_size, 9*self.square_size))
    

    def get_path_for_color(self, color):
        green_cases = [(x, 6) for x in range(9, 15)] + [(14, 7)] +[(x, 8) for x in range(14, 8, -1)]
        yellow_cases = [(8, y) for y in range(9, 15)] + [(7, 14)] +[(6, y) for y in range(14, 8, -1)]
        blue_cases = [(x, 8) for x in range(5, -1, -1)] + [(0, 7)] +[(x, 6) for x in range(0, 6)]
        red_cases = [(6, y) for y in range(5, -1, -1)] + [(7, 0)] +[(8, y) for y in range(0, 6)]

        if color == "Green":
            path = green_cases[8:] + yellow_cases + blue_cases + red_cases + green_cases[:7] + [(x, 7) for x in range(13, 7, -1)]
        elif color == "Yellow":
            path = yellow_cases[8:] + blue_cases + red_cases + green_cases + yellow_cases[:7] + [(7, y) for y in range(13, 7, -1)]
        elif color == "Blue":
            path = blue_cases[8:] + red_cases + green_cases + yellow_cases + blue_cases[:7] + [(x, 7) for x in range(1, 7)]
        elif color == "Red":
            path = red_cases[8:] + green_cases + yellow_cases + blue_cases + red_cases[:7] + [(7, y) for y in range(1, 7)]
        return path
    
    def get_home_square(self, color):
        if color == "Green":
            return (9, 9)
        elif color == "Yellow":
            return (0, 9)
        elif color == "Blue":
            return (0, 0)
        elif color == "Red":
            return (9, 0)


class Pion(pygame.rect.Rect):
    def __init__(self, color, position, board):
        super().__init__(position[0], position[1], 30, 30)  # Call the parent constructor
        self.color = color
        self.position = position  # position is a tuple (x, y)
        self.current_index = 0
        self.state = 'home'  # can be 'home', 'on_board', 'finished'
        self.board = board
        self.path = board.get_path_for_color(color)
        self.start_pos = self.path[0]
        self.finish_position = self.path[-1]
        self.pos_at_home = position

    def draw(self, screen, square_size, highlight=False):
        # center in pixels
        cx = self.position[0] * square_size + square_size // 2
        cy = self.position[1] * square_size + square_size // 2
        # Draw highlight ring (gold) behind the pawn when requested
        if highlight:
            pygame.draw.circle(screen, (200, 0, 200), (cx, cy), square_size // 3 + 6, 4)
        # Main drawing (pawn)
        pygame.draw.circle(screen, self.color,
                           (cx, cy),
                           square_size // 3)
        pygame.draw.circle(screen, (0, 0, 0),
                           (cx, cy),
                           square_size // 3, 2)
    
        
class Player:
    def __init__(self, color, start_positions, board):
        # board should be an instance of the board class (the game board)
        self.color = color
        self.start_positions = start_positions
        self.board = board
        # pass the board instance down to each pion so instance methods work
        self.pions = [Pion(color, pos, self.board) for pos in start_positions]
        self.star_square = self.get_star_square()
        self.score = 0
        self.list_of_rolls = []
        self.movable_pions = []
        self.highlight_rect = self.board.get_home_square(color)

    def draw(self, screen, square_size):
        for p in self.pions:
            highlight = p in self.movable_pions
            # call draw with highlight flag
            p.draw(screen, square_size, highlight=highlight)

    def get_star_square(self):

        if self.color == "Green":
            return(13, 8)
        elif self.color == "Yellow":
            return(6, 13)
        elif self.color == "Blue":
            return(1, 6)
        elif self.color == "Red":
            return(8, 1)

class Dice():
    def __init__(self, position, size):
        self.value = 1
        self.size = size
        self.position = position

    def roll(self):
        import random
        self.value = random.randint(1, 6)
        return self.value


import pygame

import pygame, random

class Game:
    def __init__(self):
        self.rows = 15
        self.columns = 15
        self.square_size = 600 // self.columns
        self.board = Board(self.rows, self.columns, self.square_size)
        self.players = [
            Player("Green", [(10, 10), (13, 10), (10, 13), (13, 13)], self.board),
            Player("Yellow", [(1, 10), (4, 10), (1, 13), (4, 13)], self.board),
            Player("Blue", [(1, 1), (4, 1), (1, 4), (4, 4)], self.board),
            Player("Red", [(10, 1), (13, 1), (10, 4), (13, 4)], self.board)
        ]
        self.dice = Dice((7*self.square_size, 7*self.square_size), self.square_size)

        # Chargement des images
        self.dice_anim_images = [
            pygame.transform.scale(pygame.image.load(f"images/{i}.png"), (self.dice.size, self.dice.size))
            for i in range(6)
        ]
        self.dice_value_images = [
            pygame.transform.scale(pygame.image.load(f"images/value_{i}.png"), (self.dice.size, self.dice.size))
            for i in range(1, 7)
        ]
        self.current_player_index = 0

    def draw(self, screen):
        self.board.draw_board(screen)
        for player in self.players:
            player.draw(screen, self.square_size)
        screen.blit(self.dice_value_images[self.dice.value - 1], self.dice.position)

    def check_click(self, element):
        mouse_pos = pygame.mouse.get_pos()
        element_rect = pygame.Rect((element.position[0], element.position[1]), (self.square_size, self.square_size))
        return element_rect.collidepoint(mouse_pos)

    def dice_roll(self, screen):
        # Petite animation fluide
        for _ in range(6):
            random_img = random.choice(self.dice_anim_images)
            screen.blit(random_img, self.dice.position)
            pygame.display.flip()
            pygame.time.wait(80)
        value = self.dice.roll()
        screen.blit(self.dice_value_images[value - 1], self.dice.position)
        pygame.display.flip()
        return value

    def play_turn(self, screen):
        player = self.players[self.current_player_index]
        print(player.highlight_rect)
        waiting_for_roll = True

        while waiting_for_roll:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return "quit"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.check_click(self.dice):
                        roll = self.dice_roll(screen)
                        print(f"{player.color} rolled {roll}")
                        waiting_for_roll = False
                        # Tu peux ensuite déplacer le pion ici
                        self.move_pawn(player, roll)
                        if roll == 6:
                            pass
                        else:
                            self.current_player_index = (self.current_player_index + 1) % len(self.players)

            # Toujours redessiner le plateau
            screen.fill((255, 255, 255))
            self.draw(screen)
            pygame.draw.rect(screen, (200, 0, 200), (player.highlight_rect[0]*self.square_size, player.highlight_rect[1]*self.square_size, 6*self.square_size, 6*self.square_size), 4)
            pygame.display.flip()

    def move_pawn(self, player, roll):
        """Permet au joueur de choisir un pion et de le déplacer selon le dé."""
        pion = None
        selected_pawn = None
        screen = pygame.display.get_surface()

        for p in player.pions:
            if p.state == 'home' and roll == 6:
                player.movable_pions.append(p)
            elif p.state == 'on_board' and (p.current_index + roll) < len(p.path):
                player.movable_pions.append(p)
        
        print(f"{player.color} has {len(player.movable_pions)} movable pawns.")

        # If no pawn can move, exit early
        if len(player.movable_pions) == 0:
            print(f"{player.color} has no valid pawns to move.")
            return 'quit'

        # If exactly one pawn can move, auto-select it (no need to wait for click)
        if len(player.movable_pions) == 1 or all(p.state == 'home' for p in player.movable_pions) or all(p.position == player.movable_pions[0].position for p in player.movable_pions):
            selected_pawn = player.movable_pions[0]
            print(f"Only one movable pawn. Auto-selected {player.color} pawn at {selected_pawn.position}")

        # 🎯 Étape 1 — attendre que le joueur clique sur un pion (only if multiple to choose)
        while selected_pawn is None and len(player.movable_pions) > 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return "quit"
                # if len(player.movable_pions) == 1:
                #     selected_pawn = player.movable_pions[0]
                #     print(f"Only one movable pawn. Auto-selected {player.color} pawn at {selected_pawn.position}")
                #     break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("Click detected, checking pawns...")
                    mouse_pos = pygame.mouse.get_pos()
                    for pawn in player.movable_pions:
                        # pawn.position stores board/grid coordinates (col, row).
                        # Multiply by square_size to get pixel coordinates for click detection.
                        pawn_rect = pygame.Rect((pawn.position[0] * self.square_size, pawn.position[1] * self.square_size), (self.square_size, self.square_size))
                        if pawn_rect.collidepoint(mouse_pos):
                            print(f"Pawn at {pawn.position} clicked.")
                            selected_pawn = pawn
                            print(f"{player.color} selected pawn at {pawn.position}")
                            break            
            
            # Redessiner pendant l’attente
            screen.fill((255, 255, 255))
            self.draw(screen)
            pygame.draw.rect(screen, (200, 0, 200), (player.highlight_rect[0]*self.square_size, player.highlight_rect[1]*self.square_size, 6*self.square_size, 6*self.square_size), 4)
            pygame.display.flip()

        # 🎯 Étape 2 — déplacement du pion sélectionné
        if selected_pawn is not None:
            pion = selected_pawn

        if pion is None:
            # Nothing selected (for safety)
            print('No pawn selected, aborting move.')
            return

        if pion.state == 'home' and roll == 6:
            pion.state = 'on_board'
            pion.position = pion.start_pos
            #self.board.pions[pion.position[0]][pion.position[1]].append(pion)
            # Ensure current_index matches the position on the path
            try:
                pion.current_index = pion.path.index(pion.position)
            except ValueError:
                pion.current_index = 0

        elif pion.state == 'on_board':
            # Remove pion from current board position
            self.board.pions[pion.position[0]][pion.position[1]].remove(pion)

            pion.current_index = pion.path.index(pion.position)
            if (pion.current_index + roll) <= len(pion.path) - 1:
                for _ in range(roll):
                    # Vérifie que le pion ne dépasse pas la fin du chemin
                    pion.current_index = pion.path.index(pion.position)
                    pion.current_index += 1
                    pion.position = pion.path[pion.current_index]

                    # Vérifie si le pion atteint la position finale
                    if pion.position == pion.finish_position:
                        pion.state = 'finished'
                        player.score += 1
                        print(f"{player.color} has moved a pawn to the finish! Score: {player.score}")

                    # Animation du déplacement
                    screen.fill((255, 255, 255))
                    self.draw(screen)
                    pygame.draw.rect(screen, (200, 0, 200), (player.highlight_rect[0]*self.square_size, player.highlight_rect[1]*self.square_size, 6*self.square_size, 6*self.square_size), 4)
                    pygame.display.flip()
                    pygame.time.wait(150)
        
        # Ajouter le pion à sa nouvelle position sur le plateau            
        self.board.pions[pion.position[0]][pion.position[1]].append(pion)
        for p in self.board.pions[pion.position[0]][pion.position[1]]:
            if p not in player.pions:
                
                # Remove captured pawn from board
                self.board.pions[p.position[0]][p.position[1]].remove(p)

                # Animation de la descente du pion capturé
                index = p.current_index
                for _ in range(index, -1, -1):
                    p.current_index -= 1
                    p.position = p.path[p.current_index]
                    screen.fill((255, 255, 255))
                    self.draw(screen)
                    pygame.display.flip()
                    pygame.time.wait(50)
                
                # Modifie la position et l'etat du pioncapturé
                p.state = 'home'
                p.position = p.pos_at_home
                print(f"{player.color} captured a pawn!")
        
        # Mettre à jour la liste des pions mobiles du joueur
        player.movable_pions.clear()
        # 🎯 Étape 3 — rafraîchir l’écran
        screen.fill((255, 255, 255))
        self.draw(screen)
        pygame.display.flip()
