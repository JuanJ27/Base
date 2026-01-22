# Solucionario: Introducción a la Teoría Clásica de la Radiación (Tema IV)

Este documento contiene las soluciones detalladas a la lista de problemas del Tema IV: Introducción a la Teoría Clásica de la Radiación.

**Nota sobre unidades:** Se utilizará el **Sistema Internacional (SI)** para el desarrollo de los problemas. La fórmula de Larmor en este sistema es:
$$ P = \frac{1}{4\pi\epsilon_0} \frac{2}{3} \frac{q^2 a^2}{c^3} = \frac{q^2 a^2}{6\pi \epsilon_0 c^3} $$

---

## Problema 1: Átomo de Hidrógeno y Colapso Radiativo

**Enunciado:** Considere un átomo de Hidrógeno descrito por el modelo clásico planetario de Rutherford. Suponga que el electrón gira en una órbita circular de radio $r$. En $t=0$, $r=a_0$. Calcule el tiempo de caída al núcleo.

**Solución:**

1.  **Dinámica de la órbita circular:**
    El electrón de carga $-e$ y masa $m$ orbita alrededor del núcleo (carga $+e$, masa infinita para este cálculo). La fuerza centrípeta es la fuerza de Coulomb:
    $$ m \frac{v^2}{r} = \frac{1}{4\pi\epsilon_0} \frac{e^2}{r^2} \implies v^2 = \frac{e^2}{4\pi\epsilon_0 mr} $$
    $$ a = \frac{v^2}{r} = \frac{e^2}{4\pi\epsilon_0 mr^2} $$

2.  **Energía Total:**
    $$ E = K + V = \frac{1}{2}mv^2 - \frac{1}{4\pi\epsilon_0}\frac{e^2}{r} = \frac{1}{2}\left( \frac{e^2}{4\pi\epsilon_0 r} \right) - \frac{e^2}{4\pi\epsilon_0 r} = -\frac{e^2}{8\pi\epsilon_0 r} $$
    Derivando respecto al tiempo:
    $$ \frac{dE}{dt} = \frac{e^2}{8\pi\epsilon_0 r^2} \frac{dr}{dt} $$

3.  **Potencia Radiada (Fórmula de Larmor):**
    Según la fórmula de Larmor, la potencia perdida por radiación es:
    $$ P = \frac{1}{4\pi\epsilon_0} \frac{2}{3} \frac{e^2 a^2}{c^3} $$
    Sustituyendo la aceleración $a = e^2 / (4\pi\epsilon_0 mr^2)$:
    $$ P = \frac{1}{4\pi\epsilon_0} \frac{2 e^2}{3 c^3} \left( \frac{e^2}{4\pi\epsilon_0 mr^2} \right)^2 = \frac{2 e^6}{3 (4\pi\epsilon_0)^3 m^2 c^3 r^4} $$

4.  **Balance de Energía:**
    La tasa de pérdida de energía debe ser igual a la potencia radiada ($dE/dt = -P$):
    $$ \frac{e^2}{8\pi\epsilon_0 r^2} \frac{dr}{dt} = - \frac{2 e^6}{3 (4\pi\epsilon_0)^3 m^2 c^3 r^4} $$

5.  **Integración:**
    Simplificando y despejando $dt$:
    $$ \frac{dr}{dt} = - \frac{2 e^6}{3 (4\pi\epsilon_0)^3 m^2 c^3 r^4} \cdot \frac{8\pi\epsilon_0 r^2}{e^2} $$
    $$ \frac{dr}{dt} = - \frac{16\pi\epsilon_0 e^4}{3 (4\pi\epsilon_0)^3 m^2 c^3 r^2} = - \frac{e^4}{12 \pi^2 \epsilon_0^2 m^2 c^3 r^2} $$
    $$ r^2 dr = - \frac{e^4}{12 \pi^2 \epsilon_0^2 m^2 c^3} dt $$
    Integramos desde $t=0$ ($r=a_0$) hasta $t=\tau$ ($r=0$):
    $$ \int_{a_0}^{0} r^2 dr = - \frac{e^4}{12 \pi^2 \epsilon_0^2 m^2 c^3} \int_{0}^{\tau} dt $$
    $$ \left[ \frac{r^3}{3} \right]_{a_0}^{0} = - \frac{a_0^3}{3} = - \frac{e^4}{12 \pi^2 \epsilon_0^2 m^2 c^3} \tau $$
    $$ \tau = \frac{4 \pi^2 \epsilon_0^2 m^2 c^3 a_0^3}{e^4} $$

