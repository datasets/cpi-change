import csv
import requests

def process():
    url = 'https://ers.usda.gov/sites/default/files/_laserfiche/DataFiles/50673/historicalcpi.csv?v=78562'
    response = requests.get(url)
    with open('data/data.csv', 'w') as f:
        f.write(response.text)

if __name__ == '__main__':
    process()