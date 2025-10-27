from flask import Flask, jsonify, render_template, request
import requests, json

app = Flask(__name__)

# === Azure Vision API credentials ===
subscription_key = "74zfy9oNEFghoq9YhWvdkz4P73G2fC9t3tfMqgqndVvwUhu7TX1MJQQJ99BJAC5T7U2XJ3w3AAAFACOGLsqX"
endpoint = "https://asdaasdasdads.cognitiveservices.azure.com/" 
analyze_url = endpoint + "vision/v3.2/analyze"

@app.route('/analyze', methods=['POST'])
def analyze_image():
    image = request.files['image'].read()
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-Type': 'application/octet-stream'
    }
    params = {
        'visualFeatures': 'Categories,Description,Objects,Faces,Tags'
    }
    response = requests.post(analyze_url, headers=headers, params=params, data=image)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
