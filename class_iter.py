import json


class CountryWiki:

    def __init__(self, countries):
        self.countries = countries
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > len(self.countries):
            raise StopIteration
        country = self.countries[self.counter - 1]['name']['common'].replace(' ', '_')
        self.counter += 1
        href = f'https://en.wikipedia.org/wiki/{country}'
        result = open('result.txt', 'a', encoding='utf-8')
        result.write(f'{country} -----> {href}\n')


if __name__ == '__main__':
    file = open('countries.json', encoding='utf-8')
    countries_json = json.load(file)

    wiki_searcher = CountryWiki(countries_json)
    for item in wiki_searcher:
        pass
