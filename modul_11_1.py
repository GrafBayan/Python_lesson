import numpy as np

a = np.random.rand(4, 4)
print(a)
print()

b = np.arange(5)
print(b)
print()

a = np.arange(5)
b = np.ones(5) * 3
c = a + b
print(c)
print()

import pandas as pd

data = [{'name': 'Денис', 'age': 30}, {'name': 'Макс', 'age': 25}]
df = pd.DataFrame(data)
print(df)
print()

older_than_25 = df[df['age'] > 25]
print(older_than_25)
print()

sorted_df = df.sort_values(['age'], ascending=False)
print(sorted_df)
print()

import requests

response = requests.get('https://api.github.com')
print(response.json())
print("\n Код requests завершён \n")

def get_example():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Полученные данные:", data)
    else:
        print("Ошибка:", response.status_code)

get_example()


def post_example():
    url = 'https://jsonplaceholder.typicode.com/posts'
    payload = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    response = requests.post(url, json=payload)

    if response.status_code == 201:
        data = response.json()
        print("Созданный объект:", data)
    else:
        print("Ошибка:", response.status_code)

post_example()