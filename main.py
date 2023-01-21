import requests
import unittest

# ЗАДАЧА №1
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



# Задача №2 Автотест API Яндекса
# Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
#
# Пример положительных тестов:
#
# Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов.


def folder_creation(folder_name, ya_token):
        url = f'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {ya_token}'}
        params = {'path': f'{folder_name}',
                  'overwrite': 'false'}
        response = requests.put(url=url, headers=headers, params=params)
        return response

class TestFolderCreation(unittest.TestCase):
#check Ya resonse 201 that folder is created
    def test_API_positive1(self):
        ya_token = ''
        folder_name = 'unittest'
        self.assertEqual(folder_creation(folder_name, ya_token).status_code, 201)
#check Ya absence of response 409 that there is conflict
    def test_API_negative1(self):
        ya_token = ''
        folder_name = 'unittest'
        self.assertNotEqual(folder_creation(folder_name, ya_token).status_code, 409)


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

    ya_token = ''
    folder_name = 'unittest'
    print(folder_creation(folder_name, ya_token))
    unittest.main()
