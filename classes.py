class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along...')

    def get_make_model(self):
        print(f"I have a {self.make} {self.model}.")


my_car = Vehicle('Tesla', 'Model 3')
my_car.moves()
my_car.get_make_model()


your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        self.faa_id = faa_id
        super().__init__(make, model)

    def moves(self):
        print('Flies along...')


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along...")


class GolfCart(Vehicle):
    pass


cessna = Airplane('Cessna', 'Skyhawk', 'N-125487')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

cessna.moves()
cessna.get_make_model()
mack.moves()
mack.get_make_model()
golfwagon.moves()
golfwagon.get_make_model()

print('\n\n')
# Polymorphism is the ability to behave differently in response to the same input messages
for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()
