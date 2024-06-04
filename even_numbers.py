#write a simple flask app that returns a list of even numbers from 0 to 100 as a json response
# Create a function that takes a list of numbers and returns only the even values
# create a sample list of numbers 
# create a list of even numbers from the sample list
# return the list of even numbers


from flask import Flask, jsonify

app = Flask(__name__)

def filter_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

@app.route(/)

def index 
    numbers = list(range(101))
    even_numbers = filter_even_numbers(numbers)
    return jsonify(even_numbers)

if __name__ == '__main__':
    app.run(debug=True)
    