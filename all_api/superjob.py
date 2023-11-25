import json
from pprint import pprint
import requests

from all_api.implement import api_key
from all_api.abc_class import SearchApi


class SuperJobApi(SearchApi):
    def __init__(self, text):
        self.api_key = api_key
        self.text = text
        self.headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': self.api_key,
            'Authorisation': f'Bearer {self.api_key[3:]}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        self.params = {
            'keywords': self.text
        }

        self.response = self.receiving()

    def receiving(self):
        return requests.get('https://api.superjob.ru/2.0/vacancies/', headers=self.headers, params=self.params).text

    def get_vacancies(self) -> list:
        vacancies = json.loads(self.response)
        structured_vacancy = []
        for vacancy in vacancies['objects']:
            city = 'Не указано'
            address = vacancy.get('address')
            if address is not None:
                city_parts = address.split(',')
                if len(city_parts) > 0:
                    city = city_parts[0].strip()

            currency = vacancy.get("currency", "Не указано")
            payment_from = vacancy.get("payment_from", "Не указано")
            payment_to = vacancy.get("payment_to", "Не указано")

            structured_salary = {
                "currency": currency,
                "from": payment_from,
                "to": payment_to
            }

            structured_vacancy.append({
                'name': vacancy.get('profession', 'Не указано'),
                'salary': structured_salary,
                'description': vacancy.get('candidat', 'Не указано'),
                'city': city,
                'id': vacancy.get('id', 'Не указано'),
                'alternate_url': vacancy.get('link', 'Не указано'),
                'platform': 'SuperJob'
            })

        return structured_vacancy


