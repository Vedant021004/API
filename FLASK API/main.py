from flask import Flask

app = Flask(__name__)

data = {
    "name" : "vedant kapil",
    "wife_name" : "riddhi vedant kapil",
    "age" : 21,
    "mwaah" : "marry soon"
}

@app.route("/todos")
def todos():
    response = data
    return response

if __name__ == "__main__":
    app.run(debug=True)