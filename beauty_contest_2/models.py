
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'beauty_contest_2'
    players_per_group = None
    num_rounds = 1
    num_others = 9
    reward = 5
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    guess = models.IntegerField(max=100, min=0)
    def answer(self):
        print('answer:',self.guess)