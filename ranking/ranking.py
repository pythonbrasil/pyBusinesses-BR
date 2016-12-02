#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from collections import Counter
import matplotlib.pyplot as plt


def getCities():
    file = 'README.md'
    id_city = '#### '
    cities = {}

    with open(file) as f:
        readme = f.readlines()

    for index, line in enumerate(readme):
        if id_city in line:
            cities[line[5:-1]] = int(readme[index+1][7:-1])

    return cities

def run():
    data = Counter(getCities())
    xaxis = range(len(data))
    keys_freq = []
    values_freq = []

    for key, value in data.most_common()[::1]:
        keys_freq.append(key)
        values_freq.append(value)

    plt.subplot(211)
    plt.bar(xaxis, values_freq)
    plt.xticks(xaxis, keys_freq)
    plt.title("Ranking das cidades mais pythônicas")
    plt.xlabel("Cidades")
    plt.ylabel("Número de Empresas")
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90)

    plt.savefig('ranking')

if __name__ == "__main__":
    run()
