
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Offer(Page):
    form_model = 'player'
    form_fields = ['kept', 'offer']
    def vars_for_template(self):
        return dict(
        endowment_int=int(Constants.endowment),
        endowment_dollars=int((Constants.endowment)/100)
        )
    def before_next_page(self):
        self.player.set_payoffs()
    def error_message(self, values):
        if values['offer']+values['kept']!=Constants.endowment:
            return 'The amount you allocate between yourself and the recipient must add up to ' + str(Constants.endowment_integer)
page_sequence = [Offer]