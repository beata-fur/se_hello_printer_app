from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request

moje_imie = "Beata"
msg = "Hello World!"


@app.route('/')
def index():
    print("In main route")
    arg = request.args.get('output')
    if not arg:
        arg = PLAIN
    print("arg= " + arg)
    return get_formatted(msg, moje_imie, arg)


@app.route('/outputs')
def supported_output():
    print("In outputs route")
    return ", ".join(SUPPORTED)
