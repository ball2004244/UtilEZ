import pandas as pd
import pickle
'''
This file auto convert files with different types to each other
'''

'''
This function applicable for raw text file to pkl file
'''
def pkl2txt(pkl_file: str = 'test.pkl', txt_file: str = 'test.txt') -> None:
    data: any = None
    with open(pkl_file, 'rb') as f:
        data = pickle.load(f)

    with open(txt_file, 'w') as f:
        f.write(str(data))

    print('Convert successfully!')
    
'''
This function convert the presaved pandas in pkl to txt file
'''
def pickled_df2txt(pkl_file: str = 'test.pkl', txt_file: str = 'test.txt') -> None:
    df: pd.DataFrame = pd.read_pickle(pkl_file)
    df.to_csv(txt_file, sep = '\t')
    
    print('Convert successfully!')