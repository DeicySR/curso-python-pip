# Importar modulo
import read_csv
import utils

import charts

data = [
    {"Country/Territory": "Colombia", "Population": 500},
    {"Country/Territory": "Bolivia", "Population": 300},
]


def run1():
    # Ejecutar una función de un modulo
    keys, values = utils.get_population()
    print(keys, values)
    print("--------------\n")

    # Llamar una variable de un modulo
    print(utils.A)
    print("--------------\n")

    # Ejecutar una función de un modulo
    country = input("Type Country =>")
    result = utils.population_by_country(data, country)
    print(result)
    print("--------------\n")


def run2():
    # Leer los datos del CSV
    data = read_csv.read_csv("data.csv")
    # Solicitar el país
    country = input("Type Country =>")
    # Filtrar los registros
    result = utils.population_by_country(data, country)
    # Comprobar si encontramos el país
    if len(result) > 0:
        country = result[0]
        # Obtener la información de población
        labels, values = utils.get_population_country(country)
        # Generar la gráfica
        charts.generate_bar_chart(country["Country/Territory"], labels, values)
    else:
        print("No se encontró el país solicitado")


def run3():
    # Leer los datos del CSV
    data = read_csv.read_csv("data.csv")
    # Solicitar el país
    continent = input("Type Continent =>")
    # Filtrar los registros por el continente
    result = list(filter(lambda item: item["Continent"] == continent, data))
    # Comprobar si encontramos el continente
    if len(result) > 0:
        # Obtener los paises
        countries = list(map(lambda x: x["Country/Territory"], result))
        # Obtener los porcentajes
        percentages = list(map(lambda x: x["World Population Percentage"], result))
        # Generar la gráfica
        charts.generate_pie_chart(continent, countries, percentages)
    else:
        print("No se encontró el continente")


if __name__ == "__main__":
    run3()
    run2()
