import random

class Sheep():
    def __init__(self, grid):
        while True:
            self.XY = [random.randint(0, 31), random.randint(0,31)]

            #Respawn if within pen
            if not (14 <= self.XY[0] <= 16 and 14 <= self.XY[1] <= 16):
                break

        grid.sheepXY = self.XY

    def distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def move(self, grid):
        possibleMoves = [[self.XY[0], self.XY[1]+1], [self.XY[0], self.XY[1]-1],
                         [self.XY[0]+1, self.XY[1]], [self.XY[0]-1, self.XY[1]]]
        moves = []

        #Check that sheep doesn't move to blocked or outside the grid cell
        for move in possibleMoves:
            if (0<=move[0]<31 and 0<=move[1]<31 and
                grid.XY[move[0]][move[1]] == 0):
                moves.append(move)

        #Check if bot is within sheep's field of view
        if (abs(self.XY[0]-grid.botXY[0]) <= 5 and
            abs(self.XY[1]-grid.botXY[1]) <= 5):
            #Pick the move that is closest to the bot
            lowest = 1000
            bestMove = None
            for move in moves:
                if self.distance(move, grid.botXY) < lowest:
                    bestMove = move
                    lowest = self.distance(move, grid.botXY)

            self.XY = bestMove
            grid.sheepXY = self.XY
        else:
            #Pick any random valid move
            self.XY = random.choice(moves)
            grid.sheepXY = self.XY

        #Check if sheep moved into the center of the pen:
        if self.XY == [15, 15]:
            return True


class Sheepdog1():
    #Initialize Sheepdog1
    def __init__(self, grid):
        self.grid = grid
        self.states = [(sheepdogX, sheepdogY, xSheep, ySheep)
                       for sheepdogX in range(31)
                       for sheepdogY in range(31)
                       for xSheep in range(31)
                       for ySheep in range(31)]
        #Create ranges for sheepdog to move 

        self.V = {state: 0 for state in self.states}
        self.choose = {state: random.choice(['up', 'down', 'left', 'right', 'diagonalLU', 'diagonalRU', 'diagonalLD', 'diagonalRD']) for state in self.states}
        #Discount factor 
        self.discount = 0.99
        self.diff = 0.01
        #Create Bellman equation
    def bellman(self, state):
        ev = [self.V[self.getNext(state, action)] for action in self.choose[state]]
        self.V[state] = self.discount*max(ev) + self.reward(state)
    #Calculate state reward
    def reward(self, state):
        sheepdogX, sheepdogY, xSheep, ySheep = state
        length2pen = abs(sheepdogX - 15) + abs(sheepdogY - 15)
        r = length2pen - self.grid.distance((sheepdogX, sheepdogY), (xSheep, ySheep))
        return r
    #Update values through value iteration 
    def value_iteration(self):
        for _ in range(1000000):  
            x = 0
            for state in self.states:
                old = self.V[state]
                self.bellman(state)
                x = max(x, abs(old - self.V[state]))
    #Convergence check
            if x < self.diff:
                break

    def getNext(self, state, action):
        sheepdogX, sheepdogY, xSheep, ySheep = state
        nextX, nextY = self.move_bot(sheepdogX, sheepdogY, action)
        return nextX, nextY, xSheep, ySheep
    #Max expected value 
    def evMax(self, state):
        ev = [self.V[self.getNext(state, action)] for action in self.choose[state]]
        return max(ev)

    def updateChoice(self):
        for state in self.states:
            actionMax = max(self.choose[state], key=lambda action: self.V[self.getNext(state, action)])
            self.choose[state] = actionMax
    #Move options for robot
    def move_bot(self, x, y, action):
        if action == 'up' and y > 0 and y < 31:
            y -= 1
        elif action == 'down' and y < 31 and y > 0:
            y += 1
        elif action == 'left' and x > 0 and x < 31:
            x -= 1
        elif action == 'right' and x < 31 and x > 0:
            x += 1
        elif action == 'diagonalLU' and x > 0 and y > 0 and  x < 31 and y < 31:
            x -= 1
            y -= 1
        elif action == 'diagonalRU' and x < 31 and y > 0 and y < 31:
            x += 1
            y -= 1
        elif action == 'diagonalLD' and x > 0 and y < 31 and x < 31 and y > 0:
            x -= 1
            y += 1
        elif action == 'diagonalRD' and x < 31 and y < 31 and x > 0 and y > 0:
            x += 1
            y += 1
        return x, y
    #pick a policy
    def chooseAction(self, state):
        return self.choose[state]

    def move(self, grid):
        sheepdogX, sheepdogY, xSheep, ySheep = self.grid.botXY[0], self.grid.botXY[1], grid.sheepXY[0], grid.sheepXY[1]
        state = (sheepdogX, sheepdogY, xSheep, ySheep)
        opt = self.chooseAction(state)

        nextX, nextY = self.move_bot(sheepdogX, sheepdogY, opt)
        self.grid.botXY = (nextX, nextY)

        return False
    


class Sheepdog2():
    def __init__(self, grid):
        while True:
            self.XY = [random.randint(0, 31), random.randint(0,31)]

            #Respawn if within pen or spawned onto sheep
            if not (14 <= self.XY[0] <= 16 and 14 <= self.XY[1] <= 16
                    or grid.sheepXY == self.XY):
                break

        grid.botXY = self.XY

    def move(self, grid):
        #Check if sheep moved onto bot during sheep's turn
        if self.XY == grid.sheepXY:
            return True


        pass

class Sheepdog3():
    def __init__(self, grid):
        while True:
            self.XY = [random.randint(0, 31), random.randint(0,31)]

            #Respawn if within pen or spawned onto sheep
            if not (14 <= self.XY[0] <= 16 and 14 <= self.XY[1] <= 16
                    or grid.sheepXY == self.XY):
                break

        grid.botXY = self.XY

    def move(self, grid):
        #Check if sheep moved onto bot during sheep's turn
        if self.XY == grid.sheepXY:
            return True


        pass
