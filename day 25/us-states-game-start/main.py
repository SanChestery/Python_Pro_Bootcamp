import turtle
import pandas


sc = turtle.Screen()
sc.title("U.S. States Game")
image = "blank_states_img.gif"
sc.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")


def check_answer(ans, data):
    if ans in data.state.values:
        print("True")
        return True
    else:
        print("False")
        return False


def write_state(ans, data):
    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()
    coords = data[data.state == ans]
    writer.goto(int(coords.x), int(coords.y))
    writer.write(arg=f"{ans}", align='center', font=('Arial', 14, 'normal'))


corr_answers = []

while len(corr_answers) < 50:
    answer_state = sc.textinput(title=f"{len(corr_answers)}/50 States Correct", prompt="What's another state?").title()
    print("\nNew Iteration")

    if answer_state == "Exit":
        break
    elif answer_state not in corr_answers and check_answer(answer_state, data):
        write_state(answer_state, data)
        corr_answers.append(answer_state)

    if len(corr_answers) >= 50:
        not_finished = False

all_states = data['state'].to_list()
not_guessed_states = [state for state in all_states if state not in corr_answers]
new_data = pandas.DataFrame(not_guessed_states)
new_data.to_csv("not_guessed_states.csv")

turtle.mainloop()
