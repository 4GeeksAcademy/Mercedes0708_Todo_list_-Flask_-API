from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/myroute', methods=['GET'])
def hello_world():
    json_text = jsonify(some_data)
    return json_text

@app.route('/todos', methods=['GET'])
def handle_todos():
  return todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return todos

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print(position,len (todos))
    if position >=len(todos):
      return{'message':'Fuera de rango'}, 402
    del todos [position]
    return todos


# Supongamos que tienes tus datos en la variable some_data
some_data = { "name": "Bobby", "lastname": "Rixer" }

todos =[{ "label": "My first task", "done": False },
         { "label": "Creando endpoints", "done": True }]

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)