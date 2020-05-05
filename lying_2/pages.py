
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Heads(Page):
    form_model = 'player'
    form_fields = ['switches_count']
    def vars_for_template(self):
        return dict(
        reward_int=int(Constants.reward)
        )
    def before_next_page(self):
        self.player.set_payoffs()
page_sequence = [Heads]