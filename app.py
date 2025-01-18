from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)
@app.route('/')
def home():
    return "This url is not valid :/"

@app.route('/search', methods=['GET'])
def search():
    if not request.args['q']:
        redirect(url_for('home'))
        return jsonify({"error":"please input a query!", "data": ""})
    
    else:
        redirect(url_for('home'))
        return jsonify({"error":"", "data": request.args['q']})
         

if __name__ == "__main__":
    app.run()