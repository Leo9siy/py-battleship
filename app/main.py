class Deck:
    def __init__(self, row: int, column: int, is_alive: bool = True) -> None:
        self.row = row
        self.column = column
        self.is_alive = is_alive


class Ship:
    def __init__(self, start: tuple, end: tuple,
                 is_drowned: bool = False) -> None:
        if start[0] == end[0]:
            self.decks = [Deck(start[0], y)
                          for y in range(start[1], end[1] + 1)]
        else:
            self.decks = [Deck(x, start[1])
                          for x in range(start[0], end[0] + 1)]

        self.is_drowned = is_drowned

    def get_deck(self, row: int, column: int) -> Deck | None:
        for deck in self.decks:
            if deck.row == row and deck.column == column:
                return deck
        return None

    def fire(self, row: int, column: int) -> str:
        deck = self.get_deck(row, column)
        if deck.is_alive:
            deck.is_alive = False

            for deck in self.decks:
                if deck.is_alive:
                    return "Hit!"

            self.is_drowned = True
            return "Sunk!"
        return "Already dead"


class Battleship:
    def __init__(self, ships: list[tuple]) -> None:
        self.ships = [Ship(ship_tuple[0], ship_tuple[1])
                      for ship_tuple in ships]

    def fire(self, location: tuple) -> str:
        for ship in self.ships:
            if ship.get_deck(location[0], location[1]) is not None:
                return ship.fire(location[0], location[1])
        return "Miss!"

    def check_ship(self, row: int, column: int) -> str:
        for ship in self.ships:
            if ship.get_deck(row, column) is not None:
                if ship.is_drowned:
                    return "x"
                else:
                    if ship.get_deck(row, column).is_alive:
                        return "□"
                    return "*"
        return "~"

    def print_field(self) -> None:
        for x_cord in range(11):
            line = ""
            for y_cord in range(11):
                line += self.check_ship(x_cord, y_cord) + " "
            print(line)
