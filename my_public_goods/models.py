
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'my_public_goods'
    players_per_group = 3
    num_rounds = 1
    new_constant = 10
    endowment = c(1000)
    multiplier = 2
class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        print(self.get_group_matrix())
class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    def set_payoffs(self):
        players=self.get_players()
        contributions = [p.contribution for p in players]
        self.total_contribution=sum(contributions)
        self.individual_share=self.total_contribution*Constants.multiplier/Constants.players_per_group
        for p in players:
            p.payoff = Constants.endowment - p.contribution + self.individual_share
class Player(BasePlayer):
    contribution = models.CurrencyField(label='"How much will you contribute?"', max=Constants.endowment, min=0)
