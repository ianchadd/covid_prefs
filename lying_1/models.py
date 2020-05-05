
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'lying_1'
    players_per_group = None
    num_rounds = 1
    number_coins = 5
    reward = c(30)
    number_coins_str = 'five'
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    heads_count = models.IntegerField(max=Constants.number_coins, min=0)
    def set_payoffs(self):
        self.payoff=self.heads_count*Constants.reward
        print('number heads:',self.heads_count, 'reward:', self.payoff)