**Respuesta:** El tiempo de caída es $\tau = \frac{4 \pi^2 \epsilon_0^2 m^2 c^3 a_0^3}{e^4}$.

---

## Problema 2: Protón en campos E y B cruzados

**Enunciado:** Un protón se mueve en campos $\vec{E}$ y $\vec{B}$ constantes y perpendiculares. Velocidad inicial $\vec{v}_0$. Calcular la energía radiada en tiempo $t$.
(a) Sin reacción de radiación.
(b) Con reacción de radiación.

**Solución:**

### (a) Sin reacción de radiación

1.  **Ecuación de movimiento (Lorentz):**
    $$ m \frac{d\vec{v}}{dt} = q \vec{E} + q \vec{v} \times \vec{B} $$
    Dado que $\vec{E} \perp \vec{B}$, podemos orientar $\vec{E} = E \hat{y}$ y $\vec{B} = B \hat{z}$.
    Esto induce una deriva $\vec{v}_d = \frac{\vec{E} \times \vec{B}}{B^2}$ superpuesta a un movimiento ciclotrónico.
    La aceleración $\vec{a}$ es:
    $$ \vec{a} = \frac{q}{m} \left( \vec{E} + \vec{v} \times \vec{B} \right) $$

    Escribamos la velocidad como $\vec{v}(t) = \vec{u}(t) + \vec{v}_{deriva}$, donde $\vec{u}(t)$ es la componente de rotación circular.
    En el marco de referencia que se mueve con la velocidad de deriva, el campo eléctrico efectivo se anula (o se equilibra con la fuerza magnética de la deriva). La aceleración es puramente centrípeta debida a la componente magnética sobre la velocidad rotacional.
    
    $$ \vec{a} = \frac{q}{m} (\vec{u}(t) \times \vec{B}) $$
    Su magnitud es constante: $|\vec{a}| = \frac{q B}{m} u$, donde $u = |\vec{u}|$ es la velocidad tangencial constante.
    $\omega_B = \frac{qB}{m}$.
    $a = \omega_B u$.

    Energía perdida: $W = \int_0^t P dt$.
    Potencia de Larmor (SI): $P = \frac{1}{4\pi\epsilon_0} \frac{2q^2 a^2}{3c^3}$.
    Como $a$ es constante:
    $$ W = \frac{1}{4\pi\epsilon_0} \frac{2q^2 a^2 t}{3c^3} = \frac{q^2 a^2 t}{6 \pi \epsilon_0 c^3} $$

### (b) Con reacción de radiación

La fuerza de reacción es $\vec{f}_{rad} = m \tau_0 \dot{\vec{a}}$, donde en SI:
$$ \tau_0 = \frac{1}{4\pi\epsilon_0} \frac{2q^2}{3mc^3} = \frac{q^2}{6\pi \epsilon_0 m c^3} $$
El movimiento rotacional se amortigua $u(t) = u_0 e^{-t/\tau_{damp}}$.
La energía radiada será la integral de la potencia que ahora depende del tiempo.

---

## Problema 3: Protón en órbita y Campo B

**Enunciado:** Un protón se mueve en una órbita circular perpendicular a un campo magnético uniforme $\vec{B}$. En $t=0$ su energía cinética es $W_0$. Calcular la disminución de la energía cinética como función del tiempo debido a las pérdidas por radiación:
(a) Sin considerar la fuerza de reacción de radiación en la ecuación de movimiento.
(b) Teniendo en cuenta la fuerza de reacción de radiación.

**Solución:**

### (a) Sin considerar la fuerza de reacción de radiación
En esta aproximación, asumimos que la pérdida de energía es lenta comparada con el periodo orbital (aproximación adiabática), por lo que la trayectoria sigue siendo instantáneamente circular determinada por la fuerza de Lorentz magnética.

1.  **Aceleración:**
    La fuerza magnética proporciona la aceleración centrípeta:
    $$ F_m = q v B = m a \implies a = \frac{q v B}{m} $$
    La energía cinética es $K = \frac{1}{2}mv^2$, por lo que podemos relacionar la velocidad con la energía:
    $$ v^2 = \frac{2K}{m} $$

