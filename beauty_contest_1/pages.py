
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Guess(Page):
    form_model = 'player'
    form_fields = ['guess']
    def vars_for_template(self):
        return dict(
        reward_int=int(Constants.reward),
        size_of_group=Constants.num_others+1,
        reward_half=round(Constants.reward/2,2),
        reward_one_thirds=round(Constants.reward/3,2)
        )
    def before_next_page(self):
        self.player.answer()
page_sequence = [Guess]