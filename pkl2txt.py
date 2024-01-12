import pandas as pd

'''
This function convert the presaved pandas in pkl to txt file
'''
def pickled_df2txt(pkl_file: str = 'test.pkl', txt_file: str = 'test.txt') -> None:
    df: pd.DataFrame = pd.read_pickle(pkl_file)
    df.to_csv(txt_file, sep = '\t')
    
    print('Convert successfully!')
    
if __name__ == '__main__':
    infile: str = input('Name of input pickle (default: test.pkl): ')
    outfile: str = input('Name of output txt (default: test.txt): ')

    pickled_df2txt(infile, outfile)