2.  **Potencia Radiada (Formula de Larmor):**
    $$ P = \frac{1}{4\pi\epsilon_0} \frac{2 q^2 a^2}{3 c^3} $$
    Sustituyendo $a$:
    $$ P = \frac{1}{4\pi\epsilon_0} \frac{2 q^2}{3 c^3} \left( \frac{q v B}{m} \right)^2 = \frac{1}{4\pi\epsilon_0} \frac{2 q^4 B^2}{3 m^2 c^3} v^2 $$
    Sustituyendo $v^2 = 2K/m$:
    $$ P(K) = \frac{1}{4\pi\epsilon_0} \frac{2 q^4 B^2}{3 m^2 c^3} \left( \frac{2K}{m} \right) = \frac{1}{4\pi\epsilon_0} \frac{4 q^4 B^2}{3 m^3 c^3} K $$
    Definimos la constante de amortiguamiento $\gamma$:
    $$ \gamma = \frac{1}{4\pi\epsilon_0} \frac{4 q^4 B^2}{3 m^3 c^3} $$
    $$ P(K) = \gamma K $$

3.  **Evolución Temporal:**
    La tasa de cambio de la energía cinética es igual a la potencia radiada (con signo negativo):
    $$ \frac{dK}{dt} = -P = -\gamma K $$
    Integrando:
    $$ \int_{W_0}^{K(t)} \frac{dK}{K} = -\int_0^t \gamma dt $$
    $$ \ln(K/W_0) = -\gamma t \implies K(t) = W_0 e^{-\gamma t} $$

### (b) Con fuerza de reacción de radiación
La ecuación de movimiento completa incluye la fuerza de Abraham-Lorentz $\vec{f}_{rad}$.
$$ m \dot{\vec{v}} = q(\vec{v} \times \vec{B}) + \vec{f}_{rad} $$
donde $\vec{f}_{rad} = m \tau_0 \dddot{\vec{x}} = m \tau_0 \dot{\vec{a}}$.
Para un movimiento cuasi-circular con frecuencia ciclotrón $\omega_c = qB/m$, tenemos $\vec{a} \approx -\omega_c^2 \vec{v}$.
Entonces:
$$ \vec{f}_{rad} \approx m \tau_0 (-\omega_c^2 \vec{v}) = - (m \tau_0 \omega_c^2) \vec{v} $$
Esto es una fuerza de "fricción" opuesta a la velocidad.
La tasa de cambio de energía cinética es el trabajo hecho por las fuerzas totales:
$$ \frac{dK}{dt} = \vec{v} \cdot (q\vec{v}\times\vec{B} + \vec{f}_{rad}) = \vec{v} \cdot \vec{f}_{rad} $$
(El campo magnético no hace trabajo).
Sustituyendo la aproximación de fricción:
$$ \frac{dK}{dt} = - m \tau_0 \omega_c^2 v^2 $$
Recordemos que $\tau_0 = \frac{1}{4\pi\epsilon_0}\frac{2q^2}{3mc^3}$ y $\omega_c = \frac{qB}{m}$, además de $mv^2 = 2K$:
$$ \frac{dK}{dt} = - \left( \frac{1}{4\pi\epsilon_0} \frac{2q^2}{3mc^3} \right) \left( \frac{q^2 B^2}{m^2} \right) (2K) $$
$$ \frac{dK}{dt} = - \frac{1}{4\pi\epsilon_0} \frac{4 q^4 B^2}{3 m^3 c^3} K = - \gamma K $$
Llegamos exactamente a la misma ecuación diferencial que en la parte (a).
$$ K(t) = W_0 e^{-\gamma t} $$
La inclusión de la fuerza de reacción confirma el resultado obtenido por balance energético global.
---

## Problema 4: Antena Cuadrada (Pulso Gaussiano-like)

**Enunciado:** Hilo cuadrado lado $d$. Corriente $I = I_0 e^{-\alpha t^2}$. Potencia total radiada (Aproximación dipolar magnética).

**Solución:**
1.  **Momento Dipolar Magnético ($\vec{m}$):**
    En SI: $\vec{m}(t) = I(t) \text{Area} \cdot \hat{n}$.
    Área $A = d^2$.
    $$ \vec{m}(t) = d^2 I_0 e^{-\alpha t^2} \hat{z} $$

2.  **Potencia Dipolar Magnética:**
    Fórmula SI: $P = \frac{\mu_0}{4\pi} \frac{2}{3c^3} |\ddot{\vec{m}}|^2 = \frac{\mu_0}{6\pi c^3} |\ddot{\vec{m}}|^2$.
    
3.  **Cálculo de $\ddot{m}$:**
    $$ \ddot{m} = d^2 I_0 \frac{d^2}{dt^2}(e^{-\alpha t^2}) = d^2 I_0 \left[ 2\alpha(2\alpha t^2 - 1) e^{-\alpha t^2} \right] $$

