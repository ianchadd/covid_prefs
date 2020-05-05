
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['willing_to_take_risk']
    def before_next_page(self):
        self.player.answer()
page_sequence = [Questionnaire]