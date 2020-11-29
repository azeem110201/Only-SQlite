
class Employee:
    """A sample Employee class"""

    def __init__(self, first_name, last_name, age):
        self.first = first_name
        self.last = last_name
        self.pay = age

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
