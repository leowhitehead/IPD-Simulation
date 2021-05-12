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


