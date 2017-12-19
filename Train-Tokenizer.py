import codecs
import nltk
nltk.download('punkt')
import nltk.data
import nltk.tokenize.punkt
import pickle
from nltk.tokenize import PunktSentenceTokenizer

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
    if int(input_language) >= len(languages_):
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
print('Reading corpus File..')
corpus_text = codecs.open(corpus_file,'Ur',encoding='utf-8').read()
print('Reading corpus File Completed')
print('')
print('')

#Train the tokenizer
print('Training the tokenizer..')
tokenizer = PunktSentenceTokenizer()
tokenizer.train(corpus_text)
print('Training tokeizer Completed')
print('')
print('')

#Save the trained pickle model
print('Saving the model...')
model_file = output_folder + '\\' + selected_language + '.pickle'
output_ = open(model_file,"wb")
pickle.dump(tokenizer,output_)
print('Saving the model Completed')

#Cleanup Tasks
output_.close()