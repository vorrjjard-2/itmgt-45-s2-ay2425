def relationship_status(from_member, to_member, social_graph):
    follows = to_member in social_graph.get(from_member, {}).get("following", []) #.get params : (index, def value)
    followed_by = from_member in social_graph.get(to_member, {}).get("following", [])

    if follows and followed_by:
        return "friends"
    elif follows:
        return "follower"
    elif followed_by:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(board):
    n = len(board)

    for row in board:
        if row.count(row[0]) == n and row[0] != ' ':
            return row[0]
    
    for col in range(n):
        col_vals = [board[row][col] for row in range(n)]
        if col_vals.count(col_vals[0]) == n and col_vals[0] != ' ':
            return col_vals[0]

    main_diag = [board[i][i] for i in range(n)]
    if main_diag.count(main_diag[0]) == n and main_diag[0] != ' ':
        return main_diag[0]
    
    anti_diag = [board[i][n - 1 - i] for i in range(n)]
    if anti_diag.count(anti_diag[0]) == n and anti_diag[0] != ' ':
        return anti_diag[0]

    return "NO WINNER"
    
def eta(first_stop, second_stop, route_map):
    if first_stop == second_stop:
        return 0 #in case already there
    time = 0
    stop = first_stop

    while stop != second_stop:
        for (start, end) in route_map:
            if start == stop:
                time += route_map[(start, end)]['travel_time_mins']
                stop = end
                break

    return time