4.  **Potencia Instantánea:**
    $$ P(t) = \frac{\mu_0}{6\pi c^3} \left( d^2 I_0 2\alpha(2\alpha t^2 - 1) e^{-\alpha t^2} \right)^2 $$
    $$ P(t) = \frac{2 \mu_0 \alpha^2 d^4 I_0^2}{3 \pi c^3} (2\alpha t^2 - 1)^2 e^{-2\alpha t^2} $$

---

## Problema 5: Antena Cuadrada (Corriente AC)

**Enunciado:** Misma antena, $I = I_0 \cos(\omega t)$. Potencia radiada en un período.

**Solución:**
1.  **Momento magnético:**
    $$ m(t) = d^2 I_0 \cos(\omega t) $$

2.  **Segunda derivada:**
    $$ \ddot{m} = -\omega^2 d^2 I_0 \cos(\omega t) $$

3.  **Potencia instantánea:**
    $$ P(t) = \frac{\mu_0}{6\pi c^3} \left( d^2 I_0 \omega^2 \cos(\omega t) \right)^2 = \frac{\mu_0 d^4 I_0^2 \omega^4}{6\pi c^3} \cos^2(\omega t) $$

4.  **Promedio/Integración en un período:**
    Promedio de $\cos^2$ es $1/2$.
    Potencia media $\langle P \rangle = \frac{\mu_0 d^4 I_0^2 \omega^4}{12 \pi c^3}$.
    Energía en un período $T = 2\pi/\omega$:
    $$ E = \langle P \rangle \cdot T = \frac{\mu_0 d^4 I_0^2 \omega^4}{12 \pi c^3} \frac{2\pi}{\omega} = \frac{\mu_0 d^4 I_0^2 \omega^3}{6 c^3} $$

---

## Problema 6: Neutrón en campo B (Precesión)

**Enunciado:** Momentum magnético $\vec{m} = -\kappa \vec{L}$. Campo estático $\vec{B}$. Potencia radiada (dipolo magnético).

**Solución:**
1.  **Ecuación de torque:**
    $$ \frac{d\vec{L}}{dt} = \vec{\tau} = \vec{m} \times \vec{B} $$
    $$ -\frac{1}{\kappa} \frac{d\vec{m}}{dt} = \vec{m} \times \vec{B} \implies \frac{d\vec{m}}{dt} = -\kappa (\vec{m} \times \vec{B}) $$
    Precesión con frecuencia $\omega = \kappa B$. Magnitude $|\vec{m}|$ constante.

2.  **Segunda derivada $\ddot{\vec{m}}$:**
    La magnitud es $|\ddot{\vec{m}}| = \omega^2 m_\perp = (\kappa B)^2 m \sin \theta$.

3.  **Potencia:**
    $$ P = \frac{\mu_0}{6\pi c^3} |\ddot{\vec{m}}|^2 = \frac{\mu_0}{6\pi c^3} (\kappa^2 B^2 m_\perp)^2 $$
    $$ P = \frac{\mu_0 \kappa^4 B^4 m^2 \sin^2 \theta}{6 \pi c^3} $$

---

## Problema 7: Protón en campo Eléctrico Uniforme

**Enunciado:** Un protón se mueve en un campo electrostático uniforme $\vec{E}$. Calcule la potencia radiada en:
(a) Aproximación dipolar eléctrica.
(b) Aproximación dipolar magnética. Compare los resultados.

**Solución:**
El movimiento de la partícula (carga $e$, masa $m$) en un campo constante $\vec{E} = E \hat{k}$ está dado por:
$$ m \vec{a} = e \vec{E} \implies \vec{a} = \frac{eE}{m} \hat{k} \quad (\text{constante}) $$
La velocidad es $\vec{v}(t) = \vec{v}_0 + \vec{a}t$. La posición $\vec{r}(t) = \vec{r}_0 + \vec{v}_0 t + \frac{1}{2}\vec{a}t^2$.

### (a) Radiación dipolar eléctrica
La potencia radiada por un dipolo eléctrico $\vec{p}$ es:
$$ P_E = \frac{1}{4\pi\epsilon_0} \frac{2}{3c^3} |\ddot{\vec{p}}|^2 $$
El momento dipolar de una carga puntual con respecto al origen es $\vec{p} = e \vec{r}$.
Su segunda derivada es $\ddot{\vec{p}} = e \ddot{\vec{r}} = e \vec{a}$.
Sustituyendo $\vec{a} = e\vec{E}/m$:
$$ P_E = \frac{1}{4\pi\epsilon_0} \frac{2}{3c^3} |e \vec{a}|^2 = \frac{1}{4\pi\epsilon_0} \frac{2 e^2}{3c^3} \left( \frac{eE}{m} \right)^2 $$
$$ P_E = \frac{e^4 E^2}{6 \pi \epsilon_0 m^2 c^3} $$
Nótese que $P_E$ es constante en el tiempo porque la aceleración es constante.

