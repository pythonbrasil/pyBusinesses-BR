#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from collections import Counter
import matplotlib.pyplot as plt
import re

with open('../README.md') as f:
        readme = f.readlines()

def getCities():
    id_city = '#### '
    cities = {}

    for index, line in enumerate(readme):
        if re.match(r'^\s*'+id_city, line):
            cities[line[5:-1]] = int(readme[index+1][7:-1])

    return cities


def getStates():
    id_state = '### '
    states = {}

    for index, line in enumerate(readme):
        if re.match(r'^\s*'+id_state, line):
            states[line[4:-1]] = int(readme[index+1][7:-1])

    return states

def getRegions():
    id_region = '## '
    regions = {}

    for index, line in enumerate(readme):
        if re.match(r'^\s*'+id_region, line):
            regions[line[3:-1]] = int(readme[index+1][7:-1])

    return regions

def drawPlot(data, title, region, output, subplot):
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

def generateReportCities():
    data = Counter(getCities())
    drawPlot(data, "Cidades mais pythônicas", "Cidades", "ranking_cities", 211)


def generateReportStates():
    data = Counter(getStates())
    drawPlot(data, "Estados mais pythônicos", "Estados", "ranking_states", 221)

def generateReportRegions():
    data = Counter(getRegions())
    drawPlot(data, "Regiões mais pythônicas", "Regiões", "ranking_regions", 232)


if __name__ == "__main__":
    generateReportCities()
    generateReportStates()
    generateReportRegions()
