from flask import Flask, jsonify , request
import json
app = Flask(__name__)



todos = [ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)

    # and then you can return it to the front end in the response body like this
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    decoded_object = json.loads(request.data)
    todos.append(decoded_object)
    json_text = jsonify(todos)
    return json_text    

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position)
    json_text = jsonify(todos)
    return json_text 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)