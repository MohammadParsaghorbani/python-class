import random as rnd

def randomTeamPlays(group_array):
    matches=[]
    for i in range(4):
        for j in range(i+1,4):
            if group_array[i] != group_array[j]:
                matches.append((group_array[i],group_array[j]))
                
    results={}
    for match in matches:
        score1 = rnd.randint(0,6)
        score2 = rnd.randint(0,6)
        

        results[match]=(score1,score2)
        
    return results


def lastTwoWinners(group_results):
    groups_winners = []
    for i in range(len(group_results)):
        teams_score = {}
        sorted_teams = []
        for teams, scores in group_results[i].items():
            if scores[0] > scores[1]:
                teams_score[teams[0]] = teams_score.get(teams[0], 0) + 3 
                teams_score[teams[1]] = teams_score.get(teams[0], 0) + 0
                
            elif scores[0] < scores[1]:
                teams_score[teams[1]] = teams_score.get(teams[1], 0) + 3 
                teams_score[teams[0]] = teams_score.get(teams[0], 0) + 0
                
            else:
                teams_score[teams[0]] = teams_score.get(teams[0], 0) + 1 
                teams_score[teams[1]] = teams_score.get(teams[1], 0) + 1 

        sorted_teams = sorted(teams_score.items(), key=lambda item: item[1], reverse=True)
        groups_winners.extend(sorted_teams[:2])
    
    return groups_winners

def knockoutStage(qualified_teams):
    stage_labels = ["Final" , "Semi-finals" , "Quarter-finals" , "1/8 Finals" , "1/16 finals"]
    stage_index = 0
    while len(qualified_teams) > 1:
        stage_label = stage_labels[min(len(stage_labels) - 1, (len(qualified_teams) - 1) // 2)]
        print(f"\n==== {stage_label} ====")
        next_round = []
        for i in range(0 , len(qualified_teams) , 2):
            team_1 = qualified_teams[i]
            team_2 = qualified_teams[i+1]
            score1 = rnd.randint(0,6)
            score2 = rnd.randint(0,6)
            print(f"{team_1} vs {team_2} : {score1} - {score2}")
            if score1 > score2:
                next_round.append(team_1)
            elif score1 < score2:
                next_round.append(team_2)
            else :
                print("we go for a penalty shootout")
                if rnd.randint(0,1) == 0:
                    next_round.append(team_1)
                    print(f"{team_1} won the penalty shootout\n")
                else:
                    next_round.append(team_2)
                    print(f"{team_2} won the penalty shootout\n")
        qualified_teams = next_round
        # print("\nNext Round Teams :",qualified_teams)
    return qualified_teams[0]



group_a = ["qatar" , "ecuador" , "senegal" , "netherlands"]
group_b = ["england" , "iran" , "usa" , "wales"]
group_c = ["argentina" , "saudi arabia" , "mexico" , "poland"]
group_d = ["france" , "australia" , "denmark" , "tunisia"]
group_e = ["spain" , "costarica" , "germany" , "japan"]
group_f = ["belgium" , "canada" , "morocco" , "croatia"]
group_g = ["brazil" , "serbia" , "switzerland" , "cameroon"]
group_h = ["portugal" , "ghana" , "uruguay" , "south korea"]

num_group_a = len(group_a)
matches=[]
for i in range(num_group_a):
    for j in range(i+1,num_group_a):
        if group_a[i] != group_a[j]:
            matches.append((group_a[i],group_a[j]))

results={}
for match in matches:
    team1 , team2 = match
    score1 = rnd.randint(0,6)
    score2 = rnd.randint(0,6)
    results[match]=(score1,score2)
group_results = []

group_a_results = randomTeamPlays(group_a)
group_results.append(group_a_results)

group_b_results = randomTeamPlays(group_b)
group_results.append(group_b_results)

group_c_results = randomTeamPlays(group_c)
group_results.append(group_c_results)

group_d_results = randomTeamPlays(group_d)
group_results.append(group_d_results)

group_e_results = randomTeamPlays(group_e)
group_results.append(group_e_results)

group_f_results = randomTeamPlays(group_f)
group_results.append(group_f_results)

for match, score in results.items():
    print(f"{match[0]} vs {match[0]}: \n {score[0]} - {score[1]}")
group_g_results = randomTeamPlays(group_g)
group_results.append(group_g_results)

group_h_results = randomTeamPlays(group_h)
group_results.append(group_h_results)


for i in range(8):
    print(f'\n==== Group {i+1} games ====')
    for teams, scores in group_results[i].items():
        print(f"{teams[0]} vs {teams[1]}: \n {scores[0]} - {scores[1]}")
        
for team, score in lastTwoWinners(group_results):
    print(f'\nTeam: {team} | Score: {score}')

qualified_teams = []
print("\nqualified teams :")
for team in lastTwoWinners(group_results):
    print(team[0])
    qualified_teams.append(team[0])


champion = knockoutStage(qualified_teams)
print(f"\nChampion: {champion}")
