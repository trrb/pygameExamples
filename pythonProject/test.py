class SeaMap:
    def __init__(self):
        self.map = [['.' for _ in range(10)] for _ in range(10)]
        self.ships = set()

    def shoot(self, row, col, result):
        if result == 'miss':
            self.map[row][col] = '*'
        elif result == 'hit':
            self.map[row][col] = 'x'
        elif result == 'sink':
            self.map[row][col] = 'x'
            self._mark_sunk_ship(row, col)
        self._mark_nearby_cells(row, col)

    def cell(self, row, col):
        return self.map[row][col]

    def _mark_sunk_ship(self, row, col):
        self.ships.add((row, col))
        while self.ships:
            (r, c) = self.ships.pop()
            for (i, j) in [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]:
                if 0 <= i < 10 and 0 <= j < 10 and self.map[i][j] == 'x':
                    self.ships.add((i, j))
                    self.map[i][j] = '*'

    def _mark_nearby_cells(self, row, col):
        for (i, j) in [(row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)]:
            if 0 <= i < 10 and 0 <= j < 10 and self.map[i][j] == '.':
                self.map[i][j] = '*'
