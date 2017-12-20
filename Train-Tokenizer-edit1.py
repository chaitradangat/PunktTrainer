#import codecs
#import nltk
#nltk.download('punkt')
#import nltk.data
#import nltk.tokenize.punkt
#import pickle
#from nltk.tokenize import PunktSentenceTokenizer

import sys 
import codecs, re, os
from nltk.tokenize.punkt import PunktTrainer,PunktSentenceTokenizer,PunktParameters
from nltk.tokenize import word_tokenize
import pickle


def train_punktsent(trainfile, modelfile):
  """ Trains an unsupervised NLTK punkt sentence tokenizer. """
  punkt = PunktTrainer()
  #try:
    #with codecs.open(trainfile, 'r',encoding='utf-8') as fin:
  input_ = codecs.open(trainfile, encoding='utf-8')	
  for line in input_:
      try:
       punkt.train(line, finalize=False, verbose=False)
      except:
       pass
    #except:
     #print('KeyboardInterrupt: Stopping the reading of the dump early!')
  ##HACK: Adds abbreviations from rb_tokenizer.
  #abbrv_sent = " ".join([i.strip() for i in \
   #                      codecs.open('abbrev.lex','r','utf8').readlines()])
  #abbrv_sent = "Start"+abbrv_sent+"End."
  #punkt.train(abbrv_sent,finalize=False, verbose=False)
  # Finalize and outputs trained model.
  #punkt.finalize_training(verbose=True)
  input_.close()
  model = PunktSentenceTokenizer(punkt.get_params())
  with open(modelfile, mode='wb') as fout:
    pickle.dump(model, fout, protocol=pickle.HIGHEST_PROTOCOL)
  return model





print('')
print('')
print('')
print('loading dependencies completed..')
print('----------------------------------------')
print('')
print('')
print('')

languages_ = ['czech','danish','dutch','english','estonian','finnish','french','german','greek','italian','norwegian','polish','portuguese','slovene','spanish','swedish','turkish']

lang_count = 0
selected_language = ''
input_language = ''

print('Nltk Unsupervised Trainer --v1.0 - By Chaitra Dangat')
print('')
print('Language-List')
print('-----------------------------------------------')
for language_ in languages_:
	lang_count += 1
	print(str(lang_count) + '.' + language_)
print('--------------------------------------------------')

input_language = input('Select A Language:')

try: 
    if int(input_language) > len(languages_):
     print('invalid selection!')
     quit()
    else:
     selected_language = languages_[int(input_language)-1]
     print('')
     print('language selected-->'+selected_language)
     print('')
except ValueError:
    print('invalid selection!')
    quit()

#corpus file path
corpus_file = input('Enter the '+ selected_language +' text file path :')

#output folder path
output_folder = input('Enter the output folder path :')

#read the corpus text in one go
#print('Reading corpus File..')
#corpus_text = codecs.open(corpus_file,'Ur',encoding='utf-8').read()
#print('Reading corpus File Completed')
#print('')
#print('')

#Train the tokenizer
#print('Training the tokenizer..')
#tokenizer = PunktSentenceTokenizer()
#tokenizer.train(corpus_text)
#print('Training tokeizer Completed')
#print('')
#print('')

#Save the trained pickle model
#print('Saving the model...')
model_file = output_folder + '\\' + selected_language + '.pickle'
#output_ = open(model_file,"wb")
#pickle.dump(tokenizer,output_)
#print('Saving the model Completed')

#Cleanup Tasks
#output_.close()

train_punktsent(corpus_file,model_file)

print('')
print('training completed..')


