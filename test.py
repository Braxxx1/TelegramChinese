import wikipedia

def get_wikipedia_summary(search_query):
    wikipedia.set_lang("ru")
    
    try:
        # Прямая попытка получить страницу
        page = wikipedia.page(search_query)
        return page.summary
    except wikipedia.exceptions.DisambiguationError as e:
        # Обработка неоднозначности
        print("Найдено несколько возможных страниц, пытаемся найти наиболее подходящую...")
        for option in e.options[:3]:  # Рассмотрим первые 3 варианта
            try:
                page = wikipedia.page(option)
                return page.summary
            except Exception as e:
                continue
    except wikipedia.exceptions.PageError:
        # Попытка поиска
        print("Прямая страница не найдена. Пытаемся найти через поиск...")
        search_results = wikipedia.search(search_query)
        if not search_results:
            return "Результаты поиска отсутствуют."
        
        try:
            page = wikipedia.page(search_results[0])
            return page.summary
        except Exception as e:
            return "Не удалось получить информацию даже через поиск."
    except Exception as e:
        return "Произошла ошибка при попытке получить информацию."

# search_query = "Гора Тай"
# print(get_summary(search_query))
