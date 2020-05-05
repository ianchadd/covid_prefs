
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Survey(Page):
    form_model = 'player'
    form_fields = ['name', 'age']
class Results(Page):
    form_model = 'player'
page_sequence = [Survey, Results]