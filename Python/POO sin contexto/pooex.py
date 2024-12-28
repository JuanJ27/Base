"""
Esto fue para ensayar POO
Autor: [JuanMS]
Fecha: [24/06/2023]
"""


class Personaje:
    """
    Clase para definir un personaje
    """

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        """
        Constructor
        """
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def atributos(self):
        """
        Atributos
        """
        print(self.__nombre, ":", sep="")
        print("-Fuerza", self.__fuerza)
        print("-Inteligencia", self.__inteligencia)
        print("-Defensa", self.__defensa)
        print("-Vida", self.__vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        """
        Subir nivel
        """
        self.__fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__defensa += defensa

    def get_fuerza(self):
        """
        getter de fuerza
        """
        return self.__fuerza

    def set_fuerza(self, fuerza):
        """
        setter de fuerza
        """
        if fuerza < 0:
            print("Error, no valores negativos")
        else:
            self.__fuerza = fuerza

    def get_vida(self):
        """
        getter de fuerza
        """
        return self.__vida

    def get_nombre(self):
        """
        getter de fuerza
        """
        return self.__nombre

    def set_vida(self, vida):
        """
        setter de fuerza
        """
        if vida < 0:
            print("Error, no valores negativos")
        else:
            self.__vida = vida

    def get_defensa(self):
        """
        Getter de defensa
        """
        return self.__defensa

    def get_inteligencia(self):
        """
        Getter de defensa
        """
        return self.__inteligencia

    def set_defensa(self, defensa):
        """
        Setter de defensa
        """
        self.__defensa = defensa

    def esta_vivo(self):
        """
        Verificar viviciòn
        """
        return self.__vida > 0

    def morir(self):
        """
        morir
        """
        self.__vida = 0
        print(f"{self.__nombre} ha muerto")

    def danno(self, enemigo):
        """
        daño a un 3ro
        """
        return self.__fuerza - enemigo.get_defensa()

    def atacar(self, enemigo):
        """
        atacar a 3ro
        """
        danno = self.danno(enemigo)
        enemigo.set_vida(enemigo.get_vida() - danno)
        print(
            f"{self.__nombre} ha realizado {danno} puntos de daño a {enemigo.get_nombre()}")
        if enemigo.esta_vivo():
            print(f"La vida de {enemigo.get_nombre()} es {enemigo.get_vida()}")
        else:
            enemigo.morir()


class Guerrero(Personaje):
    """
    Clase que hereda de personaje
    """

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        """
        Input numerico para cambiar arma "valo"
        """
        opcion = int(
            input("Elige un arma: (1) Acero swordyou, daño 8. (2) Matalagartos, daño 10 "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Numero errado")

    def atributos(self):
        super().atributos()
        print(f"-Espada:{self.espada}")

    def danno(self, enemigo):
        return self.get_fuerza() * self.espada - enemigo.get_defensa()


class Mago(Personaje):
    """
    Subclase de mago
    """

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print(f"-Libro:{self.libro}")

    def danno(self, enemigo):
        return self.get_inteligencia() * self.libro - enemigo.get_defensa()


goku = Personaje("Goku", 20, 15, 30, 100)
guts = Guerrero("Guts", 20, 13, 7, 100, 5)
salome = Mago("Salome", 30, 20, 30, 100, 5)
goku.atacar(guts)
guts.atacar(salome)
salome.atacar(goku)
goku.atributos()
guts.atributos()
salome.atributos()
