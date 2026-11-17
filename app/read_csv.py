# Modulo nativo para procesar csv
import csv


# función para cargar archivo solo de lectura
def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        data = []

        # Leer fila a fila
        for row in reader:
            iterable = zip(header, row)  # Array de duplas
            # print("*****" * 5)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data


if __name__ == "__main__":
    data = read_csv("./app/data.csv")
    print(data[0])
