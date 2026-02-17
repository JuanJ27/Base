# Soluciones - Lista de Problemas de Electrodinámica I
## TEMA III: ECUACIONES DE MAXWELL

---

## Problema 1: Partícula en movimiento rectilíneo

**Enunciado:** La partícula cargada con carga $q$ se mueve en el plano XY a lo largo de la recta $y = x - a$ con velocidad constante $\vec{v}$ alejándose del origen de coordenadas. En el instante de tiempo $t = 0$ la partícula se encontraba sobre el eje x. Calcule las densidades de carga y corriente asociadas a la partícula y verifique el cumplimiento de la ecuación de continuidad.

### Solución:

**Posición de la partícula:**
- En $t=0$: la partícula está sobre el eje $x$ con $y=0$, por lo tanto $x=a$. Posición inicial: $\vec{r}_0 = (a, 0, 0)$
- Dirección del movimiento: a lo largo de $y=x$, vector director $(1, 1, 0)$ normalizado: $\frac{1}{\sqrt{2}}(1, 1, 0)$
- Velocidad: $\vec{v}_p = \frac{v}{\sqrt{2}}\vec{e}_x + \frac{v}{\sqrt{2}}\vec{e}_y$
- Posición en tiempo $t$: $\vec{r}_p(t) = \left(a + \frac{vt}{\sqrt{2}}, \frac{vt}{\sqrt{2}}, 0\right)$

**Densidades de carga y corriente:**

Para una carga puntual, las densidades se expresan con la función delta de Dirac:

$$\rho(x, y, z, t) = q \, \delta\left(x - a - \frac{vt}{\sqrt{2}}\right) \delta\left(y - \frac{vt}{\sqrt{2}}\right) \delta(z)$$

$$\vec{J}(x, y, z, t) = q \left(\frac{v}{\sqrt{2}} \vec{e}_x + \frac{v}{\sqrt{2}} \vec{e}_y\right) \delta\left(x - a - \frac{vt}{\sqrt{2}}\right) \delta\left(y - \frac{vt}{\sqrt{2}}\right) \delta(z)$$

**Verificación de la ecuación de continuidad** $\frac{\partial \rho}{\partial t} + \nabla \cdot \vec{J} = 0$:

Usando la regla de la cadena para derivadas de funciones delta:

$$\frac{\partial \rho}{\partial t} = q \, \delta(z) \left[-\frac{v}{\sqrt{2}} \delta'(x - ...) \delta(y - ...) - \frac{v}{\sqrt{2}} \delta(x - ...) \delta'(y - ...)\right]$$

$$\nabla \cdot \vec{J} = q \, \frac{v}{\sqrt{2}} \delta'(x - ...) \delta(y - ...) \delta(z) + q \, \frac{v}{\sqrt{2}} \delta(x - ...) \delta'(y - ...) \delta(z)$$

Sumando ambos términos: $\frac{\partial \rho}{\partial t} + \nabla \cdot \vec{J} = 0$ ✓

---

## Problema 2: Partícula en movimiento armónico simple

**Enunciado:** La partícula cargada con carga $q$ se mueve a lo largo del eje x según la ley $x(t) = A \sin(\omega t)$. Calcule las densidades de carga y corriente asociadas a la partícula y verifique el cumplimiento de la ecuación de continuidad. Halle los valores medios $\langle\rho\rangle$ y $\langle\vec{J}\rangle$ de las densidades de carga y corriente, respectivamente, en el período $T = \frac{2\pi}{\omega}$. Demuestre que $\int \langle\rho\rangle \, dV = q$.

### Solución:

**Posición y velocidad:**
- Posición: $\vec{r}_p(t) = (A \sin(\omega t), 0, 0)$
- Velocidad: $\vec{v}_p(t) = (A\omega \cos(\omega t), 0, 0)$

**Densidades de carga y corriente:**

$$\rho(x, y, z, t) = q \, \delta(x - A \sin(\omega t)) \, \delta(y) \, \delta(z)$$

$$\vec{J}(x, y, z, t) = q \, A\omega \cos(\omega t) \, \delta(x - A \sin(\omega t)) \, \delta(y) \, \delta(z) \, \vec{e}_x$$

