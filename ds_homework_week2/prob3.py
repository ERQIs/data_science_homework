# 0 means strating point, 1 means end point
# argv: men, sheep, wolf, vegetable

doneState = [0] * 16
answers = []
route = []

def DFS(men, sheep, wolf, vegetable):
    if (men == 1 and sheep == 1 and wolf == 1 and vegetable == 1):
        answers.append(route[:])
        return
    if ((vegetable == sheep or wolf == sheep) and sheep != men):
        return
    stateIdx = (men<<3) + (sheep<<2) + (wolf<<1) + vegetable
    if (doneState[stateIdx] == 1):
        return
    else:
        doneState[stateIdx] = 1

    if (men == sheep):
        route.append("sheep " + str(sheep) + "->" + str(not sheep))
        DFS(not men, not sheep, wolf, vegetable)
        route.pop()
    if (men == wolf):
        route.append("wolf " + str(wolf) + "->" + str(not wolf))
        DFS(not men, sheep, not wolf, vegetable)
        route.pop()
    if (men == vegetable):
        route.append("vegetable " + str(vegetable) + "->" + str(not vegetable))
        DFS(not men, sheep, wolf, not vegetable)
        route.pop()

    route.append("empty " + str(men) + "->" + str(not men))
    DFS(not men, sheep, wolf, vegetable)
    route.pop()
    
    doneState[stateIdx] = 0

DFS(0, 0, 0, 0)
for answer in answers:
    print(answer)
