from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
todos = []
current_id = 1

# QUESTION 1: POST /todos 
@app.route('/todos', methods=['POST'])
def create_todo():
    """Add a new task"""
    global current_id
    
    data = request.get_json()
    
    # Validate input
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    new_todo = {
        "id": current_id,
        "title": data['title'],
        "completed": False
    }
    todos.append(new_todo)
    current_id += 1
    
    return jsonify(new_todo), 201

# QUESTION 2: GET /todos 
@app.route('/todos', methods=['GET'])
def get_all_todos():
    """Retrieve all tasks"""
    return jsonify(todos), 200

#  QUESTION 3: GET /todos/<id> 
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo_by_id(todo_id):
    """Retrieve a specific task by ID"""
    for todo in todos:
        if todo['id'] == todo_id:
            return jsonify(todo), 200
    
    return jsonify({"error": f"Task with ID {todo_id} not found"}), 404

# QUESTION 4: PUT /todos/<id> 
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update an existing task"""
    data = request.get_json()
    
    for todo in todos:
        if todo['id'] == todo_id:
            if 'title' in data:
                todo['title'] = data['title']
            if 'completed' in data:
                todo['completed'] = data['completed']
            return jsonify(todo), 200
    
    return jsonify({"error": f"Task with ID {todo_id} not found"}), 404

# QUESTION 5: DELETE /todos/<id> 
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a task by ID"""
    for index, todo in enumerate(todos):
        if todo['id'] == todo_id:
            todos.pop(index)
            return jsonify({"message": f"Task with ID {todo_id} deleted successfully"}), 200
    
    return jsonify({"error": f"Task with ID {todo_id} not found"}), 404

# Root endpoint
@app.route('/')
def root():
    return jsonify({
        "message": "Welcome to To-Do List API (Flask)",
        "endpoints": {
            "POST /todos": "Create a task",
            "GET /todos": "Get all tasks",
            "GET /todos/<id>": "Get task by ID",
            "PUT /todos/<id>": "Update a task",
            "DELETE /todos/<id>": "Delete a task"
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)