# Cuestionario 

## Descripción
Este proyecto consiste en que el usuario ingrese un número y reciba información curiosa sobre ese número.  
Incluye datos matemáticos básicos y algunas curiosidades especiales para números conocidos (por ejemplo, 42 o 1000).

## Función del Programa

### Paso 1: Pedir un número
El programa solicita al usuario que ingrese un número.  

### Paso 2: Procesar el número
Se llama a la función `trivia_fetch(num)`, que crea un diccionario con los datos del número.

### Paso 3: Crear datos del número

| Clave                     | Descripción                                                  |
|----------------------------|--------------------------------------------------------------|
| number                     | El número ingresado (importante para pruebas automáticas). |
| el numero es par           | Indica si el número es par (True = sí, False = no).         |
| el numero es impar         | Indica si el número es impar (True = sí, False = no).       |
| El numero al cuadrado es igual a | El número multiplicado por sí mismo.                  |
| digitos                    | Cantidad de dígitos que tiene el número.                    |
| dato curioso               | Una curiosidad especial sobre el número (si existe).        |

### Paso 4: Mostrar los resultados
El programa imprime todos los datos en la pantalla, mostrando claramente la información.  

Ejemplo de salida para `42`:
Trivia del número ingresado:
number: 42
el numero es par: True
el numero es impar: False
El numero al cuadrado es igual a: 1764
digitos: 2
dato curioso: 42 es 'la respuesta a la vida, el universo y todo lo demás' según Douglas Adams.

---

## Explicación sencilla del código

1. **`trivia_fetch(num)`**: Función principal que procesa el número y devuelve un diccionario con todos los datos.  
2. **`main()`**: Función que interactúa con el usuario y muestra los resultados.  
3. **`if __name__ == '__main__':`**: Asegura que `main()` solo se ejecute si corres `main.py` directamente.

---
## Cómo ejecutar el programa

1. Abre la terminal o consola.  
2. Navega a la carpeta donde están los archivos (`main.py` y `test.py`).  
3. Escribe:python main.py
4. Ingresa un número y observa la salida.

---

## Cómo probar automáticamente (`test.py`)

1. En la misma carpeta, abre la terminal.  
2. Ejecuta:
pytest test.py ò
python -m pytest test.py

