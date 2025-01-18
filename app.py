from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)
@app.route('/')
def home():
    return "This url is not valid ://"

@app.route('/search', methods=['GET'])
def search():
    return jsonify("hello, it's me")
    if not request.args['q']:
        return jsonify({"error":"please input a query!", "data": ""})
    else:
        return jsonify("hello, it's me")
         

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