### (b) Radiación dipolar magnética
La potencia radiada por un dipolo magnético $\vec{m}_{mag}$ es:
$$ P_M = \frac{\mu_0}{4\pi} \frac{2}{3c^3} |\ddot{\vec{m}}_{mag}|^2 = \frac{1}{4\pi\epsilon_0} \frac{2}{3c^5} |\ddot{\vec{m}}_{mag}|^2 $$
(Usando $\mu_0 = 1/(\epsilon_0 c^2)$).
El momento magnético orbital es $\vec{m}_{mag} = \frac{1}{2} e (\vec{r} \times \vec{v})$.
Calculamos la segunda derivada temporal:
1.  $\dot{\vec{m}}_{mag} = \frac{e}{2} (\dot{\vec{r}} \times \vec{v} + \vec{r} \times \dot{\vec{v}}) = \frac{e}{2} (\underbrace{\vec{v} \times \vec{v}}_{0} + \vec{r} \times \vec{a}) = \frac{e}{2} (\vec{r} \times \vec{a})$
2.  $\ddot{\vec{m}}_{mag} = \frac{d}{dt} \left( \frac{e}{2} (\vec{r} \times \vec{a}) \right) = \frac{e}{2} (\dot{\vec{r}} \times \vec{a} + \vec{r} \times \dot{\vec{a}})$
    Como $\vec{a}$ es constante, $\dot{\vec{a}} = 0$.
    $$ \ddot{\vec{m}}_{mag} = \frac{e}{2} (\vec{v} \times \vec{a}) $$

Sustituyendo $\vec{a} = \frac{e\vec{E}}{m}$:
$$ \ddot{\vec{m}}_{mag} = \frac{e}{2} \left( \vec{v} \times \frac{e\vec{E}}{m} \right) = \frac{e^2}{2m} (\vec{v} \times \vec{E}) $$
Calculamos el módulo cuadrado. Si $\vec{E}$ está en el eje $z$ y $\vec{v}$ tiene un ángulo $\theta$ con $z$:
$$ |\vec{v} \times \vec{E}|^2 = v^2 E^2 \sin^2 \theta $$
Entonces:
$$ P_M = \frac{1}{4\pi\epsilon_0} \frac{2}{3c^5} \left( \frac{e^4}{4m^2} v^2 E^2 \sin^2 \theta \right) $$
$$ P_M = \frac{e^4 E^2 v^2 \sin^2 \theta}{24 \pi \epsilon_0 m^2 c^5} $$

### Comparación
La relación entre la potencia magnética y eléctrica es:
$$ \frac{P_M}{P_E} = \frac{\frac{e^4 E^2 v^2 \sin^2 \theta}{24 \pi \epsilon_0 m^2 c^5}}{\frac{e^4 E^2}{6 \pi \epsilon_0 m^2 c^3}} = \frac{6}{24} \frac{v^2}{c^2} \sin^2 \theta = \frac{1}{4} \left( \frac{v}{c} \right)^2 \sin^2 \theta $$
Como estamos en el régimen no relativista, $v \ll c$, por lo tanto $P_M \ll P_E$. La radiación dipolar eléctrica es el efecto dominante.
---

## Problema 8: Radiación por colisión con Átomo Cuadrupolar

**Enunciado:** Partícula de carga $e$, masa $m$, velocidad inicial $v_0$ impacta frontalmente ("head-on") contra un átomo neutro fijo con momento cuadrupolar eléctrico $D_{ij}$. Sea $D_{11}=D_{22}=\frac{1}{2}\Delta$ y $D_{ij}=0$ para $i\neq j$, con $\Delta < 0$. La partícula se acerca hasta una distancia mínima $L$ y rebota. Calcúlese la energía total radiada.

**Solución:**

