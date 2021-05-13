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

class titForTwoTats:
    def __init__(self):
        self.roundHistory = []
    
    def __str__(self):
        return "Tit for Two Tats"
    
    def playRound(self, opponentMoves):
        if len(self.roundHistory) <= 1:
            self.roundHistory.append(True)
            return True

        if opponentMoves[-1] == False and opponentMoves[-2] == False:
            self.roundHistory.append(False)
            return False
        self.roundHistory.append(True)
        return True

class grudger:
    def __init__(self):
        self.roundHistory = []
    
    def __str__(self):
        return "Grudger"
    
    def playRound(self, opponentMoves):
        c = not False in opponentMoves
        self.roundHistory.append(c)
        return c

class pavlov:
    def __init__(self):
        self.roundHistory = []

    def __str__(self):
        return "Pavlov"

    def playRound(self, opponentMoves):
        if len(opponentMoves) == 0:
            self.roundHistory.append(True)
            return True
        if opponentMoves[-1] == True and self.roundHistory[-1] == False or opponentMoves[-1] == False and self.roundHistory[-1] == True:
            self.roundHistory.append(False)
            return False
        self.roundHistory.append(True)
        return True

class nPavlov:
    def __init__(self):
        self.roundHistory = []
        self.P = [] #probabilities of cooperation
        self.n = 0
    
    def __str__(self):
        return "n-Pavlov"
    
    def f(self, op,x,y):
        if op == '+':
            return min(x+y,1)
        elif op == '-':
            return max(x-y,0)

    def playRound(self, opponentMoves):
        self.n += 1
        if len(opponentMoves) == 0:
            self.P.append(1)
            self.roundHistory.append(True)
            return True
        if opponentMoves[-1] and self.roundHistory[-1]:
            Pn = self.f('+',self.P[-1],1/self.n)
        elif not opponentMoves[-1] and not self.roundHistory[-1]:
            Pn = self.f('-', self.P[-1], 1/self.n)
        elif not self.roundHistory[-1] and opponentMoves[-1]:
            Pn = self.f('+',self.P[-1],2/self.n)
        elif self.roundHistory[-1] and not opponentMoves[-1]:
            Pn = self.f('-', self.P[-1], 2/self.n)
        c = random.random() < Pn
        self.P.append(Pn)
        self.roundHistory.append(c)
        return c

class alternator:
    def __init__(self):
        self.roundHistory = []
    
    def __str__(self):
        return "Alternating strategy"
    
    def playRound(self, opponentMoves):
        c = len(opponentMoves)%2 == 0
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