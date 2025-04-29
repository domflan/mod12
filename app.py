from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# ⬇️ Replace this with your deployed API server URL later
api_url = "https://YOUR-API-SERVER-NAME.azurewebsites.net/predict"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    form_data = {
        "age": int(request.form["age"]),
        "gender": int(request.form["gender"]),
        "country": int(request.form["country"]),
        "highest_deg": int(request.form["highest_deg"]),
        "coding_exp": int(request.form["coding_exp"]),
        "title": int(request.form["title"]),
        "company_size": int(request.form["company_size"])
    }

    response = requests.post(api_url, json=form_data)
    prediction = response.json().get("prediction")

    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