1.  **Potencial del Átomo Cuadrupolar:**
    El potencial escalar $\Phi(\vec{r})$ debido a un cuadrupolo (con carga neta y dipolo nulos) está dado por:
    $$ \Phi(\vec{r}) = \frac{1}{4\pi\epsilon_0} \frac{1}{2} \sum_{i,j} D_{ij} \frac{\partial^2}{\partial x_i \partial x_j} \left( \frac{1}{r} \right) $$
    Consideramos el movimiento a lo largo del eje $z$ (eje 3). En este eje, $x=y=0$, $r=z$.
    Las derivadas de $1/r$ evaluadas en el eje $z$ son:
    $\frac{\partial^2}{\partial x^2}(1/r) = -1/z^3$, $\frac{\partial^2}{\partial y^2}(1/r) = -1/z^3$, $\frac{\partial^2}{\partial z^2}(1/r) = 2/z^3$.
    Para que el tensor $D_{ij}$ sea consistente con la definición de traceless (o asumiendo la estructura dada):
    La contribución es:
    $$ \Phi(z) = \frac{1}{8\pi\epsilon_0} \left[ D_{11}\left(-\frac{1}{z^3}\right) + D_{22}\left(-\frac{1}{z^3}\right) + D_{33}\left(\frac{2}{z^3}\right) \right] $$
    El problema especifica $D_{11} = D_{22} = \frac{1}{2}\Delta$. Usualmente $Tr(D)=0$ para tensores cuadripolares físicos puros, lo que implicaría $D_{33} = -(D_{11}+D_{22}) = -\Delta$.
    Sustituyendo:
    $$ \Phi(z) = \frac{1}{8\pi\epsilon_0 z^3} \left[ \frac{\Delta}{2}(-1) + \frac{\Delta}{2}(-1) + (-\Delta)(2) \right] = \frac{1}{8\pi\epsilon_0 z^3} [-\Delta - 2\Delta] = \frac{-3\Delta}{8\pi\epsilon_0 z^3} $$
    Como $\Delta < 0$, definamos $\Delta = -|\Delta|$. Entonces $\Phi(z) = \frac{3|\Delta|}{8\pi\epsilon_0 z^3}$. Es un potencial repulsivo (positivo para carga $e>0$).
    Llamemos $C = \frac{3|\Delta|e}{8\pi\epsilon_0}$. La Energía Potencial es $U(z) = e\Phi(z) = \frac{C}{z^3}$.

2.  **Dinámica de la Colisión:**
    Conservación de energía:
    $$ E_{tot} = \frac{1}{2}m v^2 + \frac{C}{z^3} = \text{constante} $$
    En el infinito ($z \to \infty$): $E_{tot} = \frac{1}{2} m v_0^2$.
    En el punto de retorno ($z = L$, $v=0$): $E_{tot} = \frac{C}{L^3}$.
    Esto nos permite relacionar $L$ con $v_0$: $\frac{1}{2} m v_0^2 = \frac{C}{L^3} \implies C = \frac{1}{2} m v_0^2 L^3$.
    
    La velocidad en función de la posición es:
    $$ v(z) = \sqrt{\frac{2}{m} \left( E_{tot} - \frac{C}{z^3} \right)} = \sqrt{\frac{2}{m} \left( \frac{C}{L^3} - \frac{C}{z^3} \right)} = \sqrt{\frac{2C}{mL^3}} \sqrt{1 - \left(\frac{L}{z}\right)^3} $$
    Como $\sqrt{\frac{2C}{mL^3}} = v_0$, tenemos:
    $$ v(z) = v_0 \sqrt{1 - \left(\frac{L}{z}\right)^3} $$

    La fuerza es $F_z = -\frac{dU}{dz} = -(-3) \frac{C}{z^4} = \frac{3C}{z^4}$.
    La aceleración es $a = \frac{F}{m} = \frac{3C}{m z^4}$.
    Sustituyendo $C$:
    $$ a(z) = \frac{3}{m z^4} \left( \frac{1}{2} m v_0^2 L^3 \right) = \frac{3}{2} v_0^2 \frac{L^3}{z^4} $$

