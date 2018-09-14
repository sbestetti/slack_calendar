class Room():
    def __init__(self, name, id, capacity, location, office ):
        self.name = name
        self.id = id
        self.capacity = capacity
        self.location = location
        self.office = office

    def __repr__(self):
        return '{} for {} people, {}, {}'.format(self.name, str(self.capacity), self.location, self.office)

