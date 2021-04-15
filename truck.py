def solution(bridge_length, weight, truck_weights):
    answer = 1
    bridge = [0]*bridge_length
    cur = 0
    while cur > 0 or len(truck_weights) > 0: 
        cur -= bridge.pop(0) 
        answer += 1
        if len(truck_weights) > 0 and weight >= cur + truck_weights[0]:
            cur += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
        if cur==0:
            answer -= 1
    return answer