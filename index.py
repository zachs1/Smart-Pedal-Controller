from flask import Flask, request, jsonify
from board_controller import BoardController
import json

ctrl = BoardController()
app = Flask(__name__)

@app.route('/pedals', methods=['GET', 'POST'])
def pedals():
    content = request.get_json()
    ctrl.set(content)
    ctrl.go()
    print(json.dumps(content, indent = 2))

    return("piss")


if __name__ == '__main__':
    app.run(debug=True)