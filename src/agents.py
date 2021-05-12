import random

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