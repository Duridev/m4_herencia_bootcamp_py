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
  
  
class Video(ContenidoDigital):

  def __init__(self,titulo, autor, fecha_publicacion, duracion, calificacion, formato, resolucion):
    super().__init__(titulo, autor, fecha_publicacion, duracion, calificacion)
    self.formato=formato
    self.resolucion=resolucion

  def subir_calidad(self):
    if self.resolucion == "4K":
      print("No es posible subir a una resolución mayor")
    elif self.resolucion == "Full HD"
      self.resolucion = "4K"
      print("Se ha subido la resolución a 4K")
    else:
      self.resolucion = "Full HD"
      print("Se ha subido la resolución a Full HD")

  def agregar_subtitulo(self):
    print("Se han activado los subtitulos")
    
class Podcast(ContenidoDigital):
  def __init__(self, titulo, autor, fecha_publicacion, duracion, calificacion, invitados, tema):
    super().__init__(titulo, autor, fecha_publicacion, duracion, calificacion)
    self.invitados=invitados
    self.tema=tema
  def agregar_invitado(self, nombre):
    self.invitados.append(nombre)

  def generar_transcripcion(self):
    print("Generando transcripción...")
    
    
class LibroDigital(ContenidoDigital):
  def __init__(self, titulo, autor, fecha_publicacion, duracion, calificacion, num_paginas, formato_lectura):
    super().__init__(titulo, autor, fecha_publicacion, duracion, calificacion)
    self.num_paginas=num_paginas
    self.formato_lectura=formato_lectura

  def marcar_pagina(self):
    print("Se ha marcado una página...")

  def calcular_tiempo_lectura(self):
    return self.num_paginas/2

class Tutorial(Video):
  def __init__(self,titulo, autor, fecha_publicacion, duracion, calificacion, formato, resolucion, dificultad, materiales_necesarios)
    super().(titulo, autor, fecha_publicacion, duracion, calificacion, formato, resolucion)
    self.dificultad = dificultad
    self.materiales_necesarios = materiales_necesarios

  def agregar_material(self, material)
    self.materiales_necesarios.append(material)