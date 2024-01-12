from random import randint, choice
import json
import pickle
'''
This file generate a random json data and store in pickle file
'''
def gen_ran_field(data_type: str) -> any:
    field_generators = {
        'str': lambda: ''.join([chr(randint(97, 122)) for _ in range(randint(1, 100))]),
        'int': lambda: randint(0, 100),
        'float': lambda: randint(0, 100) + randint(0, 100) / 100,
        'bool': lambda: choice([True, False]),
        'list': lambda: [gen_ran_field(choice(['str', 'int', 'float', 'bool'])) for _ in range(randint(1, 10))],
        'dict': lambda: {gen_ran_field('str'): gen_ran_field(choice(['str', 'int', 'float', 'bool'])) for _ in range(randint(1, 10))}
    }

    if data_type not in field_generators:
        raise Exception('Invalid type')

    return field_generators[data_type]()

def random_json() -> dict:
    allowed_fields = {
        'Name': 'str',
        'Age': 'int',
        'Job': 'str',
        'Hobby': 'str',
        'Address': 'str',
        'Phone': 'str',
        'Email': 'str',
        'Website': 'str',
        'Company': 'str',
        'School': 'str',
        'Major': 'str',
        'Degree': 'str',
        'Skill': 'str',
        'Height': 'float',
        'Weight': 'float',
        'IsMarried': 'bool',
        'Languages': 'list',
        'Education': 'dict'
    }

    num_field = randint(1, len(allowed_fields))

    data = {}
    i = 0
    while i < num_field:
        field = choice(list(allowed_fields.keys()))
        if field in data:
            continue

        data[field] = gen_ran_field(allowed_fields[field])
        i += 1
        
    return data

def save_json(data: dict, file_name: str = 'test.json') -> None:
    with open(file_name, 'w') as f:
        f.write(json.dumps(data, indent=4))
        
def save_pickle(data: dict, file_name: str = 'test.pkl') -> None:
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)
        
if __name__ == '__main__':
    data = random_json()
    save_json(data)
    save_pickle(data)