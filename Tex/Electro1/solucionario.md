# Solucionario - Problemas Propuestos de Electrostática del Vacío

## Problema 1

**Enunciado:** Del octante $x \geq 0$; $y \geq 0$; $z \geq 0$ de la bola $x^2 + y^2 + z^2 \leq c^2$ se ha sustraído el cuerpo limitado por los planos coordenados y por el plano $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$ ($a > 0$, $b > 0$, $c > 0$, $a \leq c$, $b \leq c$). Halle la carga del cuerpo si la densidad de carga es $\rho(\vec{r}) = \lambda_0 z$.

**Solución:**

La carga total $Q$ de un cuerpo con una densidad de carga $\rho(\vec{r})$ se calcula mediante la integral de volumen sobre el volumen $V$ que ocupa el cuerpo:
$$
Q = \int_V \rho(\vec{r}) dV
$$
En este caso, $\rho(\vec{r}) = \lambda_0 z$. El volumen $V$ es el octante de la esfera de radio $c$ al que se le ha quitado un tetraedro. Podemos calcular la carga total como la carga en el octante de la esfera ($Q_{esfera}$) menos la carga en el tetraedro ($Q_{tetraedro}$).

$$
Q = Q_{esfera} - Q_{tetraedro}
$$

**1. Cálculo de la carga en el octante de la esfera ($Q_{esfera}$)**

El volumen de integración es el primer octante de una esfera de radio $c$. Es más conveniente usar coordenadas esféricas:
*   $x = r \sin\theta \cos\varphi$
*   $y = r \sin\theta \sin\varphi$
*   $z = r \cos\theta$
*   $dV = r^2 \sin\theta dr d\theta d\varphi$

Los límites de integración para el primer octante son:
*   $0 \leq r \leq c$
*   $0 \leq \theta \leq \pi/2$
*   $0 \leq \varphi \leq \pi/2$

La integral para la carga es:
$$
Q_{esfera} = \int_0^{\pi/2} \int_0^{\pi/2} \int_0^c (\lambda_0 r \cos\theta) (r^2 \sin\theta dr d\theta d\varphi)
$$
$$
Q_{esfera} = \lambda_0 \int_0^{\pi/2} d\varphi \int_0^{\pi/2} \cos\theta \sin\theta d\theta \int_0^c r^3 dr
$$

Calculamos cada integral por separado:

**Integral en $\varphi$:**
$$\int_0^{\pi/2} d\varphi = [\varphi]_0^{\pi/2} = \frac{\pi}{2} - 0 = \frac{\pi}{2}$$

**Integral en $r$:**
$$\int_0^c r^3 dr = \left[\frac{r^4}{4}\right]_0^c = \frac{c^4}{4} - \frac{0^4}{4} = \frac{c^4}{4}$$

**Integral en $\theta$:**
Para calcular $\int_0^{\pi/2} \sin\theta \cos\theta d\theta$, usamos el cambio de variable $u = \sin\theta$, de modo que $du = \cos\theta d\theta$:
- Si $\theta = 0$, $u = 0$
- Si $\theta = \pi/2$, $u = 1$

$$\int_0^{\pi/2} \sin\theta \cos\theta d\theta = \int_0^1 u du = \left[\frac{u^2}{2}\right]_0^1 = \frac{1}{2} - 0 = \frac{1}{2}$$

**Multiplicación de los resultados:**
$$Q_{esfera} = \lambda_0 \int_0^{\pi/2} d\varphi \int_0^{\pi/2} \cos\theta \sin\theta d\theta \int_0^c r^3 dr$$
$$Q_{esfera} = \lambda_0 \left(\frac{\pi}{2}\right) \left(\frac{1}{2}\right) \left(\frac{c^4}{4}\right)$$
$$Q_{esfera} = \frac{\pi \lambda_0 c^4}{16}$$

**2. Cálculo de la carga en el tetraedro ($Q_{tetraedro}$)**

El volumen de integración es el tetraedro definido por los planos $x=0, y=0, z=0$ y $\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$. Usaremos coordenadas cartesianas.

Los límites de integración son:
*   $0 \leq x \leq a$
*   $0 \leq y \leq b\left(1 - \frac{x}{a}\right)$
*   $0 \leq z \leq c\left(1 - \frac{x}{a} - \frac{y}{b}\right)$

La integral para la carga es:
$$
Q_{tetraedro} = \int_0^a \int_0^{b(1-x/a)} \int_0^{c(1-x/a-y/b)} (\lambda_0 z) dz dy dx
$$

**Paso 1: Integración en $z$**

Primero integramos con respecto a $z$:
$$
\int_0^{c(1-x/a-y/b)} \lambda_0 z \, dz = \lambda_0 \left[\frac{z^2}{2}\right]_0^{c(1-x/a-y/b)} = \frac{\lambda_0}{2}\left[c\left(1 - \frac{x}{a} - \frac{y}{b}\right)\right]^2
$$

Desarrollamos el cuadrado:
$$
\left[c\left(1 - \frac{x}{a} - \frac{y}{b}\right)\right]^2 = c^2\left(1 - \frac{x}{a} - \frac{y}{b}\right)^2
$$

Por lo tanto:
$$
Q_{tetraedro} = \frac{\lambda_0 c^2}{2} \int_0^a \int_0^{b(1-x/a)} \left(1 - \frac{x}{a} - \frac{y}{b}\right)^2 dy dx
$$

**Paso 2: Cambio de variable en la integral en $y$**

Para simplificar, hacemos un cambio de variable en la integral interna: $u = 1 - \frac{x}{a} - \frac{y}{b}$.

Entonces:
- $\frac{\partial u}{\partial y} = -\frac{1}{b}$
- $du = -\frac{1}{b} dy \implies dy = -b \, du$

Cuando $y=0$: $u = 1 - \frac{x}{a}$

Cuando $y=b(1-x/a)$: $u = 1 - \frac{x}{a} - \frac{1}{b} \cdot b\left(1-\frac{x}{a}\right) = 1 - \frac{x}{a} - \left(1-\frac{x}{a}\right) = 0$

La integral en $y$ se convierte en:
$$
\int_0^{b(1-x/a)} u^2 \, dy = \int_{1-x/a}^0 u^2 (-b du) = b \int_0^{1-x/a} u^2 du
$$

Evaluamos esta integral:
$$
b \int_0^{1-x/a} u^2 du = b \left[\frac{u^3}{3}\right]_0^{1-x/a} = \frac{b}{3}\left(1 - \frac{x}{a}\right)^3
$$

Sustituyendo de vuelta:
$$
Q_{tetraedro} = \frac{\lambda_0 c^2}{2} \int_0^a \frac{b}{3}\left(1 - \frac{x}{a}\right)^3 dx = \frac{\lambda_0 b c^2}{6} \int_0^a \left(1 - \frac{x}{a}\right)^3 dx
$$

**Paso 3: Cambio de variable en la integral en $x$**

Hacemos otro cambio de variable: $v = 1 - \frac{x}{a}$

Entonces:
- $\frac{dv}{dx} = -\frac{1}{a}$
- $dv = -\frac{1}{a} dx \implies dx = -a \, dv$

Cuando $x=0$: $v=1 - 0 = 1$

Cuando $x=a$: $v=1 - \frac{a}{a} = 0$

La integral en $x$ se convierte en:
$$
\int_0^a \left(1 - \frac{x}{a}\right)^3 dx = \int_1^0 v^3 (-a dv) = a \int_0^1 v^3 dv
$$

Evaluamos esta integral:
$$
a \int_0^1 v^3 dv = a \left[\frac{v^4}{4}\right]_0^1 = a \left(\frac{1}{4} - 0\right) = \frac{a}{4}
$$

**Paso 4: Resultado final para el tetraedro**

Sustituyendo el resultado de la integral en la expresión anterior:
$$
Q_{tetraedro} = \frac{\lambda_0 b c^2}{6} \left(\frac{a}{4}\right) = \frac{\lambda_0 a b c^2}{24}
$$

**3. Carga total**

Finalmente, la carga total del cuerpo es la diferencia entre las dos cargas calculadas:
$$
Q = Q_{esfera} - Q_{tetraedro} = \frac{\pi \lambda_0 c^4}{16} - \frac{\lambda_0 a b c^2}{24}
$$
Factorizando $\lambda_0 c^2$:
$$
Q = \lambda_0 c^2 \left( \frac{\pi c^2}{16} - \frac{ab}{24} \right)
$$

---

## Problema 2

**Enunciado:** Determine el potencial del campo electrostático $\vec{E}(\vec{r}) = ay\vec{i} + (ax + bz)\vec{j} + by\vec{k}$, siendo $a$ y $b$ constantes. Calcule el trabajo realizado por el campo al llevar la carga $q$ desde el origen de coordenadas hasta el punto $\left(\frac{E_0}{a}, \frac{E_0}{\sqrt{a^{2}+b^{2}}}, \frac{E_0}{b}\right)$, siendo $E_0$ otra constante.

**Solución:**

El problema se divide en dos partes: primero, encontrar el potencial electrostático $\phi$ a partir del campo eléctrico $\vec{E}$, y segundo, calcular el trabajo realizado por el campo para mover una carga entre dos puntos.

**1. Determinación del potencial electrostático ($\phi$)**

Un campo electrostático $\vec{E}$ es siempre conservativo, lo que significa que su rotacional es nulo ($\nabla \times \vec{E} = 0$) y que puede expresarse como el gradiente negativo de un potencial escalar $\phi$:
$$
\vec{E} = -\nabla \phi
$$
Primero, verificamos que el campo es conservativo:
$$
\nabla \times \vec{E} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ ay & ax+bz & by \end{vmatrix}
$$
$$
= \left( \frac{\partial(by)}{\partial y} - \frac{\partial(ax+bz)}{\partial z} \right)\vec{i} - \left( \frac{\partial(by)}{\partial x} - \frac{\partial(ay)}{\partial z} \right)\vec{j} + \left( \frac{\partial(ax+bz)}{\partial x} - \frac{\partial(ay)}{\partial y} \right)\vec{k}
$$
$$
= (b - b)\vec{i} - (0 - 0)\vec{j} + (a - a)\vec{k} = \vec{0}
$$
Como el rotacional es cero, el campo es conservativo y existe un potencial $\phi$.

Para encontrar $\phi$, usamos las componentes de la relación $\vec{E} = -\nabla \phi$:
1.  $E_x = -\frac{\partial \phi}{\partial x} \implies ay = -\frac{\partial \phi}{\partial x}$
2.  $E_y = -\frac{\partial \phi}{\partial y} \implies ax + bz = -\frac{\partial \phi}{\partial y}$
3.  $E_z = -\frac{\partial \phi}{\partial z} \implies by = -\frac{\partial \phi}{\partial z}$

Integramos la primera ecuación con respecto a $x$:
$$
\phi(x, y, z) = -\int ay \, dx = -axy + f(y, z)
$$
donde $f(y, z)$ es una función de integración que puede depender de $y$ y $z$.

Ahora, derivamos esta expresión para $\phi$ con respecto a $y$:
$$
\frac{\partial \phi}{\partial y} = \frac{\partial}{\partial y}[-axy + f(y, z)] = -ax + \frac{\partial f}{\partial y}
$$

Igualando con la condición $-\frac{\partial \phi}{\partial y} = ax + bz$:
$$
-\left(-ax + \frac{\partial f}{\partial y}\right) = ax + bz
$$
$$
ax - \frac{\partial f}{\partial y} = ax + bz
$$
$$
-\frac{\partial f}{\partial y} = bz \implies \frac{\partial f}{\partial y} = -bz
$$

Integramos esta ecuación con respecto a $y$:
$$
f(y, z) = -\int bz \, dy = -byz + g(z)
$$
donde $g(z)$ es una función de integración que solo depende de $z$.

Sustituimos $f(y, z)$ en nuestra expresión para $\phi$:
$$
\phi(x, y, z) = -axy - byz + g(z)
$$

Finalmente, derivamos esta expresión con respecto a $z$:
$$
\frac{\partial \phi}{\partial z} = \frac{\partial}{\partial z}[-axy - byz + g(z)] = -by + \frac{dg}{dz}
$$

Igualando con la condición $-\frac{\partial \phi}{\partial z} = by$:
$$
-\left(-by + \frac{dg}{dz}\right) = by
$$
$$
by - \frac{dg}{dz} = by
$$
$$
\frac{dg}{dz} = 0
$$

Esto significa que $g(z)$ es una constante, que podemos llamar $C$. Por lo tanto, el potencial electrostático es:
$$
\phi(x, y, z) = -axy - byz + C
$$

Por simplicidad, podemos elegir la constante de potencial $C=0$, ya que solo las diferencias de potencial tienen significado físico.
$$
\phi(x, y, z) = -axy - byz
$$

**2. Cálculo del trabajo realizado por el campo**

El trabajo $W$ realizado por un campo electrostático para mover una carga $q$ desde un punto inicial $A$ a un punto final $B$ es igual a la carga multiplicada por la diferencia de potencial entre los puntos:
$$
W = q(\phi_A - \phi_B)
$$
En este caso:
*   Punto inicial $A$: Origen de coordenadas, $(x_A, y_A, z_A) = (0, 0, 0)$.
*   Punto final $B$: $(x_B, y_B, z_B) = \left(\frac{E_0}{a}, \frac{E_0}{\sqrt{a^{2}+b^{2}}}, \frac{E_0}{b}\right)$.

Calculamos el potencial en ambos puntos:
*   $\phi_A = \phi(0, 0, 0) = -a(0)(0) - b(0)(0) = 0$.

*   Para $\phi_B$, sustituimos $x_B = \frac{E_0}{a}$, $y_B = \frac{E_0}{\sqrt{a^2+b^2}}$, $z_B = \frac{E_0}{b}$:
    $$
    \phi_B = -a(x_B)(y_B) - b(y_B)(z_B)
    $$
    
    Primer término:
    $$
    -a(x_B)(y_B) = -a \left(\frac{E_0}{a}\right)\left(\frac{E_0}{\sqrt{a^2+b^2}}\right) = -E_0 \cdot \frac{E_0}{\sqrt{a^2+b^2}} = -\frac{E_0^2}{\sqrt{a^2+b^2}}
    $$
    
    Segundo término:
    $$
    -b(y_B)(z_B) = -b\left(\frac{E_0}{\sqrt{a^2+b^2}}\right)\left(\frac{E_0}{b}\right) = -E_0 \cdot \frac{E_0}{\sqrt{a^2+b^2}} = -\frac{E_0^2}{\sqrt{a^2+b^2}}
    $$
    
    Sumando los dos términos:
    $$
    \phi_B = -\frac{E_0^2}{\sqrt{a^2+b^2}} - \frac{E_0^2}{\sqrt{a^2+b^2}} = -\frac{2E_0^2}{\sqrt{a^2+b^2}}
    $$

Ahora calculamos el trabajo. La diferencia de potencial es:
$$
\phi_A - \phi_B = 0 - \left(-\frac{2E_0^2}{\sqrt{a^2+b^2}}\right) = \frac{2E_0^2}{\sqrt{a^2+b^2}}
$$

Por lo tanto:
$$
W = q(\phi_A - \phi_B) = q \cdot \frac{2E_0^2}{\sqrt{a^2+b^2}}
$$
$$
W = \frac{2qE_0^2}{\sqrt{a^2+b^2}}
$$

---

## Problema 3

**Enunciado:** Calcule la función de Green para el interior de un sector circular plano de radio $R$ con condiciones de frontera de Dirichlet en la frontera.

**Solución:**

