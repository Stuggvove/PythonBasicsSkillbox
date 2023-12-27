print("Задание 1")
number = int(input("Введите число: "))
list_num = []

for i in range(number + 1):
    if i % 2 != 0:
        list_num.append(i)
print(list_num)

print("Задание 2")
name_list = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар", "Кирилл"]
result_list = []

for i in range(len(name_list)):
    if i % 2 == 0:
        result_list.append(name_list[i])
print(result_list)

print("Задание 3")
list_cards = [3070, 2060, 3090, 3070, 3090]
result = []
max_num = max(list_cards)
for i in range(len(list_cards)):
    if list_cards[i] != max_num:
        result.append(list_cards[i])
print(result)

print("Задание 4")
films = ["Крепкий орешек", "Назад в будущее", "Таксист", "Леон", "Богемская рапсодия", "Город грехов", "Мементо", "Отступники", "Деревня"]
favourites = []
count_films = int(input("Введите количество фильмов: "))

def write_film():
    for i in range(count_films):
        your_film = input("Введите ваш фильм: ")
        search_Film(your_film, films, favourites)
    print(favourites)

def search_Film(your_film, films, favourites):
    for i in range(len(films)):
        if your_film == films[i]:
            favourites.append(your_film)
        else:
            print("Нет такого фильма")

write_film()

print("Задание 5")
count_containers = int(input("Введите количество контейнеров: "))
containers = []

for i in range(count_containers):
    container = int(input("Введите вес контейнера: "))
    containers.append(container)

new_container = int(input("Введите новый контейнер: "))
containers.append(new_container)
containers.sort()
print(containers)

print("Задание 6")
def rotate_list(lst, k):
    return lst[-k:] + lst[:-k]

lst = [1, 2, 3, 4, 5]
k = 1
rotated_lst = rotate_list(lst, k)
print(rotated_lst)

print("Задание 7")
def main():
    word = input('Введите слово: ')
    if word == word[::-1]:
        print("Палиндром")
    else:
        print("Не палиндром")
main()

print("Задание 8")

nums = [4, 9, 7, 6, 3, 2]

for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[j] < nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
print(nums)

print("Задание 9")
def print_even_in_reverse(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] % 2 == 0:
            print(lst[i])