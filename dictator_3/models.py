
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'dictator_3'
    players_per_group = None
    num_rounds = 1
    endowment = c(100)
    endowment_integer = 100
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    kept = models.CurrencyField(label='Amount for you:', max=Constants.endowment, min=0)
    offer = models.CurrencyField(label='Amount for recipient: (recipient will receive double this amount)', max=Constants.endowment, min=0)
    sent = models.CurrencyField()
    def set_payoffs(self):
        self.payoff=Constants.endowment-self.offer
        self.sent=self.offer*2
        print('kept amount:', self.payoff, ', offered amount:', self.offer, ', sent amount:', self.sent)