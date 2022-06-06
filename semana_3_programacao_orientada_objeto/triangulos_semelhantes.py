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

    def semelhantes (self,triangulo):
        tipo1=Triangulo.tipo_lado(self)
        tipo2=Triangulo.tipo_lado(triangulo)

        if (tipo1 == tipo2):
            lados_t1=[self.a,self.b,self.c]
            lados_t2=[triangulo.a,triangulo.b, triangulo.c]
            ordem_t1=sorted(lados_t1)
            ordem_t2=sorted(lados_t2)
            prop1=(ordem_t1[-1]/ordem_t2[-1])
            prop2=(ordem_t1[-2]/ordem_t2[-2])
            prop3=(ordem_t1[-3]/ordem_t2[-3])

            if ((prop1==prop2) and (prop1==prop3) and (prop2==prop3)):
                return True
            else:
                return False

        else:
            return False
