## Práctica Final

Escribir un programa que gestione claves de usuario, los datos de los usuarios se encuentran
en un archivo de texto con los siguientes campos:

`Tipo_de_documento Cedula Nombre Fecha_de_nacimiento Ciudad Correo`

---

El programa debe permitir:

* Registrar usuarios con las siguientes condiciones: Si el tipo de documento es cedula, esta debe ser numérica, La contraseña debe ser una clave fuerte, el token se genera con un método automático, la fecha de nacimiento se debe validar como dd/mm/aaaa, si el correo es del dominio del Poli se debe validar como de estudiantes, el correo puede ser de diferentes dominios. Para las validaciones se deben utilizar expresiones regulares.
* Recuperar contraseña: Si se quiere recuperar la contraseña se debe pedir el documento y el correo, validarlo y mostrar la contraseña.
* Modificar contraseña.
* Simular el ingreso al sistema.
* Mostrar todos los usuarios inscritos sin mostrar las contraseñas.

---

Las contraseñas creadas se deben guardar en un archivo, desde el cual se recupera y se valida la simulación de ingreso.
Los datos se almacenan como una matriz y las contraseñas se guardan en un árbol B donde está la cedula y el número de fila de la matriz donde está guardado.

**CRITERIOS DE EVALUACIÓN**

1. Cumplimiento de los requisitos
2. Interfaz
3. Sustentación individual
4. Validaciones
