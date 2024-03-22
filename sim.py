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
    def __init__(self, name:str, mass:int, radius:int, position:tuple, velocity:tuple=(0,0)) -> None:
        self.name = name
        self.mass = mass
        self.position = position
        self.radius = radius
        self.velocity = velocity

def draw_planets(planets:slice):
    turtle_planet.clear()
    for planet in planets:
        turtle_planet.penup()
        turtle_planet.setposition(planet.position)
        turtle_planet.write(planet.name)
        turtle_planet.dot(5)
        turtle_planet.setposition(planet.position[0], planet.position[1]-(1*planet.radius))
        turtle_planet.pendown()
        turtle_planet.circle(planet.radius)

def draw_ship():
    turtle_spaceship.clear()
    turtle_spaceship.setposition(spaceship_pos)
    turtle_spaceship.dot(10)

def move_planets(planets):
    for planet in planets:
        planet.position, planet.velocity = move_spaceship(planet.position, planet.velocity, planets)

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

def draw_orbit(spaceship_pos, spaceship_vel, planets, steps):
    turtle_orbit.clear()
    turtle_orbit.setposition(spaceship_pos)
    turtle_orbit.pendown()
    temp_vel = spaceship_vel
    temp_pos = spaceship_pos
    i=0
    while i < steps:
        i+=1
        temp_pos, temp_vel = move_spaceship(temp_pos, temp_vel, planets)
        turtle_orbit.goto(temp_pos)
    turtle_orbit.penup()

spaceship_pos = (200,0)
spaceship_vel = (0,-7)

turtle_planet = turtle.Turtle(visible=False)
turtle_planet.speed(0)
turtle_orbit = turtle.Turtle(visible=False)
turtle_orbit.speed(0)
turtle.tracer(10)
turtle_spaceship = turtle.Turtle(visible=False)
turtle_spaceship.speed(0)
turtle_orbit.tracer = False
planets.append(planet("one", 0.001, 50, (0,100), (3, 0)))
planets.append(planet("two", 0.001, 50, (0,0) , (-3, 0)) )
draw_planets(planets)

while True:
    move_planets(planets)
    spaceship_pos, spaceship_vel = move_spaceship(spaceship_pos, spaceship_vel, planets)
    draw_orbit(spaceship_pos, spaceship_vel, planets, 2000)
    draw_ship()
    draw_planets(planets)