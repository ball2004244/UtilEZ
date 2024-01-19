import os
import sys
import csv
import json

'''
This file handle data reading and writing to file
'''

'''
This functions read data from a given file
'''


def read_file(file_name: str = 'test.txt', read_bytes: bool = False) -> str:
    data: list = []
    read_type = 'r'
    if read_bytes:
        read_type += 'b'

    try:
        with open(file_name, read_type) as f:
            for line in f:
                data.append(line)

        return ''.join(data)
    except FileNotFoundError:
        print('File not found!')
        return ''


'''
This function write data to a given file, work well with large data
'''


def write_file(data: str, file_name: str = 'test.txt', write_bytes: bool = False) -> None:
    write_type = 'w'
    if write_bytes:
        write_type += 'b'

    try:
        with open(file_name, write_type) as f:
            f.write(data)
        print('Write successfully!')
    except FileNotFoundError:
        print('File not found!')


'''
This function append data to a given file, work well with large data
'''


def delete_file(file_name: str = 'test.txt') -> None:
    os.remove(file_name)
    print('Remove successfully!')


'''
This function move a file around
'''


def move_file(old_path: str = 'test.txt', new_path: str = 'test.txt') -> None:
    try:
        os.rename(old_path, new_path)
        print('Move successfully!')
    except FileNotFoundError:
        print('File not found!')


'''
This function rename a file
'''


def rename_file(old_name: str, new_name: str) -> None:
    try:
        os.rename(old_name, new_name)
        print('Rename successfully!')
    except FileNotFoundError:
        print('File not found!')


'''
This function create a new folder
'''


def create_dir(dir_name: str) -> None:
    try:
        os.mkdir(dir_name)
        print('Create successfully!')
    except FileExistsError:
        print('Directory already exists!')
    except FileNotFoundError:
        print('File not found!')


'''
This function delete a folder
'''


def delete_dir(dir_name: str, force: bool = False) -> None:
    try:
        if force:
            os.removedirs(dir_name)
        else:
            os.rmdir(dir_name)
        print('Remove successfully!')
    except FileNotFoundError:
        print('File not found!')


'''
This function reads a csv file
'''


def read_csv(file_name: str = 'test.csv') -> list:
    data: list = []
    try:
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print('File not found!')
        return []


'''
This function writes a csv file
'''


def write_csv(data: list, file_name: str = 'test.csv') -> None:
    try:
        with open(file_name, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(data)
        print('Write successfully!')
    except FileNotFoundError:
        print('File not found!')


'''
This function reads a json file
'''


def read_json(file_name: str = 'test.json') -> dict:
    data: dict = {}
    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print('File not found!')
        return {}


'''
This function writes a json file
'''


def write_json(data: dict, file_name: str = 'test.json') -> None:
    try:
        with open(file_name, 'w') as f:
            json.dump(data, f)
        print('Write successfully!')
    except FileNotFoundError:
        print('File not found!')
