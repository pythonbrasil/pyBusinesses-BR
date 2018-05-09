import re
from collections import Counter, defaultdict
import matplotlib.pyplot as plt


def get_data(file):
    region = state = city = ''
    data = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    for line in file.readlines():
        if line.startswith('## '):
            region = line[2:].strip()
        elif line.startswith('### '):
            state = line[3:].strip()
        elif line.startswith('#### '):
            city = line[4:].strip()
        elif line.startswith('!') and region and state and city:
            data[region][state][city] += 1

    return data


def get_cities(data):
    cities_data = defaultdict(int)

    for states in data.values():
        for cities in states.values():
            cities_data.update(cities)

    return cities_data


def get_states(data):
    states_data = defaultdict(int)

    for states in data.values():
        for state, cities in states.items():
            for total in cities.values():
                states_data[state] += total

    return states_data


def get_regions(data):
    regions_data = defaultdict(int)

    for region, states in data.items():
        for cities in states.values():
            for total in cities.values():
                regions_data[region] += total

    return regions_data


def draw_plot(data, title, region, output, subplot):
    xaxis = range(len(data))
    keys_freq = []
    values_freq = []

    for key, value in data.most_common()[::1]:
        keys_freq.append(key)
        values_freq.append(value)

    plt.subplot(subplot)
    plt.bar(xaxis, values_freq)
    plt.xticks(xaxis, keys_freq)
    plt.title(title)
    plt.xlabel(region)
    plt.ylabel("Número de Empresas")
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90)
    plt.savefig(output)


def generate_report_cities(data):
    data = Counter(get_cities(data))
    draw_plot(data, "Cidades mais pythônicas", "Cidades",
              "ranking_cities", 211)


def generate_report_states(data):
    data = Counter(get_states(data))
    draw_plot(data, "Estados mais pythônicos", "Estados",
              "ranking_states", 221)


def generate_report_regions(data):
    data = Counter(get_regions(data))
    draw_plot(data, "Regiões mais pythônicas", "Regiões",
              "ranking_regions", 232)


if __name__ == "__main__":
    with open('../README.md',encoding='utf-8') as file:
        data = get_data(file)

    generate_report_cities(data)
    generate_report_states(data)
    generate_report_regions(data)
