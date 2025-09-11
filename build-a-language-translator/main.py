translations = {
  "hello":"hola",
  "thank you":"gracias",
  "sorry":"lo siento"
}

done = False

print('Type "done" at any time to exit')

while not done:
    word = input("Input a word in English to get the Spanish word:  ")
    word = word.lower()
    if word == "done":
        done = True
    elif translations.get(word):
        print(translations.get(word) + " is Spanish for " + word)
    else:
        print(word + " is not in the dictionary.")
