from flask import abort, jsonify, Flask, request, Response

app = Flask(__name__)

tasks = {
    "data": {
        "loginName": "admin",
        "roles": 1,
        "permissions": 1,
        "active": 1
    },
    "stateCode": {
        "code": 0,
        "desc": "成功"
    },
    "statusText": "成功",
    "timestamp": "1500531770453",
    "success": 1
}


@app.route('/v1/testMock', methods=['GET', 'POST'])
def app_call_back():
    if request.method == 'GET':
        return jsonify(tasks)
    else:
        test_data = request.form['params']
        return jsonify(tasks[test_data])

if __name__ == "__main__":
    app.run(
        host = "127.0.0.1",
        port = 8989,
        debug = True
        )