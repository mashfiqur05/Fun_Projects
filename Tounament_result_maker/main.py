
def sortTeam(team_data):
    total_points = team_data[1]["total_point"]
    booyah_count = team_data[1]["booyah_count"]
    kill_points = team_data[1]["kill_point"]
    last_position = team_data[1]["last_position"]
    
    return (-total_points, -booyah_count, -kill_points, last_position)

tournamentName = input("Enter the name of your tournament: ")
roundName = input("Enter the round name (ex. Semi Final): ")
totalTeam = int(input("Enter the number of teams: "))

positionPoint = []
for i in range(totalTeam):
    position_suffix = ["st", "nd", "rd"] + ["th"] * (totalTeam - 3)
    point = int(input(f"Enter the point for the {i+1}{position_suffix[i]} position: "))
    positionPoint.append(point)

killPoint = int(input("Enter the point of 1 kill: "))
totalMatch = int(input("Enter the total number of matches: "))

print("\n\n")
scoreBoard = {}

for matchNo in range(totalMatch):
    position_suffix = ["st", "nd", "rd"] + ["th"] * (totalMatch - 3)
    print(f"Enter the details of {matchNo + 1}{position_suffix[i]} macth:\n")
    
    for i in range(totalTeam):
        teamName = input("Enter a team Name: ").strip().upper()
        teamPosition = int(input(f"Enter the position of {teamName}: "))
        teamKill = int(input(f"Enter the total kill of {teamName}: "))

        pos_point = positionPoint[teamPosition - 1]
        kill_pts = teamKill * killPoint
        total = pos_point + kill_pts

        if teamName not in scoreBoard:
            scoreBoard[teamName] = {
                "total_point": 0,
                "booyah_count": 0,
                "kill_point": 0,
                "last_position": 0
            }

        scoreBoard[teamName]["total_point"] += total
        scoreBoard[teamName]["kill_point"] += kill_pts
        scoreBoard[teamName]["last_position"] = teamPosition

        if teamPosition == 1:
            scoreBoard[teamName]["booyah_count"] += 1

        print()

    print()

sorted_score =  sorted(scoreBoard.items(), key=sortTeam)


# Output
print("\n\t========== RESULT ==========\n")
print(f"\t\t{tournamentName}")
print(f"\t\t{roundName}\n")
print("\nRank\tTeam\tBooyah\tKills\tPoints")

for rank, (team, stats) in enumerate(sorted_score, start=1):
    print(f"{rank}\t{team}\t{stats['total_point']}\t{stats['kill_point']}\t{stats['booyah_count']}")

