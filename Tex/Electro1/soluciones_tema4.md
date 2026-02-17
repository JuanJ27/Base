# Solucionario: Introducción a la Teoría Clásica de la Radiación (Tema IV)

Este documento contiene las soluciones detalladas a la lista de problemas del Tema IV: Introducción a la Teoría Clásica de la Radiación.

**Nota sobre unidades:** Se utilizará el **Sistema Internacional (SI)** para el desarrollo de los problemas. La fórmula de Larmor en este sistema es:
$$ P = \frac{1}{4\pi\epsilon_0} \frac{2}{3} \frac{q^2 a^2}{c^3} = \frac{q^2 a^2}{6\pi \epsilon_0 c^3} $$

---

## Problema 1: Átomo de Hidrógeno y Colapso Radiativo

**Enunciado:** Considere un átomo de Hidrógeno descrito por el modelo clásico planetario de Rutherford. El electrón describe una órbita circular de radio $r$ alrededor del núcleo. En $t=0$, el radio es el radio de Bohr $a_0$. Calcule el tiempo de colapso $\tau$ debido a la pérdida de energía por radiación.

**Solución:**
Este problema se resuelve bajo la **aproximación adiabática**, asumiendo que la pérdida de energía es muy lenta comparada con el período orbital ($\tau \gg T_{orb}$). Esto nos permite utilizar las relaciones de la mecánica orbital newtoniana (fuerza central) en cada instante, considerando que el radio $r(t)$ disminuye lentamente.

1.  **Dinámica Orbital (Instántanea):**
    El electrón (carga $-e$, masa $m$) orbita el núcleo ($+e$, masa $M \gg m$, asumimos centro fijo). La fuerza de Coulomb proporciona la aceleración centrípeta:
    $$ F_C = \frac{1}{4\pi\epsilon_0} \frac{e^2}{r^2} = m a_c = m \frac{v^2}{r} $$
    De aquí obtenemos la velocidad al cuadrado y la aceleración en función del radio $r$:
    $$ v^2 = \frac{e^2}{4\pi\epsilon_0 m r} $$
    $$ a = \frac{v^2}{r} = \frac{e^2}{4\pi\epsilon_0 m r^2} $$

2.  **Energía Mecánica Total:**
    $$ E(r) = K + U = \frac{1}{2}mv^2 - \frac{e^2}{4\pi\epsilon_0 r} $$
    Sustituimos $v^2$:
    $$ E(r) = \frac{1}{2} \left( \frac{e^2}{4\pi\epsilon_0 r} \right) - \frac{e^2}{4\pi\epsilon_0 r} = -\frac{e^2}{8\pi\epsilon_0 r} $$
    La tasa de cambio de la energía con respecto al tiempo es:
    $$ \frac{dE}{dt} = \frac{dE}{dr} \frac{dr}{dt} = \left( \frac{e^2}{8\pi\epsilon_0 r^2} \right) \dot{r} $$

3.  **Potencia Radiada (Larmor):**
    Una carga acelerada irradia potencia. En el régimen no relativista ($v \ll c$), usamos la fórmula de Larmor (SI):
    $$ P = \frac{1}{4\pi\epsilon_0} \frac{2 e^2 a^2}{3 c^3} $$
    Sustituimos la expresión de la aceleración $a(r)$:
    $$ P(r) = \frac{1}{4\pi\epsilon_0} \frac{2 e^2}{3 c^3} \left( \frac{e^2}{4\pi\epsilon_0 m r^2} \right)^2 = \frac{2 e^6}{3 (4\pi\epsilon_0)^3 m^2 c^3 r^4} $$

4.  **Balance Energético y Ecuación Diferencial:**
    La conservación de la energía implica que la disminución de energía mecánica equivale a la energía radiada al infinito: $\frac{dE}{dt} = -P$.
    $$ \frac{e^2}{8\pi\epsilon_0 r^2} \dot{r} = - \frac{2 e^6}{3 (4\pi\epsilon_0)^3 m^2 c^3 r^4} $$
    Despejamos $\dot{r}$ simplificando términos ($e^2$ y factores $4\pi\epsilon_0$):
    $$ \frac{1}{8\pi\epsilon_0 r^2} \dot{r} = - \frac{2 e^4}{3 (4\pi\epsilon_0)^3 m^2 c^3 r^4} $$
    $$ \dot{r} = - \frac{2 e^4}{3 (4\pi\epsilon_0)^3 m^2 c^3 r^4} \cdot (8\pi\epsilon_0 r^2) $$
    $$ \dot{r} = - \frac{16 \pi \epsilon_0 e^4}{3 (4\pi\epsilon_0)^3 m^2 c^3 r^2} = - \frac{4 e^4}{3 (4\pi\epsilon_0)^2 m^2 c^3 r^2} $$
    Reagrupando constantes para claridad:
    $$ dt = - \frac{3 (4\pi\epsilon_0)^2 m^2 c^3}{4 e^4} r^2 dr $$

