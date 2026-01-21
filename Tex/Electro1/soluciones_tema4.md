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

**Enunciado:** Protón en órbita perpendicular a $\vec{B}$ uniforme. En $t=0$, $K=W_0$. Calcular la disminución de $K(t)$.

**Solución:**

### (a) Sin considerar cambio en trayectoria (Aproximación adiabática)
Potencia de Larmor: $P = \frac{1}{4\pi\epsilon_0} \frac{2q^2 a^2}{3c^3}$.
Fuerza magnética: $ma = q v B \implies a = \frac{q B v}{m}$.
$$ P = \frac{1}{4\pi\epsilon_0} \frac{2q^2}{3c^3} \left( \frac{q B v}{m} \right)^2 = \frac{1}{4\pi\epsilon_0} \frac{2 q^4 B^2}{3 m^2 c^3} v^2 $$
Sabemos que $K = \frac{1}{2} m v^2 \implies v^2 = \frac{2K}{m}$.
$$ P(K) = \frac{1}{4\pi\epsilon_0} \frac{4 q^4 B^2}{3 m^3 c^3} K = \alpha K $$
Donde $\alpha = \frac{q^4 B^2}{3 \pi \epsilon_0 m^3 c^3}$.
Pérdida de energía: $\frac{dK}{dt} = -P = -\alpha K$.
$$ K(t) = W_0 e^{-\alpha t} $$

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

## Problema 7: Protón en campo E uniforme

**Enunciado:** Protón en $\vec{E}$ uniforme.
(a) Dipolo eléctrico.
(b) Dipolo magnético.

**Solución:**
El protón experimenta $\vec{F} = e\vec{E} \implies \vec{a} = e\vec{E}/m$ (constante).

### (a) Radiación dipolar eléctrica
Potencia $P_E = \frac{1}{4\pi\epsilon_0} \frac{2}{3c^3} |\ddot{\vec{p}}|^2$.
Dipolo $\vec{p} = e\vec{r}$. $\ddot{\vec{p}} = e\vec{a} = \frac{e^2 \vec{E}}{m}$.
$$ P_E = \frac{1}{4\pi\epsilon_0} \frac{2}{3c^3} \left( \frac{e^2 E}{m} \right)^2 = \frac{e^4 E^2}{6\pi \epsilon_0 m^2 c^3} $$

### (b) Radiación dipolar magnética
Potencia $P_M = \frac{\mu_0}{6\pi c^3} |\ddot{\vec{m}}|^2$.
Momento magnético orbital $\vec{m} = \frac{1}{2} e (\vec{r} \times \vec{v})$.
$\ddot{\vec{m}} = \frac{e}{2} (\vec{v} \times \vec{a}) = \frac{e}{2} (\vec{v} \times \frac{e\vec{E}}{m}) = \frac{e^2}{2m} (\vec{v} \times \vec{E})$.
$$ P_M = \frac{\mu_0}{6\pi c^3} \left| \frac{e^2}{2m} (\vec{v} \times \vec{E}) \right|^2 = \frac{\mu_0 e^4 v^2 E^2 \sin^2 \phi}{24 \pi m^2 c^3} $$

---

## Problema 8: Partícula y Átomo Cuadrupolar

**Solución:**
1.  **Potencial:**
    SI: $\Phi(\vec{r}) = \frac{1}{4\pi\epsilon_0} \frac{1}{2} \sum D_{ij} \frac{\partial^2}{\partial x_i \partial x_j} (\frac{1}{r})$.
    Aceleración $a \propto \frac{1}{4\pi\epsilon_0}$.
    
2.  **Potencia:**
    $P \propto \frac{1}{4\pi\epsilon_0 c^3} a^2$.
    El cálculo sigue la misma lógica pero arrastrando los factores $\frac{1}{4\pi\epsilon_0}$.

---

## Problema 9: Condensador Plano

**Solución:**
1.  **Aceleración:**
    $\vec{a} = \frac{qE}{m} \hat{k}$.

2.  **Potencia:**
    $$ P = \frac{1}{4\pi\epsilon_0} \frac{2q^2 a^2}{3c^3} = \frac{q^2}{6\pi \epsilon_0 c^3} \left(\frac{qE}{m}\right)^2 $$

3.  **Energía Calculada:** $E_{rad} = P \cdot t_{vuelo}$.

---

## Problema 10: Distribución Espectral

**Solución:**
Energía total $W = \int P dt$.
Dipolo eléctrico (SI):
$$ \frac{dI}{d\omega} = \frac{1}{4\pi\epsilon_0} \frac{4\omega^4}{3c^3} |\vec{p}(\omega)|^2 = \frac{\omega^4}{3\pi\epsilon_0 c^3} |\vec{p}(\omega)|^2 $$

Dipolo magnético (SI):
$$ \frac{dI}{d\omega} = \frac{\mu_0}{4\pi} \frac{4\omega^4}{3c^3} |\vec{m}(\omega)|^2 = \frac{\mu_0 \omega^4}{3\pi c^3} |\vec{m}(\omega)|^2 $$
