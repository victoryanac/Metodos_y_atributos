from pizza import Pizza


print("Precio de la pizza:", Pizza.precio)
print("Ingredientes proteicos disponibles:", Pizza.ingredientes_proteicos)
print("Ingredientes vegetales disponibles:", Pizza.ingredientes_vegetales)
print("Tipos de masa disponibles:", Pizza.tipos_de_masa)


elemento_a_validar = "salsa de tomate"
lista_para_validar = ["salsa de tomate", "salsa bbq"]
es_valido = Pizza.validar_elemento(elemento_a_validar, lista_para_validar)
print(f"¿'{elemento_a_validar}' está en la lista {lista_para_validar}? {es_valido}")


mi_pizza = Pizza()
mi_pizza.realizar_pedido()


print("Ingredientes de tu pizza:")
print("Proteico:", mi_pizza.ingredientes_proteicos)
print("Vegetal 1:", mi_pizza.primer_ingrediente_vegetal)
print("Vegetal 2:", mi_pizza.segundo_ingrediente_vegetal)
print("Tipo de masa:", mi_pizza.tipo_de_masa)
print("¿Es una pizza válida?", "Sí" if mi_pizza.es_valida else "No")

