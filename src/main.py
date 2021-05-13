import agents
import inspect
import sys
from pprint import pprint

strategies = inspect.getmembers(sys.modules["agents"], inspect.isclass)

def ave(l):
    return sum(l)/len(l)

def playRound(agentA, agentB):
    AChoice = agentA.playRound(agentB.roundHistory)
    BChoice = agentB.playRound(agentA.roundHistory[:-1]) #prevent from knowing current move
    return AChoice, BChoice

def compareStrats(stratA, stratB):
    aResults = []
    bResults = []
    for i in range(10):
        aPoints = []
        bPoints = []
        a = stratA()
        b = stratB()
        for j in range(250):
            aChoice, bChoice = playRound(a,b)
            if aChoice and bChoice:
                aPoints.append(3)
                bPoints.append(3)
            elif aChoice and not bChoice:
                aPoints.append(0)
                bPoints.append(5)
            elif not aChoice and bChoice:
                aPoints.append(5)
                bPoints.append(0)
            else:
                aPoints.append(1)
                bPoints.append(1)
        aResults.append(sum(aPoints))
        bResults.append(sum(bPoints))
    return ave(aResults), ave(bResults), str(a)

results = []
for i in strategies:
    res = []
    for j in strategies:
        a, _, name = compareStrats(i[1], j[1])
        res.append(a)
    results.append( (name, round(ave(res),2)) )

pprint(sorted(results, key = lambda x: x[1])[::-1])

    


'''
 3 3     0 5

 5 0     1 1


 R R      S T
 T S      P  P

'''