import sys
from PyQt5.QtWidgets import *

class ConnectGameGUI(QMainWindow):
    def __init__(self, rows=6, columns=7):
        super().__init__()
        self.rows = rows
        self.columns = columns
        self.board = [[' ' for _ in range(columns)] for _ in range(rows)]
        self.current_player = 0
        self.players = []
        self.scores = {}
        self.winning_combination = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Connect Game")
        self.setGeometry(100, 100, 800, 600)

        # Get player information
        self.get_player_info()

        # Main UI setup
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layouts
        self.main_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()
        self.status_label = QLabel(f"{self.players[0]}'s Turn ({self.players[0]})")
        self.main_layout.addWidget(self.status_label)
        self.main_layout.addLayout(self.grid_layout)
        self.central_widget.setLayout(self.main_layout)

        # Create the game board
        self.buttons = [[QPushButton(' ') for _ in range(self.columns)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.columns):
                self.buttons[r][c].setFixedSize(80, 80)
                self.grid_layout.addWidget(self.buttons[r][c], r, c)
                self.buttons[r][c].clicked.connect(lambda _, row=r, col=c: self.make_move(row, col))

        self.highlight_valid_moves()

    def get_player_info(self):
        """Prompt the user to input the number of players and assign markers or names."""
        while True:
            num_players, ok = QInputDialog.getInt(
                self, "Number of Players", "Enter number of players (2 or 3):", 2, 2, 3
            )
            if ok:
                self.players = []
                for i in range(num_players):
                    name, ok = QInputDialog.getText(self, f"Player {i + 1}", "Enter your name or marker:")
                    if ok and name:
                        self.players.append(name)
                        self.scores[name] = 0
                break
        QMessageBox.information(self, "Players Set", f"{num_players} players: {', '.join(self.players)}")

    def make_move(self, row, col):
        """Handle player move at a specific cell."""
        if self.board[row][col] != ' ' or (row < self.rows - 1 and self.board[row + 1][col] == ' '):
            return

        # Place the move
        self.board[row][col] = self.players[self.current_player]
        self.buttons[row][col].setText(self.players[self.current_player])

        # Check for a winner
        if self.check_win(self.players[self.current_player]):
            self.highlight_winning_combination()
            self.show_winner(self.current_player + 1)
            return
        elif all(self.board[r][c] != ' ' for r in range(self.rows) for c in range(self.columns)):
            self.show_draw()
            return

        # Switch to the next player
        self.current_player = (self.current_player + 1) % len(self.players)
        self.status_label.setText(f"{self.players[self.current_player]}'s Turn ({self.players[self.current_player]})")
        self.highlight_valid_moves()

    def check_win(self, marker):
        """Check for a winning condition."""
        for r in range(self.rows):
            for c in range(self.columns - 3):
                if all(self.board[r][c + i] == marker for i in range(4)):
                    self.winning_combination = [(r, c + i) for i in range(4)]
                    return True
        for c in range(self.columns):
            for r in range(self.rows - 3):
                if all(self.board[r + i][c] == marker for i in range(4)):
                    self.winning_combination = [(r + i, c) for i in range(4)]
                    return True
        for r in range(self.rows - 3):
            for c in range(self.columns - 3):
                if all(self.board[r + i][c + i] == marker for i in range(4)):
                    self.winning_combination = [(r + i, c + i) for i in range(4)]
                    return True
                if all(self.board[r + 3 - i][c + i] == marker for i in range(4)):
                    self.winning_combination = [(r + 3 - i, c + i) for i in range(4)]
                    return True
        return False

    def highlight_valid_moves(self):
        """Highlight all valid cells for the current player."""
        for r in range(self.rows):
            for c in range(self.columns):
                if self.board[r][c] == ' ' and (r == self.rows - 1 or self.board[r + 1][c] != ' '):
                    self.buttons[r][c].setStyleSheet("background-color: lightgreen;")
                else:
                    self.buttons[r][c].setStyleSheet("")

    def highlight_winning_combination(self):
        """Highlight the winning combination."""
        for r, c in self.winning_combination:
            self.buttons[r][c].setStyleSheet("background-color: gold; color: black;")

    def show_winner(self, player):
        winner = self.players[player - 1]
        self.scores[winner] += 1
        QMessageBox.information(self, "Game Over", f"{winner} wins! Current Scores: {self.scores}")
        self.reset_game()

    def show_draw(self):
        QMessageBox.information(self, "Game Over", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        """Reset the board for a new game."""
        self.board = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.columns):
                self.buttons[r][c].setText(' ')
                self.buttons[r][c].setStyleSheet("")
        self.current_player = 0
        self.status_label.setText(f"{self.players[0]}'s Turn ({self.players[0]})")
        self.highlight_valid_moves()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = ConnectGameGUI()
    game.show()
    sys.exit(app.exec_())
