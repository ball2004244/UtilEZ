import json

def txt2json(infile: str = 'test.txt', outfile: str = 'test.json') -> None:
    '''
    This function try to convert the txt file to json file
    '''
    data: any = None
    
    with open(infile, 'r') as f:
        data = eval(f.read())
        
    with open(outfile, 'w') as f:
        f.write(json.dumps(data, indent=4))
        
    print('Convert successfully!')
    
if __name__ == '__main__':
    infile = input('Name of input txt file (default: test.txt): ') or 'test.txt'
    outfile = input('Name of output file (default: test.json): ') or 'test.json'
    txt2json(infile, outfile)