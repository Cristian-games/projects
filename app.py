import random
from flask import Flask, render_template, request

app = Flask(__name__)


def play_round():
    # Determine length of the number
    first = random.randint(0, 9)
    second = random.randint(0, 99)
    third = random.randint(0, 999)
    fourth = random.randint(0, 9999)
    fifth = random.randint(0, 99999)

    length = 6
    if first == 0:
        length = 5
    elif first == 0 and second == 0:
        length = 4
    elif first == 0 and second == 0 and third == 0:
        length = 3
    elif first == 0 and second == 0 and third == 0 and fourth == 0:
        length = 2
    elif first == 0 and second == 0 and third == 0 and fourth == 0 and fifth == 0:
        length = 1

    # Generate a number with the determined length
    if length == 6:
        num = random.randint(100000, 999999)
    elif length == 5:
        num = random.randint(10000, 99999)
    elif length == 4:
        num = random.randint(1000, 9999)
    elif length == 3:
        num = random.randint(100, 999)
    elif length == 2:
        num = random.randint(10, 99)
    else:
        num = random.randint(1, 9)

    total = 0
    events = []

    if num % 2 == 0:
        events.append(("Num is even", 100))
        total += 100
    if num % 2 != 0:
        events.append(("Num is odd", 100))
        total += 100
    if num % 3 == 0:
        events.append(("Num is divisible by 3", 150))
        total += 150
    if num % 5 == 0:
        events.append(("Num is divisible by 5", 150))
        total += 150
    if num % 7 == 0:
        events.append(("Num is divisible by 7", 200))
        total += 200
    if num % 11 == 0:
        events.append(("Num is divisible by 11", 250))
        total += 250
    if num % 13 == 0:
        events.append(("Num is divisible by 13", 300))
        total += 300

    for digit in "1234567890":
        if digit in str(num):
            events.append((f"Num contains {digit}", 100))
            total += 100

    return num, events, total


@app.route("/", methods=["GET", "POST"])
def index():
    num = None
    events = []
    total = None
    if request.method == "POST":
        num, events, total = play_round()
    return render_template("index.html", num=num, events=events, total=total)


if __name__ == "__main__":
    app.run(debug=True)