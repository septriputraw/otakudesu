from flask import Flask, jsonify, request
app = Flask(__name__)

# import module from ./src
from src import Codeku

@app.route('/')
def home():
    return jsonify({
        "status": 200,
        "length": len(Codeku.index()),
        "data": Codeku.index()
    }), 200

@app.route('/detail/')
def detail():
    url = request.args.get('url')
    print(url)
    return jsonify({
        "status": 200,
        "data": Codeku.detail(url)
    }), 200

@app.route('/search/')
def search():
    param = request.args.get('q')
    return jsonify({
        "status": 200,
        "data": Codeku.search(param),
        "length": len(Codeku.search(param))
    }), 200

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

'''if __name__ == "__main__":
    app.run(debug=True)'''