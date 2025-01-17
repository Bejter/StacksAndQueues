translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

while True:
    english_word = input('Enter an English word: ').lower()

    if english_word in translations:
        print(f'Translation: {translations[english_word]}')
    else:
        print('Translation unavailable.')