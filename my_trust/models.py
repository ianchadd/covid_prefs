
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'my_trust'
    players_per_group = 2
    num_rounds = 1
    endowment = c(10)
    multiplication_factor = 3
class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        print(self.get_group_matrix())
class Group(BaseGroup):
    sent_amount = models.CurrencyField(label='How much do you want to send to participant B?', max=Constants.endowment, min=0)
    sent_back_amount = models.CurrencyField(label='How much do you want to send back?', min=0)
    def sent_back_amount_choices(self):
        return currency_range(
                c(0),
                self.sent_amount * Constants.multiplication_factor,
                c(1)
        )
    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
        p2.payoff = self.sent_amount * Constants.multiplication_factor - self.sent_back_amount
class Player(BasePlayer):
    pass