
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Guess(Page):
    form_model = 'player'
    form_fields = ['guess']
    def vars_for_template(self):
        return dict(
        reward_int=int(Constants.reward),
        reward_half=round(Constants.reward/2,2),
        )
    def before_next_page(self):
        self.player.answer()
page_sequence = [Guess]