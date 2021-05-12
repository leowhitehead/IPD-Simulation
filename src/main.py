import agents
import inspect
import sys

strategies = inspect.getmembers(sys.modules["agents"], inspect.isclass)

def playRound(agentA, agentB):
    AChoice = agentA.playRound(agentB.roundHistory)
    BChoice = agentB.playRound(agentA.roundHistory[:-1]) #prevent from knowing current move
    return AChoice, BChoice

a = agents.unconditionalCooperator()
b = agents.unconditionalDefector()
c = agents.titForTat()
d = agents.randomChoice()
e = agents.imperfectTitForTat()
for i in range(10):
    print(f"Round {i}:", playRound(c,e))


'''
 3 3     0 5

 5 0     1 1


 R R      S T
 T S      P  P

'''