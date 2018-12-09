ini_word = "sự tồn tại"


from google.cloud import translate
translate_client = translate.Client()
target = 'en'


translation = translate_client.translate(
    ini_word,
    target_language=target)

search_for = (translation['translatedText']).capitalize()

print(ini_word.capitalize(), ':',search_for)