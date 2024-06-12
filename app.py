from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from werkzeug.exceptions import BadRequest, Conflict, UnsupportedMediaType, Unauthorized, RequestEntityTooLarge, NotFound
from mongoengine.errors import DoesNotExist
from flask_mongoengine import MongoEngine

load_dotenv()

if not os.environ.get("MONGODB_URI") or not os.environ.get("MONGODB_DB"):
  raise Exception("Required environment variables are not found.")  

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
  "db": os.environ.get("MONGODB_DB"),
  "host": os.environ.get("MONGODB_URI")
} 
db = MongoEngine(app)

@app.route("/", methods=["GET"])
def landing_page():
    return("""
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
  <body>
    <div style='min-height: 100vh; display: flex; flex-direction: column; justify-content: center; align-items: center; font-size: 24px; font-family: "Poppins"; text-align: center'>
      <p style='font-weight: 600; margin: 0'>
        Land Price API
      </p>
    </div>
  </body>
  """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

@app.errorhandler(Exception)
def error_handler(e):
  print(e)
  if isinstance(e, NotFound):
    return jsonify({"message": str(e)}), 404
  elif isinstance(e, BadRequest):
    return jsonify({"message": str(e)}), 400
  elif isinstance(e, Conflict):
    return jsonify({"message": str(e)}), 409
  elif isinstance(e, UnsupportedMediaType):
    return jsonify({"message": str(e)}), 415
  elif isinstance(e, Unauthorized):
    return jsonify({"message": str(e)}), 401
  elif isinstance(e, DoesNotExist):
    return jsonify({"message": "Object does not exist: " + str(e)}), 404
  elif isinstance(e, RequestEntityTooLarge):
    return jsonify({"message": str(e)}), 413
  else:
    return jsonify({"message": "Unexpected error: " + str(e)}), 500