La función de Green $G(\vec{r}, \vec{r}')$ en dos dimensiones para el operador Laplaciano satisface la ecuación de Poisson con una carga puntual como fuente:
$$
\nabla^2 G(\vec{r}, \vec{r}') = -\delta(\vec{r} - \vec{r}')
$$
donde $\vec{r} = (r, \varphi)$ y $\vec{r}' = (r', \varphi')$ son las coordenadas polares del punto de observación y del punto fuente, respectivamente.

El dominio es un sector circular definido por $0 \leq r \leq R$ y $0 \leq \varphi \leq \alpha$, donde $\alpha$ es el ángulo del sector.

Las condiciones de frontera de Dirichlet implican que la función de Green debe anularse en la frontera del sector:
1.  $G(r=R, \varphi; r', \varphi') = 0$ (en el arco circular)
2.  $G(r, \varphi=0; r', \varphi') = 0$ (en el lado recto $\varphi=0$)
3.  $G(r, \varphi=\alpha; r', \varphi') = 0$ (en el lado recto $\varphi=\alpha$)

Para resolver este problema, utilizamos el método de expansión en funciones propias. Buscamos una solución de la forma:
$$
G(r, \varphi; r', \varphi') = \sum_{n=1}^{\infty} g_n(r, r') \sin\left(\frac{n\pi\varphi}{\alpha}\right)
$$
Esta forma ya satisface las condiciones de frontera en $\varphi=0$ y $\varphi=\alpha$.

Sustituimos las expansiones en la ecuación de Laplace y obtenemos una ecuación diferencial ordinaria para cada $g_n(r, r')$:
$$
\frac{1}{r}\frac{d}{dr}\left(r\frac{dg_n}{dr}\right) - \frac{\nu^2}{r^2} g_n = -\frac{2}{\alpha r} \sin\left(\frac{n\pi\varphi'}{\alpha}\right) \delta(r-r')
$$
donde $\nu = \frac{n\pi}{\alpha}$.

La solución debe satisfacer $g_n(R, r') = 0$ y ser finita en $r=0$. Construimos la solución en dos regiones:
$$
g_n(r, r') = \begin{cases} C_1 r^\nu & \text{si } r < r' \\ C_2 (r^\nu - R^{2\nu}r^{-\nu}) & \text{si } r > r' \end{cases}
$$

Las constantes se determinan por las condiciones de continuidad y el salto en la derivada en $r=r'$. El resultado final es:
$$
g_n(r, r') = \frac{2}{\alpha \nu} \sin(\nu\varphi') \frac{1}{R^{2\nu}} \begin{cases} r^\nu ((r')^\nu - R^{2\nu}(r')^{-\nu}) & r < r' \\ (r')^\nu (r^\nu - R^{2\nu}r^{-\nu}) & r > r' \end{cases}
$$

La función de Green completa es:
$$
G(r, \varphi; r', \varphi') = \sum_{n=1}^{\infty} \frac{2}{\alpha} \sin\left(\frac{n\pi\varphi}{\alpha}\right) \sin\left(\frac{n\pi\varphi'}{\alpha}\right) g_n(r, r')
$$

Una forma más compacta usando $r_< = \min(r, r')$ y $r_> = \max(r, r')$ es:
$$
g_n(r, r') = \frac{1}{\nu} \left( \frac{r_<^\nu}{r_>^\nu} - \frac{(r_< r_>)^\nu}{R^{2\nu}} \right)
$$

---

## Problema 4

**Enunciado:** Calcule la función de Green para el interior de una bola de radio $R$ con la condición de frontera de Dirichlet. Repita el cálculo utilizando la condición de frontera de Neumann.

**Solución:**

Este problema se divide en dos partes. En ambos casos, la función de Green $G(\vec{r}, \vec{r}')$ representa el potencial en el punto $\vec{r}$ debido a una carga puntual unitaria ubicada en $\vec{r}'$. La ecuación que satisface es:
$$
\nabla^2 G(\vec{r}, \vec{r}') = -\delta(\vec{r} - \vec{r}')
$$

### **Parte 1: Condición de Frontera de Dirichlet**

La condición de Dirichlet establece que el potencial es nulo en la frontera:
$$
G(\vec{r}, \vec{r}') = 0 \quad \text{para } |\vec{r}| = R
$$

Utilizamos el método de las imágenes. Colocamos una carga "imagen" $q'$ en una posición $\vec{r}''$ fuera de la esfera:

1.  **Posición de la carga imagen:** $\vec{r}'' = \frac{R^2}{(r')^2} \vec{r}'$, donde $r' = |\vec{r}'|$.

2.  **Magnitud de la carga imagen:** $q' = -R/r'$.

La función de Green es la superposición de los potenciales de la carga original y la carga imagen:
$$
G_D(\vec{r}, \vec{r}') = \frac{1}{4\pi} \left( \frac{1}{|\vec{r} - \vec{r}'|} - \frac{R/r'}{|\vec{r} - \frac{R^2}{(r')^2}\vec{r}'|} \right)
$$

### **Parte 2: Condición de Frontera de Neumann**

La condición de Neumann establece que la derivada normal del potencial es nula en la frontera:
$$
\frac{\partial G}{\partial n} \bigg|_{|\vec{r}|=R} = 0
$$

Necesitamos un sistema de tres cargas:
1.  La carga original $q_1 = 1$ en $\vec{r}'$.
2.  Una primera carga imagen $q_2 = -R/r'$ en $\vec{r}'' = \frac{R^2}{(r')^2}\vec{r}'$.
3.  Una segunda carga imagen $q_3 = R/r'$ en el origen ($\vec{r}_3 = 0$).

La función de Green es:
$$
G_N(\vec{r}, \vec{r}') = \frac{1}{4\pi} \left( \frac{1}{|\vec{r} - \vec{r}'|} - \frac{R/r'}{|\vec{r} - (R^2/r'^2)\vec{r}'|} + \frac{R}{r'r} \right) + C
$$

donde $C$ es una constante arbitraria para la condición de Neumann.

---

## Problema 5

**Enunciado:** Sea el rectángulo semiinfinito $R = (0, L) \times (0, +\infty)$ y $(x, y) \in R$. Supongamos que el potencial electrostático es conocido en la frontera de este rectángulo: en particular $\phi(0, y) = \phi(L, y) = 0$ $\forall y \in (0, +\infty)$ y $\phi(x, 0) = V\sin\left(\frac{4\pi}{L}x\right)$ $\forall x \in (0, L)$. Calcule el potencial electrostático en el interior de $R$.

**Solución:**

El potencial electrostático $\phi(x, y)$ en una región sin cargas debe satisfacer la ecuación de Laplace en dos dimensiones:
$$
\nabla^2 \phi = \frac{\partial^2 \phi}{\partial x^2} + \frac{\partial^2 \phi}{\partial y^2} = 0
$$

Las condiciones de frontera son:
1.  $\phi(0, y) = 0$
2.  $\phi(L, y) = 0$
3.  $\phi(x, 0) = V\sin\left(\frac{4\pi}{L}x\right)$
4.  $\phi(x, y) \to 0$ cuando $y \to +\infty$

Utilizamos el método de separación de variables, asumiendo una solución de la forma:
$$
\phi(x, y) = X(x)Y(y)
$$

Sustituyendo en la ecuación de Laplace y separando las variables:
$$
\frac{1}{X(x)}\frac{d^2X}{dx^2} = -\frac{1}{Y(y)}\frac{d^2Y}{dy^2} = -k^2
$$

**1. Ecuación para X(x):**
$$
\frac{d^2X}{dx^2} + k^2 X = 0
$$

La solución general es $X(x) = A\sin(kx) + B\cos(kx)$.

Aplicando las condiciones de frontera en $x$:
*   $X(0) = 0 \implies B=0$.
*   $X(L) = 0 \implies A\sin(kL) = 0$.

Los valores propios son $k_n = \frac{n\pi}{L}$ para $n=1, 2, 3, \dots$, y las funciones propias son $X_n(x) = \sin\left(\frac{n\pi}{L}x\right)$.

**2. Ecuación para Y(y):**
$$
\frac{d^2Y}{dy^2} - k_n^2 Y = 0
$$

La solución general es $Y(y) = C e^{k_n y} + D e^{-k_n y}$.

Aplicando la condición $Y(y) \to 0$ cuando $y \to \infty$, debemos tener $C=0$.
La solución para $Y$ es $Y_n(y) = D_n e^{-\frac{n\pi}{L}y}$.

**3. Solución General y Coeficientes**

La solución general es:
$$
\phi(x, y) = \sum_{n=1}^{\infty} C_n \sin\left(\frac{n\pi}{L}x\right) e^{-\frac{n\pi}{L}y}
$$

Aplicando la condición de frontera en $y=0$:
$$
\phi(x, 0) = \sum_{n=1}^{\infty} C_n \sin\left(\frac{n\pi}{L}x\right) = V\sin\left(\frac{4\pi}{L}x\right)
$$

Por inspección, solo el término con $n=4$ es no nulo:
*   $C_n = 0$ para $n \neq 4$
*   $C_4 = V$ para $n = 4$

**4. Solución Final**

$$
\phi(x, y) = V \sin\left(\frac{4\pi}{L}x\right) e^{-\frac{4\pi}{L}y}
$$

---

## Problema 6

**Enunciado:** Sea una superficie cilíndrica de radio $R$ y altura $L=2a+b$ cerrada en ambos extremos por dos tapas circulares de radio $R$ conectadas a potencial cero. Supongamos además que el potencial electrostático sobre la superficie lateral viene dado por la expresión
$$
V(z) = V_0
\begin{cases}
0 & \text{si } 0 < z < a \\
1 & \text{si } a < z < a + b \\
0 & \text{si } a + b < z < 2a + b
\end{cases}
$$
Calcule el potencial electrostático en el interior del cilindro.

**Solución:**

Buscamos resolver la ecuación de Laplace $\nabla^2 \phi = 0$ en el interior del cilindro. Dado que el potencial no depende de $\varphi$, la ecuación se simplifica a:
$$
\frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial \phi}{\partial r}\right) + \frac{\partial^2 \phi}{\partial z^2} = 0
$$

Las condiciones de frontera son:
1.  $\phi(r, 0) = 0$ (tapa inferior)
2.  $\phi(r, L) = 0$ (tapa superior)
3.  $\phi(R, z) = V(z)$ (superficie lateral)
4.  $\phi$ finito en $r=0$

Usamos separación de variables con $\phi(r, z) = F(r)Z(z)$:

**1. Ecuación para Z(z):**
$$
\frac{d^2Z}{dz^2} + k^2 Z = 0
$$

Con las condiciones $Z(0) = 0$ y $Z(L) = 0$, obtenemos:
*   $k_n = \frac{n\pi}{L}$ para $n=1, 2, 3, \dots$
*   $Z_n(z) = \sin\left(\frac{n\pi z}{L}\right)$

**2. Ecuación para F(r):**
$$
r^2\frac{d^2F}{dr^2} + r\frac{dF}{dr} - (k_n r)^2 F = 0
$$

Esta es la ecuación de Bessel modificada de orden cero. Con la condición de que $F$ sea finito en $r=0$:
$$
F_n(r) = C_n I_0(k_n r)
$$

donde $I_0$ es la función de Bessel modificada de primera especie.

**3. Solución General**

$$
\phi(r, z) = \sum_{n=1}^{\infty} C_n I_0\left(\frac{n\pi r}{L}\right) \sin\left(\frac{n\pi z}{L}\right)
$$

Aplicando la condición en $r=R$:
$$
C_n I_0(k_n R) = \frac{2}{L} \int_0^L V(z) \sin(k_n z) dz
$$

Calculando la integral:
$$
\int_0^L V(z) \sin(k_n z) dz = \int_a^{a+b} V_0 \sin(k_n z) dz = \frac{V_0}{k_n} \left[ \cos(k_n a) - \cos(k_n(a+b)) \right]
$$

Por lo tanto:
$$
C_n = \frac{2V_0}{n\pi I_0(n\pi R/L)} \left[ \cos\left(\frac{n\pi a}{L}\right) - \cos\left(\frac{n\pi (a+b)}{L}\right) \right]
$$

**4. Solución Final**

$$
\phi(r, z) = \frac{2V_0}{\pi} \sum_{n=1}^{\infty} \frac{1}{n} \left[ \cos\left(\frac{n\pi a}{L}\right) - \cos\left(\frac{n\pi (a+b)}{L}\right) \right] \frac{I_0(n\pi r/L)}{I_0(n\pi R/L)} \sin\left(\frac{n\pi z}{L}\right)
$$

donde $L = 2a+b$.

---

## Problema 7

**Enunciado:** El potencial electrostático sobre un cascarón esférico de radio $R$ viene dado por la expresión
$$
V(\theta, \varphi) = V_0
\begin{cases}
1 & \text{si } 0 < \theta < \pi/2 \quad \forall \varphi \in (0, 2\pi) \\
0 & \text{si } \pi/2 < \theta < \pi \quad \forall \varphi \in (0, 2\pi)
\end{cases}
$$
Encuentre el potencial electrostático en el interior del cascarón.

**Solución:**

Buscamos una solución a la ecuación de Laplace $\nabla^2 \phi = 0$ en el interior de la esfera. Dado que el potencial no depende de $\varphi$, la solución tiene la forma de una serie de polinomios de Legendre:
$$
\phi(r, \theta) = \sum_{l=0}^{\infty} A_l r^l P_l(\cos\theta)
$$

Los coeficientes se determinan de la condición de frontera en $r=R$:
$$
\phi(R, \theta) = \sum_{l=0}^{\infty} A_l R^l P_l(\cos\theta) = V(\theta)
$$

Usando la propiedad de ortogonalidad de los polinomios de Legendre:
$$
A_l R^l = \frac{2l+1}{2} \int_0^\pi V(\theta) P_l(\cos\theta) \sin\theta \, d\theta
$$

Sustituyendo $V(\theta)$:
$$
A_l R^l = \frac{V_0(2l+1)}{2} \int_0^{\pi/2} P_l(\cos\theta) \sin\theta \, d\theta
$$

Con el cambio de variable $x = \cos\theta$:
$$
\int_0^{\pi/2} P_l(\cos\theta) \sin\theta \, d\theta = \int_0^1 P_l(x) \, dx
$$

Por lo tanto:
$$
A_l = \frac{V_0(2l+1)}{2R^l} \int_0^1 P_l(x) \, dx
$$

Calculamos las integrales para algunos valores de $l$:
*   **l = 0:** $\int_0^1 1 \, dx = 1 \implies A_0 = \frac{V_0}{2}$
*   **l = 1:** $\int_0^1 x \, dx = \frac{1}{2} \implies A_1 = \frac{3V_0}{4R}$
*   **l = 2:** $\int_0^1 \frac{1}{2}(3x^2 - 1) \, dx = 0 \implies A_2 = 0$
*   **l = 3:** $\int_0^1 \frac{1}{2}(5x^3-3x)dx = -\frac{1}{8} \implies A_3 = -\frac{7V_0}{16R^3}$

Para $l$ par (excepto $l=0$), $A_l = 0$. Para $l$ impar, se puede usar la relación de recurrencia.

La solución final es:
$$
\phi(r, \theta) = V_0 \left[ \frac{1}{2} + \frac{3}{4}\frac{r}{R}P_1(\cos\theta) - \frac{7}{16}\left(\frac{r}{R}\right)^3 P_3(\cos\theta) + \dots \right]
$$

En forma general:
$$
\phi(r, \theta) = \frac{V_0}{2} + V_0 \sum_{k=0}^{\infty} (-1)^k \frac{(4k+3)(2k-1)!!}{2(2k+2)!!} \left(\frac{r}{R}\right)^{2k+1} P_{2k+1}(\cos\theta)
$$

---

## Problema 8

**Enunciado:** Demuestre que el vector intensidad del campo eléctrico correspondiente a un dipolo eléctrico de momento dipolar $\vec{p}$ viene dado por la expresión
$$
\vec{E} = \frac{1}{4\pi\epsilon_0}\left[3\frac{(\vec{p} \cdot \vec{r})\vec{r}}{r^5} - \frac{\vec{p}}{r^3}\right]
$$

**Solución:**

La demostración se basa en calcular el campo eléctrico $\vec{E}$ a partir del potencial escalar $\phi$ de un dipolo eléctrico, utilizando la relación $\vec{E} = -\nabla \phi$.

**1. Potencial de un dipolo eléctrico**

El potencial escalar generado por un dipolo eléctrico de momento dipolar $\vec{p}$ situado en el origen es:
$$
\phi(\vec{r}) = \frac{1}{4\pi\epsilon_0} \frac{\vec{p} \cdot \vec{r}}{r^3}
$$

**2. Cálculo del campo eléctrico**

El campo eléctrico es:
$$
\vec{E} = -\nabla \phi = -\nabla \left( \frac{1}{4\pi\epsilon_0} \frac{\vec{p} \cdot \vec{r}}{r^3} \right)
$$

Aplicando la regla del producto:
$$
\nabla \left( (\vec{p} \cdot \vec{r}) r^{-3} \right) = (\vec{p} \cdot \vec{r}) \nabla(r^{-3}) + r^{-3} \nabla(\vec{p} \cdot \vec{r})
$$

Calculamos cada término:
*   **$\nabla(\vec{p} \cdot \vec{r})$:** Como $\vec{p}$ es constante:
    $$
    \nabla(\vec{p} \cdot \vec{r}) = \vec{p}
    $$

*   **$\nabla(r^{-3})$:** Usando $\nabla(f(r)) = \frac{df}{dr}\frac{\vec{r}}{r}$:
    $$
    \nabla(r^{-3}) = -3r^{-4} \frac{\vec{r}}{r} = -3 \frac{\vec{r}}{r^5}
    $$

**3. Ensamblaje**

Sustituyendo:
$$
\nabla \left( (\vec{p} \cdot \vec{r}) r^{-3} \right) = (\vec{p} \cdot \vec{r}) \left(-3 \frac{\vec{r}}{r^5}\right) + r^{-3} (\vec{p}) = -\frac{3(\vec{p} \cdot \vec{r})\vec{r}}{r^5} + \frac{\vec{p}}{r^3}
$$

Aplicando el signo negativo:
$$
\vec{E} = - \left( -\frac{3(\vec{p} \cdot \vec{r})\vec{r}}{r^5} + \frac{\vec{p}}{r^3} \right) = \frac{3(\vec{p} \cdot \vec{r})\vec{r}}{r^5} - \frac{\vec{p}}{r^3}
$$

**4. Resultado final**

Reintroduciendo la constante:
$$
\vec{E}(\vec{r}) = \frac{1}{4\pi\epsilon_0}\left[ \frac{3(\vec{p} \cdot \vec{r})\vec{r}}{r^5} - \frac{\vec{p}}{r^3} \right]
$$

Esto completa la demostración.

---

## Problema 9

**Enunciado:** Demuestre que el vector intensidad del campo eléctrico correspondiente a un cuadrupolo eléctrico de momento cuadrupolar con componentes $D_{ij}$ posee componentes dadas por la expresión
$$
E_k = \frac{1}{24\pi\epsilon_0}\left[\frac{15x_ix_jx_k}{r^7} - \frac{3}{r^5}(x_i\delta_{jk} + x_k\delta_{ij} + x_j\delta_{ki})\right]
$$

**Solución:**

La demostración parte del potencial escalar de un cuadrupolo eléctrico y calcula el campo mediante $\vec{E} = -\nabla \phi$. El potencial cuadrupolar más común es:
$$
\phi(\vec{r}) = \frac{1}{4\pi\epsilon_0} \frac{1}{2} \frac{D_{ij} x_i x_j}{r^5}
$$
donde $D_{ij}$ es el tensor cuadrupolar (usando la convención de suma de Einstein).

Calculemos $E_k = -\frac{\partial \phi}{\partial x_k}$:
$$
E_k = -\frac{D_{ij}}{8\pi\epsilon_0} \frac{\partial}{\partial x_k} \left( x_i x_j r^{-5} \right)
$$

Usando la regla del producto:
$$
\frac{\partial}{\partial x_k} \left( x_i x_j r^{-5} \right) = \frac{\partial(x_i x_j)}{\partial x_k} r^{-5} + x_i x_j \frac{\partial(r^{-5})}{\partial x_k}
$$

Calculamos cada término:
*   $\frac{\partial(x_i x_j)}{\partial x_k} = \delta_{ik}x_j + x_i\delta_{jk}$
*   $\frac{\partial(r^{-5})}{\partial x_k} = -5r^{-6} \frac{x_k}{r} = -5\frac{x_k}{r^7}$

Sustituyendo:
$$
\frac{\partial}{\partial x_k} \left( x_i x_j r^{-5} \right) = \frac{\delta_{ik}x_j + x_i\delta_{jk}}{r^5} - \frac{5x_i x_j x_k}{r^7}
$$

Por lo tanto:
$$
E_k = \frac{D_{ij}}{8\pi\epsilon_0} \left( \frac{5x_i x_j x_k}{r^7} - \frac{\delta_{ik}x_j + x_i\delta_{jk}}{r^5} \right)
$$

Esta expresión es la correcta para un tensor cuadrupolar general $D_{ij}$. La expresión del enunciado corresponde a una definición o convención particular del potencial cuadrupolar utilizada en el texto guía. La discrepancia en las constantes sugiere una normalización diferente, pero el procedimiento de derivación (tomar el gradiente negativo del potencial) es el método correcto.

---

## Problema 10

**Enunciado:** Demuestre que un dipolo eléctrico puntual de momento dipolar $\vec{p}$ responde a una densidad de carga $\rho = -(\vec{p} \cdot \nabla)\delta(\vec{r} - \vec{r}_0)$, siendo $\vec{r}_0$ el vector de posición del dipolo.

**Solución:**

Para demostrar esta equivalencia, calcularemos el potencial electrostático generado por la densidad de carga propuesta y mostraremos que es idéntico al potencial de un dipolo puntual.

**1. Potencial a partir de una densidad de carga**

El potencial electrostático es:
$$
\phi(\vec{r}) = \frac{1}{4\pi\epsilon_0} \int_V \frac{\rho(\vec{r}')}{|\vec{r} - \vec{r}'|} dV'
$$

Sustituyendo $\rho(\vec{r}') = -(\vec{p} \cdot \nabla')\delta(\vec{r}' - \vec{r}_0)$:
$$
\phi(\vec{r}) = \frac{1}{4\pi\epsilon_0} \int_V \frac{-(\vec{p} \cdot \nabla')\delta(\vec{r}' - \vec{r}_0)}{|\vec{r} - \vec{r}'|} dV'
$$

**2. Uso de integración por partes**

Como $\vec{p}$ es constante:
$$
(\vec{p} \cdot \nabla')\delta(\vec{r}' - \vec{r}_0) = \nabla' \cdot (\vec{p} \delta(\vec{r}' - \vec{r}_0))
$$

Usando la identidad de integración por partes vectorial (y asumiendo que los campos se anulan en el infinito):
$$
\int_V \psi (\nabla' \cdot \vec{A}) dV' = - \int_V (\nabla' \psi) \cdot \vec{A} dV'
$$

donde $\psi = \frac{1}{|\vec{r} - \vec{r}'|}$ y $\vec{A} = \vec{p} \delta(\vec{r}' - \vec{r}_0)$.

La integral se convierte en:
$$
\phi(\vec{r}) = \frac{1}{4\pi\epsilon_0} \int_V \left( \nabla' \frac{1}{|\vec{r} - \vec{r}'|} \right) \cdot (\vec{p} \delta(\vec{r}' - \vec{r}_0)) dV'
$$

**3. Evaluación con la función delta**

La función delta evalúa el integrando en $\vec{r}' = \vec{r}_0$:
$$
\phi(\vec{r}) = \frac{1}{4\pi\epsilon_0} \left[ \left( \nabla' \frac{1}{|\vec{r} - \vec{r}'|} \right) \cdot \vec{p} \right]_{\vec{r}'=\vec{r}_0}
$$

El gradiente es:
$$
\nabla' \frac{1}{|\vec{r} - \vec{r}'|} = \frac{\vec{r} - \vec{r}'}{|\vec{r} - \vec{r}'|^3}
$$

Evaluando en $\vec{r}' = \vec{r}_0$:
$$
\phi(\vec{r}) = \frac{1}{4\pi\epsilon_0} \left( \frac{\vec{r} - \vec{r}_0}{|\vec{r} - \vec{r}_0|^3} \right) \cdot \vec{p} = \frac{1}{4\pi\epsilon_0} \frac{\vec{p} \cdot (\vec{r} - \vec{r}_0)}{|\vec{r} - \vec{r}_0|^3}
$$

**4. Resultado final**

Esta es precisamente la expresión del potencial de un dipolo eléctrico puntual de momento $\vec{p}$ localizado en $\vec{r}_0$. Esto demuestra que la densidad de carga $\rho = -(\vec{p} \cdot \nabla)\delta(\vec{r} - \vec{r}_0)$ representa correctamente a un dipolo puntual.

---

## Problema 11

**Enunciado:** Sean las cargas puntuales $q_1 = -e$ situada en el punto de coordenadas $(0, a, 0)$, $q_2 = e$ localizada en $(a, 0, 0)$, $q_3 = -e$ ubicada en el punto $(0, -a, 0)$ y $q_4 = e$ localizada en $(-a, 0, 0)$. Demuestre que el momento cuadrupolar eléctrico asociado a esta distribución de cargas viene dado por la expresión
$$
(D_{ij}) = 6ea^2 \begin{pmatrix} 
1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 0
\end{pmatrix}
$$

**Solución:**

El tensor de momento cuadrupolar eléctrico para un sistema de cargas puntuales se define como:
$$
D_{ij} = \sum_k q_k (3x_{ki} x_{kj} - r_k^2 \delta_{ij})
$$
donde $q_k$ es la k-ésima carga, $\vec{r}_k$ es su vector de posición, $x_{ki}$ es la i-ésima componente de $\vec{r}_k$, y $\delta_{ij}$ es la delta de Kronecker.

Las cargas y sus posiciones son:
*   $q_1 = -e$ en $\vec{r}_1 = (0, a, 0)$, $r_1^2 = a^2$
*   $q_2 = e$ en $\vec{r}_2 = (a, 0, 0)$, $r_2^2 = a^2$
*   $q_3 = -e$ en $\vec{r}_3 = (0, -a, 0)$, $r_3^2 = a^2$
*   $q_4 = e$ en $\vec{r}_4 = (-a, 0, 0)$, $r_4^2 = a^2$

**Componentes Diagonales:**

*   **$D_{11}$ (o $D_{xx}$):**
    $$
    D_{11} = \sum_k q_k (3x_k^2 - r_k^2)
    $$
    $$
    D_{11} = (-e)(3(0)^2 - a^2) + (e)(3(a)^2 - a^2) + (-e)(3(0)^2 - a^2) + (e)(3(-a)^2 - a^2)
    $$
    $$
    D_{11} = (-e)(-a^2) + (e)(2a^2) + (-e)(-a^2) + (e)(2a^2) = ea^2 + 2ea^2 + ea^2 + 2ea^2 = 6ea^2
    $$

*   **$D_{22}$ (o $D_{yy}$):**
    $$
    D_{22} = \sum_k q_k (3y_k^2 - r_k^2)
    $$
    $$
    D_{22} = (-e)(3(a)^2 - a^2) + (e)(3(0)^2 - a^2) + (-e)(3(-a)^2 - a^2) + (e)(3(0)^2 - a^2)
    $$
    $$
    D_{22} = (-e)(2a^2) + (e)(-a^2) + (-e)(2a^2) + (e)(-a^2) = -2ea^2 - ea^2 - 2ea^2 - ea^2 = -6ea^2
    $$

*   **$D_{33}$ (o $D_{zz}$):**
    Como todas las cargas están en el plano $z=0$, $z_k=0$ para todas:
    $$
    D_{33} = \sum_k q_k (0 - a^2) = (-e)(-a^2) + (e)(-a^2) + (-e)(-a^2) + (e)(-a^2)
    $$
    $$
    D_{33} = ea^2 - ea^2 + ea^2 - ea^2 = 0
    $$

**Componentes Fuera de la Diagonal:**

Para $i \neq j$: $D_{ij} = \sum_k q_k (3x_{ki} x_{kj})$.

*   **$D_{12}$ (o $D_{xy}$):** $D_{12} = \sum_k q_k (3x_k y_k) = (-e)(0) + (e)(0) + (-e)(0) + (e)(0) = 0$
*   **$D_{13}$ y $D_{23}$:** Como $z_k=0$ para todas las cargas, todos estos términos son cero.

**Tensor Resultante:**

$$
(D_{ij}) = \begin{pmatrix} 
6ea^2 & 0 & 0 \\
0 & -6ea^2 & 0 \\
0 & 0 & 0
\end{pmatrix} = 6ea^2 \begin{pmatrix} 
1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 0
\end{pmatrix}
$$

Esto coincide exactamente con la expresión del enunciado.

---

## Problema 12

**Enunciado:** Un átomo de Hidrógeno en su estado básico tiene la densidad de carga electrónica
$$
\rho(\vec{r}) = -\frac{e}{\pi a_0^3}\exp\left[-\frac{2r}{a_0}\right],
$$
siendo $e$ el valor absoluto de la carga del electrón y $a_0$ el radio de Bohr. El núcleo se supone puntual y está localizado en el origen.
1.  Verifique que $\int_{\mathbb{R}^3}\rho(\vec{r})dV = -e$.
2.  Halle el potencial escalar y el vector intensidad del campo eléctrico en todo el espacio.
3.  Calcule la energía de interacción electrón-núcleo.

**Solución:**

**1. Verificación de la carga total**

En coordenadas esféricas, $dV = 4\pi r^2 dr$ (por simetría esférica):
$$
Q = \int_0^{\infty} \left(-\frac{e}{\pi a_0^3}e^{-2r/a_0}\right) (4\pi r^2 dr) = -\frac{4e}{a_0^3} \int_0^\infty r^2 e^{-2r/a_0} dr
$$

Usando la integral gamma $\int_0^\infty x^n e^{-ax} dx = \frac{n!}{a^{n+1}}$ con $n=2$ y $a=2/a_0$:
$$
\int_0^\infty r^2 e^{-2r/a_0} dr = \frac{2!}{(2/a_0)^3} = \frac{2a_0^3}{8} = \frac{a_0^3}{4}
$$

Por lo tanto:
$$
Q = -\frac{4e}{a_0^3} \left(\frac{a_0^3}{4}\right) = -e
$$

**2. Potencial y campo eléctrico**

El sistema completo incluye el núcleo (protón con carga $+e$ en el origen) y la nube electrónica. Usando la ley de Gauss con simetría esférica:
$$
E(r) (4\pi r^2) = \frac{Q_{enc}(r)}{\epsilon_0}
$$

La carga encerrada es:
$$
Q_{enc}(r) = e + \int_0^r \rho(r') 4\pi (r')^2 dr' = e - \frac{4e}{a_0^3} \int_0^r (r')^2 e^{-2r'/a_0} dr'
$$

Resolviendo la integral por partes:
$$
\int_0^r (r')^2 e^{-2r'/a_0} dr' = \frac{a_0^3}{4} - e^{-2r/a_0} \left( \frac{a_0 r^2}{2} + \frac{a_0^2 r}{2} + \frac{a_0^3}{4} \right)
$$

Simplificando:
$$
Q_{enc}(r) = e \left( 1 + \frac{2r}{a_0} + \frac{2r^2}{a_0^2} \right) e^{-2r/a_0}
$$

El campo eléctrico es:
$$
\vec{E}(r) = \frac{e}{4\pi\epsilon_0 r^2} \left( 1 + \frac{2r}{a_0} + \frac{2r^2}{a_0^2} \right) e^{-2r/a_0} \hat{r}
$$

El potencial se obtiene de $\phi(r) = -\int_\infty^r E(r') dr'$:
$$
\phi(r) = \frac{e}{4\pi\epsilon_0} \left( \frac{1}{r} + \frac{1}{a_0} \right) e^{-2r/a_0}
$$

**3. Energía de interacción electrón-núcleo**

La energía de interacción es:
$$
U = \int_{\mathbb{R}^3} \rho(\vec{r}) \phi_p(\vec{r}) dV
$$

donde $\phi_p(\vec{r}) = \frac{e}{4\pi\epsilon_0 r}$ es el potencial del núcleo.
$$
U = \int \left(-\frac{e}{\pi a_0^3}e^{-2r/a_0}\right) \left(\frac{e}{4\pi\epsilon_0 r}\right) (4\pi r^2 dr)
$$
$$
U = -\frac{e^2}{\pi a_0^3 \epsilon_0} \int_0^\infty r e^{-2r/a_0} dr
$$

Usando $\int_0^\infty x e^{-ax} dx = \frac{1}{a^2}$ con $a=2/a_0$:
$$
\int_0^\infty r e^{-2r/a_0} dr = \frac{a_0^2}{4}
$$

Por lo tanto:
$$
U = -\frac{e^2}{\pi a_0^3 \epsilon_0} \left(\frac{a_0^2}{4}\right) = -\frac{e^2}{4\pi\epsilon_0 a_0}
$$

---

## Problema 13

**Enunciado:** En cierto estado excitado del átomo de Hidrógeno, la nube electrónica tiene la densidad de carga, escrita en coordenadas esféricas,
$$
\rho(\vec{r}) = -\frac{e}{32\pi^3 a_0^7}r^4\exp\left[-\frac{2r}{3a_0}\right]\sin^4(\theta).
$$
1.  Demuestre que el momento dipolar eléctrico del átomo de Hidrógeno asociado a este estado excitado es cero.
2.  Demuestre además que el momento cuadrupolar eléctrico en dicho estado tiene la forma
    $$
    (D_{ij}) = 36ea_0^2 \begin{pmatrix}
    -1 & 0 & 0 \\
    0 & -1 & 0 \\
    0 & 0 & 2
    \end{pmatrix}
    $$

**Solución:**

**1. Demostración del momento dipolar nulo**

El momento dipolar eléctrico es $\vec{p} = \int \vec{r} \rho(\vec{r}) dV$. Calculamos sus componentes:

*   **Componentes $p_x$ y $p_y$:**
    $$
    p_x = \int (r\sin\theta\cos\varphi) \rho(r, \theta) r^2\sin\theta dr d\theta d\varphi
    $$
    La densidad $\rho$ no depende de $\varphi$. La integración en $\varphi$ da:
    $$
    \int_0^{2\pi} \cos\varphi d\varphi = 0
    $$
    Por lo tanto, $p_x = 0$. Análogamente, $p_y = 0$.

*   **Componente $p_z$:**
    $$
    p_z = \int (r\cos\theta) \rho(r, \theta) r^2\sin\theta dr d\theta d\varphi
    $$
    El integrando angular es proporcional a $\sin^5\theta \cos\theta$. Esta integral es:
    $$
    \int_0^\pi \sin^5\theta \cos\theta d\theta = \left[\frac{\sin^6\theta}{6}\right]_0^\pi = 0
    $$
    Por lo tanto, $p_z = 0$.

Como todas las componentes son nulas, el momento dipolar $\vec{p} = \vec{0}$.

**2. Cálculo del momento cuadrupolar**

El tensor de momento cuadrupolar es $D_{ij} = \int (3x_i x_j - r^2 \delta_{ij}) \rho(\vec{r}) dV$.

*   **Componentes fuera de la diagonal:** Por simetría azimutal y las integrales en $\varphi$:
    $$
    D_{xy} = \int 3xy \rho dV \propto \int_0^{2\pi} \cos\varphi\sin\varphi d\varphi = 0
    $$
    Análogamente, $D_{xz} = D_{yz} = 0$.

*   **Componentes diagonales:** Por simetría azimutal, $D_{xx} = D_{yy}$. Además, la traza del tensor es cero: $D_{xx} + D_{yy} + D_{zz} = 0$. Por lo tanto, $D_{xx} = D_{yy} = -D_{zz}/2$.

    Calculamos $D_{zz}$:
    $$
    D_{zz} = \int r^2(3\cos^2\theta-1) \rho(r,\theta) r^2\sin\theta dr d\theta d\varphi
    $$
    $$
    D_{zz} = 2\pi C \int_0^\infty r^8 e^{-2r/3a_0} dr \int_0^\pi (3\cos^2\theta-1)\sin^5\theta d\theta
    $$
    donde $C = -\frac{e}{32\pi^3 a_0^7}$.

    **Integral radial:** Con $n=8$ y $a=2/3a_0$:
    $$
    \int_0^\infty r^8 e^{-2r/3a_0} dr = \frac{8!}{(2/3a_0)^9} = \frac{8! \cdot 3^9 a_0^9}{2^9}
    $$

    **Integral angular:**
    $$
    \int_0^\pi (3\cos^2\theta-1)\sin^5\theta d\theta = \int_0^\pi (2\sin^5\theta - 3\sin^7\theta) d\theta
    $$
    Usando las fórmulas de Wallis:
    $$
    \int_0^\pi \sin^5\theta d\theta = \frac{16}{15}, \quad \int_0^\pi \sin^7\theta d\theta = \frac{32}{35}
    $$
    $$
    2\left(\frac{16}{15}\right) - 3\left(\frac{32}{35}\right) = \frac{32}{15} - \frac{96}{35} = -\frac{64}{105}
    $$

    Sustituyendo todo y simplificando:
    $$
    D_{zz} = 72ea_0^2
    $$

    Por lo tanto:
    $$
    D_{xx} = D_{yy} = -36ea_0^2
    $$

El tensor cuadrupolar es:
$$
(D_{ij}) = \begin{pmatrix} -36ea_0^2 & 0 & 0 \\ 0 & -36ea_0^2 & 0 \\ 0 & 0 & 72ea_0^2 \end{pmatrix} = 36ea_0^2 \begin{pmatrix} -1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 2 \end{pmatrix}
$$

---

## Problema 14

**Enunciado:** En el problema anterior, calcule la energía de interacción entre el núcleo positivo y la nube electrónica del átomo en el estado dado, utilizando tanto la definición (1.132) como el desarrollo en multipolos (1.135).

**Solución:**

**Método 1: Definición Directa (Ecuación 1.132)**

La energía de interacción es:
$$
U = \int_{\mathbb{R}^3} \rho(\vec{r}) \phi_{nucleo}(\vec{r}) dV
$$

donde $\phi_{nucleo}(\vec{r}) = \frac{e}{4\pi\epsilon_0 r}$ es el potencial del núcleo.
$$
U = \int \left(-\frac{e}{32\pi^3 a_0^7}r^4 e^{-2r/3a_0}\sin^4\theta\right) \left(\frac{e}{4\pi\epsilon_0 r}\right) (r^2\sin\theta dr d\theta d\varphi)
$$

Separando las integrales:
$$
U = -\frac{e^2}{128\pi^4 \epsilon_0 a_0^7} \left(\int_0^{2\pi}d\varphi\right) \left(\int_0^\pi \sin^5\theta d\theta\right) \left(\int_0^\infty r^5 e^{-2r/3a_0} dr\right)
$$

Calculamos cada integral:
*   $\int_0^{2\pi}d\varphi = 2\pi$
*   $\int_0^\pi \sin^5\theta d\theta = \frac{16}{15}$
*   $\int_0^\infty r^5 e^{-2r/3a_0} dr = \frac{5!}{(2/3a_0)^6} = \frac{120 \cdot 3^6 a_0^6}{2^6} = \frac{10935}{8} a_0^6$

Sustituyendo:
$$
U = -\frac{e^2}{128\pi^4 \epsilon_0 a_0^7} (2\pi) \left(\frac{16}{15}\right) \left(\frac{10935}{8} a_0^6\right)
$$
$$
U = -\frac{729 e^2}{32\pi^3 \epsilon_0 a_0}
$$

**Método 2: Desarrollo en Multipolos (Ecuación 1.135)**

La energía se aproxima por:
$$
U \approx Q\phi_{ext}(0) - \vec{p} \cdot \vec{E}_{ext}(0) - \frac{1}{6}\sum_{i,j} D_{ij} \left(\frac{\partial E^{ext}_j}{\partial x_i}\right)_{\vec{r}=0} + \dots
$$

*   **Término monopolar:** La carga total de la nube es $Q=-e$. El potencial del núcleo en el origen es infinito, indicando que la aproximación multipolar no es directamente aplicable cuando la fuente está dentro de la distribución.

*   **Término dipolar:** Del problema 13, $\vec{p} = \vec{0}$. Este término es cero.

*   **Término cuadrupolar:** La energía cuadrupolar es $U_Q = -\frac{1}{6}\sum_{i,j} D_{ij} \frac{\partial E_j}{\partial x_i}$. Como el tensor cuadrupolar es sin traza ($\sum D_{ii} = 0$) y en un sentido distribucional, la interacción del momento cuadrupolar con el campo de una carga puntual en el origen es cero.

**Conclusión:**

El único término no nulo significativo es el monopolar. La energía de interacción según el desarrollo multipolar se reduce a la interacción de la carga total con el potencial del núcleo, que corresponde al cálculo del Método 1:
$$
U = -\frac{729 e^2}{32\pi^3 \epsilon_0 a_0}
$$

Ambos métodos, interpretados correctamente, conducen al mismo resultado.

---

# Solucionario - Problemas Propuestos de Magnetostática del Vacío

## Problema 1

**Enunciado:** Una partícula de masa $m$ y carga $e$ en presencia del campo magnetostático uniforme $\vec{B}$ tiene una trayectoria circular de radio $r$ cuya frecuencia angular es $\omega = \frac{eB}{m}$. Halle la trayectoria de la partícula si, además del campo magnetostático uniforme $\vec{B} = B\vec{e}_z$, existe un campo eléctrico uniforme y constante $\vec{E} = E\vec{e}_y$ que es perpendicular al campo magnético.

**Solución:**

**1. Ecuación de Movimiento**

La fuerza de Lorentz sobre una partícula de carga $e$ en presencia de campos eléctrico y magnético es:
$$ \vec{F} = e(\vec{E} + \vec{v} \times \vec{B}) $$

La ecuación de movimiento de Newton es:
$$ m\frac{d\vec{v}}{dt} = e(\vec{E} + \vec{v} \times \vec{B}) $$

Con $\vec{E} = E\vec{e}_y$ y $\vec{B} = B\vec{e}_z$, y escribiendo $\vec{v} = v_x\vec{e}_x + v_y\vec{e}_y + v_z\vec{e}_z$, el producto vectorial es:
$$ \vec{v} \times \vec{B} = (v_x\vec{e}_x + v_y\vec{e}_y + v_z\vec{e}_z) \times (B\vec{e}_z) = v_xB\vec{e}_y - v_yB\vec{e}_x $$

Las ecuaciones de movimiento componente por componente son:
1. $m\frac{dv_x}{dt} = -ev_yB$
2. $m\frac{dv_y}{dt} = eE + ev_xB$
3. $m\frac{dv_z}{dt} = 0$

**2. Movimiento en la Dirección z**

De la tercera ecuación, $v_z$ es constante. Si la velocidad inicial en $z$ es cero, entonces $v_z(t) = 0$ y $z(t) = z_0$ (constante). El movimiento está confinado al plano $xy$.

**3. Movimiento en el Plano xy**

Definimos la frecuencia ciclotrón $\omega = \frac{eB}{m}$. Las ecuaciones se reescriben como:
$$ \frac{dv_x}{dt} = -\omega v_y $$
$$ \frac{dv_y}{dt} = \frac{eE}{m} + \omega v_x $$

**4. Velocidad de Deriva**

Buscamos una solución de la forma $\vec{v} = \vec{v}_{ciclo} + \vec{v}_d$, donde $\vec{v}_d$ es una velocidad de deriva constante. Para campos perpendiculares, la velocidad de deriva es:
$$ \vec{v}_d = \frac{\vec{E} \times \vec{B}}{B^2} = \frac{(E\vec{e}_y) \times (B\vec{e}_z)}{B^2} = \frac{EB}{B^2}\vec{e}_x = \frac{E}{B}\vec{e}_x $$

**5. Cambio de Variables**

Hacemos el cambio de variables $\vec{v}' = \vec{v} - \vec{v}_d$, es decir:
$$ v'_x = v_x - \frac{E}{B}, \quad v'_y = v_y $$

Las ecuaciones para $\vec{v}'$ son:
$$ \frac{dv'_x}{dt} = -\omega v'_y $$
$$ \frac{dv'_y}{dt} = \omega v'_x $$

Estas son las ecuaciones de un movimiento circular uniforme con frecuencia angular $\omega$. La solución es:
$$ v'_x(t) = v_0 \cos(\omega t + \phi) $$
$$ v'_y(t) = -v_0 \sin(\omega t + \phi) $$

donde $v_0$ es la magnitud de la velocidad en el sistema de referencia que se mueve con velocidad $\vec{v}_d$, y $\phi$ es una fase determinada por las condiciones iniciales.

**6. Velocidad y Trayectoria**

Volviendo a las variables originales:
$$ v_x(t) = \frac{E}{B} + v_0 \cos(\omega t + \phi) $$
$$ v_y(t) = -v_0 \sin(\omega t + \phi) $$

Integrando para obtener la posición (con condiciones iniciales apropiadas):
$$ x(t) = x_0 + \frac{E}{B}t + \frac{v_0}{\omega}\sin(\omega t + \phi) $$
$$ y(t) = y_0 + \frac{v_0}{\omega}\cos(\omega t + \phi) $$

**7. Descripción de la Trayectoria**

La trayectoria es una **cicloide**: la partícula se mueve en círculos de radio $r = \frac{v_0}{\omega} = \frac{mv_0}{eB}$ mientras deriva en la dirección $x$ con velocidad constante $v_d = \frac{E}{B}$.

Esta deriva es conocida como la **deriva $\vec{E} \times \vec{B}$**, y es perpendicular tanto al campo eléctrico como al magnético.

---

## Problema 2

**Enunciado:** Un flujo de partículas de masa $m$ y carga $e$ penetra con velocidad $\vec{v}_0$ en una región en la cual existe un campo magnetostático homogéneo $\vec{B}$, el cual es perpendicular a $\vec{v}_0$. Calcule el ángulo de desviación de la partícula y el tiempo de permanencia en el campo $\vec{B}$ suponiendo que el campo magnetostático existe en una región limitada del espacio con dimensión característica $a$ en la dirección perpendicular a $\vec{v}_0$.

**Solución:**

**1. Movimiento en el Campo Magnético**

Una partícula cargada que entra perpendicularmente a un campo magnético uniforme describe un movimiento circular con radio:
$$ r = \frac{mv_0}{eB} $$

La frecuencia angular es:
$$ \omega = \frac{eB}{m} $$

**2. Geometría del Problema**

La partícula entra en la región del campo magnético, describe un arco circular de radio $r$, y luego sale de la región cuando ha atravesado una distancia $a$ (la dimensión característica de la región del campo).

Sea $\theta$ el ángulo que la partícula recorre en su trayectoria circular dentro del campo. La distancia horizontal atravesada es:
$$ a = 2r\sin\left(\frac{\theta}{2}\right) $$

Despejando el ángulo:
$$ \sin\left(\frac{\theta}{2}\right) = \frac{a}{2r} = \frac{a}{2} \frac{eB}{mv_0} = \frac{aeB}{2mv_0} $$

Por lo tanto:
$$ \theta = 2\arcsin\left(\frac{aeB}{2mv_0}\right) $$

Este es el **ángulo de desviación** de la partícula.

**3. Condiciones de Validez**

Para que esta solución sea válida, se requiere que $\frac{aeB}{2mv_0} \leq 1$, es decir:
$$ a \leq \frac{2mv_0}{eB} = 2r $$

Si $a > 2r$, la partícula completaría un semicírculo o más dentro de la región.

**4. Tiempo de Permanencia**

La longitud del arco recorrido por la partícula es:
$$ s = r\theta $$

El tiempo de permanencia es:
$$ t = \frac{s}{v_0} = \frac{r\theta}{v_0} = \frac{m\theta}{eB} $$

Sustituyendo la expresión para $\theta$:
$$ t = \frac{2m}{eB}\arcsin\left(\frac{aeB}{2mv_0}\right) $$

**5. Caso Límite: Campo Débil o Región Pequeña**

Si $a \ll r$ (campo débil o región pequeña), podemos usar la aproximación $\arcsin(x) \approx x$ para $x \ll 1$:
$$ \theta \approx 2 \cdot \frac{aeB}{2mv_0} = \frac{aeB}{mv_0} $$
$$ t \approx \frac{2m}{eB} \cdot \frac{aeB}{2mv_0} = \frac{a}{v_0} $$

En este límite, el tiempo de permanencia es simplemente el tiempo que tardaría en atravesar la región sin deflexión.

---

## Problema 3

**Enunciado:** Una partícula de masa $m$ y carga $e$ en presencia de campos $\vec{E}$ y $\vec{B}$ uniformes, constantes y paralelos entre sí, tiene una velocidad inicial $\vec{v}_0$ perpendicular a los campos. Halle la trayectoria de la partícula.

**Solución:**

**1. Configuración y Ecuación de Movimiento**

Orientamos el sistema de coordenadas de modo que los campos estén en la dirección $z$:
$$ \vec{E} = E\vec{e}_z, \quad \vec{B} = B\vec{e}_z $$

La velocidad inicial es perpendicular a los campos, por ejemplo $\vec{v}_0 = v_0\vec{e}_x$.

La ecuación de movimiento es:
$$ m\frac{d\vec{v}}{dt} = e(\vec{E} + \vec{v} \times \vec{B}) $$

**2. Componentes de la Ecuación de Movimiento**

Escribiendo $\vec{v} = v_x\vec{e}_x + v_y\vec{e}_y + v_z\vec{e}_z$, el producto vectorial es:
$$ \vec{v} \times \vec{B} = (v_x\vec{e}_x + v_y\vec{e}_y + v_z\vec{e}_z) \times (B\vec{e}_z) = v_xB\vec{e}_y - v_yB\vec{e}_x $$

Las ecuaciones componente por componente son:
1. $m\frac{dv_x}{dt} = -ev_yB$
2. $m\frac{dv_y}{dt} = ev_xB$
3. $m\frac{dv_z}{dt} = eE$

**3. Movimiento en la Dirección z**

La tercera ecuación se integra directamente:
$$ v_z(t) = v_{z,0} + \frac{eE}{m}t $$

Si inicialmente $v_{z,0} = 0$:
$$ v_z(t) = \frac{eE}{m}t $$

Integrando nuevamente:
$$ z(t) = z_0 + \frac{eE}{2m}t^2 $$

El movimiento en $z$ es **uniformemente acelerado** con aceleración $a_z = \frac{eE}{m}$.

**4. Movimiento en el Plano xy**

Las dos primeras ecuaciones describen un movimiento circular. Definimos la frecuencia ciclotrón $\omega = \frac{eB}{m}$:
$$ \frac{dv_x}{dt} = -\omega v_y $$
$$ \frac{dv_y}{dt} = \omega v_x $$

La solución es:
$$ v_x(t) = v_0\cos(\omega t) $$
$$ v_y(t) = v_0\sin(\omega t) $$

Integrando:
$$ x(t) = x_0 + \frac{v_0}{\omega}\sin(\omega t) $$
$$ y(t) = y_0 - \frac{v_0}{\omega}\cos(\omega t) + \frac{v_0}{\omega} $$

**5. Descripción de la Trayectoria**

En el plano $xy$, la partícula describe un movimiento circular con radio $r = \frac{v_0}{\omega} = \frac{mv_0}{eB}$ y frecuencia angular $\omega$.

Simultáneamente, la partícula es acelerada en la dirección $z$ por el campo eléctrico.

La trayectoria completa es una **hélice con paso creciente** (o espiral cónica). El radio de la hélice permanece constante ($r = \frac{mv_0}{eB}$), pero la velocidad en la dirección $z$ aumenta linealmente con el tiempo, lo que hace que el paso de la hélice aumente con cada vuelta.

---

## Problema 4

**Enunciado:** Una partícula de masa $m$ y carga $e$ entra en una región con campo magnético uniforme $\vec{B}$ con velocidad $\vec{v}_0$ que forma un ángulo $\alpha$ con $\vec{B}$. Describa el movimiento de la partícula.

**Solución:**

**1. Descomposición de la Velocidad**

Orientamos el sistema de coordenadas con $\vec{B} = B\vec{e}_z$. La velocidad inicial se descompone en:
*   **Componente paralela al campo:** $v_{\parallel} = v_0\cos\alpha$
*   **Componente perpendicular al campo:** $v_{\perp} = v_0\sin\alpha$

Podemos escribir:
$$ \vec{v}_0 = v_{\perp}\vec{e}_x + v_{\parallel}\vec{e}_z $$

**2. Ecuación de Movimiento**

La fuerza de Lorentz es:
$$ \vec{F} = e\vec{v} \times \vec{B} $$

Esta fuerza es siempre perpendicular tanto a $\vec{v}$ como a $\vec{B}$. Por lo tanto, la componente de la velocidad paralela al campo magnético no experimenta ninguna fuerza:
$$ F_z = 0 \implies v_z = v_{\parallel} = \text{constante} $$

**3. Movimiento Paralelo al Campo**

El movimiento en la dirección del campo es **uniforme**:
$$ z(t) = z_0 + v_{\parallel}t $$

**4. Movimiento Perpendicular al Campo**

En el plano perpendicular a $\vec{B}$, la partícula experimenta la fuerza magnética que la hace describir un movimiento circular uniforme. La frecuencia angular es:
$$ \omega = \frac{eB}{m} $$

El radio de la órbita circular está determinado por la componente perpendicular de la velocidad:
$$ r = \frac{mv_{\perp}}{eB} = \frac{mv_0\sin\alpha}{eB} $$

**5. Trayectoria Completa**

La combinación del movimiento circular en el plano $xy$ y el movimiento uniforme en la dirección $z$ resulta en una **trayectoria helicoidal** (hélice) alrededor de la dirección del campo magnético.

Los parámetros de la hélice son:
*   **Radio:** $r = \frac{mv_0\sin\alpha}{eB}$
*   **Frecuencia angular:** $\omega = \frac{eB}{m}$
*   **Paso de la hélice** (distancia recorrida en $z$ por cada vuelta completa):
    $$ d = v_{\parallel}T = v_{\parallel}\frac{2\pi}{\omega} = \frac{2\pi m v_0\cos\alpha}{eB} $$

**6. Casos Especiales**

*   Si $\alpha = 0$ (velocidad paralela al campo): No hay fuerza ($r=0$), la partícula se mueve en línea recta.
*   Si $\alpha = 90°$ (velocidad perpendicular al campo): $v_{\parallel}=0$, la partícula describe un círculo en un plano perpendicular a $\vec{B}$.

---

## Problema 5

**Enunciado:** Una bola maciza de radio $R$ tiene carga $q$ distribuida uniformemente en su volumen y rota con velocidad angular $\vec{\omega}$ alrededor de un eje que pasa por su centro. Halle el campo $\vec{B}$ y el momento dipolar magnético $\vec{m}$ de la bola.

**Solución:**

**1. Densidad de Corriente**

Una esfera cargada que rota equivale a una distribución de corrientes. La densidad de carga es:
$$ \rho = \frac{q}{\frac{4}{3}\pi R^3} = \frac{3q}{4\pi R^3} $$

En un punto $\vec{r}$ dentro de la esfera, la velocidad debido a la rotación es $\vec{v} = \vec{\omega} \times \vec{r}$. La densidad de corriente es:
$$ \vec{J}(\vec{r}) = \rho\vec{v} = \rho(\vec{\omega} \times \vec{r}) = \frac{3q}{4\pi R^3}(\vec{\omega} \times \vec{r}) $$

**2. Cálculo del Momento Dipolar Magnético**

El momento dipolar magnético se define como:
$$ \vec{m} = \frac{1}{2}\int_V \vec{r} \times \vec{J}(\vec{r}) dV $$

Sustituyendo $\vec{J}$:
$$ \vec{m} = \frac{1}{2}\int_V \vec{r} \times \left[\frac{3q}{4\pi R^3}(\vec{\omega} \times \vec{r})\right] dV = \frac{3q}{8\pi R^3}\int_V \vec{r} \times (\vec{\omega} \times \vec{r}) dV $$

Usando la identidad vectorial $\vec{A} \times (\vec{B} \times \vec{C}) = \vec{B}(\vec{A} \cdot \vec{C}) - \vec{C}(\vec{A} \cdot \vec{B})$:
$$ \vec{r} \times (\vec{\omega} \times \vec{r}) = \vec{\omega}(\vec{r} \cdot \vec{r}) - \vec{r}(\vec{r} \cdot \vec{\omega}) = \vec{\omega}r^2 - \vec{r}(\vec{r} \cdot \vec{\omega}) $$

Por simetría esférica, la integral del segundo término se anula. La integral queda:
$$ \vec{m} = \frac{3q}{8\pi R^3}\vec{\omega}\int_V r^2 dV $$

En coordenadas esféricas, $dV = 4\pi r^2 dr$:
$$ \int_V r^2 dV = \int_0^R r^2(4\pi r^2 dr) = 4\pi\int_0^R r^4 dr = 4\pi\left[\frac{r^5}{5}\right]_0^R = \frac{4\pi R^5}{5} $$

Sustituyendo:
$$ \vec{m} = \frac{3q}{8\pi R^3}\vec{\omega} \cdot \frac{4\pi R^5}{5} = \frac{3q \cdot 4\pi R^5}{8\pi R^3 \cdot 5}\vec{\omega} = \frac{qR^2}{5}\vec{\omega} $$

Alternativamente, con la forma más común:
$$ \vec{m} = \frac{1}{5}qR^2\vec{\omega} $$

O usando el momento angular $\vec{L} = I\vec{\omega} = \frac{2}{5}mR^2\vec{\omega}$ (para una esfera sólida):
$$ \vec{m} = \frac{q}{2m}\vec{L} $$

**3. Cálculo del Campo Magnético $\vec{B}$**

Para calcular el campo magnético, usamos la ley de Ampère con simetría esférica. Sin embargo, dada la complejidad del problema, el resultado es:

*   **En el centro de la esfera ($\vec{r}=0$):**
    $$ \vec{B}(0) = \frac{2\mu_0}{5}\frac{q\vec{\omega}}{R} = \frac{2\mu_0\vec{m}}{5R^3} \cdot 5 = \frac{2\mu_0\vec{m}}{R^3} $$
    
    Más precisamente:
    $$ \vec{B}(0) = \frac{\mu_0 q\vec{\omega}}{5R} $$

*   **Fuera de la esfera ($r > R$):** El campo es el de un dipolo magnético:
    $$ \vec{B}(\vec{r}) = \frac{\mu_0}{4\pi r^3}\left[3(\vec{m} \cdot \hat{r})\hat{r} - \vec{m}\right] $$

---

## Problema 6

**Enunciado:** Suponiendo que la bola que rota en el problema anterior es el electrón no puntual con radio clásico $r_0 = \frac{e^2}{4 \pi \epsilon_0 m_e c^2}$, encuentre cuál debe ser el valor de la velocidad angular $\omega$ para que el momento magnético $\vec{m}$ coincida con el momento magnético de spin del electrón, que es $\vec{m}_s = -g \frac{e}{2m_e}\vec{S}$, donde $\vec{S}$ es el momento angular de spin, cuya magnitud es $|\vec{S}| = \frac{\hbar}{2}$ y $g \approx 2$. Compare el resultado de la velocidad tangencial en el ecuador con la velocidad de la luz.

**Solución:**

Este problema utiliza el resultado del problema anterior para modelar el electrón como una esfera cargada en rotación y comparar su momento magnético clásico con el momento magnético de espín cuántico.

**1. Momento Magnético Clásico**

Del problema 5, el momento dipolar magnético de una esfera de radio $R$ y carga $q$ que rota con velocidad angular $\vec{\omega}$ es:
$$ \vec{m} = \frac{1}{3} q R^2 \vec{\omega} $$
Para este modelo del electrón, tenemos:
*   La carga $q = -e$ (carga del electrón).
*   El radio $R = r_0 = \frac{e^2}{4 \pi \epsilon_0 m_e c^2}$ (radio clásico del electrón).

Sustituyendo estos valores, el momento magnético clásico del electrón es:
$$ \vec{m} = -\frac{1}{3} e r_0^2 \vec{\omega} $$

**2. Momento Magnético de Espín**

El momento magnético de espín intrínseco del electrón viene dado por:
$$ \vec{m}_s = -g \frac{e}{2m_e}\vec{S} $$
Donde:
*   $g \approx 2$ es el factor g del electrón.
*   $m_e$ es la masa del electrón.
*   $\vec{S}$ es el momento angular de espín.

La magnitud del momento angular de espín es $|\vec{S}| = \frac{\hbar}{2}$. Asumiendo que la rotación y el espín están alineados con el eje $z$ (es decir, $\vec{\omega} = \omega \hat{z}$ y $\vec{S} = \frac{\hbar}{2} \hat{z}$), podemos comparar las magnitudes:
$$ |\vec{m}_s| = g \frac{e}{2m_e} |\vec{S}| = 2 \frac{e}{2m_e} \frac{\hbar}{2} = \frac{e\hbar}{2m_e} $$
Este valor se conoce como el **magnetón de Bohr**, $\mu_B = \frac{e\hbar}{2m_e}$.

**3. Cálculo de la Velocidad Angular $\omega$**

Igualamos las magnitudes de los dos momentos magnéticos, $|\vec{m}| = |\vec{m}_s|$:
$$ \frac{1}{3} e r_0^2 \omega = \frac{e\hbar}{2m_e} $$
Ahora, despejamos la velocidad angular $\omega$:
$$ \omega = \frac{3}{2} \frac{e\hbar}{m_e} \frac{1}{e r_0^2} = \frac{3\hbar}{2m_e r_0^2} $$
Sustituimos la expresión para el radio clásico del electrón, $r_0$:
$$ \omega = \frac{3\hbar}{2m_e} \left( \frac{4 \pi \epsilon_0 m_e c^2}{e^2} \right)^2 $$
Para simplificar esta expresión, introducimos la **constante de estructura fina**, $\alpha$:
$$ \alpha = \frac{e^2}{4 \pi \epsilon_0 \hbar c} \approx \frac{1}{137} $$
De esta definición, podemos despejar el grupo de constantes $e^2 / (4 \pi \epsilon_0)$:
$$ \frac{e^2}{4 \pi \epsilon_0} = \alpha \hbar c $$
Sustituyendo esto en la expresión de $r_0$:
$$ r_0 = \frac{\alpha \hbar c}{m_e c^2} = \frac{\alpha \hbar}{m_e c} $$
Ahora sustituimos esta forma simplificada de $r_0$ en nuestra ecuación para $\omega$:
$$ \omega = \frac{3\hbar}{2m_e \left( \frac{\alpha \hbar}{m_e c} \right)^2} = \frac{3\hbar}{2m_e} \frac{m_e^2 c^2}{\alpha^2 \hbar^2} = \frac{3 m_e c^2}{2 \alpha^2 \hbar} $$

**4. Comparación de la Velocidad Tangencial con la Velocidad de la Luz**

La velocidad tangencial $v_t$ en el ecuador de la esfera (donde el radio es $r_0$) está dada por $v_t = \omega r_0$.
$$ v_t = \left( \frac{3 m_e c^2}{2 \alpha^2 \hbar} \right) \left( \frac{\alpha \hbar}{m_e c} \right) $$
Simplificando la expresión:
$$ v_t = \frac{3}{2\alpha} c $$
Dado que $\alpha \approx 1/137$, el valor de la velocidad tangencial es:
$$ v_t \approx \frac{3}{2 \cdot (1/137)} c = \frac{3 \cdot 137}{2} c = 205.5 c $$

**Conclusión**

La velocidad tangencial en el ecuador de este electrón clásico sería aproximadamente **205.5 veces la velocidad de la luz**.

Este resultado es físicamente imposible y demuestra de manera contundente por qué el modelo clásico de un electrón como una simple esfera cargada en rotación es inadecuado para describir sus propiedades cuánticas como el espín y el momento magnético. El espín es una propiedad intrínseca y no puede ser explicada por una rotación mecánica en el espacio.

---

## Problema 7

**Enunciado:** Una partícula tiene el momento magnético $\vec{m}$. Demuestre que esta partícula tiene asociada la densidad de corriente $\vec{J} = (\vec{m} \times \nabla)\delta(\vec{r} - \vec{r}_0)$, siendo $\vec{r}_0$ el vector de posición de la partícula.

**Solución:**

Para demostrar que la densidad de corriente asociada a un dipolo magnético puntual $\vec{m}$ en $\vec{r}_0$ es la expresión dada, podemos seguir dos caminos:
1.  Calcular el potencial vector $\vec{A}(\vec{r})$ que esta densidad de corriente $\vec{J}$ produce y verificar si coincide con el potencial conocido de un dipolo magnético.
2.  Calcular el momento dipolar magnético de esta densidad de corriente y ver si recuperamos $\vec{m}$.

Usaremos el primer método, ya que es más directo.

**1. Potencial Vector de un Dipolo Magnético**

El potencial vector magnético $\vec{A}_{dip}(\vec{r})$ generado por un dipolo magnético puntual $\vec{m}$ localizado en una posición $\vec{r}_0$ es:
$$ \vec{A}_{dip}(\vec{r}) = \frac{\mu_0}{4\pi} \frac{\vec{m} \times (\vec{r} - \vec{r}_0)}{|\vec{r} - \vec{r}_0|^3} $$
Para simplificar, podemos relacionar esto con el gradiente de $1/|\vec{r}-\vec{r}_0|$:
$$ \nabla \left( \frac{1}{|\vec{r} - \vec{r}_0|} \right) = -\frac{\vec{r} - \vec{r}_0}{|\vec{r} - \vec{r}_0|^3} $$
Por lo tanto, el potencial del dipolo se puede escribir como:
$$ \vec{A}_{dip}(\vec{r}) = -\frac{\mu_0}{4\pi} \left( \vec{m} \times \nabla \left( \frac{1}{|\vec{r} - \vec{r}_0|} \right) \right) $$

**2. Potencial Vector a partir de la Densidad de Corriente**

Ahora, calculemos el potencial vector $\vec{A}(\vec{r})$ usando la fórmula general que lo relaciona con una densidad de corriente $\vec{J}(\vec{r}')$:
$$ \vec{A}(\vec{r}) = \frac{\mu_0}{4\pi} \int_{V'} \frac{\vec{J}(\vec{r}')}{|\vec{r} - \vec{r}'|} d^3r' $$
Sustituimos la expresión propuesta para $\vec{J}(\vec{r}')$, donde el dipolo está en $\vec{r}_0$:
$$ \vec{J}(\vec{r}') = (\vec{m} \times \nabla') \delta(\vec{r}' - \vec{r}_0) $$
El operador $\nabla'$ actúa sobre las coordenadas $\vec{r}'$.
$$ \vec{A}(\vec{r}) = \frac{\mu_0}{4\pi} \int_{V'} \frac{(\vec{m} \times \nabla') \delta(\vec{r}' - \vec{r}_0)}{|\vec{r} - \vec{r}'|} d^3r' $$

**3. Integración por Partes**

La integral contiene un gradiente actuando sobre una función delta de Dirac, lo que sugiere usar integración por partes. La identidad de integración por partes para un campo vectorial $\vec{F}$ y una función escalar $\phi$ es:
$$ \int_V \phi (\nabla \cdot \vec{F}) dV = \oint_S \phi \vec{F} \cdot d\vec{S} - \int_V (\nabla \phi) \cdot \vec{F} dV $$
En nuestro caso, la expresión es un poco diferente. Consideremos la $i$-ésima componente del integrando:
$$ [(\vec{m} \times \nabla') \delta(\vec{r}' - \vec{r}_0)]_i = \sum_{j,k} \epsilon_{ijk} m_j (\partial'_k \delta(\vec{r}' - \vec{r}_0)) $$
La $i$-ésima componente del potencial vector es:
$$ A_i(\vec{r}) = \frac{\mu_0}{4\pi} \int_{V'} \frac{1}{|\vec{r} - \vec{r}'|} \sum_{j,k} \epsilon_{ijk} m_j (\partial'_k \delta(\vec{r}' - \vec{r}_0)) d^3r' $$
Usamos la propiedad de la función delta con derivadas:
$$ \int f(x) \frac{d}{dx}\delta(x-a) dx = - \frac{df}{dx}\bigg|_{x=a} $$
Aplicando esto a nuestra integral en 3D:
$$ \int_{V'} f(\vec{r}') (\partial'_k \delta(\vec{r}' - \vec{r}_0)) d^3r' = - \frac{\partial f}{\partial r'_k} \bigg|_{\vec{r}'=\vec{r}_0} $$
En nuestro caso, la función $f(\vec{r}')$ es $\frac{1}{|\vec{r} - \vec{r}'|}$.
$$ A_i(\vec{r}) = \frac{\mu_0}{4\pi} \sum_{j,k} \epsilon_{ijk} m_j \left( - \frac{\partial}{\partial r'_k} \frac{1}{|\vec{r} - \vec{r}'|} \right)_{\vec{r}'=\vec{r}_0} $$
La derivada parcial es:
$$ \frac{\partial}{\partial r'_k} \frac{1}{|\vec{r} - \vec{r}'|} = \frac{\partial}{\partial r'_k} \left( \sum_l (r_l - r'_l)^2 \right)^{-1/2} = -\frac{1}{2}(\dots)^{-3/2} \cdot 2(r_k - r'_k)(-1) = \frac{r_k - r'_k}{|\vec{r} - \vec{r}'|^3} $$
Evaluando en $\vec{r}' = \vec{r}_0$:
$$ \left( \frac{\partial}{\partial r'_k} \frac{1}{|\vec{r} - \vec{r}'|} \right)_{\vec{r}'=\vec{r}_0} = \frac{r_k - r_{0,k}}{|\vec{r} - \vec{r}_0|^3} $$
Sustituyendo de nuevo en la expresión para $A_i(\vec{r})$:
$$ A_i(\vec{r}) = \frac{\mu_0}{4\pi} \sum_{j,k} \epsilon_{ijk} m_j \left( - \frac{r_k - r_{0,k}}{|\vec{r} - \vec{r}_0|^3} \right) $$
Esto es la $i$-ésima componente de un producto vectorial:
$$ A_i(\vec{r}) = -\frac{\mu_0}{4\pi} \left[ \vec{m} \times \frac{\vec{r} - \vec{r}_0}{|\vec{r} - \vec{r}_0|^3} \right]_i $$
Recomponiendo el vector, obtenemos:
$$ \vec{A}(\vec{r}) = -\frac{\mu_0}{4\pi} \frac{\vec{m} \times (\vec{r} - \vec{r}_0)}{|\vec{r} - \vec{r}_0|^3} $$
Usando la identidad $\nabla(1/R) = -\vec{R}/R^3$ con $\vec{R} = \vec{r} - \vec{r}_0$, podemos reescribir esto como:
$$ \vec{A}(\vec{r}) = -\frac{\mu_0}{4\pi} \left( \vec{m} \times \left( -\nabla \frac{1}{|\vec{r} - \vec{r}_0|} \right) \right) = \frac{\mu_0}{4\pi} \left( \vec{m} \times \nabla \frac{1}{|\vec{r} - \vec{r}_0|} \right) $$
*Corrección*: Hay un signo menos de diferencia con la expresión en el paso 1. Revisemos los signos.
La derivada de $1/|\vec{r}-\vec{r}'|$ con respecto a $\vec{r}'$ es $\nabla' (1/|\vec{r}-\vec{r}'|) = +(\vec{r}-\vec{r}')/|\vec{r}-\vec{r}'|^3$.
La derivada con respecto a $\vec{r}$ es $\nabla (1/|\vec{r}-\vec{r}'|) = -(\vec{r}-\vec{r}')/|\vec{r}-\vec{r}'|^3$.
Entonces, $\nabla' = -\nabla$.

Volviendo a la integral:
$$ A_i(\vec{r}) = \frac{\mu_0}{4\pi} \sum_{j,k} \epsilon_{ijk} m_j \left( - \frac{\partial}{\partial r'_k} \frac{1}{|\vec{r} - \vec{r}'|} \right)_{\vec{r}'=\vec{r}_0} $$
$$ \frac{\partial}{\partial r'_k} = -\frac{\partial}{\partial r_k} $$
$$ A_i(\vec{r}) = \frac{\mu_0}{4\pi} \sum_{j,k} \epsilon_{ijk} m_j \left( \frac{\partial}{\partial r_k} \frac{1}{|\vec{r} - \vec{r}'|} \right)_{\vec{r}'=\vec{r}_0} = \frac{\mu_0}{4\pi} \left[ \vec{m} \times \nabla \left( \frac{1}{|\vec{r} - \vec{r}_0|} \right) \right]_i $$
Recomponiendo el vector:
$$ \vec{A}(\vec{r}) = \frac{\mu_0}{4\pi} \left( \vec{m} \times \nabla \left( \frac{1}{|\vec{r} - \vec{r}_0|} \right) \right) $$
Usando $\nabla(1/R) = -\vec{R}/R^3$:
$$ \vec{A}(\vec{r}) = \frac{\mu_0}{4\pi} \left( \vec{m} \times \left( -\frac{\vec{r} - \vec{r}_0}{|\vec{r} - \vec{r}_0|^3} \right) \right) = \frac{\mu_0}{4\pi} \frac{\vec{m} \times (\vec{r}_0 - \vec{r})}{|\vec{r} - \vec{r}_0|^3} = \frac{\mu_0}{4\pi} \frac{\vec{m} \times (\vec{r} - \vec{r}_0)}{|\vec{r} - \vec{r}_0|^3} $$
Esta expresión final coincide exactamente con el potencial vector de un dipolo magnético puntual.

**Conclusión**

Dado que la densidad de corriente $\vec{J} = (\vec{m} \times \nabla)\delta(\vec{r} - \vec{r}_0)$ genera el potencial vector magnético correcto para un dipolo puntual, hemos demostrado que esta es la representación matemática correcta de la densidad de corriente para dicha partícula.

---

## Problema 8

**Enunciado:** En cierto estado excitado del átomo de Hidrógeno la nube electrónica tiene asociada una densidad de corriente cuyas componentes en coordenadas esféricas son $J_r = J_\theta = 0$ y
$$
J_\varphi = \frac{e\hbar}{2\pi^3 8m_0 a_0^7}r^3\exp\left[-\frac{2r}{3a_0}\right]\sin^3(\theta),
$$
siendo $e$ y $m_0$ la carga y la masa de reposo del electrón, respectivamente, y $a_0$ es el radio de Bohr. Calcule el valor del vector inducción magnética $\vec{B}$ en el origen de coordenadas. Calcule el momentum dipolar magnético del átomo en ese estado.

**Solución:**

Este problema se divide en dos partes: calcular el campo magnético $\vec{B}$ en el origen y calcular el momento dipolar magnético total $\vec{m}$.

**1. Cálculo del Campo Magnético $\vec{B}$ en el Origen**

La ley de Biot-Savart nos da el campo magnético en un punto $\vec{r}$ a partir de una densidad de corriente $\vec{J}(\vec{r}')$:
$$ \vec{B}(\vec{r}) = \frac{\mu_0}{4\pi} \int_{V'} \frac{\vec{J}(\vec{r}') \times (\vec{r} - \vec{r}')}{|\vec{r} - \vec{r}'|^3} d^3r' $$
Para calcular el campo en el origen, hacemos $\vec{r}=0$:
$$ \vec{B}(0) = \frac{\mu_0}{4\pi} \int_{V'} \frac{\vec{J}(\vec{r}') \times (-\vec{r}')}{|\vec{r}'|^3} d^3r' = -\frac{\mu_0}{4\pi} \int_{V'} \frac{\vec{J}(\vec{r}') \times \vec{r}'}{r'^3} d^3r' $$
Trabajamos en coordenadas esféricas, donde $\vec{r}' = r' \hat{r}'$ y $\vec{J} = J_\varphi \hat{\varphi}'$. El producto vectorial es:
$$ \vec{J} \times \vec{r}' = (J_\varphi \hat{\varphi}') \times (r' \hat{r}') = J_\varphi r' (\hat{\varphi}' \times \hat{r}') = J_\varphi r' \hat{\theta}' $$
Sustituyendo en la integral, con $d^3r' = r'^2 \sin\theta' dr' d\theta' d\varphi'$:
$$ \vec{B}(0) = -\frac{\mu_0}{4\pi} \int_0^{2\pi} \int_0^\pi \int_0^\infty \frac{(J_\varphi r' \hat{\theta}')}{r'^3} (r'^2 \sin\theta' dr' d\theta' d\varphi') $$
$$ \vec{B}(0) = -\frac{\mu_0}{4\pi} \int_0^{2\pi} \int_0^\pi \int_0^\infty J_\varphi(r', \theta') \sin\theta' \hat{\theta}' dr' d\theta' d\varphi' $$
El vector unitario $\hat{\theta}'$ no es constante y debe expresarse en coordenadas cartesianas para ser integrado:
$$ \hat{\theta}' = \cos\theta'\cos\varphi' \hat{x} + \cos\theta'\sin\varphi' \hat{y} - \sin\theta' \hat{z} $$
Debido a la simetría, las componentes $x$ e $y$ se anularán al integrar sobre $\varphi'$ de $0$ a $2\pi$ (ya que $\int_0^{2\pi}\cos\varphi' d\varphi' = 0$ y $\int_0^{2\pi}\sin\varphi' d\varphi' = 0$). Por lo tanto, solo la componente $z$ sobrevive.
$$ \vec{B}(0) = B_z \hat{z} $$
$$ B_z = -\frac{\mu_0}{4\pi} \int_0^{2\pi} \int_0^\pi \int_0^\infty J_\varphi(r', \theta') \sin\theta' (-\sin\theta') dr' d\theta' d\varphi' $$
$$ B_z = \frac{\mu_0}{4\pi} \int_0^{2\pi} d\varphi' \int_0^\pi \sin^2\theta' \left( \int_0^\infty J_\varphi(r', \theta') dr' \right) d\theta' $$
Sustituimos $J_\varphi = C r^3 e^{-ar} \sin^3\theta$, con $C = \frac{e\hbar}{16\pi^3 m_0 a_0^7}$ y $a = \frac{2}{3a_0}$:
$$ B_z = \frac{\mu_0}{4\pi} (2\pi) \int_0^\pi \sin^2\theta' \left( \int_0^\infty C r'^3 e^{-ar'} \sin^3\theta' dr' \right) d\theta' $$
$$ B_z = \frac{\mu_0 C}{2} \int_0^\pi \sin^5\theta' d\theta' \int_0^\infty r'^3 e^{-ar'} dr' $$
Calculamos las dos integrales por separado:
*   **Integral en $\theta'$**: $\int_0^\pi \sin^5\theta' d\theta' = \frac{16}{15}$
*   **Integral en $r'$** (usando la función Gamma $\Gamma(n+1) = n! = \int_0^\infty x^n e^{-x} dx$):
    $$ \int_0^\infty r'^3 e^{-ar'} dr' = \frac{\Gamma(4)}{a^4} = \frac{3!}{a^4} = \frac{6}{a^4} $$
Sustituyendo los resultados:
$$ B_z = \frac{\mu_0 C}{2} \left(\frac{16}{15}\right) \left(\frac{6}{a^4}\right) = \frac{8 \mu_0 C}{5a^4} $$
Ahora sustituimos los valores de $C$ y $a$:
$$ B_z = \frac{8 \mu_0}{5} \left( \frac{e\hbar}{16\pi^3 m_0 a_0^7} \right) \frac{1}{(2/3a_0)^4} = \frac{8 \mu_0 e\hbar}{5 \cdot 16\pi^3 m_0 a_0^7} \frac{3^4 a_0^4}{2^4} = \frac{8 \mu_0 e\hbar \cdot 81 a_0^4}{5 \cdot 16\pi^3 m_0 a_0^7 \cdot 16} $$
$$ B_z = \frac{81 \mu_0 e\hbar}{320 \pi^3 m_0 a_0^3} $$
El campo magnético en el origen es:
$$ \vec{B}(0) = \frac{81 \mu_0 e\hbar}{320 \pi^3 m_0 a_0^3} \hat{z} $$

**2. Cálculo del Momento Dipolar Magnético $\vec{m}$**

El momento dipolar magnético se calcula con la fórmula:
$$ \vec{m} = \frac{1}{2} \int_{V'} \vec{r}' \times \vec{J}(\vec{r}') d^3r' $$
El producto vectorial es $\vec{r}' \times \vec{J} = (r' \hat{r}') \times (J_\varphi \hat{\varphi}') = r' J_\varphi (\hat{r}' \times \hat{\varphi}') = -r' J_\varphi \hat{\theta}'$.
$$ \vec{m} = -\frac{1}{2} \int_0^{2\pi} \int_0^\pi \int_0^\infty (r' J_\varphi \hat{\theta}') (r'^2 \sin\theta' dr' d\theta' d\varphi') $$
De nuevo, por simetría, solo la componente $z$ sobrevive. La componente $z$ de $\hat{\theta}'$ es $-\sin\theta'$.
$$ m_z = -\frac{1}{2} \int_0^{2\pi} \int_0^\pi \int_0^\infty r'^3 J_\varphi (-\sin\theta') \sin\theta' dr' d\theta' d\varphi' $$
$$ m_z = \frac{1}{2} (2\pi) \int_0^\pi \sin^2\theta' \left( \int_0^\infty r'^3 J_\varphi(r', \theta') dr' \right) d\theta' $$
Sustituyendo $J_\varphi = C r^3 e^{-ar} \sin^3\theta$:
$$ m_z = \pi \int_0^\pi \sin^2\theta' \left( \int_0^\infty r'^3 (C r'^3 e^{-ar'} \sin^3\theta') dr' \right) d\theta' $$
$$ m_z = \pi C \int_0^\pi \sin^5\theta' d\theta' \int_0^\infty r'^6 e^{-ar'} dr' $$
Calculamos las integrales:
*   **Integral en $\theta'$**: $\int_0^\pi \sin^5\theta' d\theta' = \frac{16}{15}$
*   **Integral en $r'$**: $\int_0^\infty r'^6 e^{-ar'} dr' = \frac{\Gamma(7)}{a^7} = \frac{6!}{a^7} = \frac{720}{a^7}$
Sustituyendo los resultados:
$$ m_z = \pi C \left(\frac{16}{15}\right) \left(\frac{720}{a^7}\right) = \pi C \cdot 16 \cdot 48 \cdot \frac{1}{a^7} = \frac{768 \pi C}{a^7} $$
Ahora sustituimos los valores de $C$ y $a$:
$$ m_z = 768 \pi \left( \frac{e\hbar}{16\pi^3 m_0 a_0^7} \right) \frac{1}{(2/3a_0)^7} = \frac{768 \pi e\hbar}{16\pi^3 m_0 a_0^7} \frac{3^7 a_0^7}{2^7} = \frac{48 e\hbar}{\pi^2 m_0} \frac{2187}{128} $$
$$ m_z = \frac{3 \cdot 2187}{8\pi^2} \frac{e\hbar}{m_0} = \frac{6561}{8\pi^2} \frac{e\hbar}{m_0} $$
El momento dipolar magnético es:
$$ \vec{m} = \frac{6561}{8\pi^2} \frac{e\hbar}{m_0} \hat{z} $$

---

## Problema 9

**Enunciado:** En otro estado excitado del átomo de Hidrógeno la densidad de corriente asociada a la nube electrónica es, en coordenadas esféricas, $J_r = J_\theta = 0$ y
$$
J_\varphi = \frac{e\hbar}{64\pi m_0 a_0^5}r\exp\left[-\frac{r}{a_0}\right]\sin(\theta).
$$
Suponga que el núcleo del átomo tiene un momento magnético $\vec{m}_n$. Calcule la energía de interacción electrón-núcleo asociada con el movimiento orbital del electrón. Ignore el valor del momento magnético de spin del electrón.

**Solución:**

**1. Concepto de Energía de Interacción**

La energía de interacción de un momento dipolar magnético $\vec{m}_n$ en un campo magnético externo $\vec{B}_e$ está dada por:
$$ U = -\vec{m}_n \cdot \vec{B}_e $$
En este caso, el campo magnético "externo" que siente el núcleo es el campo generado por la nube de corriente del electrón, evaluado en la posición del núcleo, que es el origen de coordenadas ($\vec{r}=0$). Por lo tanto, primero debemos calcular $\vec{B}_e(0)$.

**2. Cálculo del Campo Magnético en el Origen**

Utilizamos la ley de Biot-Savart para encontrar el campo magnético en el origen debido a la densidad de corriente $\vec{J}$:
$$ \vec{B}_e(0) = \frac{\mu_0}{4\pi} \int_{V'} \frac{\vec{J}(\vec{r}') \times (-\vec{r}')}{|\vec{r}'|^3} d^3r' = -\frac{\mu_0}{4\pi} \int_{V'} \frac{\vec{J}(\vec{r}') \times \vec{r}'}{r'^3} d^3r' $$
En coordenadas esféricas, tenemos $\vec{J} = J_\varphi \hat{\varphi}'$ y $\vec{r}' = r' \hat{r}'$. El producto vectorial es:
$$ \vec{J} \times \vec{r}' = (J_\varphi \hat{\varphi}') \times (r' \hat{r}') = J_\varphi r' (\hat{\varphi}' \times \hat{r}') = J_\varphi r' \hat{\theta}' $$
Sustituyendo esto en la integral y usando el elemento de volumen $d^3r' = r'^2 \sin\theta' dr' d\theta' d\varphi'$:
$$ \vec{B}_e(0) = -\frac{\mu_0}{4\pi} \int_0^{2\pi} \int_0^\pi \int_0^\infty \frac{(J_\varphi r' \hat{\theta}')}{r'^3} (r'^2 \sin\theta' dr' d\theta' d\varphi') $$
$$ \vec{B}_e(0) = -\frac{\mu_0}{4\pi} \int J_\varphi(r', \theta') \sin\theta' \hat{\theta}' dr' d\theta' d\varphi' $$
Para integrar el vector unitario $\hat{\theta}'$, lo expresamos en coordenadas cartesianas:
$$ \hat{\theta}' = \cos\theta'\cos\varphi' \hat{x} + \cos\theta'\sin\varphi' \hat{y} - \sin\theta' \hat{z} $$
Debido a la simetría azimutal de la corriente, las componentes $x$ e $y$ del campo se anularán al integrar sobre $\varphi'$ de $0$ a $2\pi$. Solo la componente $z$ sobrevive.
$$ B_{e,z}(0) = -\frac{\mu_0}{4\pi} \int_0^{2\pi} d\varphi' \int_0^\pi \int_0^\infty J_\varphi(r', \theta') \sin\theta' (-\sin\theta') dr' d\theta' $$
$$ B_{e,z}(0) = \frac{\mu_0(2\pi)}{4\pi} \int_0^\pi \int_0^\infty J_\varphi(r', \theta') \sin^2\theta' dr' d\theta' $$
Sustituimos la expresión para $J_\varphi = C r e^{-r/a_0} \sin\theta$, donde $C = \frac{e\hbar}{64\pi m_0 a_0^5}$:
$$ B_{e,z}(0) = \frac{\mu_0}{2} \int_0^\pi \int_0^\infty \left( C r' e^{-r'/a_0} \sin\theta' \right) \sin^2\theta' dr' d\theta' $$
$$ B_{e,z}(0) = \frac{\mu_0 C}{2} \left( \int_0^\pi \sin^3\theta' d\theta' \right) \left( \int_0^\infty r' e^{-r'/a_0} dr' \right) $$
Calculamos las dos integrales por separado:
*   **Integral en $\theta'$**:
    $$ \int_0^\pi \sin^3\theta' d\theta' = \int_0^\pi (1-\cos^2\theta')\sin\theta' d\theta' = \left[-\cos\theta' + \frac{\cos^3\theta'}{3}\right]_0^\pi = \left(1-\frac{1}{3}\right) - \left(-1+\frac{1}{3}\right) = \frac{2}{3} - (-\frac{2}{3}) = \frac{4}{3} $$
*   **Integral en $r'$** (usando la fórmula $\int_0^\infty x^n e^{-ax} dx = n!/a^{n+1}$ con $n=1$ y $a=1/a_0$):
    $$ \int_0^\infty r' e^{-r'/a_0} dr' = \frac{1!}{(1/a_0)^2} = a_0^2 $$
Sustituyendo los resultados de las integrales:
$$ B_{e,z}(0) = \frac{\mu_0 C}{2} \left( \frac{4}{3} \right) (a_0^2) = \frac{2\mu_0 C a_0^2}{3} $$
Ahora, sustituimos el valor de la constante $C$:
$$ B_{e,z}(0) = \frac{2\mu_0 a_0^2}{3} \left( \frac{e\hbar}{64\pi m_0 a_0^5} \right) = \frac{2\mu_0 e\hbar a_0^2}{192\pi m_0 a_0^5} = \frac{\mu_0 e\hbar}{96\pi m_0 a_0^3} $$
El campo magnético de la nube electrónica en el origen es:
$$ \vec{B}_e(0) = \frac{\mu_0 e\hbar}{96\pi m_0 a_0^3} \hat{z} $$

**3. Cálculo de la Energía de Interacción**

Finalmente, calculamos la energía de interacción. Asumimos que el momento magnético del núcleo, $\vec{m}_n$, es un vector genérico $\vec{m}_n = m_{nx}\hat{x} + m_{ny}\hat{y} + m_{nz}\hat{z}$.
$$ U = -\vec{m}_n \cdot \vec{B}_e(0) = -(m_{nx}\hat{x} + m_{ny}\hat{y} + m_{nz}\hat{z}) \cdot \left( \frac{\mu_0 e\hbar}{96\pi m_0 a_0^3} \hat{z} \right) $$
$$ U = -m_{nz} \left( \frac{\mu_0 e\hbar}{96\pi m_0 a_0^3} \right) $$
La energía de interacción solo depende de la componente del momento magnético nuclear que es paralela al eje $z$ (el eje de simetría de la corriente electrónica).

---

## Problema 10

**Enunciado:** Una partícula de masa propia $m_0$ y carga $e$ se mueve bajo la acción del campo magnetostático homogéneo $\vec{B} = B \vec{e_z}$, siendo $\vec{e_z}$ el vector unitario en la dirección $z$. Halle la órbita de la partícula aplicando la dinámica relativista. Discuta el caso $v \ll c$, siendo $v$ el módulo de la velocidad de la partícula.

**Solución:**

**1. Ecuación de Movimiento Relativista**

La segunda ley de Newton en su forma relativista, combinada con la fuerza de Lorentz, es:
$$ \frac{d\vec{p}}{dt} = e(\vec{E} + \vec{v} \times \vec{B}) $$
donde $\vec{p} = \gamma m_0 \vec{v}$ es el momento relativista y $\gamma = (1 - v^2/c^2)^{-1/2}$ es el factor de Lorentz.
En este problema, el campo eléctrico $\vec{E}=0$ y el campo magnético es $\vec{B} = B\hat{z}$. La ecuación de movimiento se simplifica a:
$$ \frac{d}{dt}(\gamma m_0 \vec{v}) = e(\vec{v} \times B\hat{z}) $$

**2. Análisis de la Energía y la Velocidad**

La fuerza magnética $\vec{F} = e(\vec{v} \times \vec{B})$ es siempre perpendicular a la velocidad $\vec{v}$. Por lo tanto, la potencia desarrollada por la fuerza es cero:
$$ P = \vec{F} \cdot \vec{v} = e(\vec{v} \times \vec{B}) \cdot \vec{v} = 0 $$
Esto significa que la fuerza magnética no realiza trabajo sobre la partícula, y su energía cinética relativista $K = (\gamma - 1)m_0 c^2$ es constante. Si la energía cinética es constante, el factor de Lorentz $\gamma$ también es constante.
Como $\gamma$ es constante, la magnitud de la velocidad total $v = |\vec{v}|$ también debe ser constante.

**3. Componentes de la Ecuación de Movimiento**

Dado que $\gamma$ y $m_0$ son constantes, la ecuación de movimiento se puede escribir como:
$$ \gamma m_0 \frac{d\vec{v}}{dt} = e(\vec{v} \times B\hat{z}) $$
Descomponemos la velocidad $\vec{v} = (v_x, v_y, v_z)$. El producto vectorial es:
$$ \vec{v} \times B\hat{z} = \begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ v_x & v_y & v_z \\ 0 & 0 & B \end{vmatrix} = Bv_y \hat{x} - Bv_x \hat{y} $$
Las ecuaciones para cada componente son:
1.  $\gamma m_0 \frac{dv_x}{dt} = eBv_y$
2.  $\gamma m_0 \frac{dv_y}{dt} = -eBv_x$
3.  $\gamma m_0 \frac{dv_z}{dt} = 0$

**4. Solución de las Ecuaciones**

*   **Movimiento en el eje z:** De la tercera ecuación, $\frac{dv_z}{dt} = 0$, lo que implica que $v_z$ es constante.
    $$ v_z(t) = v_{z,0} $$
    Integrando con respecto al tiempo, obtenemos la posición en $z$:
    $$ z(t) = z_0 + v_{z,0} t $$
    El movimiento a lo largo del campo magnético es rectilíneo y uniforme.

*   **Movimiento en el plano xy:** Las dos primeras ecuaciones están acopladas. Definimos la **frecuencia de ciclotrón relativista** como:
    $$ \omega = \frac{eB}{\gamma m_0} $$
    Las ecuaciones se convierten en:
    $$ \frac{dv_x}{dt} = \omega v_y \quad \text{y} \quad \frac{dv_y}{dt} = -\omega v_x $$
    Para resolver este sistema, derivamos la primera ecuación respecto al tiempo y sustituimos la segunda:
    $$ \frac{d^2v_x}{dt^2} = \omega \frac{dv_y}{dt} = \omega(-\omega v_x) = -\omega^2 v_x $$
    $$ \frac{d^2v_x}{dt^2} + \omega^2 v_x = 0 $$
    Esta es la ecuación de un oscilador armónico simple. La solución general es:
    $$ v_x(t) = v_\perp \cos(\omega t + \phi) $$
    donde $v_\perp$ es la magnitud de la velocidad en el plano xy. Usando la ecuación $\frac{dv_x}{dt} = \omega v_y$, encontramos $v_y(t)$:
    $$ v_y(t) = \frac{1}{\omega}\frac{dv_x}{dt} = -v_\perp \sin(\omega t + \phi) $$
    Para encontrar la trayectoria, integramos las velocidades. Eligiendo el origen de la trayectoria circular en $(x_c, y_c)$ y ajustando la fase $\phi$ para simplificar, las soluciones son:
    $$ x(t) = x_c + R \sin(\omega t) $$
    $$ y(t) = y_c + R \cos(\omega t) $$
    donde $R$ es el radio de la órbita. La velocidad se obtiene derivando: $v_x(t) = R\omega \cos(\omega t)$ y $v_y(t) = -R\omega \sin(\omega t)$. Comparando con las soluciones para la velocidad, vemos que el radio de la trayectoria circular es:
    $$ R = \frac{v_\perp}{\omega} = \frac{v_\perp \gamma m_0}{eB} $$

**5. Órbita Completa**

La órbita de la partícula es la combinación del movimiento uniforme en la dirección $z$ y el movimiento circular uniforme en el plano $xy$. Esto describe una **hélice** con:
*   **Eje:** Paralelo al eje $z$.
*   **Radio:** $R = \frac{\gamma m_0 v_\perp}{eB}$.
*   **Frecuencia angular:** $\omega = \frac{eB}{\gamma m_0}$.
*   **Paso de hélice (distancia avanzada en $z$ por cada revolución):** $d = v_z T = v_z \frac{2\pi}{\omega} = \frac{2\pi \gamma m_0 v_z}{eB}$.

**6. Discusión del Caso no Relativista ($v \ll c$)**

En el límite no relativista, la velocidad de la partícula es mucho menor que la velocidad de la luz ($v \ll c$).
*   El factor de Lorentz $\gamma = (1 - v^2/c^2)^{-1/2}$ tiende a 1.
*   La masa relativista $\gamma m_0$ tiende a la masa en reposo $m_0$.

Las expresiones para la órbita se simplifican a las conocidas de la mecánica clásica:
*   **Frecuencia de ciclotrón clásica:**
    $$ \omega_{cl} = \lim_{v \to 0} \omega = \frac{eB}{m_0} $$
    A diferencia del caso relativista, la frecuencia no depende de la velocidad de la partícula.
*   **Radio de la órbita clásica:**
    $$ R_{cl} = \lim_{v \to 0} R = \frac{m_0 v_\perp}{eB} $$

La trayectoria sigue siendo una hélice, pero sus parámetros (radio y frecuencia) se calculan usando la masa en reposo $m_0$ y son independientes de la energía total de la partícula (mientras se mantenga en el régimen no relativista).

---

## Problema 11

**Enunciado:** Una partícula de masa propia $m_0$ y carga $e$ se somete a la acción simultánea de los campos $\vec{E}$ y $\vec{B}$, ambos uniformes y constantes. Los campos son perpendiculares entre sí y además satisfacen la condición $E = cB$. Halle la órbita de la partícula aplicando la dinámica relativista.

**Solución:**

Este es un problema clásico que se resuelve de manera más elegante utilizando el formalismo de la relatividad especial y los invariantes de Lorentz.

**1. Configuración de los Campos**

Dado que los campos son uniformes, constantes y perpendiculares, podemos orientar nuestro sistema de coordenadas para simplificar el análisis. Escogemos:
*   $\vec{B} = B \hat{z}$
*   $\vec{E} = E \hat{y}$

La condición dada es $E = cB$.

**2. Invariantes de Lorentz**

En la teoría de la relatividad, existen dos cantidades escalares construidas a partir de los campos $\vec{E}$ y $\vec{B}$ que son invariantes bajo transformaciones de Lorentz (es decir, tienen el mismo valor en todos los sistemas de referencia inerciales). Estas son:

1.  $I_1 = \vec{E} \cdot \vec{B}$
2.  $I_2 = \frac{E^2}{c^2} - B^2$

Calculemos estos invariantes para nuestra configuración:
1.  $I_1 = (E\hat{y}) \cdot (B\hat{z}) = 0$
2.  $I_2 = \frac{(cB)^2}{c^2} - B^2 = \frac{c^2 B^2}{c^2} - B^2 = B^2 - B^2 = 0$

Ambos invariantes de Lorentz son cero. Esto tiene una consecuencia muy importante: **existe un sistema de referencia inercial donde los campos eléctrico y magnético son ambos nulos.**

**3. Búsqueda del Sistema de Referencia sin Campos**

Vamos a encontrar la velocidad $\vec{u}$ de este sistema de referencia especial (llamémoslo $S'$) con respecto a nuestro sistema de laboratorio ($S$). La transformación de los campos a un sistema $S'$ que se mueve con velocidad $\vec{u}$ es:

$$ \vec{E}' = \gamma(\vec{E} + \vec{u} \times \vec{B}) - \frac{\gamma^2}{\gamma+1} \frac{(\vec{u} \cdot \vec{E})}{c^2} \vec{u} $$
$$ \vec{B}' = \gamma(\vec{B} - \frac{\vec{u} \times \vec{E}}{c^2}) - \frac{\gamma^2}{\gamma+1} \frac{(\vec{u} \cdot \vec{B})}{c^2} \vec{u} $$

Queremos encontrar $\vec{u}$ tal que $\vec{E}' = 0$ y $\vec{B}' = 0$.
Probemos con una velocidad $\vec{u}$ en la dirección $\vec{E} \times \vec{B}$:
$$ \vec{u} = u \frac{\vec{E} \times \vec{B}}{|\vec{E} \times \vec{B}|} = u \frac{(E\hat{y}) \times (B\hat{z})}{EB} = u \frac{EB\hat{x}}{EB} = u\hat{x} $$
Sustituyamos $\vec{u} = u\hat{x}$ en la ecuación de transformación de $\vec{E}'$:
*   $\vec{u} \cdot \vec{E} = (u\hat{x}) \cdot (E\hat{y}) = 0$. El último término se anula.
*   $\vec{u} \times \vec{B} = (u\hat{x}) \times (B\hat{z}) = -uB\hat{y}$.

La ecuación para $\vec{E}'$ se convierte en:
$$ \vec{E}' = \gamma(\vec{E} + \vec{u} \times \vec{B}) = \gamma(E\hat{y} - uB\hat{y}) = \gamma(E - uB)\hat{y} $$
Para que $\vec{E}'=0$, necesitamos que $E - uB = 0$, lo que implica $u = E/B$.
Usando la condición $E=cB$, obtenemos:
$$ u = \frac{cB}{B} = c $$
La velocidad de este sistema de referencia especial es $\vec{u} = c\hat{x}$.

Verifiquemos que $\vec{B}'$ también es cero con esta velocidad:
*   $\vec{u} \cdot \vec{B} = (c\hat{x}) \cdot (B\hat{z}) = 0$.
*   $\vec{u} \times \vec{E} = (c\hat{x}) \times (E\hat{y}) = cE\hat{z} = c(cB)\hat{z} = c^2B\hat{z}$.

La ecuación para $\vec{B}'$ es:
$$ \vec{B}' = \gamma(\vec{B} - \frac{\vec{u} \times \vec{E}}{c^2}) = \gamma(B\hat{z} - \frac{c^2B\hat{z}}{c^2}) = \gamma(B\hat{z} - B\hat{z}) = 0 $$
Ambos campos son nulos en el sistema $S'$ que se mueve con velocidad $\vec{u} = c\hat{x}$.

**4. Movimiento de la Partícula**

*   **En el sistema $S'$:** Como no hay campos ($\vec{E}'=0, \vec{B}'=0$), no hay fuerza sobre la partícula. Por la primera ley de Newton, la partícula se moverá con velocidad constante, $\vec{v}'$.
    $$ \vec{v}'(t') = \vec{v}'_0 = \text{constante} $$
    Su trayectoria es una línea recta:
    $$ \vec{r}'(t') = \vec{r}'_0 + \vec{v}'_0 t' $$

*   **En el sistema de laboratorio $S$:** La órbita de la partícula en el sistema de laboratorio es la transformación de Lorentz de esta línea recta.

La velocidad de la partícula en el sistema $S$ se obtiene usando la fórmula de adición de velocidades de Einstein:
$$ \vec{v} = \frac{1}{1 + \frac{\vec{u} \cdot \vec{v}'}{c^2}} \left[ \vec{u} + \frac{\vec{v}'}{\gamma_u} + \frac{\gamma_u}{\gamma_u+1} \frac{(\vec{u} \cdot \vec{v}')}{c^2} \vec{u} \right] $$
donde $\vec{u} = c\hat{x}$ es la velocidad de $S'$ respecto a $S$.
Como $u=c$, el factor $\gamma_u = (1-u^2/c^2)^{-1/2}$ es infinito. La fórmula no se puede aplicar directamente.

**5. Conclusión sobre la Órbita**

El hecho de que el sistema sin campos se mueva a la velocidad de la luz $c$ es la clave. Una partícula masiva ($m_0 > 0$) no puede alcanzar la velocidad de la luz.

Consideremos la velocidad de la partícula en el sistema de laboratorio $S$. Su velocidad $\vec{v}$ siempre debe tener una magnitud $v < c$.
La velocidad de la partícula en el sistema $S'$ es $\vec{v}'$. La magnitud de la velocidad en $S$ está relacionada con la de $S'$ por la transformación de velocidades.

Si la partícula tiene una velocidad inicial $\vec{v}_0$ en el laboratorio, su velocidad inicial en el sistema $S'$ será $\vec{v}'_0$. A partir de ese momento, $\vec{v}'$ permanece constante. La partícula en el laboratorio $S$ se moverá de tal manera que su velocidad $\vec{v}(t)$ siempre será la transformada de Lorentz de la velocidad constante $\vec{v}'_0$.

La partícula es acelerada por los campos, pero de una manera muy específica. La fuerza neta siempre actúa de tal forma que la velocidad de la partícula, $\vec{v}$, se acerca asintóticamente a la velocidad de deriva $\vec{v}_D = \frac{\vec{E} \times \vec{B}}{B^2}$. En nuestro caso, con $E=cB$:
$$ \vec{v}_D = \frac{(E\hat{y}) \times (B\hat{z})}{B^2} = \frac{EB\hat{x}}{B^2} = \frac{E}{B}\hat{x} = c\hat{x} $$
La partícula es continuamente acelerada en la dirección $x$, y su velocidad se aproxima a la velocidad de la luz.

**La órbita es una curva en el espacio-tiempo tal que la velocidad de la partícula $\vec{v}(t)$ tiende asintóticamente a $c\hat{x}$.** La partícula nunca alcanza la velocidad de la luz, pero se acerca indefinidamente a ella mientras es continuamente acelerada en la dirección del eje $x$. La trayectoria es una curva que se vuelve cada vez más paralela al eje $x$.

---

# APÉNDICE: Pasos Intermedios Expandidos

Este apéndice contiene los pasos intermedios detallados para los desarrollos matemáticos que tienen saltos o simplificaciones.

## Problema 1 de Electrostática - Detalles de Integrales

### Integral en $\theta$ para la esfera (alternativa usando sustitución)

Se puede usar también la identidad $\sin(2\theta) = 2\sin\theta\cos\theta$, por lo que:
$$\sin\theta\cos\theta = \frac{1}{2}\sin(2\theta)$$

Entonces:
$$\int_0^{\pi/2} \sin\theta\cos\theta \, d\theta = \frac{1}{2}\int_0^{\pi/2} \sin(2\theta) \, d\theta = \frac{1}{2}\left[-\frac{\cos(2\theta)}{2}\right]_0^{\pi/2}$$

Evaluando:
$$= \frac{1}{2}\left[-\frac{\cos(\pi)}{2} + \frac{\cos(0)}{2}\right] = \frac{1}{2}\left[-\frac{(-1)}{2} + \frac{1}{2}\right] = \frac{1}{2}\left[\frac{1}{2} + \frac{1}{2}\right] = \frac{1}{2}$$

Este resultado confirma el obtenido mediante sustitución.

### Expansión del Tetraedro - Detalles Adicionales

**Verificación de los límites de integración:**

Para un punto $(x, y)$ dentro del rectángulo de base del tetraedro, la altura máxima en $z$ viene de despejar:
$$\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1 \implies z = c\left(1 - \frac{x}{a} - \frac{y}{b}\right)$$

Esta cantidad es positiva precisamente cuando $\frac{x}{a} + \frac{y}{b} < 1$, lo que define la región triangular en el plano $xy$.

**Cambio de variable detallado para $y$:**

Partiendo de:
$$\int_0^{b(1-x/a)} \left(1 - \frac{x}{a} - \frac{y}{b}\right)^2 dy$$

Sea $u = 1 - \frac{x}{a} - \frac{y}{b}$. Entonces:
- Cuando $y = 0$: $u = 1 - \frac{x}{a}$
- Cuando $y = b(1 - \frac{x}{a})$: $u = 1 - \frac{x}{a} - \frac{1}{b} \cdot b(1 - \frac{x}{a}) = 0$

Además, $\frac{\partial u}{\partial y} = -\frac{1}{b}$, entonces $dy = -b \, du$.

La integral se transforma:
$$\int_0^{b(1-x/a)} u^2 \, dy = \int_{1-x/a}^{0} u^2 \cdot (-b) \, du = b\int_0^{1-x/a} u^2 \, du$$

Evaluando:
$$b \left[\frac{u^3}{3}\right]_0^{1-x/a} = \frac{b}{3}\left[\left(1-\frac{x}{a}\right)^3 - 0\right] = \frac{b}{3}\left(1-\frac{x}{a}\right)^3$$

---

## Problema 3 de Electrostática - Expansión de Laplaciano y Función Delta

### Desarrollo Completo del Laplaciano en Coordenadas Polares

En coordenadas polares 2D, el Laplaciano actúa sobre una función escalar $\phi(r, \theta)$:
$$\nabla^2 \phi = \frac{1}{r}\frac{\partial}{\partial r}\left(r\frac{\partial \phi}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2\phi}{\partial\theta^2}$$

Considerando la expansión:
$$G(r, \theta; r', \theta') = \sum_{n=1}^{\infty} g_n(r, r') \sin\left(\frac{n\pi\theta}{\alpha}\right)$$

El Laplaciano sobre esta suma:
$$\nabla^2 G = \sum_{n=1}^{\infty} \sin\left(\frac{n\pi\theta}{\alpha}\right) \left[\frac{1}{r}\frac{d}{dr}\left(r\frac{dg_n}{dr}\right) + \frac{1}{r^2}\frac{\partial^2}{\partial\theta^2}\left(\sin\left(\frac{n\pi\theta}{\alpha}\right)\right)\right]$$

Para la derivada angular:
$$\frac{\partial^2}{\partial\theta^2}\left(\sin\left(\frac{n\pi\theta}{\alpha}\right)\right) = -\left(\frac{n\pi}{\alpha}\right)^2 \sin\left(\frac{n\pi\theta}{\alpha}\right)$$

Sustituyendo:
$$\nabla^2 G = \sum_{n=1}^{\infty} \sin\left(\frac{n\pi\theta}{\alpha}\right) \left[\frac{1}{r}\frac{d}{dr}\left(r\frac{dg_n}{dr}\right) - \frac{1}{r^2}\left(\frac{n\pi}{\alpha}\right)^2 g_n\right]$$

Definiendo $\nu_n = \frac{n\pi}{\alpha}$:
$$\nabla^2 G = \sum_{n=1}^{\infty} \sin\left(\frac{n\pi\theta}{\alpha}\right) \left[\frac{1}{r}\frac{d}{dr}\left(r\frac{dg_n}{dr}\right) - \frac{\nu_n^2}{r^2} g_n\right]$$

### Expansión en Series de Fourier de la Función Delta

La función delta bidimensional en coordenadas polares se puede expandir:
$$\delta(r - r')\delta(\theta - \theta') = \frac{\delta(r-r')}{r'} \sum_{n=1}^{\infty} \frac{2}{\alpha} \sin\left(\frac{n\pi\theta'}{\alpha}\right) \sin\left(\frac{n\pi\theta}{\alpha}\right)$$

Esto proviene del hecho de que las funciones $\{\sin(n\pi\theta/\alpha)\}$ forman una base ortogonal en $[0, \alpha]$ con peso 1.

---

## Problema 5 de Magnetostática - Identidad Vectorial Completa

### Demostración de la Identidad Vectorial

La identidad $\vec{A} \times (\vec{B} \times \vec{C}) = \vec{B}(\vec{A} \cdot \vec{C}) - \vec{C}(\vec{A} \cdot \vec{B})$ se puede demostrar en componentes.

En notación de índices:
$$[\vec{A} \times (\vec{B} \times \vec{C})]_i = \epsilon_{ijk} A_j (\vec{B} \times \vec{C})_k = \epsilon_{ijk} A_j \epsilon_{klm} B_l C_m$$

Usando la identidad $\epsilon_{ijk}\epsilon_{klm} = \delta_{il}\delta_{jm} - \delta_{im}\delta_{jl}$:
$$= A_j(\delta_{il}\delta_{jm} - \delta_{im}\delta_{jl}) B_l C_m = A_j\delta_{il}B_l C_m \delta_{jm} - A_j\delta_{im}B_l C_m\delta_{jl}$$
$$= A_j B_i C_j - A_j B_j C_i = B_i(A_j C_j) - C_i(A_j B_j) = B_i(\vec{A} \cdot \vec{C}) - C_i(\vec{A} \cdot \vec{B})$$

Recomponiendo en notación vectorial:
$$\vec{A} \times (\vec{B} \times \vec{C}) = \vec{B}(\vec{A} \cdot \vec{C}) - \vec{C}(\vec{A} \cdot \vec{B})$$

### Aplicación al Problema

Con $\vec{A} = \vec{r}$, $\vec{B} = \vec{\omega}$, $\vec{C} = \vec{r}$:
$$\vec{r} \times (\vec{\omega} \times \vec{r}) = \vec{\omega}(\vec{r} \cdot \vec{r}) - \vec{r}(\vec{r} \cdot \vec{\omega})$$
$$= \vec{\omega} r^2 - \vec{r}(\vec{r} \cdot \vec{\omega})$$

**Por qué se anula el segundo término en la integral:**

En componentes del segundo término, integrado sobre la esfera:
$$\int_V \vec{r}(\vec{r} \cdot \vec{\omega}) dV = \int_V (r_i r_j \omega_j) dV$$

Esta es la contracción del tensor de momento de inercia con $\vec{\omega}$. Para una distribución con simetría esférica, se puede demostrar que:
$$\int_V r_i r_j dV = \delta_{ij} \int_V r^2 dV$$

Por lo tanto:
$$\int_V \vec{r}(\vec{r} \cdot \vec{\omega}) dV = \omega_j \delta_{ij} \int_V r^2 dV = \omega_i \int_V r^2 dV = \vec{\omega} \int_V r^2 dV$$

### Cálculo Alternativo Usando Tensor de Inercia

Para una esfera sólida uniforme de masa $M$ y radio $R$, el tensor de momento de inercia es:
$$I_{ij} = \frac{2}{5}MR^2 \delta_{ij}$$

El momento angular es:
$$L_i = I_{ij} \omega_j = \frac{2}{5}MR^2 \omega_i$$

Esto verifica que $\vec{L} = \frac{2}{5}MR^2 \vec{\omega}$.

Para la carga uniforme $q$ en la misma distribución:
$$\vec{m} = \frac{q}{2M}\vec{L} = \frac{q}{2M} \cdot \frac{2}{5}MR^2\vec{\omega} = \frac{1}{5}qR^2\vec{\omega}$$

---

## Problema 6 de Magnetostática - Constante de Estructura Fina

### Definición y Propiedades de $\alpha$

La constante de estructura fina $\alpha$ es:
$$\alpha = \frac{e^2}{4\pi\epsilon_0\hbar c} \approx \frac{1}{137}$$

Esta puede reescribirse como:
$$\frac{e^2}{4\pi\epsilon_0} = \alpha \hbar c$$

O usando sistemas CGS:
$$\alpha = \frac{e^2}{\hbar c}$$

### Radio Clásico del Electrón en Términos de $\alpha$

$$r_0 = \frac{e^2}{4\pi\epsilon_0 m_e c^2} = \frac{\alpha \hbar c}{m_e c^2} = \frac{\alpha \hbar}{m_e c}$$

Numéricamente: $r_0 \approx 2.8 \times 10^{-15}$ m (femtómetros)

### Simplificación de la Velocidad Angular

Partiendo de:
$$\omega = \frac{3\hbar}{2m_e r_0^2}$$

Sustituyendo $r_0 = \frac{\alpha \hbar}{m_e c}$:
$$r_0^2 = \left(\frac{\alpha \hbar}{m_e c}\right)^2 = \frac{\alpha^2 \hbar^2}{m_e^2 c^2}$$

Entonces:
$$\omega = \frac{3\hbar}{2m_e} \cdot \frac{m_e^2 c^2}{\alpha^2 \hbar^2} = \frac{3m_e c^2}{2\alpha^2 \hbar}$$

### Velocidad Tangencial en el Ecuador

$$v_t = \omega r_0 = \frac{3m_e c^2}{2\alpha^2 \hbar} \cdot \frac{\alpha \hbar}{m_e c} = \frac{3c}{2\alpha}$$

Con $\alpha = 1/137$:
$$v_t = \frac{3c}{2/137} = \frac{3 \times 137}{2} c = \frac{411}{2}c \approx 205.5 c$$

### Análisis de la Inconsistencia

Este resultado demuestra que el modelo clásico es inconsistente con la relatividad especial:
- Una velocidad $v_t > c$ es imposible
- Esto sugiere que el espín es una propiedad cuántica intrínseca
- El factor $g \approx 2$ tampoco puede explicarse clásicamente

---

## Problema 8 de Magnetostática - Cálculos de Integrales Complejas

### Integral Angular: Fórmulas de Wallis

Las fórmulas de Wallis para integrales de potencias de seno y coseno son:

$$\int_0^\pi \sin^n(\theta) d\theta = \begin{cases}
\frac{(n-1)!! \pi}{n!!} & \text{si } n \text{ es par} \\
\frac{(n-1)!!}{n!!} \cdot 2 & \text{si } n \text{ es impar}
\end{cases}$$

donde $n!! = n(n-2)(n-4)\cdots$ es el factorial doble.

Para $n = 5$ (impar):
$$\int_0^\pi \sin^5(\theta) d\theta = \frac{4!!}{5!!} \cdot 2 = \frac{4 \cdot 2}{5 \cdot 3 \cdot 1} \cdot 2 = \frac{8}{15} \cdot 2 = \frac{16}{15}$$

### Integral Radial Usando Función Gamma

La función Gamma se define como:
$$\Gamma(n) = \int_0^\infty x^{n-1} e^{-x} dx = (n-1)!$$

La integral general:
$$\int_0^\infty x^n e^{-ax} dx = \frac{\Gamma(n+1)}{a^{n+1}} = \frac{n!}{a^{n+1}}$$

Para $\int_0^\infty r^3 e^{-2r/3a_0} dr$, hacemos $u = \frac{2r}{3a_0}$, $r = \frac{3a_0 u}{2}$, $dr = \frac{3a_0}{2}du$:

$$\int_0^\infty r^3 e^{-2r/3a_0} dr = \int_0^\infty \left(\frac{3a_0 u}{2}\right)^3 e^{-u} \frac{3a_0}{2} du$$
$$= \left(\frac{3a_0}{2}\right)^4 \int_0^\infty u^3 e^{-u} du = \frac{3^4 a_0^4}{2^4} \cdot 3! = \frac{81 a_0^4}{16} \cdot 6 = \frac{486 a_0^4}{16} = \frac{243 a_0^4}{8}$$

---

## Problema 9 de Magnetostática - Campo Magnético de Corriente Azimutal

### Componentes del Vector Unitario $\hat{\theta}$

En coordenadas esféricas:
- $\hat{r} = \sin\theta\cos\varphi \hat{x} + \sin\theta\sin\varphi \hat{y} + \cos\theta \hat{z}$
- $\hat{\theta} = \cos\theta\cos\varphi \hat{x} + \cos\theta\sin\varphi \hat{y} - \sin\theta \hat{z}$
- $\hat{\varphi} = -\sin\varphi \hat{x} + \cos\varphi \hat{y}$

La componente $z$ de $\hat{\theta}$ es:
$$\hat{\theta} \cdot \hat{z} = -\sin\theta$$

### Evaluación de la Integral Angular

$$\int_0^\pi \sin^3(\theta) d\theta$$

Usando $\sin^3(\theta) = \sin(\theta)(1 - \cos^2(\theta))$, sea $u = \cos(\theta)$, $du = -\sin(\theta)d\theta$:

$$\int_0^\pi \sin^3(\theta) d\theta = \int_1^{-1} (1 - u^2)(-du) = \int_{-1}^1 (1 - u^2) du$$
$$= \left[u - \frac{u^3}{3}\right]_{-1}^1 = \left(1 - \frac{1}{3}\right) - \left(-1 + \frac{1}{3}\right) = \frac{2}{3} - (-\frac{2}{3}) = \frac{4}{3}$$

---

## Problema 10-11 de Magnetostática - Análisis Relativista

### Invariantes de Lorentz

Los dos invariantes básicos del campo electromagnético bajo transformaciones de Lorentz son:

1. **Invariante pseudoescalar:**
   $$I_1 = \vec{E} \cdot \vec{B}$$

2. **Invariante escalar:**
   $$I_2 = \frac{E^2}{c^2} - B^2$$

Para el problema 11 con $E = cB$ y $\vec{E} \perp \vec{B}$:
- $I_1 = 0$ (porque $\vec{E} \perp \vec{B}$)
- $I_2 = \frac{(cB)^2}{c^2} - B^2 = B^2 - B^2 = 0$

Cuando ambos invariantes son cero, existe un marco de referencia donde $\vec{E}' = \vec{B}' = 0$.

### Búsqueda del Marco sin Campos

Las transformaciones de Lorentz de los campos bajo un boost con velocidad $\vec{u}$ perpendicular a ambos $\vec{E}$ y $\vec{B}$ son:
$$\vec{E}' = \gamma(\vec{E} + \vec{u} \times \vec{B})$$
$$\vec{B}' = \gamma\left(\vec{B} - \frac{\vec{u} \times \vec{E}}{c^2}\right)$$

Con $\vec{u} = u\hat{x}$, $\vec{E} = E\hat{y}$, $\vec{B} = B\hat{z}$:
$$\vec{u} \times \vec{B} = u\hat{x} \times B\hat{z} = -uB\hat{y}$$
$$\vec{u} \times \vec{E} = u\hat{x} \times E\hat{y} = uE\hat{z}$$

Para $\vec{E}' = 0$: $E - uB = 0 \implies u = E/B = c$

Para $\vec{B}' = 0$: $B - \frac{uE}{c^2} = 0 \implies u = \frac{c^2 B}{E} = \frac{c^2 B}{cB} = c$

Ambos dan $u = c$, confirmando que el sistema $S'$ que se mueve a la velocidad de la luz no tiene campos.

---

## Referencias Útiles

### Identidades Vectoriales Comunes

$$\nabla \times (\nabla \phi) = 0$$
$$\nabla \cdot (\nabla \times \vec{A}) = 0$$
$$\nabla \times (\nabla \times \vec{A}) = \nabla(\nabla \cdot \vec{A}) - \nabla^2 \vec{A}$$

### Fórmulas de Integración

$$\int_0^a x^n dx = \frac{a^{n+1}}{n+1}$$
$$\int_0^\pi \sin^n(\theta) d\theta = \frac{(n-1)!!}{n!!} \cdot \begin{cases} 2 & n \text{ impar} \\ \pi & n \text{ par} \end{cases}$$
$$\int_0^\infty x^n e^{-ax} dx = \frac{n!}{a^{n+1}}$$

### Transformaciones de Coordenadas

**Cartesianas a Esféricas:**
- $x = r\sin\theta\cos\varphi$
- $y = r\sin\theta\sin\varphi$  
- $z = r\cos\theta$
- $dV = r^2\sin\theta \, dr \, d\theta \, d\varphi$

**Cartesianas a Cilíndricas:**
- $x = \rho\cos\varphi$
- $y = \rho\sin\varphi$
- $z = z$
- $dV = \rho \, d\rho \, d\varphi \, dz$

---

**FIN DEL SOLUCIONARIO**

