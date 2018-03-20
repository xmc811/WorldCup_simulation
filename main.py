
# This is a test file for class

import random
import numpy as np
from pandas import DataFrame
import pandas as pd
import string

np.random.seed(10)
class Team:
    """To define a team"""
    
    def __init__(self, name, rank = 0):
        self.name = name
        self.rank = rank
        self.group_records = [self.name] + [0] * 5

    def init_records(self):
        self.group_records = [self.name] + [0] * 5


class Match:
    """To define a match"""

    def __init__(self, team_a, team_b, rule = "home_away", group = True):
        self.a = team_a
        self.b = team_b
        self.rule = rule
        self.group = group
            
        
    def start_match(self):

        if self.a == XXX or self.b == XXX:
            return "Empty Round"

        else:

            self.diff = abs(self.a.rank - self.b.rank) / 30
            
            if self.rule == "home_away":
                if  self.a.rank < self.b.rank:
                    self.score_a = np.random.poisson(1 + self.diff + 0.4, 1)[0]
                    self.score_b = np.random.poisson(1 / (1 + self.diff), 1)[0]
                else:
                    self.score_b = np.random.poisson(1 + self.diff - 0.2, 1)[0]
                    self.score_a = np.random.poisson(1 / (1 + self.diff) + 0.2, 1)[0]

            if self.rule == "neutral":
                score_h = np.random.poisson(1 + self.diff, 1)[0]
                score_l = np.random.poisson(1 / (1 + self.diff), 1)[0]

                if  self.a.rank < self.b.rank:
                    self.score_a = score_h
                    self.score_b = score_l

                else:
                    self.score_a = score_l
                    self.score_b = score_h 

            print('{:>15}'.format(self.a.name)  + '{:^11}'.format(str(self.score_a) + " - " + str(self.score_b)) + self.b.name)

            if self.score_a > self.score_b:

                self.a.group_records[1] += 1
                self.b.group_records[3] += 1

            elif self.score_a == self.score_b:
                self.a.group_records[2] += 1
                self.b.group_records[2] += 1

            else:
                self.a.group_records[3] += 1
                self.b.group_records[1] += 1

            self.a.group_records[4] += self.score_a
            self.a.group_records[5] += self.score_b

            self.b.group_records[4] += self.score_b
            self.b.group_records[5] += self.score_a

class Group:
    """To define a group"""

    def __init__(self, ID, teams, rule = "home_away"):
        self.ID = ID
        self.teams = teams
        self.round = 0
        self.rule = rule

    def setup_fixture(self):
        if len(self.teams) % 2:
            self.teams.append(XXX)

        rounds = len(self.teams) - 1
        schedule = []
        for turn in range(rounds):
            pairings = []
            for i in range(int(len(self.teams) / 2)):
                pairings.append((self.teams[i], self.teams[len(self.teams) - i - 1]))
            self.teams.insert(1, self.teams.pop())
            schedule.append(pairings)

        if self.rule == "home_away":
            for turn in range(rounds):
                pairings = []
                for i in range(int(len(self.teams) / 2)):
                    pairings.append((self.teams[len(self.teams) - i - 1], self.teams[i]))
                self.teams.insert(1, self.teams.pop())
                schedule.append(pairings)

        self.schedule = schedule

        for i in self.teams:
            i.init_records()

    def print_table(self):

        if XXX in self.teams:
            self.teams.pop()

        table = [i.group_records for i in self.teams]

        df = DataFrame.from_records(table)

        df[6] = df[4] - df[5]
        df[7] = df[1] * 3 + df[2]

        df.columns = ['Team', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts']

        print(df.sort_values(by=['Pts','GD'], ascending=False))



    def next_round(self):
        if self.round == len(self.schedule):
            print("Group " + self.ID + " Round Finished")

        else:
            print("Group " + self.ID + ": Round " + str(self.round + 1))
            print("---------------")
            for i in range(len(self.schedule[0])):
                Match(self.schedule[self.round][i][0], self.schedule[self.round][i][1]).start_match()
            print("---------------")
            self.round += 1

        self.print_table()
        print("===============")

    def finish_all_rounds(self):
        while self.round < len(self.schedule):
            self.next_round()


class Association:

    def __init__(self, ID, teams):
        self.ID = ID
        self.teams = teams

    def setup_groups(self, num_groups):
        self.num_groups = num_groups
        self.kick_num = len(self.teams) % self.num_groups
        self.temp_teams = [i for i in self.teams]

        if self.kick_num != 0:
            kick_list = random.sample(range(-1, self.kick_num * (-2) - 1, -1), self.kick_num)
            for index in sorted(kick_list):
                del self.temp_teams[index]

        
        assoc_df = df[df['Assoc'] == self.ID]
        code_list = assoc_df['Code'].tolist()
        
        x = self.num_groups
        y = int(len(self.temp_teams) / x)

        print(x)
        print(y)

        all_index = []
        
        for i in range(y):
            b = list(np.random.permutation(x))
            all_index.append(b)

        group_name_list = [self.ID + "_Group_" + i for i in list(string.ascii_uppercase)]
        
        for m, n in zip(list(range(x)), group_name_list):
           
            group_team = []
            
            for i in range(y):
                group_team.append(eval(code_list[all_index[i][m] + x * i]))

            globals()[n] = Group(n, group_team)

        group_names = group_name_list[:x]
        
        table = []

        for k in group_names:
            
            team = []
            
            for l in eval(k).teams:
                team.append(l.name)
            table.append(team)
        
        grouping_df = DataFrame.from_records(table).transpose()

        grouping_df.columns = group_names

        print(grouping_df)


# Load team data from file

df = pd.read_csv("rank_data.txt", sep='\t', header = None)

column_names = ['Code', 'Rank', 'Name', 'Assoc']

df.columns = column_names

df = df.sort_values(by = ['Rank'])

for u in column_names:
    globals()[u] = df[u].tolist()

for u,v in zip(Code, zip(Name, Rank)):
    globals()[u] = Team(v[0], v[1])

XXX = Team("NULL", 0)

# Construct associations

assoc_list = list(set(Assoc))

for u in assoc_list:
    tmp_df = df[df['Assoc'] == u]
    tmp_code = tmp_df['Code'].tolist()
    team_list = []
    for v in tmp_code:
        team_list.append(eval(v))
    globals()[u] = Association(u, team_list)



AFC.setup_groups(1)

AFC_Group_A.setup_fixture()

AFC_Group_A.finish_all_rounds()

# UEFA_Group_A.setup_fixture()

# UEFA_Group_A.finish_all_rounds()



# print(one)

# group_a.setup_fixture()

# group_a.finish_all_rounds()



