from typing import List, Tuple, Dict
import functions.globals as g


def load_teams(teams_file: str) -> List[str]:
    """ Load teams from file and return a list with its names"""
    team_list = []
    file = open(teams_file, "r")

    for team in file:
        team_list.append(team.rstrip("\n"))

    return team_list


def create_league(*team_list: List[str]) -> Dict:
    """ Creates the league matrix. """
    league_dict = {}

    for local_team in g.teams:
        league_dict[local_team] = {}
        for visiting_team in g.teams:
            if visiting_team == local_team:
                league_dict[local_team][visiting_team] = "X"
            else:
                league_dict[local_team][visiting_team] = ""

    return league_dict


def create_ranking(*team_list: List[str]) -> Dict:
    """ Creates the ranking dictionary. """
    ranking_dict = {}

    for local_team in g.teams:
        ranking_dict[local_team] = 0

    return ranking_dict


def update_league(local_team: str, visiting_team: str, local_goals: str,
visiting_goals: str) -> None:
    """ Update league values """
    g.league[local_team][visiting_team] = local_goals
    g.league[visiting_team][local_team] = visiting_goals


def update_ranking():
    pass
