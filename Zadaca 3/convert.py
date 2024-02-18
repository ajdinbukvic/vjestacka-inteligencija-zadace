import pandas as pd

def convert_csv(csv_input, csv_output):
    # Učitaj CSV datoteku u pandas DataFrame
    data = pd.read_csv(csv_input)

    # Iteriraj kroz sve kolone i mapiraj vrijednosti u jedinstvene numeričke vrijednosti
    for column in data.columns:
        if isinstance(data[column], pd.core.series.Series):
            data[column] = pd.factorize(data[column])[0]

    # Spremi podatke u novi CSV fajl
    data.to_csv(csv_output, index=False)
    print('Podaci su konvertovani i spremljeni u novi CSV')