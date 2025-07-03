from flask import Flask, jsonify, request

app = Flask(__name__)


## initial to do list 
items = [    
    {'id': 1, 'task': 'Buy groceries'},
    {'id': 2, 'task': 'Walk the dog'},
    {'id': 3, 'task': 'Read a book'}    
]
@app.route('/')
def home():
    """Home page."""
    return "Welcome to the To-Do List API!"

@app.route('/items', methods=['GET'])
def get_items():
    """Get the list of items."""
    return jsonify(items)

## get: retrieve specific item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """Get a specific item by ID."""
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404
    
# post : create a new task
@app.route('/items', methods=['POST'])
def create_item():
    """Create a new item."""
    if not request.json or 'task' not in request.json:
        return jsonify({'error': 'Bad Request'}), 400
    
    new_item = {
        'id': items[-1]["id"] + 1 if items else 1,
        'task': request.json['task']
    }
    items.append(new_item)
    return jsonify(new_item), 201

# put: update an existing task
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """Update an existing item."""
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    item['task'] = request.json.get('task', item['task'])
    
    item['task'] = request.json.get('task')
    return jsonify(item)

# delete: delete an existing task
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Delete an existing item."""
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'result': "item deleted", 'success': True}), 204

if __name__ == '__main__':
    app.run(debug=True)

