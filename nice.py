from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
      <html>
        <head>
          <title>Hi There!</title>
        </head>
        <body>
          <h1>Hi! This is the home page.</h1>
          <br>
          <p>Click <a href="/hello">here</a> to say hello.</p>
        </body>
      </html>
      """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          <label>What's your name? <input type="text" name="person"></label>
          <br>
          <br>
          Which compliment would you like?
            <select name="compliment">
              <option value="awesome">awesome</option>
              <option value="terrific">terrific</option>
              <option value="fantastic">fantastic</option>
              <option value="neato">neato</option>
              <option value="fantabulous">fantabulous</option>
              <option value="wowza">wowza</option>
              <option value="oh-so-not-meh">oh-so-not-meh</option>
              <option value="brilliant">brilliant</option>
              <option value="ducky">ducky</option>
              <option value="coolio">coolio</option>
              <option value="incredible">incredible</option>
              <option value="wonderful">wonderful</option>
              <option value="smashing">smashing</option>                                                                      
              <option value="lovely">lovely</option>
            </select>  
          <br>
          <br>
          Are you having a good day?
           <input type="radio" name="daystatus" value="good">Good
           <input type="radio" name="daystatus" value="bad">Bad
           <input type="radio" name="daystatus" value="meh">Meh          
           <input type="radio" name="daystatus" value="none-of-your-business">None of your business
          <br>
          <br>
          What would you like to eat today?
          <input type="checkbox" name="foodpreference" value="pasta">Pasta
          <input type="checkbox" name="foodpreference" value="salad">Salad
          <input type="checkbox" name="foodpreference" value="anything">Anything
          <br>
          <br>
          <input type="submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    daystatus = request.args.get("daystatus")

    foodpreference = request.args.get("foodpreference")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
        
        <style>
          body {
          background-color: red;
          }

        </style>
      
      </head>
      <body>
        Hi %s I think you're %s!

        You're having a %s kind of day and you'd like to eat %s.

      </body>
    </html>
    """ % (player, compliment, daystatus, foodpreference)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
