class Person(object):

    def __init__(self, first, last, number, city):
        self.first = first
        self.last = last
        self.number = number
        self.city = city
        self.email = first + '.' + last + '@email.com'


    def intro(self):
        return(self.first, self.last, self.number, self.city, self.email)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


Dan = Person("Dan", "Pena", "714-111-1111", "Cypress")
Jay = Person("Jay", "Pak", "714-222-2222", "Cypress")


action = input("> ")

if action == "Dan":
    print(Dan.intro())

if action == "Jay":
    print(Jay.intro())
