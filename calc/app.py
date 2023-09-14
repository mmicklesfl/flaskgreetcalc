from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

OPERATIONS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operation>')
def do_math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    result = OPERATIONS[operation](a, b)
    return str(result)

@app.route('/add')
def do_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)

@app.route('/sub')
def do_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return str(result)

@app.route('/mult')
def do_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)

@app.route('/div')
def do_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
