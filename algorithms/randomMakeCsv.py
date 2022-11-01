#배열을 랜덤으로 만드는 
import numpy as np
import pandas as pd
import os

for i in range(1):
    T = []
    for _ in range(1024):
        a = np.random.randint(-2 ** 31 - 1, 2 ** 31)
        T.append([a])
    try:
        os.makedirs('./data')
    except:
        pass
    df = pd.DataFrame(T)
    df.to_csv(f'./data/{i}_random.csv', index=False, line_terminator='')
    df = pd.DataFrame(sorted(T))
    df.to_csv(f'./data/{i}_sort.csv', index=False, line_terminator='')
    df = pd.DataFrame(sorted(T, reverse=True))
    df.to_csv(f'./data/{i}_reverse.csv', index=False, line_terminator='')