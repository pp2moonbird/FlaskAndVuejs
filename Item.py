from flask import Flask, request, jsonify, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/todo/tasks', methods=['GET'])
def get_tasks():
    list = ['1st: get an apple', '2nd: eat an apple']
    tasks = [{'text':x} for x in list]
    return jsonify({'tasks': tasks}), 200, {'Access-Control-Allow-Origin':'*'}


if __name__ == '__main__':
    app.run(debug=True)




