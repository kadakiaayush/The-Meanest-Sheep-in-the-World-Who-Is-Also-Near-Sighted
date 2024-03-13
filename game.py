class Grid:
    def __init__(self):
        self.XY = [[0 for x in range(31)] for y in range(31)]

        for x in range(14, 17):
            for y in range(14, 17):
                self.XY[x][y] = 1
        self.XY[14][15], self.XY[15][15] = 0, 0

        self.sheepXY, self.botXY = None, (0, 0)  # Initialize botXY to a default value

    def printGrid(self):
        for x in range(31):
            for y in range(31):
                if [x, y] == self.sheepXY:
                    print("S", end = ' ')
                elif [x, y] == self.botXY:
                    print("B", end = ' ')
                else:
                    print(self.XY[x][y], end = ' ')
            print()
        print()


class Game:
    def __init__(self):
        self.grid = Grid()
        self.turns = 0
        self.sheep, self.bot = None, None

    def run(self, numSteps):
        #self.grid.printGrid()

        for i in range(numSteps):
            self.turns += 1

            #print("Turn #" + str(self.turns))

            if self.sheep.move(self.grid): return 1
            if self.bot.move(self.grid): return 0

            #self.grid.printGrid()
