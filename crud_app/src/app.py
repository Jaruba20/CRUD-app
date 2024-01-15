from flask import Flask, render_template, jsonify
from Interface import show_all

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/show_all', methods=['GET'])
def show_all_route():
    result = show_all()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