**Verificación de la ecuación de continuidad:**

$$\frac{\partial \rho}{\partial t} = -q \, A\omega \cos(\omega t) \, \delta'(x - A \sin(\omega t)) \, \delta(y) \, \delta(z)$$

$$\nabla \cdot \vec{J} = q \, A\omega \cos(\omega t) \, \delta'(x - A \sin(\omega t)) \, \delta(y) \, \delta(z)$$

Por lo tanto: $\frac{\partial \rho}{\partial t} + \nabla \cdot \vec{J} = 0$ ✓

**Valores medios:**

Para el valor medio de $\rho$, consideramos que la ecuación $x = A \sin(\omega t)$ tiene dos soluciones en $[0, T]$ para $|x| < A$. Usando las propiedades de la función delta:

$$\langle\rho\rangle = \frac{q}{\pi\sqrt{A^2 - x^2}} \, \delta(y) \, \delta(z) \quad \text{para } |x| < A$$

Para la corriente, el integrando es una función impar en el período, por lo que:

$$\langle\vec{J}\rangle = 0$$

**Demostración** $\int\langle\rho\rangle \, dV = q$:

$$\int\langle\rho\rangle \, dV = \int_{-A}^{A} \frac{q}{\pi\sqrt{A^2 - x^2}} \, dx = \frac{q}{\pi} \left[\arcsin\left(\frac{x}{A}\right)\right]_{-A}^{A}$$

$$= \frac{q}{\pi} \left[\frac{\pi}{2} - \left(-\frac{\pi}{2}\right)\right] = \frac{q}{\pi} \cdot \pi = q$$ ✓

---

## Problema 3: Partícula en movimiento circular

**Enunciado:** La partícula cargada con carga $q$ se mueve en el plano XY siguiendo una trayectoria circular de radio $a$ con velocidad angular constante $\omega$. La trayectoria circular tiene su centro en el origen de coordenadas, y en el instante de tiempo $t = 0$ la partícula se encontraba sobre la rama positiva del eje x. Halle las densidades de carga y corriente asociadas a la partícula y escríbalas en coordenadas cilíndricas. Demuestre que $\int \langle\rho\rangle \, dV = q$ y que $\int dr \int dz \, \langle J_\phi\rangle = \frac{q}{T}$.

### Solución:

**Posición y velocidad:**
- Posición (cartesianas): $\vec{r}_p(t) = (a \cos(\omega t), a \sin(\omega t), 0)$
- Posición (cilíndricas): $r_p = a$, $\phi_p = \omega t$, $z_p = 0$
- Velocidad: $\vec{v}_p = a\omega \, \vec{e}_\phi$

**Densidades en coordenadas cilíndricas:**

El elemento de volumen es $dV = r \, dr \, d\phi \, dz$. La función delta se transforma como:

$$\rho(r, \phi, z, t) = \frac{q}{r} \, \delta(r - a) \, \delta(\phi - \omega t) \, \delta(z)$$

$$\vec{J}(r, \phi, z, t) = \frac{qa\omega}{r} \, \delta(r - a) \, \delta(\phi - \omega t) \, \delta(z) \, \vec{e}_\phi$$

**Valor medio de $\rho$:**

Con $T = \frac{2\pi}{\omega}$:

$$\langle\rho\rangle = \frac{1}{T} \int_0^T \rho \, dt = \frac{q}{2\pi r} \, \delta(r - a) \, \delta(z)$$

**Demostración** $\int\langle\rho\rangle \, dV = q$:

$$\int\langle\rho\rangle \, dV = \int_0^\infty \int_0^{2\pi} \int_{-\infty}^{+\infty} \frac{q}{2\pi r} \, \delta(r-a) \, \delta(z) \, r \, dr \, d\phi \, dz$$

$$= \frac{q}{2\pi} \int_0^{2\pi} d\phi \int_0^\infty \delta(r-a) \, dr \int_{-\infty}^{+\infty} \delta(z) \, dz = \frac{q}{2\pi} \cdot 2\pi \cdot 1 \cdot 1 = q$$ ✓

