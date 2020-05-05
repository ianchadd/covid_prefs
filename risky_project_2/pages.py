
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Investment(Page):
    form_model = 'player'
    form_fields = ['amount_risky']
    def vars_for_template(self):
        return dict(
        p_success_int=int(Constants.p_success*100),
        endowment_int=int(Constants.endowment),
        endowment_money=int(Constants.endowment.to_real_world_currency(self.session))
        )
    def before_next_page(self):
        self.player.set_payoffs()
page_sequence = [Investment]