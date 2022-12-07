import numpy as np
import pandas as pd
import subprocess
import matplotlib.pyplot as plt


def create_sim_row(cache_size, blocks_per, block_size, addresses):
    output = simulate(cache_size, blocks_per, block_size, addresses)
    hits = output.count("HIT")
    return cache_size, blocks_per, block_size, hits


def simulate(cache_size, blocks_per, block_size, addresses):
    proc = subprocess.Popen(f"cache-simulator --cache-size {cache_size} "
                            f"--num-blocks-per-set {blocks_per} "
                            f"--num-words-per-block {block_size} "
                            f"--word-addrs {' '.join(map(str, addresses))}",
                            stdout=subprocess.PIPE, shell=True)

    return proc.stdout.read().decode("utf-8")


def part2():
    words1 = [0, 89, 20, 0, 94, 43, 94, 6, 89, 21, 92, 125]
    words2 = [3, 118, 29, 3, 125, 58, 125, 10, 118, 30, 122, 165]
    words3 = [2, 128, 30, 2, 136, 62, 136, 10, 128, 32, 133, 180]

    data = []
    data.append(create_sim_row(6, 1, 2, words3))
    data.append(create_sim_row(6, 2, 2, words3))
    data.append(create_sim_row(6, 3, 2, words3))
    data.append(create_sim_row(9, 1, 2, words3))
    data.append(create_sim_row(9, 2, 2, words3))
    data.append(create_sim_row(9, 3, 2, words3))
    data.append(create_sim_row(12, 1, 2, words3))
    data.append(create_sim_row(12, 2, 2, words3))
    data.append(create_sim_row(12, 3, 2, words3))
    data.append(create_sim_row(15, 1, 2, words3))
    data.append(create_sim_row(15, 2, 2, words3))
    data.append(create_sim_row(15, 3, 2, words3))
    df = pd.DataFrame(data, columns=["cache size", "set size", "block size", "hits"])
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    top = df["hits"]
    bottom = np.zeros_like(top)
    width = 3
    depth = 1
    ax1.bar3d(df["cache size"], df["set size"], bottom, width, depth, top, shade=True)
    ax1.set_title("Address Set 3")
    ax1.set_ylabel("Set Size")
    ax1.set_xlabel("Cache Size")
    ax1.set_zlabel("Hits")
    plt.tight_layout()
    plt.savefig("set3_p1.jpg")

def part3():
    words1 = [0, 89, 20, 0, 94, 43, 94, 6, 89, 21, 92, 125]
    words2 = [3, 118, 29, 3, 125, 58, 125, 10, 118, 30, 122, 165]
    size = 12
    data = []
    word = words1
    data.append(create_sim_row(size, 1, 1, word))
    data.append(create_sim_row(size, 1, 2, word))
    data.append(create_sim_row(size, 1, 3, word))
    data.append(create_sim_row(size, 2, 1, word))
    data.append(create_sim_row(size, 2, 2, word))
    data.append(create_sim_row(size, 2, 3, word))
    data.append(create_sim_row(size, 3, 1, word))
    data.append(create_sim_row(size, 3, 2, word))
    data.append(create_sim_row(size, 3, 3, word))
    data.append(create_sim_row(size, 4, 1, word))
    data.append(create_sim_row(size, 4, 2, word))
    data.append(create_sim_row(size, 4, 3, word))
    df = pd.DataFrame(data, columns=["cache size", "set size", "block size", "hits"])
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    top = df["hits"]
    bottom = np.zeros_like(top)
    width = 1
    depth = 1
    ax1.bar3d(df["block size"], df["set size"], bottom, width, depth, top, shade=True)
    ax1.set_title("Address Set 1")
    ax1.set_ylabel("Set Size")
    ax1.set_xlabel("Block Size")
    ax1.set_zlabel("Hits")
    plt.tight_layout()
    plt.savefig("set1_p3.jpg")


if __name__ == '__main__':
    part3()

