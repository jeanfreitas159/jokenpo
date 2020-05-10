#'''criar uma classe que modela um retangulo
#-atributos : lado A, lado B 
#-métodos: -mudar o valor dos lados , 
#-retornar o valor dos lados, 
#-calcular e mostrar  Area,
#-calcular e mostrar o  perimetro , '''


class Retangulo:
   def __init__ (self,ladoA, ladoB):
         self.ladoA = ladoA
         self.ladoB = ladoB
   def mudarLados(self,ladoA, ladoB):
     if ladoA > 0:
         self.ladoA = ladoA
     if ladoB > 0:
         self.ladoB = ladoB
   def retornarLados (self):
      return (self.ladoA,self.ladoB)
   def calcularArea (self):
      return self.ladoA*self.ladoB
   def calcularPerimetro (self):
      return (self.ladoA*2)+(self.ladoB*2)
      lado1 = int(input("informe o lado A:"))
      lado2 = int(input("informe o lado B:"))
      R1 = Retangulo(lado1,lado2)
    print "A qtde de azuleijos e: " + str(area/2)