def solution(bridge_length, weight, truck_weights):
    sec = 0
    inprogress_queue = [0] * bridge_length
    while len(inprogress_queue) != 0:
        sec += 1
        inprogress_queue.pop(0)
        if truck_weights:
            if sum(inprogress_queue) + truck_weights[0] <= weight:
                inprogress_queue.append(truck_weights.pop(0))
            else:
                inprogress_queue.append(0)
    return sec


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))
