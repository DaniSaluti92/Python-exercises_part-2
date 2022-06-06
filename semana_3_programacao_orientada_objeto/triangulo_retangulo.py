class Triangulo:
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c

    def perimetro(self):
        return (self.a+self.b+self.c)

    def tipo_lado(self):
        if (self.a==self.b)and(self.a==self.c) and (self.b==self.c):
            return "equilátero"
        elif (self.a!=self.b)and(self.a!=self.c) and (self.b!=self.c):
            return "escaleno"
        else:
            return "isósceles"

    def retangulo(self):
        tipo=Triangulo.tipo_lado(self)

        if (tipo=="escaleno"):
            lados=[self.a,self.b,self.c]
            ordem=sorted(lados)
            hipotenusa=ordem[-1]
            lado1=ordem[-2]
            lado2=ordem[-3]

            if ((hipotenusa**2)==(lado1**2)+(lado2**2)):
                return True
            else:
                return False

        else:
            return False
