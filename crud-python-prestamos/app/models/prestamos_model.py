from database import db

class Prestamo(db.Model):
   __tablename__ = "prestamos"

   id = db.Column(db.Integer, primary_key=True)
   usuario_id = db.Column(db.Integer, nullable=False)
   libro_id = db.Column(db.Integer, nullable=False)
   fecha_prestamo = db.Column(db.Date, nullable=False)
   fecha_devolucion = db.Column(db.Date, nullable=True)
   estado = db.Column(db.String(50), nullable=False)

   def __init__(self, usuario_id, libro_id, fecha_prestamo, fecha_devolucion=None, estado="activo"):
      self.usuario_id = usuario_id
      self.libro_id = libro_id
      self.fecha_prestamo = fecha_prestamo
      self.fecha_devolucion = fecha_devolucion
      self.estado = estado

   def save(self):
      db.session.add(self)
      db.session.commit()

   @staticmethod
   def get_all():
      return Prestamo.query.all()

   @staticmethod
   def get_by_id(id):
      return Prestamo.query.get(id)

   def update(self, usuario_id=None, libro_id=None, fecha_prestamo=None, fecha_devolucion=None, estado=None):
      if usuario_id is not None:
            self.usuario_id = usuario_id
      if libro_id is not None:
            self.libro_id = libro_id
      if fecha_prestamo is not None:
            self.fecha_prestamo = fecha_prestamo
      if fecha_devolucion is not None:
            self.fecha_devolucion = fecha_devolucion
      if estado is not None:
            self.estado = estado
      db.session.commit()

   def delete(self):
      db.session.delete(self)
      db.session.commit()
