# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#
# import types
#
# def flat_generator_(values_):
#     new_list = reemoveNestings(values_)
#     cursor = 0
#     while cursor != len(new_list):
#         yield new_list[cursor]
#         cursor += 1
#
# def test_4():
#
#     list_of_lists_2 = [
#         [['a'], ['b', 'c']],
#         ['d', 'e', [['f'], 'h'], False],
#         [1, 2, None, [[[[['!']]]]], []]
#     ]
#
#     for flat_iterator_item, check_item in zip(
#             flat_generator_(list_of_lists_2),
#             ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
#     ):
#
#         assert flat_iterator_item == check_item
#
#     assert list(flat_generator_(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
#
#     assert isinstance(flat_generator_(list_of_lists_2), types.GeneratorType)
#
#
# if __name__ == '__main__':
#     test_1()
#     test_2()
#     test_3()
#     test_4()

#Task1 0906
#Дан список с визитами по городам и странам. Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России."
def task_1(geo_logs):
    result = filter(lambda log_item: {key: value for key, value in log_item.items() if value[1] == 'Россия'}, geo_logs)
    return list(result)

def test_1():
        geo_logs = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Лиссабон', 'Португалия']},
            {'visit5': ['Париж', 'Франция']},
            {'visit6': ['Лиссабон', 'Португалия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]

        geo_logs_check = [
            {'visit1': ['Москва', 'Россия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]
        # for task_1_item, check_item in zip(task_1(geo_logs)),geo_logs_check):
        #     assert task_1_item == check_item

        for task1_item in task_1(geo_logs):
            for key, value in task1_item.items():
                assert value[1] == 'Россия'

        assert list(task_1(geo_logs)) == geo_logs_check


# #task2
# #Выведите на экран все уникальные гео-ID из значений словаря ids.#Т.е. список вида [213, 15, 54, 119, 98, 35]
def task_2(ids):
    result_set = set(sum(ids.values(), []))
    return result_set

def test_2():
        ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
        ids_check = [98, 35, 15, 213, 54, 119]
        for task_2_item in task_2(ids):
            assert task_2_item in ids_check
        assert list(task_2(ids)) == ids_check

#task3
#Дан список поисковых запросов. Получить распределение количества слов в них. Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.
def task_3(queries):
    len_queries = len(queries)
    #шаг1 - подсчет слов в текстовых запросах списка
    words_counter = []
    for words in queries:
      words = list(words.split())
      words_counter.append(len(words))
    #шаг2 - мэппинг к-во слов в запросе к к-ву запросов
    occurrences = {}
    for x in words_counter:
        if x in occurrences:
            occurrences[x] += 1
        else:
            occurrences[x] = 1
    #шаг3 - % распределение запросов по к-ву слов
    result=[]
    for key,value in occurrences.items():
        result.append(f'Поисковых запросов из {key} слов/слова - {round(value/len_queries*100)} %')
    return result

def test_3():
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]
# queries_check = ['Поисковых запросов из 3 слов/слова - 57 %', 'Поисковых запросов из 2 слов/слова - 43 %']
    key_numbers_check = ['3','57','2','43']
    task_3_check = []
    for task_3_item in task_3(queries):
        for word in task_3_item.split():
            task_3_check.append(word)
    print(task_3_check)

    for key_number in key_numbers_check:
        assert key_number in task_3_check

# #task4
# #Дана статистика рекламных каналов по объемам продаж.
# #Напишите скрипт, который возвращает название канала с максимальным объемом. #Т.е. в данном примере скрипт должен возвращать 'yandex'.
#
# stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
# channal_max = max(stats, key = stats.get)
# #https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-max/
# print(channal_max)
# print()
#
# #Task5
# #Напишите код для преобразования произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100] (он может быть любой длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}
# random_ = ['2018-01-01', 'yandex', 'cpc', 100]
# random_dict = {random_[-2]: random_[-1]}
# # print(random_dict)
# # print(random_[-3::-1])
# for x in random_[-3::-1]:
#   random_dict = {x:random_dict}
# print(random_dict)
# #Alternative solution from Expert comments:
# #Вы вводите первый словарь list[-2]: list[-1] #Далее по циклу идете по правильному срезу с конца листа, т.е. можно применять сразу несколько срезов на лист. Пройти с конца [::-1] и с нужного элемента [2:] т.е. как бы в 3-его элемента с конца листа. #Дальше думаю разберетесь. Главное по сути правильно сделать срезу в листе, а так задача на 3 строчки.
#
#
if __name__ == '__main__':
    logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]

    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]

    print(task_1(logs))
    test_1()
    print(task_2(ids))
    test_2()
    print(task_3(queries))
    test_3()
