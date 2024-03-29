# Amaan Muhammad
# PSID: 1607608

# Initiate class and identify attributes
class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    def set_team_name(self, team_name):
        self.team_name = team_name

    def set_team_wins(self, team_wins):
        self.team_wins = team_wins

    def set_team_losses(self, team_losses):
        self.team_losses = team_losses

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        percent = float(self.team_wins) / (float(self.team_wins) + float(self.team_losses))
        return percent


# Main
if __name__ == "__main__":

    team = Team()
    # User Input
    team_name = input()
    team_wins = float(input())
    team_losses = float(input())

    team.set_team_name(team_name)
    team.set_team_wins(team_wins)
    team.set_team_losses(team_losses)
    # Print Output
    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.team_name, 'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')