**Valor medio de $J_\phi$:**

$$\langle J_\phi\rangle = \frac{qa}{Tr} \, \delta(r - a) \, \delta(z)$$

**Demostración** $\int dr \int dz \, \langle J_\phi\rangle = \frac{q}{T}$:

$$\int_0^\infty \int_{-\infty}^{+\infty} \frac{qa}{Tr} \, \delta(r - a) \, \delta(z) \, dr \, dz = \frac{qa}{T} \int_0^\infty \frac{1}{r} \delta(r-a) \, dr \cdot 1$$

$$= \frac{qa}{T} \cdot \frac{1}{a} = \frac{q}{T}$$ ✓

---

## Problema 4: FEM inducida en circuito parabólico

**Enunciado:** En el plano XY se encuentra un hilo conductor que describe la parábola $y = \alpha x^2$ ($\alpha > 0$). Un campo magnético homogéneo y constante de inducción $\vec{B}$ está aplicado en la dirección perpendicular al plano de la parábola, orientado según el eje z. En el instante de tiempo $t = 0$ comienza a desplazarse desde el origen, con aceleración constante $a$ dirigida a lo largo del eje y, un puente metálico que une las dos ramas de la parábola y que es paralelo al eje x. Hallar la fuerza electromotriz inducida en el circuito formado por la parábola y el puente en función del tiempo t. Efectúe el análisis dimensional del resultado.

### Solución:

**Posición del puente y geometría:**
- Posición del puente: $y(t) = \frac{1}{2}at^2$
- Puntos de intersección con la parábola: $x = \pm\sqrt{\frac{y}{\alpha}}$
- Ancho del puente: $L(y) = 2\sqrt{\frac{y}{\alpha}}$

**Área encerrada:**

