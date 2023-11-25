import json
from work_with_vacancy.abc_changing import ChangeVacancy


class ChangeVacancyOrig(ChangeVacancy):
    def __init__(self, path):
        self.path = path

    def get_all_vacancies(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError as e:
            print(f"Error reading the file: {e}")
            return []
        except Exception as e:
            print(f"Error reading the file: {e}")
            return []

    def save_vacancies(self, jobs):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(jobs, file, indent=2)

    def add_vacancy(self, data):
        all_vacancies = self.get_all_vacancies()
        all_vacancies.append(data)
        self.save_vacancies(all_vacancies)

    def get_vacancy_by_id(self, vacancy_id):
        all_vacancies = self.get_all_vacancies()
        for vacancy in all_vacancies:
            if str(vacancy.get('id')) == f'{vacancy_id}':
                return vacancy

    def get_vacancy_by_salary(self, salary):
        all_vacancies = self.get_all_vacancies()
        good_vacancies = []
        for vacancy in all_vacancies:
            if vacancy['salary'].get("to", 0) is not None:
                if vacancy['salary'].get("to", 0) >= salary:
                    good_vacancies.append(vacancy)
            else:
                if vacancy['salary'].get("from", 0) >= salary:
                    good_vacancies.append(vacancy)
        return good_vacancies

