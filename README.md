# Conceptos Generales

## Pickling & Unpickling

Pickling es el proceso de serializar objetos de Python, se convierte en una secuencia de bytes.

```
import pickle

data = {'nombre': 'Juan', 'edad': 30, 'hobbies': ['natación', 'senderismo']}

with open('datos.pickle', 'wb') as file:
    pickle.dump(data, file)
```

El unpickling es la operación inversa, deserializar un objeto, es el proceso de reconstruir un objeto, convertir una secuencia de bytes de un archivo binario ó un objeto tipo binario (bytes-like object) es convertido nuevamente en una jerarquía de objetos.

```
import pickle

with open('datos.pickle', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)  # Imprime: {'nombre': 'Juan', 'edad': 30, 'hobbies': ['natación', 'senderismo']}
```

## Mutable e Inmutable

Significa que se cambia la dirección de memoria después de ser modificados.

Mutables:

- Listas
- Bytearray
- Memoryview
- Diccionarios
- Sets

Inmutables:

- Booleanos
- Complejos
- Enteros
- Float
- Frozenset
- Cadenas
- Tuplas
- Range
- Bytes

## Funciones Lambda

La primera diferencia es que una función lambda no tiene un nombre, y por lo tanto salvo que sea asignada a una variable, es totalmente inútil