3.  **Cálculo de la Energía Radiada:**
    Potencia de Larmor: $P = \frac{1}{4\pi\epsilon_0} \frac{2 e^2 a^2}{3 c^3}$.
    Energía total $W = \int_{-\infty}^{\infty} P(t) dt = 2 \int_{t(L)}^{t(\infty)} P dt = 2 \int_{L}^{\infty} P \frac{dz}{v}$.
    
    Sustituyendo $P(a(z))$ y $v(z)$:
    $$ W = 2 \int_L^\infty \left[ \frac{1}{4\pi\epsilon_0} \frac{2 e^2}{3 c^3} \left( \frac{3}{2} v_0^2 \frac{L^3}{z^4} \right)^2 \right] \frac{dz}{v_0 \sqrt{1 - (L/z)^3}} $$
    $$ W = \frac{e^2}{3 \pi \epsilon_0 c^3} \frac{9}{4} v_0^4 L^6 \frac{1}{v_0} \int_L^\infty \frac{dz}{z^8 \sqrt{1 - (L/z)^3}} $$
    $$ W = \frac{3 e^2 v_0^3 L^6}{4 \pi \epsilon_0 c^3} \int_L^\infty \frac{dz}{z^8 \sqrt{1 - (L/z)^3}} $$

    **Resolviendo la integral:**
    Cambio de variable: $u = \frac{L}{z} \implies z = \frac{L}{u}$.
    $dz = -\frac{L}{u^2} du$.
    Límites: $z=L \to u=1$; $z=\infty \to u=0$.
    $$ I = \int_1^0 \frac{1}{(L/u)^8 \sqrt{1-u^3}} \left( -\frac{L}{u^2} \right) du = \frac{1}{L^7} \int_0^1 \frac{u^6}{\sqrt{1-u^3}} du $$
    Ahora sea $x = u^3 \implies u = x^{1/3}$, $du = \frac{1}{3} x^{-2/3} dx$.
    $$ \int_0^1 \frac{x^2}{\sqrt{1-x}} \frac{1}{3} x^{-2/3} dx = \frac{1}{3} \int_0^1 x^{4/3} (1-x)^{-1/2} dx $$
    Esta es una función Beta: $B(p, q) = \int_0^1 x^{p-1} (1-x)^{q-1} dx$.
    Aquí $p-1 = 4/3 \implies p=7/3$. $q-1 = -1/2 \implies q=1/2$.
    Integral = $\frac{1}{3} B(7/3, 1/2) = \frac{1}{3} \frac{\Gamma(7/3)\Gamma(1/2)}{\Gamma(17/6)}$.
    
    El valor físico importante es la dependencia paramétrica:
    $$ W = \frac{3 e^2 v_0^3 L^6}{4 \pi \epsilon_0 c^3} \cdot \frac{K_{num}}{L^7} = \frac{A}{L} $$
    Donde $A$ agrupa las constantes. La energía radiada es inversamente proporcional a la distancia de máximo acercamiento.

    Resultado final simbólico:
    $$ W = \frac{e^2 v_0^3}{4 \pi \epsilon_0 c^3 L} \left[ \frac{3}{3} B(7/3, 1/2) \right] = \frac{e^2 v_0^3}{4 \pi \epsilon_0 c^3 L} B\left(\frac{7}{3}, \frac{1}{2}\right) $$
---

## Problema 9: Radiación en Condensador Plano

**Enunciado:** Partícula de masa $m$, carga $e$, entra con velocidad $\vec{v}_0$ (formando un ángulo $\alpha$ con $\vec{E}$) en un condensador plano de espesor $d$ con campo $\vec{E}$ uniforme. Calcular energía radiada al atravesarlo.

**Solución:**
1.  **Cinemática:**
    Orientemos $\vec{E} = E \hat{y}$. La partícula entra en $y=0$ y sale en $y=d$.
    Velocidad inicial: $v_{0x} = v_0 \sin\alpha$, $v_{0y} = v_0 \cos\alpha$. (Asumiendo $\alpha$ es con respecto a la normal/campo).
    Fuerza: $\vec{F} = qE \hat{y}$. Aceleración: $\vec{a} = \frac{qE}{m} \hat{y}$ (constante).
    
    El tiempo de tránsito $t_{vuelo}$ se determina por el movimiento en la dirección $y$:
    $$ y(t) = v_{0y} t + \frac{1}{2} a t^2 $$
    Queremos el tiempo $\tau$ tal que $y(\tau) = d$:
    $$ \frac{qE}{2m} \tau^2 + (v_0 \cos\alpha) \tau - d = 0 $$
    Resolviendo para $\tau$ (tomando la raíz positiva):
    $$ \tau = \frac{-v_0 \cos\alpha + \sqrt{v_0^2 \cos^2\alpha + 2 \frac{qE}{m} d}}{(qE/m)} $$
    $$ \tau = \frac{m}{qE} \left( \sqrt{v_0^2 \cos^2\alpha + \frac{2qEd}{m}} - v_0 \cos\alpha \right) $$

2.  **Potencia Radiada:**
    La aceleración es constante, por lo que la potencia es constante en el tiempo (y en el espacio):
    $$ P = \frac{1}{4\pi\epsilon_0} \frac{2 q^2 a^2}{3 c^3} = \frac{1}{4\pi\epsilon_0} \frac{2 q^2}{3 c^3} \left( \frac{qE}{m} \right)^2 $$
    $$ P = \frac{q^4 E^2}{6 \pi \epsilon_0 m^2 c^3} $$

