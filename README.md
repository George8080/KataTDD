# KataTDD
Repositorio que contiene el código necesario para ejecutar el programa "[Ohce Kata](https://kata-log.rocks/ohce-kata)" de "Kata-Log".
## Algoritmo KataTDD
**Input**
* Para iniciar el programa se debe ingresar "**ohce \<tuNombre\>**".
* Para hacer una consulta por el inverso de una palabra simplemente debe escribirla.
* Para terminar el programa debe ingresar "**Stop!**".

**Output**
* Cuando se inicia el programa imprime "**¡Buenos días \<tuNombre\>!**" si es de 6 a 12, "**¡Buenas tardes \<tuNombre\>!**" si es de 12 a 20, y "**¡Buenas noches \<tuNombre\>!**" si es de 20 a 6.
* Para cada consulta te imprime el inverso de la palabra, y si es un palíndromo, tambièn añade "**¡Bonita palabra!**".
* Cuando el programa finaliza, se despide imprimiendo "**Adios \<tuNombre\>**" 
## Preparación para correr códigos
Todo este proyecto fue realizado dentro de Ubuntu - Linux, corriendo todos los comandos dentro de las terminales. Para poder probar el código, ses debe instalar lo siguiente:
* El lenguaje de programación que usa, Python, y para instalarlo en la terminal se debe escribir lo siguiente:
  ```
  apt install python3-pip
  ```
* Pytest, el cual es un framework utilizado en Python para correr test. Para instalarlo se utiliza el siguiente comando:
  ```
  pip install -U pytest
  ```
  Si quieres verificar que Pytest se instaló correctamente puedes ejecutar el siguiente código:
  ```
  pytest --version
  ```
* Para hacer los mocks se debe agregar Pytest-mock, una extensión de Pytest la cual permitirá hacer estas pruebas. Esta se instala de la siguiente manera:
  ```
  pip install pytest-mock
  ```
* Para poder realizar el mock correctamente utilizando Monkeytype, se requiere de instalar el siguiente aditamento de Pytest: 
  ```
  pip install pytest-monkeytype
  ```
## Como correr los programas
En primer lugar, para hacer las pruebas tiene que primero descargar todos los archivos presentes dentro de este repositorio. Para esto se puede hacer manualmente o utilizar el siguiente comando:
```
git clone https://github.com/George8080/KataTDD.git
```
Una vez hecho esto es posible realizar el resto de programas posibles.
* Para poder correr los test presentes en el programa simplemente se debe escribir este comando en la terminal:
  ```
  pytest -q test.py
  ```
* Para poder correr el programa principal (main) se tiene que escribir el siguiente comando:
  ```
  python main.py
  ```
* Si quieres usar una entrada predeterminada externa debes utilizar el siguiente comando:
  ```
  python main.py < input.txt
  ```
  (Siendo "input.txt" un archivo con la entrada la cual se desea probar)
* Si quieres grabar el resultado en un archivo aparte debes utilizar el siguiente comando:
  ```
  python main.py > output.txt
  ```
  (Siendo "output.txt" un nuevo archivo en el cual se guardarán y/o sobreescribirán los resultados)
* También es posible usar una entrada predeterminada y un archivo que guarde el resultado al mismo tiempo:
  ```
  python main.py < input.txt > output.txt
  ```
