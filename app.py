from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

file_path = 'user_data.xlsx'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index1.html', results=None)


@app.route('/save-user-data', methods=['POST'])
def save_user_data():
    data = request.json
    email = data.get('email')
    role = data.get('role')

    new_data = pd.DataFrame({
        'Email': [email],
        'Role': [role]
    })
    if os.path.exists(file_path):
        existing_data = pd.read_excel(file_path)
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    else:
        updated_data = new_data

    updated_data.to_excel(file_path, index=False)

    return jsonify({'message': 'User data saved successfully!'})


if __name__ == '__main__':
    app.run(debug=True)
