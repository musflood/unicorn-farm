"""Unicorn position tracker."""
import json


class Unicorn(object):
    """A unicorn."""

    def __init__(self, name, color, fave_food, position='barn'):
        """Create a new unicorn."""
        self.name = name
        self.color = color
        self.fave_food = fave_food
        self.position = position

    def __repr__(self):
        """Print a unicorn nicely."""
        return f'{self.name:^11} {self.position:^11} {self.color:^11} {self.fave_food:^11}'

    def _move(self, position):
        """Move the unicorn to the barn, trails, field."""
        if position.lower() not in ('barn', 'trails', 'field'):
            raise ValueError('Invalid position to move.')
        self.position = position

    @classmethod
    def list(cls):
        """List the unicorns and their current positions."""
        print('{:^11} {:^11} {:^11} {:^11}'.format('name', 'location', 'color', 'fave food'))
        for unicorn in cls.unicorns:
            print(unicorn)

    @classmethod
    def move(cls, name):
        """Move the given unicorn."""
        unicorn_to_move = [unicorn for unicorn in cls.unicorns if unicorn.name == name.title()]
        if not unicorn_to_move:
            print('invalid unicorn')
            return
        position = input('where to move? (barn, trails, field) ')
        for unicorn in unicorn_to_move:
            try:
                unicorn._move(position)
                print(f'{unicorn.name} moved to {unicorn.position}')
            except ValueError:
                print(f'cannot move unicorn to {position}')

    @classmethod
    def add(cls):
        """Add a unique unicorn."""
        name = input('name of unicorn? ').title()
        while name in [unicorn.name for unicorn in cls.unicorns]:
            print('name taken, choose another.')
            name = input('name of unicorn? ').title()

        color = input('color of unicorn? ')
        fave_food = input('favorite food of unicorn? ')

        cls.unicorns.append(Unicorn(name, color, fave_food))

        print(f'{name} has been put in the barn')

    @classmethod
    def load(cls):
        """Pull saved unicorns from file."""
        unicorns = []
        try:
            with open('unicorns.txt') as f:
                unicorns = json.load(f)
        except IOError:
            print('no saved unicorns')
        cls.unicorns = [Unicorn(**unicorn_data) for unicorn_data in unicorns]

    @classmethod
    def save(cls):
        """Write all unicorns to a file."""
        with open('unicorns.txt', 'w') as f:
            json.dump(cls.unicorns, f, default=lambda u: u.__dict__)


def main():
    """Main content of script."""
    print('Welcome to unicorn tracker!')
    user_input = ''
    Unicorn.load()
    while user_input.lower() != 'q':
        print()
        print('1. add unicorn')
        print('2. current locations')
        print('3. move unicorn')
        print('q: quit')
        user_input = input('Choose an option: ')

        if user_input == '1':
            Unicorn.add()

        if user_input == '2':
            Unicorn.list()
            continue

        if user_input == '3':
            Unicorn.list()
            name = input('Which unicorn to move? ')
            Unicorn.move(name)

        Unicorn.save()


if __name__ == '__main__':
    main()
