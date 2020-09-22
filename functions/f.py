from typing import List, Tuple, Dict


def load_teams(teams_file: str) -> List[str]:
    """ Load teams from file and return a list with its names"""
    team_list = []
    file = open(teams_file, "r")

    for team in file:
        team_list.append(team.rstrip("\n"))

    return team_list


def create_league(team_list: List[str]) -> Tuple[Dict, Dict]:
    """ Creates the league matrix. """
    league_dict = {}
    ranking_dict = {}

    for local_team in team_list:
        league_dict[local_team] = {}
        ranking_dict[local_team] = 0
        for visitant_team in team_list:
            league_dict[local_team][visitant_team] = None

    return league_dict, ranking_dict


teams = load_teams("teams.cfg")
league, matrix = create_league(teams)
