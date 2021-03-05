"""
Defines the Person repository
"""

from models import Person

class PersonRepository:
    """ The repository for the user model """

    @staticmethod
    def get(guid):
        """ Query a person by the first and last name """
        return Person.query.filter_by(guid=guid).one()

    def update(self, guid, age):
        """ Update a person's age """
        person = self.get(guid)
        person.age = age

        return user.save()

    @staticmethod
    def create(guid, age):
        """ Create a new user """
        person = Person(guid=guid, age=age)

        return person.save()