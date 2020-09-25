from typing import List, Tuple, Dict
import functions.globals as g


def create_teams(teams_file: str) -> List[str]:
    """ Load teams from file and return a list with its names"""
    team_list = []
    file = open(teams_file, "r")

    for team in file:
        team_list.append(team.rstrip("\n"))

    return team_list


def create_league() -> None:
    """ Creates the league matrix. """
    for local_team in g.teams:
        g.league[local_team] = {}
        for visiting_team in g.teams:
            if visiting_team == local_team:
                g.league[local_team][visiting_team] = "X"
            else:
                g.league[local_team][visiting_team] = ""

def create_ranking() -> None:
    """ Creates the ranking dictionary. """
    for local_team in g.teams:
        g.ranking[local_team] = 0


def update_league(local_team: str, local_goals: str, visiting_team: str,
                  visiting_goals: str) -> None:
    """ Update league values. """
    if local_team == visiting_team:
      pass
    else:
      g.league[local_team][visiting_team] = (int(local_goals), int(visiting_goals))
      g.league[visiting_team][local_team] = (int(visiting_goals), int(local_goals))


def update_ranking(local_team: str, local_goals: str, visiting_team: str,
                  visiting_goals: str) -> None:
  """ Determines ranking position according to match result """
  if int(local_goals) > int(visiting_goals):
    g.ranking[local_team] += 1
  elif int(local_goals) < int(visiting_goals):
    g.ranking[visiting_team] += 1