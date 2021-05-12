import random

R = 3
S = 0
T = 5
P = 1

class unconditionalCooperator:
    def __init__(self):
        self.roundHistory = []
    
    def __str__(self):
        return "Unconditional Cooperation"
    
    def playRound(self, opponentMoves):
        self.roundHistory.append(True)
        return True   #cooperate

class unconditionalDefector:
    def __init__(self):
        self.roundHistory = []
    
    def __str__(self):
        return "Unconditional Defection"
    
    def playRound(self, opponentMoves):
        self.roundHistory.append(False)
        return False   #defect


class randomChoice:
    def __init__(self):
        self.roundHistory = []
    
    def __str__(self):
        return "Random Choice"
    
    def playRound(self, opponentMoves):
        c = random.choice([True, False])
        self.roundHistory.append(c)
        return c   #cooperate

class titForTat:
    def __init__(self):
        self.roundHistory = []
    
    def __str__(self):
        return "Tit for tat"
    
    def playRound(self, opponentMoves):
        #cooperate on first move
        if len(self.roundHistory) == 0:
            self.roundHistory.append(True)
            return True

        self.roundHistory.append(opponentMoves[len(self.roundHistory)-1])
        return opponentMoves[-1] #return last move by opponent

class susTitForTat:
    def __init__(self):
        self.roundHistory = []
    
    def __str__(self):
        return "Suspicious Tit for tat"
    
    def playRound(self, opponentMoves):
        #Defect on first move
        if len(self.roundHistory) == 0:
            self.roundHistory.append(False)
            return False

        self.roundHistory.append(opponentMoves[len(self.roundHistory)-1])
        return opponentMoves[-1] #return last move by opponent

class genTitForTat:
    def __init__(self):
        self.roundHistory = []
    
    def __str__(self):
        return "Generous Tit for Tat"
    
    def playRound(self, opponentMoves):
        if len(opponentMoves) == 0:
            self.roundHistory.append(True)
            return True
        if opponentMoves[-1]:
            self.roundHistory.append(True)
            return True
        c = random.random() < min(1 - (T-R)/(R-S), (R-P)/(T-P))
        self.roundHistory.append(c)
        return c

class imperfectTitForTat:
    def __init__(self):
        self.roundHistory = []
    
    def __str__(self):
        return "Imperfect Tit for tat"
    
    def playRound(self, opponentMoves):
        #cooperate on first move
        if len(self.roundHistory) == 0:
            self.roundHistory.append(True)
            return True
        lastMove = opponentMoves[-1]
        if random.random() < 0.9:
            c = lastMove
        else:
            c = not lastMove
        self.roundHistory.append(c)
        return c
'''
 3 3     0 5

 5 0     1 1


 R R      S T
 T S      P  P
R = 3
S = 0
T = 5
P = 1
'''