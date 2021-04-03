import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Laberinto")
wn.setup(700,700)

class Pen(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("white")
		self.penup()
		self.speed(0)

class Player(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("circle")
		self.color("yellow")
		self.penup()
		self.speed(0)


niveles = []

#Definir nivel 1
nivel_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXP                   XX",
"XXX      XXXXXXX   XXXXXX",
"XXX      XXX        XXXXX",
"XXX      XXX    XXXXXX  X",
"XXX      XXX    XXXXXXXXX",
"XXX  XXXXXXX    XXXXXXXXX",
"XXX  XXXXXXX     XXXXXXXX",
"XXX  XXXXXXX    XXXXXXXXX",
"XXX  XXXXXXXXX        XXX",
"XXX  XXXXXXXXX        XXX",
"XXX  XXXXXXXXX    XXXXXXX",
"XXX  XXXXXXXXX    XXXXXXX",
"XXX  XXXXXXXXX    XXXXXXX",
"XXX  XXXXXXXXX    XXXXXXX",
"XXX  XXXXXXXXX    XXXXXXX",
"XXX  XXXXXXXXX     XXXXXX",
"XXX  XXXXXXXXX     XXXXXX",
"XXX  XXXXXXXXX        XXX",
"XXX  XXXXXXXXXXXXXX   XXX",
"XXX  XXXXXXXXXXXXXX   XXX",
"XXX  XXXXXXXXXXXXXX   XXX",
"XXX  XXXXXXXXXXXXXX   XXX",
"XXX                    XX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]
niveles.append(nivel_1)

def iniciar_lab(nivel):
	for fila in range(len(nivel)):
		for column in range(len(nivel[fila])):

			letra_x = nivel[fila][column]
			screen_x = -288 + (column * 24)
			screen_y = 288 - (fila * 24)

			if letra_x == "X":
				pen.goto(screen_x, screen_y)
				pen.stamp()

			if letra_x == "P":
				player.goto(screen_x, screen_y)

pen = Pen()
player = Player()

iniciar_lab(niveles[0])