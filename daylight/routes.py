from daylight import app


@app.route("/")
def index():
    app.logger.warning("sample message")
    return "Hello from daylight!"