5.  **Integración:**
    Integramos desde el estado inicial ($t=0, r=a_0$) hasta el colapso ($t=\tau, r=0$):
    $$ \int_0^\tau dt = - \frac{3 (4\pi\epsilon_0)^2 m^2 c^3}{4 e^4} \int_{a_0}^0 r^2 dr $$
    $$ \tau = - \frac{3 (4\pi\epsilon_0)^2 m^2 c^3}{4 e^4} \left[ \frac{r^3}{3} \right]_{a_0}^0 $$
    $$ \tau = - \frac{3 (4\pi\epsilon_0)^2 m^2 c^3}{4 e^4} \left( -\frac{a_0^3}{3} \right) = \frac{(4\pi\epsilon_0)^2 m^2 c^3 a_0^3}{4 e^4} $$
    O simplificando usando $\epsilon_0$:
    $$ \tau = \frac{16 \pi^2 \epsilon_0^2 m^2 c^3 a_0^3}{4 e^4} = \frac{4 \pi^2 \epsilon_0^2 m^2 c^3 a_0^3}{e^4} $$

**Respuesta:** El tiempo clásico de vida es $\tau = \frac{4 \pi^2 \epsilon_0^2 m^2 c^3 a_0^3}{e^4}$ (aprox. $1.3 \times 10^{-11}$ s).

---

## Problema 2: Protón en campos E y B cruzados

**Enunciado:** Un protón (masa $m$, carga $q$) se mueve en una región con campos uniformes y estáticos perpendiculares $\vec{E} = E \hat{y}$ y $\vec{B} = B \hat{z}$. La velocidad inicial es $\vec{v}_0$. Calcule la energía total radiada por el protón en un intervalo de tiempo $t$.
(a) Sin reacción de radiación.
(b) Con reacción de radiación.

**Solución:**

### (a) Sin considerar la fuerza de reacción de radiación

1.  **Análisis del Movimiento:**
    La ecuación de movimiento es la fuerza de Lorentz:
    $$ m \frac{d\vec{v}}{dt} = q (\vec{E} + \vec{v} \times \vec{B}) $$
    Este movimiento se puede descomponer en una velocidad de deriva constante $\vec{v}_d$ y un movimiento circular ("ciclotrónico") $\vec{v}_c(t)$.
    Definimos la velocidad de deriva para anular el campo eléctrico en el sistema móvil:
    $$ \vec{v}_d = \frac{\vec{E} \times \vec{B}}{B^2} = \frac{E}{B} \hat{x} $$
    Sustituyendo $\vec{v} = \vec{v}_d + \vec{v}_c(t)$:
    $$ m \dot{\vec{v}}_c = q (\vec{E} + (\vec{v}_d + \vec{v}_c) \times \vec{B}) = q (\vec{E} + \vec{v}_d \times \vec{B} + \vec{v}_c \times \vec{B}) $$
    Como $q(\vec{E} + \vec{v}_d \times \vec{B}) = 0$, nos queda:
    $$ m \dot{\vec{v}}_c = q (\vec{v}_c \times \vec{B}) $$
    Esto describe un movimiento circular uniforme con frecuencia de ciclotrón $\omega = qB/m$.
    La aceleración total de la partícula es igual a la aceleración de la parte circular (ya que $\vec{v}_d$ es constante):
    $$ \vec{a} = \dot{\vec{v}}_c = \frac{q}{m} (\vec{v}_c \times \vec{B}) $$
    El módulo de la aceleración es constante: $a = \omega |\vec{v}_c| = \omega v_{c0}$, donde $v_{c0}$ es la componente de velocidad circular inicial (determinada por $\vec{v}_0 - \vec{v}_d$).

2.  **Cálculo de la Energía Radiada:**
    La potencia radiada instantánea está dada por la fórmula de Larmor:
    $$ P = \frac{1}{4\pi\epsilon_0} \frac{2 q^2 a^2}{3 c^3} $$
    Como la aceleración $a$ es constante en magnitud en esta aproximación (el radio de giro no cambia sin fricción), la potencia es constante.
    La energía radiada $W$ en un tiempo $t$ es simplemente:
    $$ W_{rad} = \int_0^t P dt = P \cdot t = \frac{1}{4\pi\epsilon_0} \frac{2 q^2 a^2 t}{3 c^3} $$
    Expresado en términos de la velocidad perpendicular al campo magnético $v_{c0}$:
    $$ W_{rad} = \frac{q^2 (\omega v_{c0})^2 t}{6 \pi \epsilon_0 c^3} = \frac{q^4 B^2 v_{c0}^2 t}{6 \pi \epsilon_0 m^2 c^3} $$

