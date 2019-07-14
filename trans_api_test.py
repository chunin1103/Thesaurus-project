# Imports the Google Cloud client library
from google.cloud import translate

# Instantiates a client
translate_client = translate.Client()

# The text to translate
tungu = ['aleuromancy', 'confused-flour-beetle','floury', 'flourman', 'glacial-milk', 'flour-treatment-agent' ]
for w in tungu:
    text = w
    # The target language
    target = 'vi'

    # Translates some text into [Language]
    translation = translate_client.translate(
        text,
        target_language=target)

    print(u'Text: {}'.format(text))
    print(u'Translation: {}'.format(translation['translatedText']))
    print(translation['translatedText'])