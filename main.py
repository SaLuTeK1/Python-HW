import turtle
import time

# Побудова фонового статичного рисунка
def draw_background():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("skyblue")

    # Намалюємо небо
    sky = turtle.Turtle()
    sky.penup()
    sky.goto(-400, -100)
    sky.pendown()
    sky.color("lightblue")
    sky.begin_fill()
    sky.goto(400, -100)
    sky.goto(400, 600)
    sky.goto(-400, 600)
    sky.goto(-400, -100)
    sky.end_fill()

    # Намалюємо землю
    ground = turtle.Turtle()
    ground.penup()
    ground.goto(-400, -400)
    ground.pendown()
    ground.color("burlywood4")
    ground.begin_fill()
    ground.goto(400, -400)
    ground.goto(400, -100)
    ground.goto(-400, -100)
    ground.goto(-400, -400)
    ground.end_fill()

    # Намалюємо траву
    grass = turtle.Turtle()
    grass.penup()
    grass.goto(-400, -110)
    grass.pendown()
    grass.color("green")
    grass.begin_fill()
    grass.goto(400, -110)
    grass.goto(400, -90)
    grass.goto(-400, -90)
    grass.goto(-400, -110)
    grass.end_fill()

    # Намалюємо хмари
    cloud(-300,200,20)
    cloud(270,250,20)
    cloud(100,180,20)
    cloud(-90,230,20)

    # Відключимо анімацію для сповільнення
    turtle.tracer(0)

# Функція для малювання хмар
def filled_circle(radius, color):
    turtle.color(color,color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
def cloud(x,y, radius, cloud_color="white"):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    filled_circle(radius,cloud_color)
    turtle.forward(radius)
    filled_circle(radius,cloud_color)
    turtle.right(90)
    filled_circle(radius,cloud_color)
    turtle.right(90)
    filled_circle(radius,cloud_color)
    turtle.right(90)
    filled_circle(radius,cloud_color)
    turtle.right(90)


# Анімація запуску ракети
def launch_rocket(thrust, mass):
    # Створення ракети
    rocket = turtle.Turtle()
    rocket.shape("triangle")
    rocket.color("red")
    rocket.penup()
    rocket.goto(0, -90)

    # Розвернемо трикутник для рівнобедренного вигляду
    rocket.setheading(90)  # Змінюємо кут нахилу трикутника на 90 градусів

    # Включимо анімацію
    turtle.tracer(1)

    # Симуляція руху ракети
    for _ in range(120):
        rocket.sety(rocket.ycor() + 2 * (thrust / mass))  # Збільшуємо y-координату з урахуванням сили тяги та маси
        time.sleep(0.1)

    turtle.done()

# Інтерактивна взаємодія
def interactive_launch():
    thrust = float(input("Введіть силу тяги двигуна: "))
    mass = float(input("Введіть масу ракети: "))
    draw_background()
    launch_rocket(thrust, mass)

# Виклик функції для інтерактивного запуску ракети
interactive_launch()
