#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id='0'):
    return render_template('9-states.html',
                           states=storage.all(State).values(), id=id)


@app.teardown_appcontext
def remove(execute):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
