import pandas as pd
import numpy as np

if __name__ == '__main__':
    dataset = pd.read_csv('annotations_full.csv')
    dataset['1'] = dataset['xmax_relative']
    dataset['2'] = dataset['ymin_relative']
    dataset['3'] = dataset['xmin_relative']
    dataset['4'] = dataset['ymax_relative']
    dataset.to_csv('annotations_full_filled.csv', index=False)