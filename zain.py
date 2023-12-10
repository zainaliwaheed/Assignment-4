# Importing the necessary modules from Flask
import flask, render_template

# Creating a Flask web application
app = flask.Flask(__name__)

# Define a route for the root URL
@app.route('/')
def index():
    return render_template('zainaliwaheed.html')

# Run the app if this script is executed
if __name__ == '__main__':
    app.run()
