
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Time(Page):
    form_model = 'player'
    form_fields = ['time100', 'time150']
    def before_next_page(self):
        self.player.answers()
page_sequence = [Time]