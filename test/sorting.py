
'''Сортировка вставками'''
def insertion_sort(array):
  for i in 1 .. (length(array) - 1):
    item_to_insert = array[i]
    j = i
    while j > 0 and item_to_insert < array[j-1]:
      array[j] = array[j-1]
      j -= 1
    array[j] = item_to_insert
    print('step {i}, sorted {i+1} elements: {array}')


insertion_sort([11, 2, 9, 7, 1])


'''Сортировка по ключу 1'''
digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6] # длины слов «ноль», «один»,...


def card_strength(card): # ключ сравнения
    return digit_lengths[card]

# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_key(array, key):
  for i in range(1, len(array)):
    item_to_insert = array[i]
    j = i
    # заменим сравнение item_to_insert < array[j-1] на сравнение ключей
    while j > 0 and key(item_to_insert) < key(array[j-1]):
      array[j] = array[j-1]
      j -= 1
    array[j] = item_to_insert


cards = [3, 7, 9, 2, 3]
insertion_sort_by_key(cards, card_strength)


'''Сортировка по ключу 2'''
digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]  # длины слов «ноль», «один»,...

def is_first_card_weaker(card_1, card_2):  # функция-компаратор
    return digit_lengths[card_1] < digit_lengths[card_2]

# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_comparator(array, less):
  for i in range(1, len(array)):
    item_to_insert = array[i]
    j = i
    # заменим сравнение item_to_insert < array[j-1] на компаратор less
    while j > 0 and less(item_to_insert, array[j-1]):
      array[j] = array[j-1]
      j -= 1
    array[j] = item_to_insert

cards = [3, 7, 9, 2, 3]
insertion_sort_by_comparator(cards, is_first_card_weaker)