
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    form_model = 'player'
class Offer(Page):
    form_model = 'group'
    form_fields = ['kept']
    def is_displayed(self):
        return self.player.id_in_group == 1
class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()
class Results(Page):
    form_model = 'player'
    def vars_for_template(self):
        return dict(offer=Constants.endowment - self.group.kept)
page_sequence = [Introduction, Offer, ResultsWaitPage, Results]