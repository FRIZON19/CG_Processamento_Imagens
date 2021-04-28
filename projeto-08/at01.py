import numpy
class Vertice:
 def __init__(self, x, y, z):
 self.x = x
 self.y = y
 self.z = z

class Poligono:
 def __init__(self):
 self.sequenciaVertices = []

 def setSequenciaVertices(self, sequencia):
 self.sequenciaVertices = sequencia

 def getVertices(self):
 return self.sequenciaVertices

class Malha:
 def __init__(self):
 self.vertices = set()
 self.poligonos = set()

 def getVertices(self):
 return self.vertices

 def getPoligonos(self):
 return self.poligonos

 def addPoligono(self,poligono):
 self.poligono.add(poligono)
 self.vertices.add(poligono.getVertices())
Em seguida, você deve implementar classes abstratas que representem as
câmeras virtuais, os dados de iluminação, cor e textura e a cena 3D.
class CameraVirtual:
 #câmera virtual com centro de coordenadas (0,0,0)
e centro de projeção (0,0,-d)
 def __init__(self, d):
 self.d = -d #distancia do centro de projeção
 self.posicaoDirecao = None

 def setPosicaoDirecao(self, matriz):
 # matriz é uma matriz 4x4 de transformação afim
 self.posicaoDirecao = matriz

class CoresTexturas:
 # mapeamento de um polígono para sua respectiva
CorTextura
 def __init__(self):
 self.map = {}
 def addCorTextura(self,poligono,cortextura):
 self.map[poligono] = cortextura

class FonteLuz:
 # fonte de luz omnidirecional
 def __init__(self, x, y, z):
 self.x = x
 self.y = y
 self.z = z

class Cena:
 def __init__
(self, iluminacao, camera, malhas, corestexturas):
 self.iluminacao = iluminacao
 self.camera = camera
 self.malhas = malhas
 self.corestexturas = corestexturas
Cada estágio do pipeline deve ser implementado.
def transformacoes(camera, vertices):
 novosVertices = set()
 #novosVertices = aplicação da matriz a todos os
vértices de vertices
 return novosVertices

def digitalizacao(vertices,poligonos,iluminacao,corestexturas):
 fragmentos = []
 # fragmentos = execução da digitalização
 return fragmentos

def montagem(fragmentos):
 imagem = numpy.zeros(1)
 # imagem = execução da montagem
 return imagem

def pipeline(cena,matriz):
 #matriz é a mat
 vertices = set()
 poligonos = set()
 for malha in cena.malhas:
 vertices.union(malha.vertices)
 poligonos.union(malha.poligonos)
 vertices = transformacoes(cena.camera, vertices)
 fragmentos = digitalizacao(vertices,poligonos,cena.
iluminacao,cena.corestexturas)
114 - U3 / Computação gráfica tridimensiona
 imagem = montagem(fragmentos)
 return imagem
