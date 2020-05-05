
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'dictator_4'
    players_per_group = None
    num_rounds = 1
    endowment = c(300)
    endowment_integer = 300
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    kept = models.CurrencyField(label='Amount for you:', max=Constants.endowment, min=0)
    offer = models.CurrencyField(label='Amount for recipient:', max=Constants.endowment, min=0)
    sent = models.CurrencyField()
    def set_payoffs(self):
        self.payoff=Constants.endowment-self.offer
        self.sent=self.offer
        print('kept amount:', self.payoff, ', offered amount:', self.offer, ', sent amount:', self.sent)