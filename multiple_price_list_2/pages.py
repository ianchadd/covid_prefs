
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Information(Page):
    form_model = 'player'
    def vars_for_template(self):
        return dict(
        increment_int=int(Constants.increment)
        )
class Color_Select(Page):
    form_model = 'player'
    form_fields = ['winning_color_red']
    def vars_for_template(self):
        return dict(
        number_balls_total=Constants.number_balls_red+Constants.number_balls_black,
        endowment_int=int(Constants.endowment)
        )
    def before_next_page(self):
        self.player.choose_color()
class Gamble_vs_Safe(Page):
    form_model = 'player'
    form_fields = ['Q0_gamble', 'Q1_gamble', 'Q2_gamble', 'Q3_gamble', 'Q4_gamble', 'Q5_gamble', 'Q6_gamble', 'Q7_gamble', 'Q8_gamble', 'Q9_gamble', 'Q10_gamble']
    def vars_for_template(self):
        return dict(
        number_balls_total=Constants.number_balls_red+Constants.number_balls_black,
        endowment_int=int(Constants.endowment)
        )
    def before_next_page(self):
        self.player.set_payoffs()
page_sequence = [Information, Color_Select, Gamble_vs_Safe]