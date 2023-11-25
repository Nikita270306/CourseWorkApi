
from abc import ABC, abstractmethod


class SearchApi(ABC):
    @abstractmethod
    def get_vacancies(self) -> list:
        pass
