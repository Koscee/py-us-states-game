import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

total_score = 50
score = 0
correct_guesses = []
location_data = pandas.read_csv("50_states.csv")

while score < total_score:
    input_title = 'Guess the State' if score == 0 else f'{score}/{total_score} States Correct'
    answer_state = screen.textinput(title=input_title, prompt="Whats another state's name?")
    answer_state = answer_state.title() if answer_state else ''
    found_data = location_data[location_data.state == answer_state]

    is_marked = answer_state in correct_guesses

    if not is_marked and not found_data.empty:
        state = found_data.state.item()
        position = (int(found_data.x), int(found_data.y))
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        marker.goto(position)
        marker.write(state, align="center", font=("Arial", 9, "bold"))
        correct_guesses.append(state)
        score += 1

screen.exitonclick()
