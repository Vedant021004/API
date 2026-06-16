from flask import Flask

app = Flask(__name__)



data = {
    "name" : "vedant kapil",
    "wife_name" : "riddhi vedant kapil",
    "age" : 21,
    "mwaah" : "marry soon"
}



@app.route("/")
def todos():
    
    response = data
    return response



if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)


