import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def create_compare_gragh (filename):
    df = pd.read_csv(filename + ".csv")
    fig, ax = plt.subplots()
    ax.plot(df['n'] ,df['encode_time'],color="b", label="encode time")
    # ax.plot(df['n'] ,df['decode_time'],color="b", label="decode time")
    ax.set_xlabel("number of rows (n)")
    ax.set_ylabel("time (seconds)",color="b")
    # set the x and y lims to better present the data
    ax.set_xlim(0,1*10**4)
    ax.set_ylim(0,30)

    ax2 = ax.twinx()
    ax2.plot(df['n'] ,df['count_flips'], color="g",label="number of flips")
    ax2.set_ylabel("number of iterative steps",color="g")
    ax2.set_ylim(0, 20000)
    # plt.legend()
    # plt.savefig("{}_compare.png".format(filename))
    size = "n*n"
    if len(filename.split("_")) > 2:
        size = "n*(n/{})".format(filename.split("_")[2])
    p = str(float(filename.split("_")[1]) * 100)[:2]
    plt.title("time and number of iterations as a function of n\n {} matrices\n {} percent chance to write 1".format(size,p))
    plt.savefig("{}_compare.png".format(filename), bbox_inches='tight')

    plt.show()

def check_similarity(filename):
    df = pd.read_csv(filename)
    x = np.array(range(0,10000,200))**2
    log_y = np.log2(x)
    sqrt_y  = np.sqrt(x) * 1.7
    # plt.plot(x,log_y,color="b", label="log")
    plt.plot(df['n'] **2 ,df['count_flips'], color="g",label="number of flips")
    plt.plot(x,sqrt_y,color="r", label="sqrt * const")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    datesets = [
        "results_0.5",
        "results_0.5_1.6",
        "results_0.5_2",
        "results_0.48",
        "results_0.49",
        "results_0.51",
        "results_0.5_4"
    ]
    for name in datesets:
        create_compare_gragh(name)