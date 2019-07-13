from daylight import app


@app.routes('/users/photos', methods=['DELETE'])
def delete_photo():
    return 'Not implemented'
