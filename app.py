from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can be a local static JSON file)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route("/")
def home():
    print("Home route was accessed")
    return jsonify({"Message": "You made it!!!"})

@app.route("/access", methods=["GET", "POST", "PUT", "DELETE"])
def access():
    if request.method == "GET":
        name = request.args.get("name", "Default User")
        return jsonify({"Message": f"GET request received for {name}"})
    elif request.method == "POST":
        data = request.get_json()
        name = data.get("name", "Default User")
        return jsonify({"Message": f"POST request received with name {name}"})
    elif request.method == "PUT":
        data = request.get_json()
        name = data.get("name", "Default User")
        return jsonify({"Message": f"PUT request received with name {name}"})
    elif request.method == "DELETE":
        name = request.args.get("name", "Default User")
        return jsonify({"Message": f"DELETE request for {name}"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
