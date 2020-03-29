import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle


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
    c = None
    if len(filename.split("_")) > 2:
        c = filename.split("_")[2]
    if not c is None:
        plt.savefig("{}p_{}c.png".format(p,c), bbox_inches='tight')
    else:
        plt.savefig("{}p.png".format(p), bbox_inches='tight')

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


def num_loops():
    df = pd.read_csv("loop_count.csv")
    plt.plot('n','loop_count',data=df,marker='.',ls='--')
    plt.ylabel("number of loops")
    plt.xlabel("n (numer of rows)")
    plt.savefig("num_loops_per_size.png", bbox_inches='tight')
    plt.show()


def partial_steps():
    size = 5
    colors = ['r','b','g','y','c'] * 2
    with open("list_dump","rb") as dump_file:
        df = pickle.load(dump_file)
    fig, ax = plt.subplots()
    lines = list(range(1, size+1))
    for row in df:
        tmp_row = row[1][:size]
        ax.scatter([row[0]] * size, tmp_row, c=colors[:size])
    # add annotation to the final coll
    final_row = df[-1]
    final_list = final_row[1][:size]
    for i, txt in enumerate(lines):
        ax.annotate(txt, (final_row[0],final_list[i]), xytext=(3, 3), textcoords='offset pixels')

    x = []
    yy = [[] for i in range(size)]
    for row in df:
        x.append(row[0])
        for i in range(size):
            yy[i].append(row[1][i])

    for i in range(size):
        fit, _, _, _, _ = np.polyfit(x, yy[i], 1, full=True)

        label = "{}: y = {:.3}x + ({:.3})".format(i+1,fit[0],fit[1])
        y = np.polyval(fit,x)
        ax.plot(x,y,c=colors[i],label=label)

    ax.legend()
    plt.ylabel("Number of flips per loop")
    plt.xlabel("n (number of rows(")
    plt.savefig("num_flips_per_loop.png", bbox_inches='tight')
    plt.show()


def test():
    size = 5
    with open("list_dump", "rb") as dump_file:
        df = pickle.load(dump_file)
    x = []
    yy = [[] for i in range(size)]
    for row in df:
        x.append(row[0])
        for i in range(size):
            yy[i].append(row[1][i])
    fit, _, _, _, _ = np.polyfit(x, yy[0], 1,full=True)
    print(fit)
    # print(R)

if __name__ == "__main__":
    # datesets = [
    #     "results_0.5",
    #     "results_0.5_1.6",
    #     "results_0.5_2",
    #     "results_0.49",
    #     "results_0.51"
    # ]
    # for name in datesets:
    #     create_compare_gragh(name)
    # num_loops()
    # partial_steps()
    # test()
    pass