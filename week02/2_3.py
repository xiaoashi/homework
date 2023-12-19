##输出结果中(人，狼，菜，羊)
##输出结果里，1为到达对岸，0为原岸
def is_valid(state):
    farmer = state[0]
    wolf = state[1]
    goat = state[2]
    cabbage = state[3]
    if goat == cabbage and farmer != goat:
        return False
    if wolf == goat and farmer != goat:
        return False
    return True


def generate_next_states(state):
    farmer = state[0]
    wolf = state[1]
    goat = state[2]
    cabbage = state[3]
    next_states = []
    next_states.append((1 - farmer, wolf, goat, cabbage))
    if farmer == wolf:
        next_states.append((1 - farmer, 1 - wolf, goat, cabbage))
    if farmer == goat:
        next_states.append((1 - farmer, wolf, 1 - goat, cabbage))
    if farmer == cabbage:
        next_states.append((1 - farmer, wolf, goat, 1 - cabbage))
    return next_states


def find_solutions():
    initial_state = (0, 0, 0, 0)
    goal_state = (1, 1, 1, 1)
    queue = [(initial_state, [])]
    solutions = []
    i = 0
    while len(queue) > 0:
        current_state, path = queue.pop(0)
        if current_state == goal_state:
            solutions.append(path)
        for next_state in generate_next_states(current_state):
            if is_valid(next_state) and next_state not in path:
                queue.append((next_state, path + [next_state]))
    return solutions


solutions = find_solutions()
for i, solution in enumerate(solutions):
    print(f"方案{i + 1}:")
    for step, state in enumerate(solution):
        print(f"{step + 1}: {state}")
    print()