from flask import Blueprint, jsonify
from server.models.guest import Guest

guest_bp = Blueprint('guest', __name__)

@guest_bp.route('/guests', methods=['GET'])
def list_guests():
    guests = Guest.query.all()
    guests_list = [{"id": g.id, "name": g.name, "occupation": g.occupation} for g in guests]
    return jsonify(guests_list), 200
