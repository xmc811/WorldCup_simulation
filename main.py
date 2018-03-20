
# This is a test file for class

import random
import numpy as np
from pandas import DataFrame

np.random.seed(3)
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

        df.columns = ['Team', 'W', 'D', 'L', 'GS', 'GA', 'GD', 'Pts']

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

    def setup_groups(self, num_groups, kick_num = 0):
        self.num_groups = num_groups
        self.kick_num = kick_num
        self.temp_teams = [i for i in self.teams]

        if self.kick_num != 0:
            kick_list = random.sample(range(-1, self.kick_num * -2 - 1, -1), self.kick_num)
            for index in sorted(kick_list):
                del self.temp_teams[index]
        
        print(str(len(self.teams)))
        print(str(len(self.temp_teams)))
        
        print([i.name for i in self.temp_teams])

        if len(self.temp_teams) % self.num_groups != 0:
            print("Please adjust number of teams to be kicked.")

        # else:

            

XXX = Team("NULL", 0)

# load AFC teams data

IRN = Team("Iran", 33)
AUS = Team("Australia", 37)
JPN = Team("Japan", 55)
KOR = Team("South Korea", 59)
CHN = Team("China PR", 65)
SAU = Team("Saudi Arabia", 69)
UZB = Team("Uzbekistan", 72)
PSE = Team("Palestine", 73)
SYR = Team("Syria", 74)
ARE = Team("UAE", 79)
IRQ = Team("Iraq", 83)
LBN = Team("Lebanon", 87)
IND = Team("India", 99)
QAT = Team("Qatar", 101)
OMN = Team("Oman", 103)
VNM = Team("Vietnam", 113)
TKM = Team("Turkmenistan", 114)
KGZ = Team("Kyrgyz", 115)
JOR = Team("Jordan", 117)
PRK = Team("North Korea", 119)
PHL = Team("Philippines", 122)
TJK = Team("Tajikistan", 124)
BHR = Team("Bahrain", 125)
THA = Team("Thailand", 129)
TWN = Team("Chinese Taipei", 134)
YEM = Team("Yemen", 140)
MMR = Team("Myanmar", 142)
HKG = Team("Hong Kong", 145)
AFG = Team("Afghanistan", 148)
MDV = Team("Maldives", 150)
IDN = Team("Indonesia", 162)
NPL = Team("Nepal", 165)
SGP = Team("Singapore", 171)
KHM = Team("Cambodia", 171)
KWT = Team("Kuwait", 173)
MYS = Team("Malaysia", 178)
LAO = Team("Laos", 183)
MAC = Team("Macau", 186)
BTN = Team("Bhutan", 188)
MNG = Team("Mongolia", 189)
TLS = Team("Timor-Leste", 190)
GUM = Team("Guam", 191)
BRN = Team("Brunei", 193)
BGD = Team("Bangladesh", 197)
LKA = Team("Sri Lanka", 200)
PAK = Team("Pakistan", 203)

# 

AFC = Association("Asia", [IRN, AUS, JPN, KOR, CHN, SAU, UZB, PSE, SYR, ARE, IRQ, 
    LBN, IND, QAT, OMN, VNM, TKM, KGZ, JOR, PRK, PHL, TJK, BHR, THA, TWN, YEM, MMR, 
    HKG, AFG, MDV, IDN, NPL, SGP, KHM, KWT, MYS, LAO, MAC, BTN, MNG, TLS, GUM, BRN, 
    BGD, LKA, PAK])

AFC.setup_groups(10, 2)

c = ["AAA", "BBB", "CCC"]
d = ["Aaa", "Bbb", "Ccc"]
e = [20, 30, 40]

f = dict(zip(c, zip(d, e)))

for u,v in f.items():
    globals()[u] = Team(v[0], v[1])

print(AAA.rank)


# print(one)

# group_a.setup_fixture()

# group_a.finish_all_rounds()



