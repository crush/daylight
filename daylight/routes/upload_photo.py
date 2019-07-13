from daylight import app


@app.routes('/users/photos', methods=['POST'])
def upload_photo():
    return 'Not implemented'
