from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0.01, participation_fee=0)
SESSION_CONFIGS = [dict(name='my_session', num_demo_participants=2, app_sequence=['risky_project_1', 'risky_project_2', 'multiple_price_list_1', 'multiple_price_list_2', 'risk_qualitative', 'lying_1', 'lying_2', 'beauty_contest_1', 'beauty_contest_2', 'beauty_contest_3', 'dictator_1', 'dictator_2', 'dictator_3', 'dictator_4', 'competitive', 'prisoners_dilemma_1', 'prisoners_dilemma_2', 'time_1', 'time_2'])]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
ROOMS = []
POINTS_CUSTOM_NAME = 'tokens'

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


