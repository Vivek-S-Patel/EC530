from flask import Flask, request

app = Flask(__name__)

# entities
users = []
houses = []
rooms = []
devices = []

# Users
@app.route('/users', methods=['POST'])
def create_user():
    username = request.json.get('username')
    return ""

@app.route('/users', methods=['GET'])
def get_users():
    return ""

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    username = request.json.get('username')
    return ""

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return ""

# Houses
@app.route('/houses', methods=['POST'])
def create_house():
    username = request.json.get('username')
    return ""

@app.route('/houses', methods=['GET'])
def get_houses():
    return ""

@app.route('/houses/<int:house_id>', methods=['PUT'])
def update_house(house_id):
    username = request.json.get('username')
    return ""

@app.route('/houses/<int:house_id>', methods=['DELETE'])
def delete_house(house_id):
    return ""

# Rooms
@app.route('/rooms', methods=['POST'])
def create_room():
    username = request.json.get('username')
    return ""

@app.route('/rooms', methods=['GET'])
def get_rooms():
    return ""

@app.route('/rooms/<int:room_id>', methods=['PUT'])
def update_room(room_id):
    username = request.json.get('username')
    return ""

@app.route('/rooms/<int:room_id>', methods=['DELETE'])
def delete_room(room_id):
    return ""

# Devices
@app.route('/devices', methods=['POST'])
def create_device():
    username = request.json.get('username')
    device_type = request.json.get('device_type')
    house_id = request.json.get('house_id')
    return ""

@app.route('/devices', methods=['GET'])
def get_devices():
    return ""

@app.route('/devices/<int:device_id>', methods=['PUT'])
def update_device(device_id):
    username = request.json.get('username')
    device_type = request.json.get('device_type')
    house_id = request.json.get('house_id')
    return ""

@app.route('/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    return ""

if __name__ == '__main__':
    app.run(debug=True)
