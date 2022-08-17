import requests
import pandas as pd

#voeg csv met daarin adresbestanden toe geformateerd als volgt: https://loc.geopunt.be/v1/Location?q=Gent%2C%20Wellingstraat%202
df = pd.read_csv(r"C:\Users\vandewsa\Downloads\urls - Blad1 (2).csv")

lijst = df['url'].tolist()

for value in lijst:
    response = requests.get(value)
    print(response.json())
