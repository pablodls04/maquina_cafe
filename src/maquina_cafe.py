class Vaso:
    def __init__(self):
        self.pequenos = 5
        self.medianos = 5
        self.grandes = 5

    def obtener(self, tamano):
        if tamano == "pequeño" and self.pequenos > 0:
            self.pequenos -= 1
            return 3
        elif tamano == "mediano" and self.medianos > 0:
            self.medianos -= 1
            return 5
        elif tamano == "grande" and self.grandes > 0:
            self.grandes -= 1
            return 7
        else:
            return 0


class Cafetera:
    def __init__(self):
        self.cantidad_cafe = 100  # en Oz

    def usar_cafe(self, cantidad):
        if self.cantidad_cafe >= cantidad:
            self.cantidad_cafe -= cantidad
            return True
        return False


class Azucarero:
    def __init__(self):
        self.cantidad = 50  # cucharadas

    def usar_azucar(self, cucharadas):
        if self.cantidad >= cucharadas:
            self.cantidad -= cucharadas
            return True
        return False


class MaquinaCafe:
    def __init__(self):
        self.vasos = Vaso()
        self.cafetera = Cafetera()
        self.azucarero = Azucarero()
        self.vaso_seleccionado = None
        self.azucar_seleccionada = 0

    def seleccionar_vaso(self, tamano):
        cantidad = self.vasos.obtener(tamano)
        if cantidad == 0:
            return "No hay vasos disponibles" if tamano in ["pequeño", "mediano", "grande"] else "Tamaño de vaso no válido"
        self.vaso_seleccionado = cantidad
        return f"Vaso {tamano} seleccionado: {cantidad} Oz"

    def seleccionar_azucar(self, cucharadas):
        self.azucar_seleccionada = cucharadas
        return f"Seleccionaste {cucharadas} cucharadas de azúcar"

    def preparar_cafe(self):
        if not self.vaso_seleccionado:
            return "Seleccione un vaso primero"
        if not self.cafetera.usar_cafe(self.vaso_seleccionado):
            return "No hay suficiente cafe"
        if not self.azucarero.usar_azucar(self.azucar_seleccionada):
            return "No hay suficiente azúcar"
        return "Aquí está su cafe"