### (b) Con fuerza de reacción de radiación

Ahora incluimos la fuerza de Abraham-Lorentz $\vec{f}_{rad} = m\tau_0 \dot{\vec{a}}$. Esto actúa como una fricción que amortigua el movimiento.

1.  **Ecuación efectiva:**
    Como vimos en el Problema 3, para el movimiento ciclotrónico, la fuerza de radiación se aproxima a una fuerza de fricción viscosa:
    $$ \vec{f}_{rad} \approx -m \tau_0 \omega^2 \vec{v}_c $$
    La ecuación de movimiento para la componente circular se convierte en:
    $$ m \dot{\vec{v}}_c = q (\vec{v}_c \times \vec{B}) - m \Gamma \vec{v}_c $$
    Donde $\Gamma = \tau_0 \omega^2$.
    (Nota: La velocidad de deriva $\vec{v}_d$ está dictada por el equilibrio de fuerzas $q\vec{E} + q\vec{v}\times\vec{B} \approx 0$ en promedio, por lo que se mantiene constante en esta aproximación de primer orden).

2.  **Amortiguamiento de la Energía Cinética:**
    La energía cinética asociada al movimiento circular es $K_c = \frac{1}{2} m v_c^2$.
    La tasa de cambio es:
    $$ \frac{dK_c}{dt} = \vec{v}_c \cdot (m \dot{\vec{v}}_c) = \vec{v}_c \cdot (q \vec{v}_c \times \vec{B} - m \Gamma \vec{v}_c) $$
    $$ \frac{dK_c}{dt} = - m \Gamma v_c^2 = - 2 \Gamma K_c $$
    Solución: $K_c(t) = K_{c0} e^{-2\Gamma t}$.

3.  **Energía Radiada:**
    La energía radiada proviene de la pérdida de energía mecánica del sistema. Asumiendo que toda la pérdida de $K_c$ se convierte en radiación:
    $$ W_{rad}(t) = K_c(0) - K_c(t) = K_{c0} (1 - e^{-2\Gamma t}) $$
    Sustituyendo $\Gamma = \tau_0 \omega^2 = \left( \frac{1}{4\pi\epsilon_0} \frac{2q^2}{3mc^3} \right) \left( \frac{qB}{m} \right)^2$:
    $$ \Gamma = \frac{q^4 B^2}{6 \pi \epsilon_0 m^3 c^3} $$
    Para tiempos cortos ($2\Gamma t \ll 1$), $1 - e^{-2\Gamma t} \approx 2\Gamma t$, recuperando el resultado de (a):
    $$ W_{rad} \approx K_{c0} (2\Gamma t) = \frac{1}{2} m v_{c0}^2 (2 \frac{P_{Larmor}}{m v_{c0}^2} t) = P_{Larmor} t $$

    **Respuesta:** La energía radiada es $W_{rad} = \frac{1}{2} m v_{c0}^2 \left( 1 - \exp\left( - \frac{q^4 B^2 t}{3 \pi \epsilon_0 m^3 c^3} \right) \right)$.


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

## Problema 4: Antena Cuadrada (Pulso Gaussiano)

**Enunciado:** Un hilo conductor forma un cuadrado de lado $d$. Circula una corriente $I(t) = I_0 e^{-\alpha t^2}$. Calcule la potencia instantánea radiada en la aproximación de dipolo magnético.

**Solución:**

1.  **Justificación de la Aproximación:**
    Asumimos que el tamaño del sistema $d$ es pequeño comparado con la longitud de onda característica ($d \ll \lambda \sim c/\sqrt{\alpha}$) y que las velocidades de los portadores son no relativistas. Esto permite utilizar la aproximación dipolar, donde el término dominante es el dipolo magnético $\vec{m}$ (ya que el lazo es neutro y cerrado, $\vec{p}=0$ y $\dot{\vec{p}}=0$).

2.  **Momento Dipolar Magnético:**
    El momento magnético de una espira plana es $\vec{m}(t) = I(t) A \hat{n}$.
    Aquí $A = d^2$ y orientamos $\hat{n} = \hat{z}$.
    $$ \vec{m}(t) = (d^2 I_0 e^{-\alpha t^2}) \hat{z} $$

