def choose(dispensers, demand, time):
    candidate_dispenser, candidate_wait = -1, 9999
    for i in range(len(dispensers)):
        if dispensers[i][1] >= demand + dispensers[i][0]:
            wait = max(dispensers[i][0] - time, 0)
            if candidate_wait > wait:
                if wait == 0:
                    return i
                else:
                    candidate_dispenser = i
                    candidate_wait = wait
    return candidate_dispenser

def solution(A, X, Y, Z):
    dispensers = [(0,X), (0,Y), (0,Z)]
    current_time = 0
    for car in A:
        choice = choose(dispensers, car, current_time)
        if choice == -1:
            return -1
        if dispensers[choice][0] > current_time:
            wait = dispensers[choice][0] - current_time
            current_time += wait
        dispensers[choice] = (dispensers[choice][0]+car, dispensers[choice][1])
    return current_time
