from chatterbot import ChatBot, chatterbot, filters, comparisons, response_selection
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import UbuntuCorpusTrainer
from chatterbot.comparisons import levenshtein_distance
from chatterbot.response_selection import get_first_response
import logging

logging.basicConfig(level=logging.INFO)

ninefa_bot = ChatBot(name='NineFABot', 
                     read_only=False,
                     logic_adapters=[
                    {
                        "import_path": "chatterbot.logic.BestMatch",
                        "statement_comparison_function": levenshtein_distance,
                        "response_selection_method": get_first_response
                    }],             
                    filters=[filters.get_recent_repeated_responses]
                    )

#                  logic_adapters=['chatterbot.logic.MathematicalEvaluation',
#                                  'chatterbot.logic.BestMatch'],

# small_talk = ['hi there!',
#               'hi!',
#               'how do you dooooo?',
#               'how are you?',
#               'i\'m cool.',
#               'fine, you?',
#               'always cool.',
#               'i\'m ok',
#               'glad to hear that.',
#               'i\'m fine',
#               'glad to hear that.',
#               'i feel awesome',
#               'excellent, glad to hear that.',
#               'not so good',
#               'sorry to hear that.',
#               'what\'s your name?',
#               'i\'m 900FootAlien. ask me a math question, please.']
# math_talk_1 = ['pythagorean theorem',
#                'a squared plus b squared equals c squared.']
# math_talk_2 = ['law of cosines',
#                'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']
# 
# print('Loading list trainers...')
# list_trainer = ListTrainer(ninefa_bot)
# for item in (small_talk, math_talk_1, math_talk_2):
#     list_trainer.train(item)
# print('...done.')

print('Loading Ubuntu trainer...')
ubuntu_trainer = UbuntuCorpusTrainer(ninefa_bot)
# print('Training...')
# ubuntu_trainer.train()
print('...done.')

print('Loading corpus trainers...')
corpus_trainer = ChatterBotCorpusTrainer(ninefa_bot)
print('Training...')
corpus_trainer.train('chatterbot.corpus.english.greetings',
                     'chatterbot.corpus.english.ai',
                     'chatterbot.corpus.english.conversations',
                     'chatterbot.corpus.english.emotion',
                     'chatterbot.corpus.english.food',
                     'chatterbot.corpus.english.gossip',
                     'chatterbot.corpus.english.health',
                     'chatterbot.corpus.english.history',
                     'chatterbot.corpus.english.humor',
                     'chatterbot.corpus.english.literature',
                     'chatterbot.corpus.english.money',
                     'chatterbot.corpus.english.movies',
                     'chatterbot.corpus.english.politics',
                     'chatterbot.corpus.english.psychology',
                     'chatterbot.corpus.english.science',
                     'chatterbot.corpus.english.sports',
                     'chatterbot.corpus.english.trivia')
print('...done.')

def getchatbot():
    return ninefa_bot
