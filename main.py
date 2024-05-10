import requests
from bs4 import BeautifulSoup
from googletrans import Translator


def get_russian_words():
    url = "https://randomword.com/"
    translator = Translator()
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        english_word = soup.find("div", id='random_word').text.strip()
        word_definition = soup.find("div", id='random_word_definition').text.strip()

        # Перевод слова и определения на русский язык
        russian_word = translator.translate(english_word, src='en', dest='ru').text
        russian_definition = translator.translate(word_definition, src='en', dest='ru').text

        return {'russian_word': russian_word,
                'word_definition': russian_definition
                }
    except Exception as e:
        print("Error Occurred:", e)
        return None


def word_game():
    print('Добро пожаловать в игру!')

    while True:
        word_dict = get_russian_words()
        if word_dict is None:
            print("Не удалось получить слово.")
            return

        word = word_dict['russian_word']
        word_definition = word_dict['word_definition']
        print(f'Определение слова: {word_definition}')
        user_input = input('Какое это слово?: ')
        if user_input.lower() == word.lower():
            print('Верно!')
        else:
            print(f'Неправильно, правильное слово: {word}')

        play_again = input('Хотите сыграть еще раз? (y/n): ')
        if play_again.lower() != 'y':
            print('Спасибо за игру!')
            break


word_game()


