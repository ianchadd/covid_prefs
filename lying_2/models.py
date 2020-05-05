
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'lying_2'
    players_per_group = None
    num_rounds = 1
    number_coins = 10
    reward = c(30)
    number_coins_str = 'ten'
    max_switches = 9
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    switches_count = models.IntegerField(max=Constants.max_switches, min=0)
    def set_payoffs(self):
        self.payoff=self.switches_count*Constants.reward
        print('number switches:',self.switches_count, 'reward:', self.payoff)