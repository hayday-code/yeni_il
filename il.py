import turtle
import random
import math

# Ekranı hazırlamaq
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Yeni İl Yolkasının Turtle ilə")

# Turtle obyektlər
tree = turtle.Turtle()
tree.hideturtle()
tree.speed(0)

decor = turtle.Turtle()
decor.hideturtle()
decor.speed(0)

# Funksiya: üçbucaq çəkmək
def draw_triangle(x, y, width, height, color):
    tree.penup()
    tree.goto(x - width/2, y)
    tree.pendown()
    tree.fillcolor(color)
    tree.begin_fill()
    tree.goto(x + width/2, y)
    tree.goto(x, y + height)
    tree.goto(x - width/2, y)
    tree.end_fill()

# Funksiya: beşguşəli ulduz
def draw_star(x, y, size, color):
    decor.penup()
    decor.goto(x, y)
    decor.setheading(90)
    decor.forward(size)
    decor.right(144)
    decor.pendown()
    decor.fillcolor(color)
    decor.begin_fill()
    for _ in range(5):
        decor.forward(2*size*math.sin(math.radians(36)))
        decor.right(144)
    decor.end_fill()

# Funksiya: dairə (topa və işıq)
def draw_circle(x, y, radius, color):
    decor.penup()
    decor.goto(x, y - radius)
    decor.pendown()
    decor.fillcolor(color)
    decor.begin_fill()
    decor.circle(radius)
    decor.end_fill()

# Çəmən (bir az aşağı çəkildi)
tree.penup()
tree.goto(-300, -180)  # əvvəl -150 idi
tree.pendown()
tree.fillcolor("darkgreen")
tree.begin_fill()
tree.goto(300, -180)
tree.goto(300, -130)
tree.goto(-300, -130)
tree.goto(-300, -180)
tree.end_fill()

# Yolkanın təbəqələri (piramida)
base_width = 200
height = 60
y_start = -100

for i in range(4):
    draw_triangle(0, y_start, base_width, height, "green")
    # İşıqlar hər təbəqənin üzərində nizamlı yerləşdirək
    num_lights = max(3, base_width // 40)
    step = base_width / (num_lights + 1)
    x_left = -base_width/2 + step
    for _ in range(num_lights):
        draw_circle(x_left, y_start + height/2, 5, random.choice(["red", "yellow", "blue", "orange", "purple", "pink"]))
        x_left += step
    base_width -= 40
    y_start += height - 10

# Yolkanın ayağı (kök)
tree.penup()
tree.goto(-15, -150)
tree.pendown()
tree.fillcolor("brown")
tree.begin_fill()
for _ in range(2):
    tree.forward(30)
    tree.left(90)
    tree.forward(50)
    tree.left(90)
tree.end_fill()

# Yolkanın başına ulduz
draw_star(0, y_start + 10, 15, "yellow")

# Qar dekorasiyası (sabit)
for _ in range(30):
    x = random.randint(-300, 300)
    y = random.randint(-50, 250)
    draw_circle(x, y, 5, "white")

# Təbrik mesajı
message = turtle.Turtle()
message.hideturtle()
message.penup()
message.goto(0, 180)
message.color("darkblue")
message.write("🎉 HAYDAY LÜKS Yönetim 🎉\nYeni İl Bayramınızı Təbrik Edir!", align="center", font=("Comic Sans MS", 18, "bold"))

turtle.done()