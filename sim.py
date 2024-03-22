import turtle, time, math

planets = []

class vector:
    def __init__(self, tuple) -> None:
        self.tuple = tuple
    
    @classmethod
    def from_positions(cls, pos_from:tuple, pos_to:tuple) -> None:
        x_from = pos_from[0]
        y_from = pos_from[1]

        x_to = pos_to[0]
        y_to = pos_to[1]

        x_diff = x_from - x_to
        y_diff = y_from - y_to
        return cls(tuple((x_diff, y_diff)))
    
    def magnitude(self):
        x = self.tuple[0]
        y = self.tuple[1]
        return math.sqrt(y**2+x**2)
    
    def multiply(self, int):
        return (self.tuple[0]*int, self.tuple[1]*int)
    
    def add(self, other):
        self.tuple = (self.tuple[0]+other[0], self.tuple[1]+other[1])
        return None

class planet:
    def __init__(self, name:str, mass:int, radius:int, position:tuple, next:tuple=(0,0)) -> None:
        self.name = name
        self.mass = mass
        self.position = position
        self.radius = radius
        self.next = next

def draw(planets:slice):
    turtle_spaceship.clear()
    turtle_planet.clear()
    for planet in planets:
        turtle_planet.penup()
        turtle_planet.setposition(planet.position)
        turtle_planet.write(planet.name)
        turtle_planet.dot(5)
        turtle_planet.setposition(planet.position[0], planet.position[1]-(1*planet.radius))
        turtle_planet.pendown()
        turtle_planet.circle(planet.radius)
    turtle_spaceship.setposition(spaceship_pos)
    turtle_spaceship.dot(10)

def move_planets(planets):
    for planet in planets:
        planet.position = (planet.position[0] + planet.next[0], planet.position[1] + planet.next[1])

def calculate_overall_force(spaceship_pos, planets):
    overall_force = vector((0,0))
    for planet in planets:
        weight_vector = vector.from_positions(spaceship_pos, planet.position).multiply(planet.mass)
        overall_force.add(weight_vector)
    return overall_force

def move_spaceship(spaceship_pos, spaceship_vel, planets):
    force = calculate_overall_force(spaceship_pos, planets)
    spaceship_vel = (spaceship_vel[0] - force.tuple[0], spaceship_vel[1] - force.tuple[1])
    spaceship_pos = (spaceship_pos[0] + spaceship_vel[0], spaceship_pos[1] + spaceship_vel[1])
    return spaceship_pos, spaceship_vel

spaceship_pos = (130,100)
spaceship_vel = (0,-25)

turtle_planet = turtle.Turtle(visible=False)
turtle_planet.speed(0)
turtle_spaceship = turtle.Turtle(visible=False)
turtle_spaceship.speed(0)
#planets.append(planet("mars", 0.01, 50, (150,50)))
planets.append(planet("earth", 0.01, 100, (0,0), next=(0,0) ) )
draw(planets)
while True:
    time.sleep(0.1)
    move_planets(planets)
    spaceship_pos, spaceship_vel = move_spaceship(spaceship_pos, spaceship_vel, planets)
    draw(planets)