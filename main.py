import requests


# решил добавить Iron Man чтоб сравнить если будут одинаково большие статы
superheroes_intelligence = {}
superheroes = ['Hulk', 'Captain America', 'Thanos', 'Iron Man']

url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
response = requests.get(url)
for i in response.json():
    if i['name'] in superheroes:
        superheroes_intelligence[i['name']] = i['powerstats']['intelligence']

# Сортируем словарь по значениям чтоб 1 значением словаря было самым большим
sorted_tuples = reversed(sorted(superheroes_intelligence.items(), key=lambda x: x[1]))
superheroes_intelligence = dict(sorted_tuples)

# Сравниваем в цикле каждое значение с самым большим
print(f'Самым умным супергероем из {", ".join(superheroes)} является:')
for name, stat in superheroes_intelligence.items():
    if stat == list(superheroes_intelligence.values())[0]:
        print(name)
