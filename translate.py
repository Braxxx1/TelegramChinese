from googletrans import Translator


def translate(text="紫禁城", dest='ru'):
    try:
        translator = Translator()
        translation = translator.translate(text=text, dest=dest)
        return translation.text
    
    except Exception as ex:
        return ex