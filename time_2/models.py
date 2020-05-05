
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'time_2'
    players_per_group = None
    num_rounds = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    time100 = models.IntegerField(min=0)
    time150 = models.IntegerField(min=0)
    def answers(self):
        print('for 100: ', self.time100, ' for 150: ', self.time150)