3.  **Potencia Radiada por Dipolo Magnético:**
    La fórmula para la potencia radiada por un dipolo magnético variante en el tiempo (en SI) es análoga a la del dipolo eléctrico, con la sustitución $\vec{p} \to \vec{m}/c$:
    $$ P(t) = \frac{\mu_0}{4\pi} \frac{2 |\ddot{\vec{m}}|^2}{3 c^3} $$
    (Recordando que $\mu_0 = 1/(\epsilon_0 c^2)$, esto equivale a $P = \frac{1}{4\pi\epsilon_0} \frac{2 |\ddot{\vec{m}}|^2}{3 c^5}$).

4.  **Derivadas Temporales:**
    Calculamos $\ddot{m}(t)$:
    $$ m(t) = d^2 I_0 e^{-\alpha t^2} $$
    $$ \dot{m}(t) = d^2 I_0 (-2\alpha t) e^{-\alpha t^2} $$
    $$ \ddot{m}(t) = d^2 I_0 \left[ (-2\alpha) e^{-\alpha t^2} + (-2\alpha t)(-2\alpha t) e^{-\alpha t^2} \right] $$
    $$ \ddot{m}(t) = d^2 I_0 2\alpha (2\alpha t^2 - 1) e^{-\alpha t^2} $$

5.  **Potencia Instantánea:**
    Sustituimos $\ddot{m}$ en la fórmula de potencia:
    $$ P(t) = \frac{\mu_0}{6\pi c^3} \left[ d^2 I_0 2\alpha (2\alpha t^2 - 1) e^{-\alpha t^2} \right]^2 $$
    $$ P(t) = \frac{2 \mu_0 \alpha^2 d^4 I_0^2}{3 \pi c^3} (2\alpha t^2 - 1)^2 e^{-2\alpha t^2} $$
    
    *Análisis físico:* La potencia es nula en $t = \pm 1/\sqrt{2\alpha}$ (puntos de inflexión de la corriente) y máxima en $t=0$ o con picos secundarios. El sistema radia debido al cambio en la corriente.


---

## Problema 5: Antena Cuadrada (Corriente AC)

**Enunciado:** Considere la misma antena cuadrada de lado $d$, ahora con corriente oscilante $I(t) = I_0 \cos(\omega t)$. Calcule la potencia media radiada durante un período.

**Solución:**

1.  **Momento Magnético y Derivadas:**
    $$ \vec{m}(t) = d^2 I_0 \cos(\omega t) \hat{z} $$
    Derivando dos veces respecto al tiempo:
    $$ \dot{\vec{m}} = - \omega d^2 I_0 \sin(\omega t) \hat{z} $$
    $$ \ddot{\vec{m}} = - \omega^2 d^2 I_0 \cos(\omega t) \hat{z} $$
    
2.  **Potencia Instantánea:**
    Usando la fórmula de Larmor magnética:
    $$ P(t) = \frac{\mu_0}{6\pi c^3} |\ddot{\vec{m}}|^2 = \frac{\mu_0}{6\pi c^3} \left( \omega^2 d^2 I_0 \cos(\omega t) \right)^2 $$
    $$ P(t) = \frac{\mu_0 \omega^4 d^4 I_0^2}{6 \pi c^3} \cos^2(\omega t) $$

3.  **Potencia Media y Energía:**
    Queremos la potencia promediada en un período $T = 2\pi/\omega$.
    Sabemos que el promedio temporal de $\cos^2(\omega t)$ sobre un ciclo completo es $1/2$.
    $$ \langle P \rangle = \frac{1}{T} \int_0^T P(t) dt = \frac{\mu_0 \omega^4 d^4 I_0^2}{6 \pi c^3} \underbrace{\langle \cos^2(\omega t) \rangle}_{1/2} $$
    $$ \langle P \rangle = \frac{\mu_0 \omega^4 d^4 I_0^2}{12 \pi c^3} $$
    
    La energía total radiada en un período es simplemente la potencia media por el período:
    $$ E_{periodo} = \langle P \rangle \cdot T = \left( \frac{\mu_0 \omega^4 d^4 I_0^2}{12 \pi c^3} \right) \left( \frac{2\pi}{\omega} \right) $$
    $$ E_{periodo} = \frac{\mu_0 \omega^3 d^4 I_0^2}{6 c^3} $$

    **Nota sobre la Resistencia de Radiación:** Este cálculo permite definir una "resistencia de radiación" $R_{rad}$ tal que $\langle P \rangle = \frac{1}{2} I_0^2 R_{rad}$.
    $$ R_{rad} = \frac{\mu_0 \omega^4 d^4}{6 \pi c^3} $$
    Esto confirma que la capacidad de radiación aumenta fuertemente con la frecuencia ($\omega^4$).


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
La potencia rxNadiada por un dipolo magnético $\vec{m}_{mag}$ es:
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

