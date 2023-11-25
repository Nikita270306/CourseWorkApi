
class Comparison:
    def __init__(self, job, link, salary_to, salary_from, description):
        self.job = job
        self.link = link
        self.salary_to = salary_to
        self.salary_from = salary_from
        self.description = description

    def is_valid(self, job, link, salary_to, salary_from, description):
        if not job or not link or not salary_to or not salary_from or not description:
            raise ValueError('Not all atributes here')

    def __str__(self):
        return f'Профессия: {self.job},\nСсылка: {self.link},\nЗарплата до: {self.salary_to},\nЗарплата от: {self.salary_from},\nОписание: {self.description}'

    def __eq__(self, other):
        if not isinstance(other, Comparison):
            return False
        if self.salary_to is None or other.salary_to is None:
            return self.salary_from == other.salary_from
        return self.salary_to == other.salary_to

    def __gt__(self, other):
        if not isinstance(other, Comparison):
            return False
        if self.salary_to is None or other.salary_to is None:
            return self.salary_from > other.salary_from
        return self.salary_to > other.salary_to

    def __lt__(self, other):
        if not isinstance(other, Comparison):
            return False
        if self.salary_to is None or other.salary_to is None:
            return self.salary_from < other.salary_from
        return self.salary_to < other.salary_to


