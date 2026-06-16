from run import app


@app.route("/user/signup")
def signup():
    return "This is signup operation"