3.  **Energía Total Radiada:**
    Como $P$ es constante:
    $$ W = P \cdot \tau $$
    Sustituyendo $\tau$:
    $$ W = \left( \frac{q^4 E^2}{6 \pi \epsilon_0 m^2 c^3} \right) \cdot \frac{m}{qE} \left( \sqrt{v_0^2 \cos^2\alpha + \frac{2qEd}{m}} - v_0 \cos\alpha \right) $$
    Simplificando:
    $$ W = \frac{q^3 E}{6 \pi \epsilon_0 m c^3} \left( \sqrt{v_0^2 \cos^2\alpha + \frac{2qEd}{m}} - v_0 \cos\alpha \right) $$

    Caso límite: Si el campo es débil o la velocidad muy alta, $\tau \approx d / (v_0 \cos\alpha)$, y $W \approx P \frac{d}{v_0 \cos\alpha}$.
---

## Problema 10: Distribución Espectral de la Radiación

**Enunciado:** Obtenga las expresiones para la distribución espectral de la energía radiada $\frac{dW}{d\omega}$ para sistemas dipolares eléctricos y magnéticos.

**Solución:**
Partimos de la expresión general para la energía total radiada utilizando el Teorema de Parseval sobre la potencia total.
$$ W = \int_{-\infty}^{\infty} P(t) dt $$

1.  **Dipolo Eléctrico:**
    La potencia instantánea es $P(t) = \frac{1}{4\pi\epsilon_0} \frac{2}{3c^3} |\ddot{\vec{p}}(t)|^2$.
    Por Parseval:
    $$ \int_{-\infty}^{\infty} |\ddot{\vec{p}}(t)|^2 dt = \int_{-\infty}^{\infty} |\tilde{\ddot{\vec{p}}}(\omega)|^2 \frac{d\omega}{2\pi} $$
    Usando la propiedad de la transformada de Fourier $\tilde{\ddot{f}}(\omega) = (i\omega)^2 \tilde{f}(\omega) = -\omega^2 \tilde{\vec{p}}(\omega)$, tenemos $|\tilde{\ddot{\vec{p}}}|^2 = \omega^4 |\vec{p}(\omega)|^2$.
    (Nota: Aquí definimos la transformada como $f(t) = \frac{1}{2\pi} \int \tilde{f}(\omega) e^{-i\omega t} d\omega$. Debido a que la energía es real e integramos frecuencias positivas):
    
    $$ W = \frac{1}{4\pi\epsilon_0} \frac{2}{3c^3} \frac{1}{2\pi} 2 \int_{0}^{\infty} \omega^4 |\vec{p}(\omega)|^2 d\omega $$
    $$ W = \int_{0}^{\infty} \left( \frac{1}{4\pi\epsilon_0} \frac{2 \omega^4}{3 \pi c^3} |\vec{p}(\omega)|^2 \right) d\omega $$
    Por lo tanto, la distribución espectral $I(\omega) \equiv \frac{dW}{d\omega}$ es:
    $$ \frac{dW}{d\omega} = \frac{1}{4\pi\epsilon_0} \frac{2 \omega^4}{3 \pi c^3} |\vec{p}(\omega)|^2 $$

2.  **Dipolo Magnético:**
    La analogía es directa sustituyendo el momento dipolar eléctrico por el magnético (y ajustando constantes $c$).
    Potencia: $P_M(t) = \frac{\mu_0}{6\pi c^3} |\ddot{\vec{m}}(t)|^2$.
    Siguiendo el mismo procedimiento de Fourier: $|\ddot{\vec{m}}(\omega)|^2 = \omega^4 |\vec{m}(\omega)|^2$.
    $$ W = \frac{\mu_0}{6\pi c^3} \frac{1}{\pi} \int_{0}^{\infty} \omega^4 |\vec{m}(\omega)|^2 d\omega $$
    $$ \frac{dW}{d\omega} = \frac{\mu_0 \omega^4}{6 \pi^2 c^3} |\vec{m}(\omega)|^2 $$
    Reescribiendo $\mu_0 = 1/(\epsilon_0 c^2)$:
    $$ \frac{dW}{d\omega} = \frac{1}{4\pi\epsilon_0} \frac{2 \omega^4}{3 \pi c^5} |\vec{m}(\omega)|^2 $$

**Resumen:**
*   Dipolo Eléctrico: $\frac{dW}{d\omega} = \frac{1}{4\pi\epsilon_0} \frac{2\omega^4}{3\pi c^3} |\vec{p}(\omega)|^2$
*   Dipolo Magnético: $\frac{dW}{d\omega} = \frac{\mu_0 \omega^4}{6\pi^2 c^3} |\vec{m}(\omega)|^2$

