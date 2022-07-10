import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

def normalize(df):
    #cols = df.select_dtypes('number')
    for col in df:
        df[col] = df[col].apply(lambda val: (val - df[col].mean()) / df[col].std())
    return df

def get_grades(dataset, prep_dataset, house, topic):
    df = prep_dataset[dataset["Hogwarts House"] == house][topic]
    df = df.dropna(inplace=True)
    return df

def plot_hist(dataset, prep_dataset):
    for col in prep_dataset.columns:
        plt.figure()
        plt.hist(get_grades(dataset, prep_dataset, "Gryffindor", col), bins=25, alpha=0.5, label = 'Gry', color = 'r')
        plt.hist(get_grades(dataset, prep_dataset, "Ravenclaw", col), bins=25, alpha=0.5, label = 'Rav', color = 'b')
        plt.hist(get_grades(dataset, prep_dataset, "Slytherin", col), bins=25, alpha=0.5, label = 'Sly', color = 'g')
        plt.hist(get_grades(dataset, prep_dataset, "Hufflepuff", col), bins=25, alpha=0.5, label = 'Huf', color = 'y')
        plt.legend(loc = 'upper right')
        plt.title(col)
        plt.show()



        
def plot_histogram(df, feature):
    plt.figure(figsize=(8, 6))
    print(df.groupby('Hogwarts House')[feature])
    df.groupby('Hogwarts House')[feature].plot(kind='hist', alpha=.5);
    plt.legend();
    plt.title(feature)
    plt.show()
    
        
if __name__ == "__main__":
    courses = ['Arithmancy',
 'Astronomy',
 'Herbology',
 'Defense Against the Dark Arts',
 'Divination',
 'Muggle Studies',
 'Ancient Runes',
 'History of Magic',
 'Transfiguration',
 'Potions',
 'Care of Magical Creatures',
 'Charms',
 'Flying']
    
    df = pd.read_csv(sys.argv[1], index_col = "Index")
    #df = normalize(df)
    
    for course in courses:
        plot_histogram(df, course)
    