from ingredientes import ingredientes_proteicos, ingredientes_vegetales, tipos_de_masa


class Pizza:
    #caracteristicas de la pizza
    precio = 10000
    tamanio = "familiar"
    ingredientes_proteicos = ingredientes_proteicos
    ingredientes_vegetales = ingredientes_vegetales
    tipos_de_masa = tipos_de_masa
    
    @staticmethod
    def validar_elemento(elemento, posibles_valores):
        return elemento in posibles_valores
    
    def __init__(self) -> None:
        self.ingredientes_proteicos = ''
        self.primer_ingredientes_vegetales = ''
        self.segundo_ingredinte_vegetal = ''
        self.tipos_de_masa = ''
        self.es_valida = False
        pass
        
    #realizar pedido
    def realizar_pedido(self):
        print('ingrese los detalles de su pizza: ')
        self.ingredientes_proteicos = input('Ingrediente proteico: ')
        self.primer_ingrediente_vegetal = input("Primer ingrediente vegetal: ")
        self.segundo_ingrediente_vegetal = input("Segundo ingrediente vegetal: ")        
        self.tipo_de_masa = input("Tipo de masa: ")
        
        # Validación de los ingredientes y el tipo de masa
        self.es_valida = (Pizza.validar_elemento(self.ingredientes_proteicos, Pizza.ingredientes_proteicos) and
                        Pizza.validar_elemento(self.primer_ingrediente_vegetal, Pizza.ingredientes_vegetales) and
                        Pizza.validar_elemento(self.segundo_ingrediente_vegetal, Pizza.ingredientes_vegetales) and
                        Pizza.validar_elemento(self.tipo_de_masa, Pizza.tipos_de_masa))
