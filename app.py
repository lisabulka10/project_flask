from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, world!'


@app.route('/info')
def info():
    return "This is an informational page."


@app.route('/calc/<num1>/<num2>')
def calc(num1, num2):
    try:
        sum_num = int(num1) + int(num2)
        return f'The sum of {num1} and {num2} is {sum_num}'
    except ValueError:
        return f'The {num1} and {num2} is not a number.'


@app.route('/reverse/<text>')
def reverse(text):
    try:
        return text[::-1]
    except ValueError:
        return 'This is a mistake in your text.'


@app.route('/user/<name>/<age>')
def hello_user(name, age):
    try:
        name = str(name)
        age = int(age)
        if age < 0 or len(name) < 1 or name.isnumeric():
            raise ValueError
        return f'Hello, {name}! You are {age} years old.'
    except ValueError:
        return 'Valid name or age'


# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)