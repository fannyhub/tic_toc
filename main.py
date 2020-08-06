from enum import Enum


class Symbol(Enum):
    CIRCLE = 'o'
    CROSS = 'x'


class Game:
    """
    class for ttt game
    """

    def __init__(self):

        self.status = list(range(9))
        self.display_board()
        self.symbol = Symbol.CIRCLE

    def toggle_symbol(self):
        if self.symbol == Symbol.CIRCLE:
            self.symbol = Symbol.CROSS
        else:
            self.symbol = Symbol.CIRCLE

    def display_board(self):
        graph = ''
        for i in range(0, 9, 3):
            graph += f'|{self.status[i]}|{self.status[i + 1]}|{self.status[i + 2]}|\n'
        print(graph)

    def fill_square(self, s, symbol):
        if not s.isdigit():
            return False
        i = int(s)
        if i not in range(9):
            return False
        if self.status[i] in (Symbol.CIRCLE.value, Symbol.CROSS.value):
            return False
        else:
            self.status[i] = symbol.value
            return True

    def check_game_status(self):
        for i in range(0, 9, 3):
            if len(set(self.status[i:i + 3])) == 1:
                print(self.status[i:i + 2])
                return self.status[i]
        for i in range(3):
            if len({self.status[i], self.status[i + 3], self.status[i + 6]}) == 1:
                return self.status[i]
        if len(set(self.status[::4])) == 1 and self.status[0]:
            return self.status[0]
        if len({self.status[2], self.status[4], self.status[6]}) == 1:
            return self.status[2]
        return None


if __name__ == '__main__':
    game = Game()
    game.winner = None
    turns = 1
    while not game.winner:
        s = input('pick the square number:\n')
        success = game.fill_square(s, game.symbol)
        if not success:
            print('you have provided wrong value or this square is already taken')
            continue
        game.winner = game.check_game_status()
        game.toggle_symbol()
        game.display_board()
        turns += 1
        if turns > 9:
            print('truce')
            break
    else:
        print(f'{game.winner} won')
