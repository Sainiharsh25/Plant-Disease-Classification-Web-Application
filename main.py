from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
# Define the API URL
API_URL = "https://us-central1-seventh-program-396918.cloudfunctions.net/predict"

@app.route("/", methods=['GET'])
def main():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def uploadFile():
    try:
        file = request.files['file']

        if file:
            # Create a dictionary with the file data
            files = {'file': (file.filename, file)}

            # Make a POST request to the API
            response = requests.post(API_URL, files=files)

            # Check the response from the API
            if response.status_code == 200:
                result = response.json() 
                return render_template('result2.html', result=result)
            else:
                return "API request failed with status code: " + str (response.status_code)
    except Exception as e:
        return "An error occurred: " + str(e)

if __name__ == "__main__":
    app.run(debug=True)
