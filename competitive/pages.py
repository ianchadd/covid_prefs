
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Information(Page):
    form_model = 'player'
    def vars_for_template(self):
        return dict(
        reward_int=int(Constants.reward)
        )
    def before_next_page(self):
        import time
        # user has 3 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + 10
class Sum1(Page):
    form_model = 'player'
    form_fields = ['answer_1']
    timer_text = 'Time left to complete this task'
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.set_payoffs()
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()
class Sum2(Page):
    form_model = 'player'
    form_fields = ['answer_2']
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.set_payoffs()
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()
class Sum3(Page):
    form_model = 'player'
    form_fields = ['answer_3']
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.set_payoffs()
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()
class Sum4(Page):
    form_model = 'player'
    form_fields = ['answer_4']
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.set_payoffs()
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()
class Sum5(Page):
    form_model = 'player'
    form_fields = ['answer_5']
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.set_payoffs()
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()
class Sum6(Page):
    form_model = 'player'
    form_fields = ['answer_6']
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.set_payoffs()
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()
class Sum7(Page):
    form_model = 'player'
    form_fields = ['answer_7']
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.set_payoffs()
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()
class Sum8(Page):
    form_model = 'player'
    form_fields = ['answer_8']
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.set_payoffs()
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()
class Rank(Page):
    form_model = 'player'
    form_fields = ['rank']
    def vars_for_template(self):
        return dict(
        reward_guess_int=Constants.reward_guess
        )
class Information_2(Page):
    form_model = 'player'
    form_fields = ['piece_rate_payment']
    def before_next_page(self):
        import time
        # user has 3 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + 10
class Part2_Sum1(Page):
    form_model = 'player'
    form_fields = ['answer_1b']
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.set_payoffs_2()
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()
class Part2_Sum2(Page):
    form_model = 'player'
    form_fields = ['answer_2b']
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.set_payoffs_2()
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()
class Part2_Sum3(Page):
    form_model = 'player'
    form_fields = ['answer_3b']
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.set_payoffs_2()
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()
class Part2_Sum4(Page):
    form_model = 'player'
    form_fields = ['answer_4b']
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.set_payoffs_2()
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()
class Part2_Sum5(Page):
    form_model = 'player'
    form_fields = ['answer_5b']
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.set_payoffs_2()
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()
class Part2_Sum6(Page):
    form_model = 'player'
    form_fields = ['answer_6b']
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.set_payoffs_2()
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()
class Part2_Sum7(Page):
    form_model = 'player'
    form_fields = ['answer_7b']
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.set_payoffs_2()
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()
class Part2_Sum8(Page):
    form_model = 'player'
    form_fields = ['answer_8b']
    def is_displayed(self):
        return self.get_timeout_seconds() > 3
    def before_next_page(self):
        self.player.set_payoffs_2()
    def get_timeout_seconds(self):
        import time
        return self.participant.vars['expiry'] - time.time()
page_sequence = [Information, Sum1, Sum2, Sum3, Sum4, Sum5, Sum6, Sum7, Sum8, Rank, Information_2, Part2_Sum1, Part2_Sum2, Part2_Sum3, Part2_Sum4, Part2_Sum5, Part2_Sum6, Part2_Sum7, Part2_Sum8]