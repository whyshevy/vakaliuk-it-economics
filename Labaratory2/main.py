# Імпортуємо бібілотеку регулярних виразів
import re


def getWordsByRegexTemplate():
    # Передаємо у змінну sampleText - певний текст, по якому ми будемо шукати регулярні вирази за нашим шаблоном
    sampleText = "Comme des Garçons (also known as CDG) is a Japanese fashion label founded and headed by Kawakubo, " \
                 "R. in " \
                 "Paris. The label began in 1969 and the company was founded in 1973. Its French flagship store is in " \
                 "Paris. It also establishes country-wide and world-wide store chain for various lines of products, " \
                 "including Dover Street Market, in major cities such as London and New York City." \
                 "Other than fashion, it expands its business to jewelry and perfume. " \
                 "The Biden team is “right to want to " \
                 "have a good relationship with him. They’re going to agree with him on a lot of things," \
                 "” said Rhodes, B. " \
                 "who served as a key force behind diplomatic openings with Cuba and Iran during the Obama years." \
                 "Miyazaki, H. (born in 5 January 1941) is a Japanese animator, " \
                 "director, producer, screenwriter, author, and manga artist. A co-founder of Studio Ghibli, " \
                 "a film and " \
                 "animation studio, he has attained international acclaim as a masterful storyteller and as a maker of " \
                 "animated feature films, and is widely regarded as one of the most accomplished filmmakers in the " \
                 "history " \
                 "of animation. " \
                 "Guitar is an old instrument, but its development through ages was influenced not only " \
                 "by the natural evolution of the manufacturing and musical tastes but also with the direct " \
                 "contributions of few very talented investors. Guitar makers are considered to be Gaetano, V., " \
                 "Rickenbacker, A and  Jurado, A. "
    # Створюємо шаблон регулярного виразу, за умовою нашої задачі
    regexTemplate = r"[A-Z][a-z]+,\s[A-Z]."
    # Шукаємо всі підходящі вирази, за вказаним текстом і шаблоном, та передаємо ці значення у массив -
    # allResultsByTemplate
    allResultsByTemplate = re.findall(regexTemplate, sampleText)
    # Вивід массиву всіх підходящих виразів, за вказаним текстом і шаблоном
    print("We found such coincidences by your template as: ", allResultsByTemplate)
    # Вивід довжини массиву всіх підходящих виразів, за вказаним текстом і шаблоном
    print("The length of your coincidences is: ", len(allResultsByTemplate))


# Виклик функції
getWordsByRegexTemplate()
