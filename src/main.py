import agents
import inspect
import sys

strategies = inspect.getmembers(sys.modules["agents"], inspect.isclass)

a = agents.unconditionalCooperator()
print(a.roundHistory)