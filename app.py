from flask import Flask, jsonify, after_this_request

app = Flask(__name__)

@app.route("/search", methods=['GET'])
def search():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    return jsonify([{"hello":"world", "hi":"worl"}, {"h":"wor"}])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)