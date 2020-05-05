
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'multiple_price_list_1'
    players_per_group = None
    num_rounds = 1
    increment = c(10)
    endowment = c(150)
    number_balls_red = 15
    number_balls_black = 15
    num_questions = 16
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    winning_color_red = models.BooleanField(choices=[[True, 'red'], [False, 'black']], widget=widgets.RadioSelect)
    Q0_gamble = models.BooleanField(choices=[[True, 'Urn Gamble'], [False, '0 tokens']], initial=True, widget=widgets.RadioSelectHorizontal)
    Q1_gamble = models.BooleanField(choices=[[True, 'Urn Gamble'], [False, '10 tokens']], widget=widgets.RadioSelectHorizontal)
    Q2_gamble = models.BooleanField(choices=[[True, 'Urn Gamble          '], [False, '20 tokens']], widget=widgets.RadioSelectHorizontal)
    Q3_gamble = models.BooleanField(choices=[[True, 'Urn Gamble'], [False, '30 tokens']], widget=widgets.RadioSelectHorizontal)
    Q4_gamble = models.BooleanField(choices=[[True, 'Urn Gamble'], [False, '40 tokens']], widget=widgets.RadioSelectHorizontal)
    Q5_gamble = models.BooleanField(choices=[[True, 'Urn Gamble'], [False, '50 tokens']], widget=widgets.RadioSelectHorizontal)
    Q6_gamble = models.BooleanField(choices=[[True, 'Urn Gamble'], [False, '60 tokens']], widget=widgets.RadioSelectHorizontal)
    Q7_gamble = models.BooleanField(choices=[[True, 'Urn Gamble'], [False, '70 tokens']], widget=widgets.RadioSelectHorizontal)
    Q8_gamble = models.BooleanField(choices=[[True, 'Urn Gamble'], [False, '80 tokens']], widget=widgets.RadioSelectHorizontal)
    Q9_gamble = models.BooleanField(choices=[[True, 'Urn Gamble'], [False, '90 tokens']], widget=widgets.RadioSelectHorizontal)
    Q10_gamble = models.BooleanField(choices=[[True, 'Urn Gamble'], [False, '100 tokens']], widget=widgets.RadioSelectHorizontal)
    Q11_gamble = models.BooleanField(choices=[[True, 'Urn Gamble'], [False, '110 tokens']], widget=widgets.RadioSelectHorizontal)
    Q12_gamble = models.BooleanField(choices=[[True, 'Urn Gamble'], [False, '120 tokens']], widget=widgets.RadioSelectHorizontal)
    Q13_gamble = models.BooleanField(choices=[[True, 'Urn Gamble'], [False, '130 tokens']], widget=widgets.RadioSelectHorizontal)
    Q14_gamble = models.BooleanField(choices=[[True, 'Urn Gamble'], [False, '140 tokens']], widget=widgets.RadioSelectHorizontal)
    Q15_gamble = models.BooleanField(choices=[[True, 'Urn Gamble'], [False, '150 tokens']], initial=False, widget=widgets.RadioSelectHorizontal)
    color = models.StringField()
    def set_payoffs(self):
        import random
        import math   
        
        if self.winning_color_red:
            probability_win=(Constants.number_balls_red)/(Constants.number_balls_red+Constants.number_balls_black)
        else:
            probability_win=(Constants.number_balls_black)/(Constants.number_balls_red+Constants.number_balls_black)
        print('probability_win:', probability_win)
        
        random_win=random.random()
        if random_win < probability_win:
            win=1
        else:
            win=0
        
        print('random_win', random_win)
        print('win',win)
        
        random_question=random.random()
        chosen_question=math.floor(random_question*Constants.num_questions)
        print('random question:', random_question)
        print('chosen question:', chosen_question)
        # question = self._meta.get_field('Q' + str(chosen_question) + '_gamble')
        
        answers = [self.Q0_gamble, self.Q1_gamble, self.Q2_gamble, self.Q3_gamble, self.Q4_gamble, self.Q5_gamble, self.Q6_gamble, self.Q7_gamble, self.Q8_gamble, self.Q9_gamble, self.Q10_gamble, self.Q11_gamble, self.Q12_gamble, self.Q13_gamble, self.Q14_gamble, self.Q15_gamble]
        
        print(answers)
        
        for i in range (Constants.num_questions):
            if chosen_question==i:
                print('question',i)
                print('answer', answers[i])
                if answers[i]:
                    if win == 1:
                        self.payoff=Constants.endowment
                    else:
                        self.payoff=0
                else:
                    self.payoff=c(chosen_question*10)
                    
        print('payoff',self.payoff)
    def choose_color(self):
        if self.winning_color_red:
            self.color='red'
        else:
            self.color='black'