$$A(y) = \int_0^y L(y') \, dy' = \int_0^y 2\sqrt{\frac{y'}{\alpha}} \, dy' = \frac{2}{\sqrt{\alpha}} \cdot \frac{2}{3} y^{3/2} = \frac{4}{3\sqrt{\alpha}} y^{3/2}$$

Sustituyendo $y(t) = \frac{1}{2}at^2$:

$$A(t) = \frac{4}{3\sqrt{\alpha}} \left(\frac{at^2}{2}\right)^{3/2} = \frac{4}{3\sqrt{\alpha}} \cdot \frac{a^{3/2}}{2^{3/2}} t^3 = \frac{4a^{3/2}}{3\sqrt{\alpha} \cdot 2\sqrt{2}} t^3$$

**Derivada del área:**

$$\frac{dA}{dt} = \frac{4a^{3/2}}{3\sqrt{\alpha} \cdot 2\sqrt{2}} \cdot 3t^2 = \frac{\sqrt{2} a^{3/2}}{\sqrt{\alpha}} t^2$$

**FEM inducida:**

$$\varepsilon(t) = -B \frac{dA}{dt} = -\frac{\sqrt{2} B a^{3/2}}{\sqrt{\alpha}} t^2$$

**Análisis dimensional:**
- $[B] = M T^{-2} I^{-1}$ (Tesla)
- $[\alpha] = L^{-1}$ (de $y = \alpha x^2$)
- $[a] = L T^{-2}$ (aceleración)
- $[t] = T$ (tiempo)
- $[\varepsilon] = [B] [\alpha]^{-1/2} [a]^{3/2} [t]^2 = (M T^{-2} I^{-1}) \cdot (L^{1/2}) \cdot (L^{3/2} T^{-3}) \cdot (T^2)$
- $[\varepsilon] = M L^2 T^{-3} I^{-1}$ (Voltio) ✓

---

## Problema 5: Polarización de onda electromagnética

**Enunciado:** En el plano $z = 0$, el vector $\vec{E}$ del campo electromagnético de una onda monocromática plana que se propaga en la dirección del eje z es:

$$\vec{E} = E_0 \left[e^{-i(\omega t - \pi/4)} \vec{e}_x + e^{-i\omega t} \vec{e}_y\right]$$

siendo $\vec{e}_x$ y $\vec{e}_y$ los vectores unitarios a lo largo de las direcciones de los ejes x y y, respectivamente, $\omega$ es la frecuencia de la onda y $E_0$ es un número real. Encuentre una expresión que vincula las partes reales de las dos componentes dadas de $\vec{E}$. ¿Qué tipo de polarización posee la onda dada?

### Solución:

**Componentes reales:**

$$E_x(t) = \text{Re}\left[E_0 e^{i\pi/4} e^{-i\omega t}\right] = E_0 \cos\left(\omega t - \frac{\pi}{4}\right)$$

$$E_y(t) = \text{Re}\left[E_0 e^{-i\omega t}\right] = E_0 \cos(\omega t)$$

**Relación entre componentes:**

Expandiendo $E_x$:

$$E_x = E_0 \left[\cos(\omega t)\cos\left(\frac{\pi}{4}\right) + \sin(\omega t)\sin\left(\frac{\pi}{4}\right)\right]$$

$$E_x = \frac{E_0}{\sqrt{2}} \left[\cos(\omega t) + \sin(\omega t)\right] = \frac{E_y}{\sqrt{2}} + \frac{E_0}{\sqrt{2}}\sin(\omega t)$$

Usando $\sin(\omega t) = \pm\sqrt{1 - \cos^2(\omega t)} = \pm\sqrt{1 - \frac{E_y^2}{E_0^2}}$ y manipulando algebraicamente:

$$E_x^2 + E_y^2 - \sqrt{2} E_x E_y = \frac{E_0^2}{2}$$

Esta es la ecuación de una **elipse rotada**.

**Tipo de polarización:**

La onda tiene **polarización elíptica**. 

Las amplitudes de ambas componentes son iguales ($E_0$), pero la diferencia de fase es $\delta = \pi/4$, que no corresponde ni a polarización lineal ($\delta = 0$ o $\pi$) ni circular ($\delta = \pm\pi/2$).

---

## Problema 6: Fuerza sobre neutrón en campo coulombiano

**Enunciado:** Un neutrón con momentum dipolar magnético $\vec{\mu}$ se mueve con velocidad $\vec{v}$, en el campo coulombiano de un núcleo que posee carga $Q$, con respecto a dicho núcleo. Halle la fuerza $\vec{F}$ que actúa sobre el neutrón en el SRI propio del núcleo en la aproximación no relativista (despreciando términos del orden de $(v/c)^2$ y/o superiores).

### Solución:

**Campo eléctrico del núcleo:**

$$\vec{E} = \frac{1}{4\pi\varepsilon_0} \frac{Q}{r^3} \vec{r}$$

**Campo magnético en el SRI del neutrón:**

En el sistema de referencia del neutrón (SRI'), este ve un campo magnético debido al movimiento relativo del núcleo. En la aproximación no relativista:

$$\vec{B}' \approx -\frac{\vec{v}}{c^2} \times \vec{E}$$

**Fuerza sobre el dipolo magnético:**

La fuerza sobre un dipolo magnético en un campo magnético no homogéneo es:

$$\vec{F}' = \nabla(\vec{\mu} \cdot \vec{B}')$$

Transformando de vuelta al SRI del núcleo, $\vec{F} \approx \vec{F}'$:

$$\vec{F} = -\frac{1}{c^2} \nabla[\vec{\mu} \cdot (\vec{v} \times \vec{E})]$$

Usando la identidad del triple producto escalar $\vec{A} \cdot (\vec{B} \times \vec{C}) = \vec{B} \cdot (\vec{C} \times \vec{A})$:

$$\vec{F} = -\frac{1}{c^2} \nabla[\vec{v} \cdot (\vec{E} \times \vec{\mu})]$$

Como $\vec{v}$ y $\vec{\mu}$ son constantes respecto a la posición:

$$\vec{F} = -\frac{1}{c^2} (\vec{v} \cdot \nabla)(\vec{E} \times \vec{\mu})$$

Alternativamente, usando la expresión general de la fuerza sobre un dipolo magnético en movimiento:

$$\vec{F} = -\frac{1}{4\pi\varepsilon_0 c^2} \nabla\left[(\vec{\mu} \times \vec{v}) \cdot \frac{Q\vec{r}}{r^3}\right]$$

---

## Problema 7: Fuerza sobre dipolo eléctrico en campo magnético

**Enunciado:** Una partícula eléctricamente neutra tiene momentum dipolar eléctrico $\vec{p}$ y se mueve con velocidad $\vec{v}$ en el campo magnético no homogéneo $\vec{B}$ medido en el SRI respecto del cual se refiere $\vec{v}$. Halle la fuerza $\vec{F}$ que actúa sobre la partícula en la aproximación no relativista (despreciando términos del orden de $(v/c)^2$ y/o superiores).

### Solución:

**Campo eléctrico en el SRI de la partícula:**

En el sistema de referencia de la partícula (SRI'), esta ve un campo eléctrico dado por (aproximación no relativista):

$$\vec{E}' \approx \vec{v} \times \vec{B}$$

**Fuerza sobre el dipolo eléctrico:**

La fuerza sobre un dipolo eléctrico en un campo eléctrico no homogéneo es:

$$\vec{F}' = (\vec{p} \cdot \nabla')\vec{E}'$$

Transformando de vuelta al SRI del laboratorio, $\vec{F} \approx \vec{F}'$:

$$\vec{F} \approx (\vec{p} \cdot \nabla)(\vec{v} \times \vec{B})$$

Como $\vec{p}$ y $\vec{v}$ son constantes respecto a la posición:

$$\vec{F} = \vec{v} \times [(\vec{p} \cdot \nabla)\vec{B}]$$

O equivalentemente:

$$\vec{F} = (\vec{p} \cdot \nabla)(\vec{v} \times \vec{B})$$

---

## Problema 8: Efecto Doppler en radiación solar

**Enunciado:** Conociendo la velocidad radial media de la Tierra alrededor del Sol, estime el cambio $\Delta\lambda$ de la longitud de onda de la radiación electromagnética solar correspondiente a la línea fundamental del hidrógeno.

### Solución:

**Efecto Doppler relativista:**

La fórmula para el cambio en la longitud de onda cuando la fuente y el observador se alejan es:

$$\lambda' = \lambda \sqrt{\frac{1 + \beta}{1 - \beta}}$$

donde $\beta = \frac{v}{c}$ y $v$ es la velocidad radial.

**Datos:**
- Velocidad orbital media de la Tierra: $v_{\text{orb}} \approx 30 \, \text{km/s} = 3 \times 10^4 \, \text{m/s}$
- Velocidad de la luz: $c = 3 \times 10^8 \, \text{m/s}$
- $\beta = \frac{3 \times 10^4}{3 \times 10^8} = 10^{-4}$

**Aproximación para $\beta \ll 1$:**

Como $\beta$ es muy pequeño, usamos la aproximación de Taylor:

$$\lambda' \approx \lambda(1 + \beta)^{1/2}(1 - \beta)^{-1/2} \approx \lambda(1 + \beta/2)(1 + \beta/2) \approx \lambda(1 + \beta)$$

Por lo tanto:

$$\Delta\lambda = \lambda' - \lambda \approx \lambda \beta$$

**Línea fundamental del hidrógeno:**

La línea Lyman-alfa (transición $n=2 \to n=1$) tiene una longitud de onda:

$$\lambda \approx 121.6 \, \text{nm}$$

**Cambio en la longitud de onda:**

$$\Delta\lambda = (121.6 \, \text{nm}) \times (10^{-4}) = 0.01216 \, \text{nm} \approx 0.012 \, \text{nm}$$

**Resultado:** El cambio estimado en la longitud de onda es de aproximadamente **$\Delta\lambda \approx 0.012$ nm** o **$12$ pm** (picómetros).

---

**Nota:** Estas soluciones corresponden a los problemas del Tema III sobre Ecuaciones de Maxwell, abarcando densidades de carga y corriente, ecuación de continuidad, FEM inducida, polarización de ondas, fuerzas sobre dipolos y efecto Doppler.
