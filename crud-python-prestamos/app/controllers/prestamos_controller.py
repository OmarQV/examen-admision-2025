from flask import Blueprint, request, jsonify
from models.prestamos_model import Prestamo
from views.prestamos_view import render_prestamo_list, render_prestamo_detail
from datetime import datetime

prestamo_bp = Blueprint("prestamo", __name__)

@prestamo_bp.route("/prestamos", methods=["GET"])
def get_prestamos():
   prestamos = Prestamo.get_all()
   return jsonify(render_prestamo_list(prestamos))

@prestamo_bp.route("/prestamos/<int:id>", methods=["GET"])
def get_prestamo(id):
   prestamo = Prestamo.get_by_id(id)
   if prestamo:
      return jsonify(render_prestamo_detail(prestamo))
   return jsonify({"error": "Préstamo no encontrado"}), 404

@prestamo_bp.route("/prestamos", methods=["POST"])
def create_prestamo():
   data = request.json
   usuario_id = data.get("usuario_id")
   libro_id = data.get("libro_id")
   fecha_prestamo = datetime.strptime(data.get("fecha_prestamo"), "%Y-%m-%d").date()
   
   if usuario_id is None or libro_id is None or fecha_prestamo is None:
      return jsonify({"error": "Faltan datos requeridos"}), 400

   prestamo = Prestamo(usuario_id=usuario_id, libro_id=libro_id, fecha_prestamo=fecha_prestamo)
   prestamo.save()

   return jsonify(render_prestamo_detail(prestamo)), 201

@prestamo_bp.route("/prestamos/<int:id>", methods=["PUT"])
def update_prestamo(id):
   prestamo = Prestamo.get_by_id(id)
   if not prestamo:
      return jsonify({"error": "Préstamo no encontrado"}), 404

   data = request.json
   usuario_id = data.get("usuario_id")
   libro_id = data.get("libro_id")
   fecha_prestamo = data.get("fecha_prestamo")
   fecha_devolucion = data.get("fecha_devolucion")
   estado = data.get("estado")

   prestamo.update(usuario_id=usuario_id, libro_id=libro_id, fecha_prestamo=fecha_prestamo, fecha_devolucion=fecha_devolucion, estado=estado)

   return jsonify(render_prestamo_detail(prestamo))

@prestamo_bp.route("/prestamos/<int:id>", methods=["DELETE"])
def delete_prestamo(id):
   prestamo = Prestamo.get_by_id(id)
   if not prestamo:
      return jsonify({"error": "Préstamo no encontrado"}), 404

   prestamo.delete()
   return "", 204
