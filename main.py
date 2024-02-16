import turtle
import pandas

screen = turtle.Screen()
screen.title("Animals Quiz")
screen.setup(width=650, height=680)
image = "animals_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_cool(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cool)
# turtle.mainloop()

data = pandas.read_csv("14_animals.csv")
all_animals = data.animal.to_list()
guessed_animals = []

while len(guessed_animals) < 14:
    answer_animal = screen.textinput(title=f"{len(guessed_animals)}/14 Animals Correct",
                                    prompt="How is this called?").title()
    print(answer_animal)
    if answer_animal == "Exit":
        missing_animals = []
        for animal in all_animals:
            if animal not in guessed_animals:
                missing_animals.append(animal)
        new_data = pandas.DataFrame(missing_animals)
        new_data.to_csv("animals_to_learn.csv")
        break

    if answer_animal in all_animals:
        guessed_animals.append(answer_animal)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        animal_data = data[data.animal == answer_animal]
        t.goto(int(animal_data.x), int(animal_data.y))
        t.write(animal_data.animal.item())


screen.exitonclick()


