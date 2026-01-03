class ContenidoDigital:
  def __init__(self, titulo, autor, fecha_publicacion, duracion, calificacion):
    self.titulo=titulo
    self.autor=autor
    self.fecha_publicacion=fecha_publicacion
    self.duracion=duracion
    self.calificacion=calificacion

  def reproducir(self):
    print("Reproduciendo ",self.titulo)

  def calificar(self,nueva_calificacion):
    self.calificacion=nueva_calificacion

  def es_largo(self):
    if self.duracion>30:
      return True