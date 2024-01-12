import pickle

'''
This file try to convert the pkl file to txt file
'''

infile = input('Name of input pickle file (default: test.pkl): ') or 'test.pkl'
outfile = input('Name of output file (default: test.txt): ') or 'test.txt'

data: any = None

with open(infile, 'rb') as f:
    data = pickle.load(f)
    
with open(outfile, 'w') as f:
    f.write(str(data))
    
print('Convert successfully!')