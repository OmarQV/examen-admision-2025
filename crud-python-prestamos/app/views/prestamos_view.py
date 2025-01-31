def render_prestamo_list(prestamos):
   return [
      {
         "id": prestamo.id,
         "usuario_id": prestamo.usuario_id,
         "libro_id": prestamo.libro_id,
         "fecha_prestamo": prestamo.fecha_prestamo.isoformat(),
         "fecha_devolucion": prestamo.fecha_devolucion.isoformat() if prestamo.fecha_devolucion else None,
         "estado": prestamo.estado,
      }
      for prestamo in prestamos
   ]

def render_prestamo_detail(prestamo):
   return {
      "id": prestamo.id,
      "usuario_id": prestamo.usuario_id,
      "libro_id": prestamo.libro_id,
      "fecha_prestamo": prestamo.fecha_prestamo.isoformat(),
      "fecha_devolucion": prestamo.fecha_devolucion.isoformat() if prestamo.fecha_devolucion else None,
      "estado": prestamo.estado,
   }
