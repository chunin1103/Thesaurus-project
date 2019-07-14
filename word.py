
######################################
# word = input(str('dafuq you want?'))
word = "decoration"
######################################




from google.cloud import translate
translate_client = translate.Client()
target = 'en'

word_trans = translate_client.translate(
    word,
    target_language=target)

search_for = word_trans['translatedText']

print(word.capitalize(), ': ', search_for)
