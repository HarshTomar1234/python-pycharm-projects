import pandas as pd

concentric = pd.read_csv('toy_datasets/concertriccir2.csv', delimiter='\t')
linear = pd.read_csv('toy_datasets/linearsep.csv', delimiter='\t')
outlier = pd.read_csv('toy_datasets/outlier.csv', delimiter='\t')
spiral = pd.read_csv('toy_datasets/twoSpirals.csv', delimiter='\t')
ushape = pd.read_csv('toy_datasets/ushape.csv', delimiter='\t')
xor = pd.read_csv('toy_datasets/xor.csv', delimiter='\t')

def load_dataset():

    return concentric,linear,outlier,spiral,ushape,xor

def load_initial_graph(dataset,ax):
    if dataset == "U-Shaped":
        ax.scatter(ushape.iloc[:, 0], ushape.iloc[:, 1], c=ushape.iloc[:, 2], cmap='rainbow')
        df = ushape
    elif dataset == "Linearly Separable":
        ax.scatter(linear.iloc[:, 0], linear.iloc[:, 1], c=linear.iloc[:, 2], cmap='rainbow')
        df = linear
    elif dataset == "Outlier":
        ax.scatter(outlier.iloc[:, 0], outlier.iloc[:, 1], c=outlier.iloc[:, 2], cmap='rainbow')
        df = outlier
    elif dataset == "Two Spirals":
        ax.scatter(spiral.iloc[:, 0], spiral.iloc[:, 1], c=spiral.iloc[:, 2], cmap='rainbow')
        df = spiral
    elif dataset == "Concentric Circles":
        ax.scatter(concentric.iloc[:, 0], concentric.iloc[:, 1], c=concentric.iloc[:, 2], cmap='rainbow')
        df = concentric
    elif dataset == "XOR":
        ax.scatter(xor.iloc[:, 0], xor.iloc[:, 1], c=xor.iloc[:, 2], cmap='rainbow')
        df = xor


    return df

