
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class PD(Page):
    form_model = 'player'
    form_fields = ['A1']
page_sequence = [PD]