# Jueves 11 de septiembre del 2025
El dia de hoy solo se realizo la presentacion del curso, el profe tiene experiencia en estado solido y paneles solares. Tambien menciono que trabajo en finanzas.

- Clases de teoria en la primera hora y laboratorio en la segunda hora.
- Muestra el mismo pensum del semestre pasado.
- El curso es 100% presencial.
- EDO.
- Montecarlo.
- Data sciences.
---
# Martes 16 de septiembre del 2025
Otra presentacion del curso ademas de que se planteo la posibilidad de que el profesor sea Pachon.
- A la 1:04 abrió la terminal.

Ejemplos de uso de ls, cd, y pwd. Aprendí sobre la existencia de 'crt + l' para limpiar la terminal. Nocion del super usuario.

---

# Jueves 18 de septiembre del 2025
La clase empezo a las y 15, nuevamente el profe llamó a lista. Procede a presentar el curso y la metodologia.
El profe procede a mostar el concepto de Error de truncamiento y uso de series de taylor.
$$f(x) = f(c) + f'(c)(x - c) + \frac{f''(c)}{2!}(x - c)^2 + \frac{f'''(c)}{3!}(x - c)^3 + ...$$

Por practicidad esta expresion se debe truncar, en el termino $n+1$ se obtiene el polinomio de Taylor de grado n.
$$P_n(x) = f(c) + f'(c)(x - c) + \frac{f''(c)}{2!}(x - c)^2 + ... + \frac{f^{(n)}(c)}{n!}(x - c)^n$$
## Podemos cuantificar el error cometido
Siempre en funcion de los termino que no se tuvieron en cuenta.
$$ R_n(x) = \frac{f^{(n+1)}(z)}{(n+1)!}(x - c)^{n+1} + \frac{f^{(n+2)}(z)}{(n+2)!}(x - c)^{n+2} + ...$$
Usando el teorema del valor medio, obtenemos la froma *lintegral*
$$ R_n(x) = \int_{c}^{x} \frac{f^{(n+1)}(t)}{n!}(x - t)^n dt$$
Y por lo tanto se puede escribir:
$$f(x) = P_n(x) + R_n(x)$$
o la forma *lagrangiana*:
$$ R_n(x) = \frac{f^{(n+1)}(z)}{(n+1)!}(x - c)^{n+1}$$

### Ejemplo: $sin(x)$
$f(x) = sin(x)|_{c=0} = 0$
$f'(x) = cos(x)|_{c=0} = 1$
$f''(x) = -sin(x)|_{c=0} = 0$
$f'''(x) = -cos(x)|_{c=0} = -1$
$f^{(4)}(x) = sin(x)|_{c=0} = 0$
$$ f(x) = 0 + 1(x - 0) + 0(x - 0)^2 - \frac{1}{6}(x - 0)^3 + 0(x - 0)^4 = 0 + 1x - \frac{1}{6}x^3$$
$$f(x) = x - \frac{1}{6}x^3  $$
#### Tarea: Calcular $R(x)?$ para ese orden y el siguiente.
---
La clase acabó a las 12:45pm

---
#### Solución de la tarea:
$R(x)$ para el orden 4 y la funcion $sin(x)$ es:
$$ R_3(x) = \int_{0}^{x} \frac{f^{(4)}(t)}{3!}(x - t)^3 dt = \int_{0}^{x} \frac{sin(t)}{6}(x - t)^3 dt$$
Y para el orden 5:
$$ R_4(x) = \int_{0}^{x} \frac{f^{(5)}(t)}{4!}(x - t)^4 dt = \int_{0}^{x} \frac{cos(t)}{24}(x - t)^4 dt$$

---
# Martes 23 de septiembre del 2025

No hubo clase por asamblea estudiantil.

---
# Jueves 25 de septiembre del 2025

El profe nuevamente llamó a lista y procedio a explicar brevemente las funciones basicas de python, ademas de recordar la definicion de error en una medicion.

$$Error\;relativo = \frac{Valor\;medido - Valor\;real}{Valor\;real}*100$$

El profe nos mostró la pagina de interactivechaos, para consultar documentacion de python. -12:50pm

Dejo una tarea en los correos.

---
# Martes 30 de septiembre
12 y media y aun nada, hay 4 estudiantes en el salón.