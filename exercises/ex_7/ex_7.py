'''
Stworzyć skrypt pythonowy, który połączy się z API, które zawiera informacje
o browarach (dokumentacja https://www.openbrewerydb.org/documentation).
Należy w pythonie zrobić klasę
Brewery , która będzie zawierała takie atrybuty jakich dostarcza API wraz z
odpowiednim typowaniem.
W klasie należy zaimplementować magiczną metodę
__str__ która będzie opisywała dane przechowywane w obiekcie.
Skrypt ma się połączyć do API i pobrać 20 pierwszych obiektów, a następnie
utworzyć listę 20 instancji klasy
Brewery , którą przeiteruje i wyświetli każdy obiekt z osobna.
'''
from typing import List

import requests

from exercises.ex_7.Brewery import Brewery


def fetch_breweries() -> List[Brewery]:
    url = 'https://api.openbrewerydb.org/v1/breweries'
    response = requests.get(url, params={'per_page': 20})
    data = response.json()

    breweries = []

    # Tworzymy obiekty Brewery na podstawie danych z API
    for brewery_data in data:
        brewery = Brewery(
            id=brewery_data.get('id'),
            name=brewery_data.get('name'),
            brewery_type=brewery_data.get('brewery_type'),
            street=brewery_data.get('street', ''),
            city=brewery_data.get('city', ''),
            state=brewery_data.get('state', ''),
            postal_code=brewery_data.get('postal_code', ''),
            country=brewery_data.get('country', ''),
            phone=brewery_data.get('phone', ''),
        )
        breweries.append(brewery)

    return breweries


if __name__ == "__main__":
    breweries = fetch_breweries()
    for brewery in breweries:
        print(brewery)
