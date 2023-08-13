import pygame

class ChessGame:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Set up the display
        self.screen = pygame.display.set_mode((350, 350))
        pygame.display.set_caption("KongMingQi")

        self.board_info = [
            [-1, -1, 1, 1, 1, -1, -1],
            [-1, -1, 1, 1, 1, -1, -1],
            [1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1],
            [-1, -1, 1, 1, 1, -1, -1],
            [-1, -1, 1, 1, 1, -1, -1]
        ]

        self.color = [(0, 0, 0), (0, 128, 0), (128, 0, 0), (255, 255, 255)]

    def display_board(self):
        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Draw the board
        for row in range(7):
            for col in range(7):
                # Draw the squares
                if self.board_info[row][col] == 1:
                    pygame.draw.circle(self.screen, self.color[3], (row*50+25, col*50+25), radius=20)
                    pygame.draw.circle(self.screen, self.color[1], (row*50+25, col*50+25), radius=15)
                elif self.board_info[row][col] == 0:
                    pygame.draw.circle(self.screen, self.color[3], (row*50+25, col*50+25), radius=20)
                elif self.board_info[row][col] == 2:
                    pygame.draw.circle(self.screen, self.color[3], (row*50+25, col*50+25), radius=20)
                    pygame.draw.circle(self.screen, self.color[2], (row*50+25, col*50+25), radius=15)
        pygame.display.flip()

    def show_popup(self, message):
        popup_font = pygame.font.Font(None, 36)
        popup_text = popup_font.render(message, True, (255, 255, 255))
        popup_rect = popup_text.get_rect(center=(200, 200))
        pygame.draw.rect(self.screen, (0, 0, 0), popup_rect)
        self.screen.blit(popup_text, popup_rect)
        pygame.display.flip()
    
    def victory_check(self):
        count = 0
        for i in range(7):
            for j in range(7):
                if self.board_info[i][j] == 1 or self.board_info[i][j] == 2:
                    count += 1
        if count == 1:
            self.show_popup("Congratulation, WIN!")
    
    def play(self):
        self.display_board()
        # pick a spot that doesn't matter
        selected = [2, 2]
        while(True):
            self.victory_check()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    clicked_row = event.pos[0] // 50
                    clicked_col = event.pos[1] // 50
                    if self.board_info[clicked_row][clicked_col] == 1:
                        self.board_info[selected[0]][selected[1]] = 1
                        selected[0] = clicked_row
                        selected[1] = clicked_col
                        self.board_info[clicked_row][clicked_col] = 2
                    elif self.board_info[clicked_row][clicked_col] == 0:
                        if abs(selected[0] - clicked_row) == 2 and (selected[1] == clicked_col):
                            clean_row = int((selected[0] + clicked_row) / 2)
                            clean_col = int((selected[1] + clicked_col) / 2)
                            if self.board_info[clean_row][clean_col] == 1:
                                self.board_info[selected[0]][selected[1]] = 0
                                self.board_info[clean_row][clean_col] = 0
                                self.board_info[clicked_row][clicked_col] = 2
                                selected[0] = clicked_row
                                selected[1] = clicked_col
                        elif abs(selected[1] - clicked_col) == 2 and (selected[0] == clicked_row):
                            clean_row = int((selected[0] + clicked_row) / 2)
                            clean_col = int((selected[1] + clicked_col) / 2)
                            if self.board_info[clean_row][clean_col] == 1:
                                self.board_info[selected[0]][selected[1]] = 0
                                self.board_info[clean_row][clean_col] = 0
                                self.board_info[clicked_row][clicked_col] = 2
                                selected[0] = clicked_row
                                selected[1] = clicked_col
                    self.display_board()

# Create and start the game
game = ChessGame()
game.play()


