from flask import Flask, request, render_template, jsonify
import os
import time

app = Flask(__name__)

@app.route('/')
def ld_pass_form():
    return render_template('ld-form.html')

@app.route('/', methods=['POST'])
def ld_pass_post():
    text = request.form['password']
    processed_text = text.strip()
    try:
        if not processed_text:
            return jsonify({"message": "Password is empty"}), 401
        else:
            print(f"pass: {processed_text}", flush=True)
            return jsonify({"message": "Password is Ok"}), 200
    finally:
        time.sleep(2)
        os._exit(0)

if __name__ == '__main__':
    app.run(port=5000)

# superver=$(python3 test_flask.py | grep -oP '(?<=pass: ).*')