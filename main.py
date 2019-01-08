'''
Created on Feb 13, 2014

@author: sushant
'''

from dbscanner import DBScanner
import re, csv, sys


CONFIG = 'config'
DATA = 'data/abc.csv'

def get_data(config):
    data = []
    with open(DATA, 'rb') as file_obj:
        csv_reader = csv.reader(file_obj)
        for id_, row in enumerate(csv_reader):
            if len(row) < config['dim']:
                print ("ERROR: The data you have provided has fewer \
                    dimensions than expected (dim = %d < %d)"
                    % (config['dim'], len(row)))
                sys.exit()
            else:
                point = {'id':id_, 'value': []}
                for dim in range(0, config['dim']):
                    point['value'].append(float(row[dim]))
                data.append(point)
    return data


def read_config():
    config = {}
    try:
        with open(CONFIG, 'rb') as file_obj:
            for line in file_obj:
                if line[0] != '#' and line.strip() !='':
                    key, value = line.split('=')
                    if '.' in value.strip():
                        config[key.strip()] = float(value.strip())
                    else:
                        config[key.strip()] = int(value.strip())
    except:
        print ("Error reading the configuration file.\
            expected lines: param = value \n param = {eps, min_pts, dim}, \
            value = {float, int, int}")
        sys.exit()
    return config

def main():

    config = read_config()
    dbc = DBScanner(config)
    data = get_data(config)

    dbc.dbscan(data)
    dbc.export()

if __name__ == "__main__":
    main()
