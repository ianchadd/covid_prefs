
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'risky_project_2'
    players_per_group = None
    num_rounds = 1
    endowment = c(100)
    p_success = 0.35
    multiplier = 3
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    amount_risky = models.CurrencyField(max=Constants.endowment, min=0)
    project_success = models.BooleanField()
    return_from_investment = models.CurrencyField(initial=0)
    def set_payoffs(self):
        import random
        random_number=random.random()
        print(random_number)
        self.payoff=Constants.endowment-self.amount_risky
        if random_number > Constants.p_success:
            self.project_success=False
        else: 
            self.project_success=True
            self.return_from_investment=self.amount_risky*Constants.multiplier
        self.payoff=self.payoff+self.return_from_investment
        print('amount invested:', self.amount_risky)
        print('project success:', self.project_success)
        print('return from investment:', self.return_from_investment)
        print('payoff:', self.payoff)