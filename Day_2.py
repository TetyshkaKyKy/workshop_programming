def text_analyzer(text, max_length):
    text_lenght = len(text)
    print(f"Количество символов в тексте: {text_lenght}")
    text_repl = len(text.replace(" ", ""))
    print((f"Количество символов без учета пробелов: {text_repl}"))
    text_multiplicity = text_lenght % 2
    if text_multiplicity == 0:
        print("Количество символов в тексте четное")
    else:
        print("Количество символов в тексте нечетное")
    if text_lenght > max_length:
        print(f"Длина текста превышает длину {max_length} символов")

'''
text_analyzer('«Не забывайте о том, что все великие волшебники в истории в свое время были такими же, как мы,'
              ' – школьниками. Если у них получилось, то получится и у нас», – Гарри Поттер.', 35)
'''
