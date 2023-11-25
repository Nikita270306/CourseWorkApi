import json
from pprint import pprint

from all_api.superjob import SuperJobApi
from all_api.headhunter import HeadHunterApi
from work_with_vacancy.changing import ChangeVacancyOrig
from work_with_vacancy.comparison_of_vacancies import Comparison


def conversation_with_user():

    platform = int(input("Привет! На какой платформе будем искать вакансии?)\n1 - HeadHunter, 2 - SuperJob: "))
    if platform == 1:
        print("HeadHunter так HeadHunter, погнали!")
    elif platform == 2:
        print("SuperJob так SuperJob, погнали!")
    profession = input("Вакансии по каким профессиям вы бы хотели рассмотреть?")

    manager = ChangeVacancyOrig('work_with_vacancy/vacancies.json')

    f = open('work_with_vacancy/vacancies.json', 'w')
    f.close()

    if platform == 1:
        final_list = HeadHunterApi(profession).get_vacancies()
        for job in final_list:
            manager.add_vacancy(job)
    elif platform == 2:
        final_list = SuperJobApi(profession).get_vacancies()
        for job in final_list:
            manager.add_vacancy(job)

    user_salary = int(input("Сколько хочешь зарабатывать?"))

    pprint(manager.get_vacancy_by_salary(user_salary))

    user_choosing = int(input("Выберите следующее действие:\n"
                              "1: Хочу добавить вакансию в список\n"
                              "2: Хочу сравнить по зарплате две вакансии "))

    if user_choosing == 1:
        new_vacancy = input("Введите данные новой вакансии: ")
        manager.add_vacancy(json.loads(new_vacancy))
        print("Вакансия добавлена")

    elif user_choosing == 2:
        print('Сравнение двух вакансий')
        job_id_1 = int(input("Введите id первой: "))
        job_id_2 = int(input("Введите id второй: "))

        vacancy_1 = manager.get_vacancy_by_id(f"{job_id_1}")
        vacancy_2 = manager.get_vacancy_by_id(f"{job_id_2}")


        self_vac = Comparison(vacancy_1.get('job'), vacancy_1.get("link"), vacancy_1.get("salary").get('to'), vacancy_1.get("salary").get('from'),
                              vacancy_1.get('description'))
        other_vac = Comparison(vacancy_2.get('job'), vacancy_2.get("link"), vacancy_2.get("salary").get('to'), vacancy_2.get("salary").get('from'),
                               vacancy_2.get('description'))

        if self_vac > other_vac:
            print("По вакансии 1 зарплата больше")
        elif self_vac == other_vac:
            print("По обоим вакансиям зарплата одинаковая")
        elif self_vac < other_vac:
            print("По вакансии 2 зарплата больше")


if __name__ == "__main__":
    conversation_with_user()
