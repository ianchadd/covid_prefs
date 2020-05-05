
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = '\nOne player decides how to divide a certain amount between himself and the other\nplayer.\n\nSee: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness\nand the assumptions of economics." Journal of business (1986):\nS285-S300.\n\n'
class Constants(BaseConstants):
    name_in_url = 'dictator'
    players_per_group = 2
    num_rounds = 1
    endowment = c(100)
    instructions_template = 'dictator/instructions.html'
class Subsession(BaseSubsession):
    def creating_sessions(self):
        self.group_randomly()
        print(self.get_group_matrix())
class Group(BaseGroup):
    kept = models.CurrencyField(doc='Amount dictator decided to keep for himself', max=Constants.endowment, min=0)
    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        print(p1, p2)
        p1.payoff = self.kept
        p2.payoff = Constants.endowment - self.kept
class Player(BasePlayer):
    pass