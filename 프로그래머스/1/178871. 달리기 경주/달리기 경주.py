def solution(players, callings):
    answer = []
    ranking_player = {}
    ranking_rank = {}
    for i in range(len(players)):
        ranking_player[players[i]] = i+1
        ranking_rank[i+1] = players[i]
    
    for call in callings:
        loser = ranking_rank[ranking_player[call]-1]
        loser_idx = ranking_player[loser]
        ranking_player[call] -= 1
        ranking_player[loser] += 1
        ranking_rank[loser_idx] = call
        ranking_rank[loser_idx+1] = loser
    
    for i in range(len(players)):
        answer.append(ranking_rank[i+1])
        

    return answer