from flask import Blueprint, request, jsonify, g
from werkzeug.exceptions import BadRequest, NotFound, Conflict, Unauthorized
# from mongoengine.errors import DoesNotExist
from models.land import Land

land_bp = Blueprint("land_blueprint", __name__)

@land_bp.route("/<id>", methods=["GET"])
def get_land(id):
  land = Land.objects(id=id).first()
  return jsonify(
    land
  )
  
@land_bp.route("/", methods=["POST"])
def add_land():
  body = request.get_json()
  if not body.get("city") or not body.get("width") or not body.get("length") or not body.get("local_price_per_area") or not body.get("tax_per_area"):
    raise BadRequest("Missing required parameters")
  land = Land(
    city = body["city"],
    length = body["length"],
    width = body["width"],
    local_price_per_area = body["local_price_per_area"],
    tax_per_area = body["tax_per_area"]
  )
  land.save()
  return jsonify({
    "message": "Land added successfully",
    "id": land.id
  })
  
  