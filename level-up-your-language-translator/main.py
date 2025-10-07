import csv

def intro():
  print(f'Welcome to the Spanish and French transltor app.\nPlease enter an Englih word and press the "Enter" key.')
 


translations = {}

with open("translations.csv","r", encoding="utf-8") as words:
  reader = csv.DictReader(words, delimiter=",")
  for line in reader:
    english = line["English"].lower()
    spanish = line["Spanish"].lower()
    french = line["French"].lower()
    translations[english] = [spanish,french]

done = False

def exit():
  print('\nThanks for using hte translator app.  Have a nice day!')

intro()

while not done:
 
  print('\nType "done" at any time to exit.')
  word = input("Type an English word to translate: ")
  word = word.lower()

  if word == "done":
    exit()
    done = True
  elif word in translations:
    print(f'\nSPANISH:  {translations[word][0]}')
    print(f'\nFRENCH:  {translations[word][1]}')
  else:
    print("Translation is not known")

