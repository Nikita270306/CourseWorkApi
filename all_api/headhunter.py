from pprint import pprint

import requests

from all_api.abc_class import SearchApi


class HeadHunterApi(SearchApi):
    def __init__(self, profession):
        self.profession = profession

    def get_vacancies(self) -> list:
        params = {
            'text': self.profession,
            'only_with_salary': 'true'}
        data = requests.get("https://api.hh.ru/vacancies", params=params).json()
        structured_vacancy = []
        for vacancy in data['items']:
            city = None
            address = vacancy.get('address')
            if address is not None:
                city = address.get('city')
            if city is None:
                city = 'Не указано'
            description = vacancy.get('snippet', {})
            requirements = vacancy.get('requirement', 'Не указано')
            responsibilities = vacancy.get('responsibility', 'Не указано')

            if requirements == 'Не указано' and responsibilities == 'Не указано':
                formatted_description = "Не указано"
            else:
                formatted_description = f"Требования: {requirements}\nОбязанности:{responsibilities}"

            structured_vacancy.append({
                'id': vacancy.get('id', 'Не указано'),
                'name': vacancy.get('name', 'Не указано'),
                'salary': vacancy.get('salary', 'Не указано'),
                'description': formatted_description,
                'url': vacancy.get('alternate_url', 'Не указано'),
                'city': city,
                'platform': 'HeadHunter'
            })

        return structured_vacancy


if __name__ == "__main__":
    pprint(HeadHunterApi('Юрист').get_vacancies())