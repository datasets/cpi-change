import requests


def process():
    url = "https://ers.usda.gov/sites/default/files/_laserfiche/DataFiles/50673/historicalcpi.csv?v=78562"
    response = requests.get(url)
    response.raise_for_status()
    text = response.content.decode("utf-8-sig")
    with open("data/data.csv", "w") as f:
        f.write(text)


if __name__ == "__main__":
    process()
