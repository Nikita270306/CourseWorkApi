
from abc import ABC, abstractmethod


class ChangeVacancy(ABC):
    @abstractmethod
    def add_vacancy(self, data):
        pass

    @abstractmethod
    def get_vacancy_by_salary(self, salary):
        pass
