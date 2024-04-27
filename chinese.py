import spacy
from translate import translate
from vikipedia import get_wikipedia_summary

nlp = spacy.load("zh_core_web_lg")


def extract_toponyms(text):
        # Обработка текста
    doc = nlp(text)
    # Извлечение топонимов
    toponyms = []
    for entity in doc.ents:
        print(entity, entity.label_)
        if entity.label_ in ["GPE", "LOC"]:
            # Ваш код обработки сущности
        # GPE (Geopolitical Entity) - топоним
            if "°" not in entity.text:
                toponyms.append(entity.text)
    return list(set(toponyms))


def get_info(word):
    trans = translate(word)
    text = f"{word} -- {trans}\n{get_wikipedia_summary(trans.strip())}"
    return text







# pip install spacy
# python -m spacy download zh_core_web_lg
# pip install yandex-translater