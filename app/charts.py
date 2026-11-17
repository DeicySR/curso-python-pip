import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    # plt.show()
    plt.savefig(f"./imgs/{name}_bar_chart.png")
    plt.close(fig)


def generate_pie_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis("equal")
    # plt.show()
    plt.savefig(f"./imgs/{name}_pie_chart.png")
    plt.close(fig)


if __name__ == "__main__":
    labels = ["a", "b", "c"]
    values = [10, 40, 800]
    # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
