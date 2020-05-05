
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

doc = ''
class Constants(BaseConstants):
    name_in_url = 'competitive'
    players_per_group = None
    num_rounds = 1
    reward = c(40)
    number_questions = 8
    reward_guess = c(50)
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    answer_1 = models.IntegerField(min=0)
    answer_2 = models.IntegerField(min=0)
    answer_3 = models.IntegerField(min=0)
    answer_4 = models.IntegerField(min=0)
    answer_5 = models.IntegerField(min=0)
    answer_6 = models.IntegerField(min=0)
    answer_7 = models.IntegerField(min=0)
    answer_8 = models.IntegerField(min=0)
    rank = models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4']], widget=widgets.RadioSelectHorizontal)
    piece_rate_payment = models.BooleanField(choices=[[True, '10 tokens per sum correctly answered; or'], [False, 'When all surveys are submitted, we will randomly group you with 3 other people (so you will be in a group of 4). We will compare the number of sums you correctly answer now with the number of sums the other 3 correctly answered in the previous stage you just concluded. You will be paid only if you achieve the highest number of correctly answered sums within this group, in which case you will be paid 40 tokens per sum correctly answered.']], widget=widgets.RadioSelect)
    answer_1b = models.IntegerField(min=0)
    answer_2b = models.IntegerField(min=0)
    answer_3b = models.IntegerField(min=0)
    answer_4b = models.IntegerField(min=0)
    answer_5b = models.IntegerField(min=0)
    answer_6b = models.IntegerField(min=0)
    answer_7b = models.IntegerField(min=0)
    answer_8b = models.IntegerField(min=0)
    correct_answers_part1 = models.IntegerField(initial=0)
    correct_answers_part2 = models.IntegerField(initial=0)
    def set_payoffs(self):
        correct_answers=[175,344,224,220,236,147,246,280]
        print('correct_answers:',correct_answers)
        
        answers=[self.answer_1, self.answer_2, self.answer_3, self.answer_4, self.answer_5, self.answer_6, self.answer_7, self.answer_8]
        print('answers:',answers)
        for i in range(Constants.number_questions):
            print('answer',i," :", answers[i])
        num_correct_answers=0
        print('num_correct_answers:',num_correct_answers)
        for i in range(Constants.number_questions):
            print('Question:', i)
            if answers[i]==correct_answers[i]:
                num_correct_answers=num_correct_answers+1
            print('num_correct_answers:',num_correct_answers)   
        print('Final num_correct_answers:',num_correct_answers)
        self.correct_answers_part1=num_correct_answers
        print('P1',self.correct_answers_part1)
    def set_payoffs_2(self):
        correct_answers=[232,261,362,250,359,362,331,164]
        print('correct_answers:',correct_answers)
        
        answers=[self.answer_1b, self.answer_2b, self.answer_3b, self.answer_4b, self.answer_5b, self.answer_6b, self.answer_7b, self.answer_8b]
        print('answers:',answers)
        for i in range(Constants.number_questions):
            print('answer',i," :", answers[i])
        num_correct_answers=0
        print('num_correct_answers:',num_correct_answers)
        for i in range(Constants.number_questions):
            print('Question:', i)
            if answers[i]==correct_answers[i]:
                num_correct_answers=num_correct_answers+1
            print('num_correct_answers:',num_correct_answers)   
        print('Final num_correct_answers:',num_correct_answers)
        self.correct_answers_part2=num_correct_answers
        print('P2',self.correct_answers_part2)