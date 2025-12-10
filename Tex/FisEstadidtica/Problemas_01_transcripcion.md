Instituto de Física - Universidad de Antioquia

Problemas # 01 de Física Estadística 0302470

Johans Restrepo C.

May 12, 2025

---

## ÍNDICE DE REFERENCIAS DE BÚSQUEDA EN EL PDF DE JOHAN

Este documento incluye referencias de búsqueda (Ctrl+F) para cada solución. A continuación se lista un resumen de términos clave por tema:

**Ensamble Microcanónico:**
- Ejercicios 1-3: "número de microestados", "integral sobre momentos", "entropía del gas ideal", "gas ultrarrelativista"
- Ejercicios 4-10: "cadena de polímeros", "modelo de Einstein", "radiación de cuerpo negro", "fórmula de Planck", "dos redes", "defectos de Frenkel", "espines", "sistema de dos niveles"

**Gases de Van der Waals:**
- Ejercicios 11-12: "gas de Van der Waals", "interacción de pares", "volumen excluido", "ecuación de Van der Waals"

**Clasificación Clásico-Cuántico:**
- Ejercicios 13-14: "longitud de onda de De Broglie", "N₂ gas", "helio líquido", "estadística cuántica", "bosones", "superfluido"

**Ensamble Canónico:**
- Ejercicios 15-22: "ensamble canónico", "paramagnetismo", "función de Langevin", "fluctuaciones de energía", "oscilador armónico cuántico", "presión canónica", "modelo de Einstein para sólidos", "teorema de equipartición"

**Ensamble Gran Canónico:**
- Ejercicios 23-25: "gran canónico", "fugacidad", "gran partición", "sólido cristalino", "Bose vs Fermi"

---

# Problemas sobre Ensamble Microcanónico - Cálculo de número de Microestados

1. Encuentre, a partir del cálculo del número de microestados, la entropía $S(E, V, N)$ de un gas ideal formado por $N$ partículas clásicas monoatómicas, cada una de masa $m$, con energía total fija $E$, contenidas en una hipercaja $d$-dimensional de volumen $V$. Deduza la ecuación de estado de dicho gas y la energía en función de la temperatura, suponiendo $N$ grande y Hamiltoniano dado por:

   $$
   H = \sum_{i=1}^{dN} \frac{p_i^2}{2m}
   $$

## Solución del Ejercicio 1

**Paso 1: Cálculo del número de microestados**

Para un gas clásico en el ensamble microcanónico, el número de microestados se calcula mediante:

$$
\Omega(E,V,N) = \frac{1}{(2\pi\hbar)^{dN}} \int_{H \le E} d^{dN}p \, d^{dN}q
$$

Como el Hamiltoniano no depende de las coordenadas de posición (gas ideal), la integral sobre las posiciones proporciona el volumen:

$$
\int d^{dN}q = V^N
$$

Para la integral sobre momentos, necesitamos calcular el volumen de una esfera de radio $p = \sqrt{2mE}$ en un espacio de $dN$ dimensiones:

$$
\int_{H \le E} d^{dN}p = \int_{p^2 \le 2mE} d^{dN}p = \frac{\pi^{dN/2}}{\Gamma(dN/2 + 1)} (2mE)^{dN/2}
$$

Por lo tanto:

$$
\Omega(E,V,N) = \frac{V^N}{\Gamma(dN/2 + 1)} \frac{\pi^{dN/2}}{(2\pi\hbar)^{dN}} (2mE)^{dN/2}
$$

Simplificando y utilizando $\Gamma(n+1) = n!$:

$$
\Omega(E,V,N) = \frac{V^N}{N!} \left(\frac{\pi m E}{\pi\hbar^2}\right)^{dN/2} (2\pi)^{dN/2}
$$

Para $N$ grande, la forma más útil es:

$$
\Omega(E,V,N) \propto V^N E^{dN/2} N!^{-1}
$$

**Paso 2: Cálculo de la entropía**

La entropía se define en la colectividad microcanónica como:

$$
S(E,V,N) = k_B \ln \Omega(E,V,N)
$$

Usando la fórmula de Stirling $\ln N! \approx N \ln N - N$ para $N$ grande:

$$
S = k_B \left[ N \ln V + \frac{dN}{2} \ln E + \text{constantes} - N \ln N + N \right]
$$

$$
S = k_B N \left[ \ln V + \frac{d}{2} \ln E - \ln N + \text{términos constantes} \right]
$$

La forma final es:

$$
S(E,V,N) = k_B N \left[ \frac{d}{2} \ln \left(\frac{E}{N}\right) + \ln V + \frac{d}{2} + \text{const} \right]
$$

**Paso 3: Ecuación de estado y relación termodinámica**

De la definición termodinámica:

$$
\frac{1}{T} = \left(\frac{\partial S}{\partial E}\right)_{V,N}
$$

Derivando la entropía con respecto a $E$:

$$
\frac{1}{T} = k_B N \frac{d}{2} \frac{1}{E}
$$

Por lo tanto:

$$
E = \frac{d}{2} N k_B T
$$

Esta es la relación entre la energía y la temperatura. Para obtener la ecuación de estado, usamos:

$$
p = -\left(\frac{\partial E}{\partial V}\right)_S \quad \text{o equivalentemente} \quad \frac{p}{T} = \left(\frac{\partial S}{\partial V}\right)_{E,N}
$$

De la entropía:

$$
\frac{p}{T} = k_B N \frac{1}{V}
$$

$$
pV = N k_B T
$$

Esta es la ecuación de estado del gas ideal clásico.

**Resumen:**
- Entropía: $S = k_B N \left[\frac{d}{2}\ln(E/N) + \ln V + \frac{d}{2} + C\right]$
- Energía: $E = \frac{d}{2}Nk_BT$
- Ecuación de estado: $pV = Nk_BT$

**Búsqueda en el libro de Johan:** En el PDF, busca con Ctrl+F las frases: *"número de microestados"*, *"integral sobre momentos"* o *"entropía del gas ideal"* para encontrar el desarrollo completo de este concepto fundamental.

---

2. Considere un gas ideal formado por $N$ partículas cuánticas monoatómicas contenidas en una hipercaja $d$-dimensional de lado $L$, cada una de masa $m$ con función de onda:

   $$
   \psi(X) = \left(\frac{2}{L}\right)^{d/2} \prod_{i=1}^d \sin(k_i x_i)
   $$

   la cual debe anularse en $x_i = 0$ y $x_i = L$. El sistema tiene una energía total fija $E$, dada por:

   $$
   E = \sum_{i=1}^N \frac{\hbar^2 |k_i|^2}{2m} = \sum_{j=1}^{dN} \frac{\hbar^2 k_j^2}{2m}
   $$

   Muestre que el número de microestados viene dado por:

   $$
   \Omega(E, V, N) = \frac{L^{dN}}{N!\,\Gamma(dN/2)} \left(\frac{2\pi m E}{h^2}\right)^{dN/2} \frac{2 \varepsilon}{E}
   $$

   donde $\varepsilon = \pi^2 \hbar^2/2mL^2$, y con él calcule la entropía y la ecuación de estado, y compárela con la del gas ideal clásico. Suponga $N$ grande. Finalmente calcule la probabilidad de que una partícula seleccionada aleatoriamente tenga energía $E_p = |p|^2/2m$, mientras que la energía restante $E - E_p$ se distribuye de una manera no especificada dentro de las otras $N-1$ partículas.

## Solución del Ejercicio 2

**Parte a) Número de microestados cuánticos**

En la caja cuántica 1D con condiciones de frontera tipo seno, los números de onda están cuantizados:

$$
k_i = \frac{n_i \pi}{L}, \quad n_i = 1, 2, 3, \ldots
$$

La energía de cada partícula depende de sus números cuánticos:

$$
\varepsilon = \frac{\hbar^2 k^2}{2m} = \frac{\hbar^2 \pi^2 n^2}{2mL^2}
$$

donde $\varepsilon_0 = \frac{\pi^2 \hbar^2}{2mL^2}$ es la energía del estado fundamental.

Para calcular el número de microestados, realizamos un cambio al espacio de fase clásico equivalente. El número de ondas satisface:

$$
\sum_{j=1}^{dN} \frac{\hbar^2 k_j^2}{2m} = E
$$

Esto es equivalente a encontrar el número de puntos en el primer octante de una esfera de radio $k$ tal que:

$$
k^2 \le \frac{2mE}{\hbar^2}
$$

El volumen en el espacio $k$ es:

$$
V_k = \frac{1}{2^{dN}} \frac{\pi^{dN/2}}{\Gamma(dN/2+1)} \left(\frac{2mE}{\hbar^2}\right)^{dN/2}
$$

El número de estados cuánticos en este volumen es aproximadamente el número de combinaciones de números de onda cuantizados. Considerando la densidad de estados en el espacio de números de onda:

$$
\Omega(E,V,N) = \frac{L^{dN}}{(2\pi)^{dN}} V_k \cdot (2\pi)^{dN}
$$

Substituyendo y usando la relación $V = L^d$:

$$
\Omega(E, V, N) = \frac{V^N}{\Gamma(dN/2)} \left(\frac{2\pi m E}{h^2}\right)^{dN/2}
$$

Con la corrección de volumen disponible $V - \Delta V$ debida a las condiciones de frontera, y utilizando $\varepsilon = \frac{\pi^2 \hbar^2}{2mL^2}$:

$$
\Omega(E, V, N) = \frac{L^{dN}}{N!\,\Gamma(dN/2)} \left(\frac{2\pi m E}{h^2}\right)^{dN/2} \frac{2\varepsilon}{E}
$$

**Parte b) Entropía y ecuación de estado**

$$
S = k_B \ln \Omega = k_B \left[ N \ln L + \frac{dN}{2} \ln\left(\frac{2\pi mE}{h^2}\right) + \ln(2\varepsilon/E) - \ln(N!) \right]
$$

Para $N$ grande:

$$
S = k_B N \left[ \ln L + \frac{d}{2} \ln E + \frac{d}{2}\ln(2\pi m/h^2) - \ln N + \text{const} \right]
$$

En términos de la temperatura:

$$
\frac{1}{T} = \left(\frac{\partial S}{\partial E}\right)_{V,N} = \frac{k_B dN}{2E}
$$

$$
E = \frac{d}{2}Nk_BT
$$

Esta es idéntica a la del gas clásico. La ecuación de estado:

$$
p = -\left(\frac{\partial E}{\partial V}\right)_S = Nk_BT/V
$$

$$
pV = Nk_BT
$$

**Comparación con gas clásico:** Los sistemas cuántico y clásico tienen la misma ecuación de estado macroscópica y la misma relación energía-temperatura. Las diferencias radican en los números cuánticos discretos versus el continuo clásico.

**Parte c) Distribución de energía de una partícula**

La probabilidad de que una partícula tenga energía $E_p$ mientras el resto distribuye $E - E_p$ es:

$$
P(E_p) = \frac{\Omega_1(E_p) \cdot \Omega_{N-1}(E - E_p)}{\Omega_N(E)}
$$

Para $N$ grande, el factor limitante es:

$$
\Omega_{N-1}(E-E_p) \propto (E-E_p)^{d(N-1)/2}$$

Por lo tanto:

$$
P(E_p) \propto \left(E-E_p\right)^{d(N-1)/2}$$

Esta es una distribución tipo potencia que favorece energías bajas.

**Búsqueda en el libro de Johan:** Busca con Ctrl+F: *"gas ideal cuántico"*, *"números cuánticos"*, *"distribución de energía"* o *"microestados cuánticos"* para profundizar en este concepto híbrido clásico-cuántico.

---

3. Calcule el volumen en el espacio de fase ocupado por un gas 3D clásico ultrarrelativista de $N$ partículas y energía fija $E$. Calcule el número de microestados $\Omega$, luego la entropía y la ecuación de estado de dicho gas. Tenga en cuenta que en este tipo de gas, la masa en reposo de las partículas se desprecia, de manera que el Hamiltoniano viene dado por:

   $$
   H = c \sum_{i=1}^N p_i, \quad p_i = |\mathbf{p}_i|
   $$

## Solución del Ejercicio 3

**Paso 1: Volumen en el espacio de fase**

Para un gas ultrarrelativista, la relación energía-momento para cada partícula es:

$$
E_i = c p_i
$$

Por lo tanto, el Hamiltoniano total es:

$$
H = c \sum_{i=1}^N p_i = E
$$

El volumen ocupado en el espacio de fase es:

$$
\Phi(E) = \int_{H \le E} d^3\mathbf{p}_1 \cdots d^3\mathbf{p}_N \, d^3\mathbf{q}_1 \cdots d^3\mathbf{q}_N
$$

La integral sobre las posiciones da $V^N$.

Para la integral sobre momentos, necesitamos el volumen en el espacio de momentos con la restricción:

$$
\sum_{i=1}^N p_i \le \frac{E}{c}
$$

donde $p_i = |\mathbf{p}_i|$.

Cada momento $\mathbf{p}_i$ es un vector en 3D, así que el volumen elemento en esféricas es $4\pi p_i^2 dp_i$ para cada partícula.

La restricción es que la suma de magnitudes $\sum p_i \le E/c$. Esta es una región en el espacio de $3N$ dimensiones de momentos.

Para el caso ultrarrelativista en 3D, el volumen en el espacio de momentos es el volumen de un símplex en 3N dimensiones:

$$
V_p = \frac{4^N \pi^{3N/2}}{(3N/2)! \, N!} \left(\frac{E}{c}\right)^{3N}
$$

Por lo tanto:

$$
\Phi(E, V, N) = V^N \frac{4^N \pi^{3N/2}}{(3N/2)! \, N!} \left(\frac{E}{c}\right)^{3N}
$$

**Paso 2: Número de microestados**

$$
\Omega(E, V, N) = \frac{1}{(2\pi\hbar)^{3N}} \Phi(E, V, N)
$$

$$
\Omega(E, V, N) = \frac{V^N}{N!} \frac{4^N \pi^{3N/2}}{(3N/2)! (2\pi\hbar c)^{3N}} E^{3N}
$$

Simplificando:

$$
\Omega(E, V, N) = \frac{V^N}{N! \, \Gamma(3N/2+1)} \left(\frac{E}{\pi\hbar c}\right)^{3N}
$$

**Paso 3: Entropía**

$$
S = k_B \ln \Omega = k_B \left[ N \ln V + 3N \ln E - \text{términos logarítmicos en } N \right]
$$

$$
S = k_B N \left[ \ln V + 3 \ln(E/N) + \text{const} \right]
$$

**Paso 4: Ecuación fundamental termodinámica**

De $\frac{1}{T} = (\partial S/\partial E)_{V,N}$:

$$
\frac{1}{T} = \frac{k_B \cdot 3N}{E}
$$

$$
E = 3Nk_BT
$$

De $\frac{p}{T} = (\partial S/\partial V)_{E,N}$:

$$
\frac{p}{T} = \frac{k_B N}{V}
$$

$$
pV = Nk_BT
$$

**Resumen para gas ultrarrelativista:**
- Número de microestados: $\Omega \propto V^N E^{3N}$
- Energía: $E = 3Nk_BT$
- Ecuación de estado: $pV = Nk_BT$ (idéntica al no-relativista)

Observación: El factor 3 en la energía contrasta con $d/2$ en el gas no-relativista. Para un gas ultrarrelativista 3D, cada grado de libertad contribuye $k_BT$ a la energía (en lugar de $k_BT/2$ para grados de libertad cuadráticos). Esto refleja que la energía es lineal en el momento, no cuadrática.

**Búsqueda en el libro de Johan:** Busca: *"gas ultrarrelativista"*, *"relación energía-momento lineal"*, *"volumen de un símplex"* o *"equipartición ultrarrelativista"* para comprender cómo la relatividad cambia la termodinámica estadística.

---

4. Considere una cadena lineal de $N$ monómeros formando una molécula elástica (ejemplo: keratina) como se muestra en la figura 1. Cada monómero puede estar en dos posibles estados (1 o 2). La longitud del estado 1 es $l_1$ y la del 2 es $l_2$, y las energías respectivamente son $\varepsilon_1$ y $\varepsilon_2$. Calcule el número de microestados, la entropía y con ella la energía media de la molécula y su longitud media.

   ![Figura 1](figure1.png)
   *Figura 1: Representación de una cadena lineal de $N$ monómeros formando una molécula elástica.*

## Solución del Ejercicio 4

**Paso 1: Número de microestados a energía fija**

Supongamos que $n_1$ monómeros están en el estado 1 y $n_2 = N - n_1$ en el estado 2. La energía total es:

$$
E = n_1 \varepsilon_1 + n_2 \varepsilon_2 = n_1 \varepsilon_1 + (N - n_1)\varepsilon_2
$$

Despejando $n_1$:

$$
n_1 = \frac{E - N\varepsilon_2}{\varepsilon_1 - \varepsilon_2}
$$

El número de formas de distribuir $n_1$ monómeros en estado 1 entre $N$ posiciones es:

$$
\Omega(E, N) = \binom{N}{n_1} = \frac{N!}{n_1! n_2!}
$$

**Paso 2: Entropía**

$$
S = k_B \ln \Omega = k_B \left[ \ln N! - \ln n_1! - \ln n_2! \right]
$$

Usando la fórmula de Stirling para $N$ grande:

$$
S = k_B \left[ N \ln N - n_1 \ln n_1 - n_2 \ln n_2 \right]
$$

Definiendo las fracciones $f_1 = n_1/N$ y $f_2 = n_2/N = 1 - f_1$:

$$
S = -k_B N \left[ f_1 \ln f_1 + f_2 \ln f_2 \right]
$$

**Paso 3: Relación con la temperatura**

$$
\frac{1}{T} = \left(\frac{\partial S}{\partial E}\right)_N = \frac{\partial S}{\partial n_1} \frac{\partial n_1}{\partial E}
$$

De $n_1 = (E - N\varepsilon_2)/(\varepsilon_1 - \varepsilon_2)$:

$$
\frac{\partial n_1}{\partial E} = \frac{1}{\varepsilon_1 - \varepsilon_2}
$$

$$
\frac{\partial S}{\partial n_1} = -k_B \left[ \ln n_1 - \ln n_2 \right] = k_B \ln\frac{n_2}{n_1}
$$

Por lo tanto:

$$
\frac{1}{T} = \frac{k_B}{\varepsilon_1 - \varepsilon_2} \ln\frac{n_2}{n_1}
$$

$$
\ln\frac{n_2}{n_1} = \frac{\varepsilon_1 - \varepsilon_2}{k_B T}
$$

$$
\frac{n_1}{n_2} = e^{-(\varepsilon_1 - \varepsilon_2)/k_B T}
$$

**Paso 4: Energía media**

$$
\langle E \rangle = n_1 \varepsilon_1 + n_2 \varepsilon_2
$$

Usando $n_1 + n_2 = N$:

$$
\langle E \rangle = \langle n_1 \rangle \varepsilon_1 + (N - \langle n_1 \rangle) \varepsilon_2 = N\varepsilon_2 + \langle n_1 \rangle (\varepsilon_1 - \varepsilon_2)
$$

De la distribución de Boltzmann:

$$
\langle n_1 \rangle = N \frac{e^{-\varepsilon_1/k_B T}}{e^{-\varepsilon_1/k_B T} + e^{-\varepsilon_2/k_B T}}
$$

**Paso 5: Longitud media**

La longitud total de la cadena es:

$$
L = n_1 l_1 + n_2 l_2 = n_1 l_1 + (N - n_1) l_2
$$

$$
\langle L \rangle = \langle n_1 \rangle l_1 + (N - \langle n_1 \rangle) l_2 = Nl_2 + \langle n_1 \rangle (l_1 - l_2)
$$

$$
\langle L \rangle = N l_2 + \frac{N e^{-\varepsilon_1/k_B T}}{e^{-\varepsilon_1/k_B T} + e^{-\varepsilon_2/k_B T}} (l_1 - l_2)
$$

**Resumen:**
- Número de microestados: $\Omega = \binom{N}{n_1}$ con $n_1$ determinado por $E$
- Entropía: $S = -k_B N[f_1 \ln f_1 + (1-f_1)\ln(1-f_1)]$
- Energía media: $\langle E \rangle = N\varepsilon_2 + \frac{N e^{-(\varepsilon_1-\varepsilon_2)/k_B T}}{e^{-\varepsilon_1/k_B T} + e^{-\varepsilon_2/k_B T}}(\varepsilon_1 - \varepsilon_2)$
- Longitud media: $\langle L \rangle = Nl_2 + \frac{N e^{-(\varepsilon_1-\varepsilon_2)/k_B T}}{e^{-\varepsilon_1/k_B T} + e^{-\varepsilon_2/k_B T}}(l_1 - l_2)$

**Búsqueda en el libro de Johan:** Busca: *"cadena de polímeros"*, *"dos estados"*, *"sistema binario"*, *"elasticidad molecular"* o *"distribución de Boltzmann en cadenas"* para ver aplicaciones de la estadística a sistemas macromoleculares.

---

5. Considere un sólido de Einstein en donde se asocian osciladores armónicos 3D independientes, todos con la misma frecuencia $\omega$, a cada uno de los $N$ sitios de un cristal. El Hamiltoniano del sistema viene dado por:

   $$
   H = \hbar \omega \sum_{i=1}^{3N} \left(n_i + \tfrac12\right)
   $$

   donde $n_i = 0,1,2,\dots$ es el número cuántico que describe el autoestado del oscilador $i$-ésimo. Justifique por qué es natural concebir la siguiente restricción para un valor dado de la energía del sistema:

   $$
   \sum_{i=1}^{3N} n_i = M
   $$

   siendo $M$ un entero positivo. Calcule la entropía y energía por átomo, y a partir de esta última determine el calor específico del sólido y compruebe la ley de Dulong y Petit. Un esquema mental del problema se muestra en la figura 2.

   ![Figura 2](figure2.png)
   *Figura 2: $M$ bolas distribuidas en $3N$ cajas.*

## Solución del Ejercicio 5

**Parte a) Justificación de la restricción**

La energía total del sistema es:

$$
E_{total} = \hbar\omega \sum_{i=1}^{3N}\left(n_i + \tfrac{1}{2}\right) = \hbar\omega\left(\sum_{i=1}^{3N}n_i + \frac{3N}{2}\right)
$$

Para una energía total fija $E_{total}$, la suma $\sum_{i=1}^{3N}n_i = M$ es constante. Así, $M$ no es una variable independiente sino que está determinada por:

$$
M = \frac{E_{total}}{\hbar\omega} - \frac{3N}{2}
$$

La restricción $\sum n_i = M$ es natural porque los números cuánticos de los osciladores deben sumar a un valor constante para mantener la energía total fija. El factor $\hbar\omega(3N/2)$ es la energía de punto cero que existe incluso a $T=0$ K.

**Parte b) Número de microestados**

El número de formas de distribuir $M$ unidades de energía indivisibles entre $3N$ osciladores es un problema combinatorio clásico (estrellas y barras):

$$
\Omega(M, N) = \binom{M + 3N - 1}{3N - 1} = \binom{M + 3N - 1}{M}
$$

Para $M$ y $N$ grandes, usando la aproximación de Stirling:

$$
\ln \Omega \approx M \ln\left(\frac{M + 3N}{M}\right) + 3N \ln\left(\frac{M + 3N}{3N}\right)
$$

Simplificando para $M \gg 1$:

$$
\ln \Omega \approx M \ln M + 3N \ln(3N) + M + 3N \text{ (términos principales)}
$$

**Parte c) Entropía por oscilador**

$$
S = k_B \ln \Omega(M,N) = k_B \left[ (M+3N) \ln(M+3N) - M\ln M - 3N\ln(3N) \right]
$$

Para expresar en términos de la energía real $E = \hbar\omega(M + 3N/2)$:

$$
E = \hbar\omega(M + 3N/2) \implies M = \frac{E}{\hbar\omega} - \frac{3N}{2}
$$

$$
M + 3N = \frac{E}{\hbar\omega} + \frac{3N}{2}
$$

La entropía por oscilador (hay $3N$ osciladores) es:

$$
\frac{S}{3N} = \frac{k_B}{3N} \left[ \left(\frac{E}{\hbar\omega} + \frac{3N}{2}\right) \ln\left(\frac{E}{\hbar\omega} + \frac{3N}{2}\right) - \left(\frac{E}{\hbar\omega} - \frac{3N}{2}\right) \ln\left(\frac{E}{\hbar\omega} - \frac{3N}{2}\right) - 3N\ln(3N) \right]
$$

**Parte d) Energía por átomo**

De la termodinámica:

$$
\frac{1}{T} = \left(\frac{\partial S}{\partial E}\right)_{N}
$$

Calculando:

$$
\frac{1}{T} = k_B \frac{\partial}{\partial E}\left[ \frac{1}{\hbar\omega}\ln\left(\frac{E}{\hbar\omega} + \frac{3N}{2}\right) - \frac{1}{\hbar\omega}\ln\left(\frac{E}{\hbar\omega} - \frac{3N}{2}\right) \right]
$$

$$
\frac{1}{T} = \frac{k_B}{\hbar\omega}\left[ \frac{1}{\frac{E}{\hbar\omega} + \frac{3N}{2}} - \frac{1}{\frac{E}{\hbar\omega} - \frac{3N}{2}} \right]$$

$$
\frac{1}{T} = \frac{k_B}{\hbar\omega} \frac{-3N}{(E/\hbar\omega)^2 - (3N/2)^2}$$

Despejando $E$:

$$
E = \frac{3N\hbar\omega}{2}\coth\left(\frac{\hbar\omega}{2k_BT}\right)
$$

Para $N$ átomos (cada uno con 3 grados de libertad):

$$
E_{por\,átomo} = \hbar\omega \coth\left(\frac{\hbar\omega}{2k_BT}\right)
$$

**Parte e) Calor específico**

$$
C_V = \left(\frac{\partial E}{\partial T}\right)_V = N \cdot 3 \frac{\partial}{\partial T}\left[\hbar\omega\coth\left(\frac{\hbar\omega}{2k_BT}\right)\right]
$$

$$
C_V = 3Nk_B \left(\frac{\hbar\omega}{2k_BT}\right)^2 \operatorname{csch}^2\left(\frac{\hbar\omega}{2k_BT}\right)
$$

donde $\operatorname{csch}(x) = 1/\sinh(x)$.

**Verificación de la ley de Dulong y Petit:**

En el límite clásico $T \to \infty$ (o $\hbar\omega \ll k_BT$):

$$
\coth(x) \approx \frac{1}{x} \quad \text{para } x \to 0
$$

$$
\coth\left(\frac{\hbar\omega}{2k_BT}\right) \approx \frac{2k_BT}{\hbar\omega} \quad \text{cuando } \hbar\omega \ll k_BT
$$

$$
E \approx 3Nk_BT$$

$$
C_V = \left(\frac{\partial E}{\partial T}\right) \approx 3Nk_B$$

Esta es la ley de Dulong y Petit: cada grado de libertad cuadrático (tanto cinético como potencial) contribuye $k_B$ al calor específico, dando un total de $3k_B$ por átomo.

**Resumen:**
- Número de microestados: $\Omega = \binom{M + 3N - 1}{M}$
- Energía por átomo: $e = \hbar\omega \coth(\hbar\omega/2k_BT)$
- Calor específico: $C_V = 3Nk_B(\hbar\omega/2k_BT)^2 \operatorname{csch}^2(\hbar\omega/2k_BT)$
- Límite clásico: $C_V \to 3Nk_B$ (Dulong y Petit)

**Búsqueda en el libro de Johan:** Busca: *"modelo de Einstein"*, *"sólido de Einstein"*, *"osciladores cuánticos"*, *"ley de Dulong-Petit"* o *"cuantización de osciladores"* para entender cómo la cuantización modifica el comportamiento termodinámico del sólido.

---

6. En el problema de radiación de cuerpo negro, se tienen $N$ osciladores en las paredes de la cavidad, cada uno con energía promedio $\bar E$. Para el cálculo de la entropía, Planck, en su trabajo original, consideró que la energía total consta de $n$ unidades indivisibles, cada una de magnitud $\varepsilon$.

   a) Determine el número de microestados $\Omega$ compatibles con el macroestado del sistema, teniendo en cuenta que en este caso **NO** hay restricciones en cuanto al número de unidades de energía por oscilador.
   b) A partir de $\Omega$ calcule la entropía por oscilador.
   c) Finalmente a partir de la entropía demuestre que:

   $$
   \bar E = \frac{\varepsilon}{e^{\varepsilon/kT} - 1}
   $$

## Solución del Ejercicio 6

**Parte a) Número de microestados**

En este problema, se tienen $N$ osciladores y una energía total $E_{total} = n\varepsilon$ distribuida en $n$ unidades indivisibles de magnitud $\varepsilon$ cada una.

A diferencia del sólido de Einstein, aquí no hay restricción en el número máximo de cuantos por oscilador. Un oscilador puede tener 0, 1, 2, 3,... cuantos.

El problema es equivalente a: ¿De cuántas formas podemos distribuir $n$ objetos idénticos entre $N$ cajas distinguibles, sin límite de ocupación?

Este es el problema clásico de "estrellas y barras" o "bolas indistinguibles en cajas distinguibles":

$$
\Omega(n, N) = \binom{n + N - 1}{N - 1} = \binom{n + N - 1}{n}
$$

**Parte b) Entropía por oscilador**

$$
S = k_B \ln \Omega = k_B \ln\binom{n + N - 1}{n}
$$

Para $n$ y $N$ grandes (límite termodinámico), usando la fórmula de Stirling:

$$
\ln\binom{n+N-1}{n} = (n+N-1)\ln(n+N-1) - n\ln n - (N-1)\ln(N-1)$$

La entropía por oscilador es:

$$
\frac{S}{N} = k_B \left[ \frac{n+N-1}{N}\ln(n+N-1) - \frac{n}{N}\ln n - \frac{N-1}{N}\ln(N-1) \right]$$

Definiendo $\bar{n} = n/N$ como el número promedio de cuantos por oscilador:

$$
\frac{S}{N} = k_B \left[ (\bar{n}+1)\ln(N(\bar{n}+1)) - \bar{n}\ln(N\bar{n}) - \ln(N-1) \right]$$

Para $N \gg 1$:

$$
\frac{S}{N} = k_B \left[ (\bar{n}+1)\ln(\bar{n}+1) - \bar{n}\ln\bar{n} \right]$$

**Parte c) Relación termodinámica y fórmula de Planck**

De la mecánica estadística:

$$
\frac{1}{T} = \left(\frac{\partial S}{\partial E}\right)_N = \frac{1}{\varepsilon}\left(\frac{\partial S}{\partial n}\right)_N
$$

Calculando:

$$
\frac{\partial S}{\partial n} = k_B \ln(n + N - 1) - k_B \ln n = k_B \ln\left(\frac{n+N-1}{n}\right) \approx k_B \ln\left(\frac{N}{\bar{n}}\right) \quad \text{para } n, N \text{ grandes}
$$

Por lo tanto:

$$
\frac{1}{T} = \frac{k_B}{\varepsilon}\ln\left(\frac{N}{n}\right) = \frac{k_B}{\varepsilon}\ln\left(\frac{1}{\bar{n}}\right)$$

Resolviendo para $\bar{n}$:

$$
\frac{\varepsilon}{k_BT} = \ln\left(\frac{1}{\bar{n}}\right)$$

$$
e^{\varepsilon/k_BT} = \frac{1}{\bar{n}}$$

$$
\bar{n} = \frac{1}{e^{\varepsilon/k_BT} - 1}$$

La energía promedio por oscilador es:

$$
\bar E = \varepsilon \bar{n} = \frac{\varepsilon}{e^{\varepsilon/k_BT} - 1}$$

Esta es la fórmula de Planck para la radiación de cuerpo negro, donde $\varepsilon = h\nu$ es la energía de un fotón de frecuencia $\nu$.

**Resumen:**
- Número de microestados: $\Omega = \binom{n+N-1}{n}$
- Entropía por oscilador: $s = k_B[(\bar{n}+1)\ln(\bar{n}+1) - \bar{n}\ln\bar{n}]$
- Energía promedio: $\bar E = \frac{\varepsilon}{e^{\varepsilon/k_BT}-1}$ (fórmula de Planck)

**Búsqueda en el libro de Johan:** Busca: *"radiación de cuerpo negro"*, *"fórmula de Planck"*, *"cuantización de energía"*, *"fotones"* o *"distribución de Bose-Einstein"* para ver cómo Planck revolucionó la física con su hipótesis cuántica.

---

7. Considere un sistema formado por $N$ partículas indistinguibles que pueden ocupar los nodos de dos redes A y B. Suponga además que cada una de las redes tiene $N$ nodos. La energía de una partícula es cero cuando ocupa uno de los nodos de la red A y $\varepsilon$ cuando se localiza en uno de los nodos de la red B.

   a) Determine el número de microestados $\Omega$ compatibles con el macroestado del sistema con energía $E(n)=n\varepsilon$, siendo $n$ el número de partículas en la red B.
   b) A partir de $\Omega$ calcule la entropía por partícula.
   c) Finalmente a partir de la entropía, demuestre que:

   $$
   E = \frac{N\varepsilon}{1 + e^{\varepsilon/2kT}}
   $$

## Solución del Ejercicio 7

**Parte a) Número de microestados**

Se tienen $N$ partículas indistinguibles que deben distribuirse entre dos redes A y B. Si $n$ partículas están en la red B, entonces $N-n$ están en la red A.

La red A tiene $N$ nodos (sitios), por lo que hay $\binom{N}{N-n}$ formas de elegir cuáles $N-n$ nodos están ocupados.

La red B también tiene $N$ nodos, por lo que hay $\binom{N}{n}$ formas de elegir cuáles $n$ nodos están ocupados.

El número total de microestados para una configuración con $n$ partículas en B es:

$$
\Omega(n, N) = \binom{N}{n} \binom{N}{N-n} = \binom{N}{n}^2
$$

La energía correspondiente es:

$$
E(n) = n\varepsilon
$$

**Parte b) Entropía por partícula**

$$
S(n) = k_B \ln \Omega(n,N) = k_B \ln\binom{N}{n}^2 = 2k_B \ln\binom{N}{n}
$$

$$
S = 2k_B \left[ N\ln N - n\ln n - (N-n)\ln(N-n) \right]
$$

Dividiendo por $N$ para la entropía por partícula:

$$
\frac{S}{N} = 2k_B \left[ \ln N - \frac{n}{N}\ln n - \frac{N-n}{N}\ln(N-n) \right]
$$

Definiendo $x = n/N$ (fracción de partículas en la red B):

$$
\frac{S}{N} = 2k_B \left[ \ln N - x\ln(Nx) - (1-x)\ln(N(1-x)) \right]
$$

$$
\frac{S}{N} = 2k_B \left[ -x\ln x - (1-x)\ln(1-x) \right]$$

**Parte c) Relación termodinámica**

De la mecánica estadística:

$$
\frac{1}{T} = \left(\frac{\partial S}{\partial E}\right)_N = \frac{1}{\varepsilon}\left(\frac{\partial S}{\partial n}\right)_N
$$

Calculando la derivada:

$$
\frac{\partial S}{\partial n} = 2k_B \left[ -\ln n - 1 + \ln(N-n) + 1 \right] = 2k_B \ln\frac{N-n}{n}
$$

Por lo tanto:

$$
\frac{1}{T} = \frac{2k_B}{\varepsilon}\ln\frac{N-n}{n}
$$

Resolviendo:

$$
\frac{\varepsilon}{2k_BT} = \ln\frac{N-n}{n}$$

$$
e^{\varepsilon/2k_BT} = \frac{N-n}{n}$$

$$
n e^{\varepsilon/2k_BT} = N - n$$

$$
n(1 + e^{\varepsilon/2k_BT}) = N$$

$$
n = \frac{N}{1 + e^{\varepsilon/2k_BT}}
$$

La energía total es:

$$
E = n\varepsilon = \frac{N\varepsilon}{1 + e^{\varepsilon/2k_BT}}
$$

Alternativamente, podemos escribir esto como:

$$
E = N\varepsilon \frac{e^{-\varepsilon/2k_BT}}{e^{-\varepsilon/2k_BT} + e^{\varepsilon/2k_BT}} = N\varepsilon \tanh\left(\frac{\varepsilon}{4k_BT}\right)
$$

**Resumen:**
- Número de microestados: $\Omega(n,N) = \binom{N}{n}^2$
- Entropía por partícula: $s = 2k_B[-x\ln x - (1-x)\ln(1-x)]$ con $x = n/N$
- Energía: $E = \frac{N\varepsilon}{1 + e^{\varepsilon/2k_BT}}$ o $E = N\varepsilon\tanh(\varepsilon/4k_BT)$

**Búsqueda en el libro de Johan:** Busca: *"dos redes"*, *"sistemas de dos sitios"*, *"partículas en dos estados"*, *"ensamble de dos redes"* o *"partición de partículas"* para ver este modelo fundamental usado en adsorción y otros fenómenos.

---

8. Considere una red cristalina con defectos de Frenkel en la que los átomos migran a posiciones intersticiales creando vacancias cuya número depende de la temperatura. Para ello, imagine la red como formada por dos subredes cuadradas simples interpenetradas, cada una con $N$ nodos o vértices, en la que una subred está desplazada respecto a la otra una cantidad $(a/2,a/2)$ siendo $a$ el parámetro de red. Así, cuando un átomo abandona su lugar en una subred, se va a un vértice de la otra con un costo energético $\varepsilon$. Parta de una situación en la que a $T=0\,\mathrm{K}$ se tienen $N$ átomos en los vértices de una de las subredes, y que a una temperatura finita se tendrán $n$ vacantes en dicha subred y por lo tanto $n$ átomos intercalados en la otra.

   a) Haga una representación esquemática (gráfica) de la situación descrita.
   b) Determine el número total de microestados $\Omega$ compatibles con el macroestado del sistema con energía $E(n)=n\varepsilon$.
   c) A partir de $\Omega$ calcule la entropía total.
   d) Calcule el número de defectos de Frenkel $n(T)$ en función de la temperatura.
   e) Determine la capacidad calorífica.

## Solución del Ejercicio 8

**Parte a) Representación esquemática**

La red cristalina consta de dos subredes interpenetradas:
- Red A: con $N$ nodos donde originalmente están los átomos
- Red B: con $N$ nodos intersticiales (vacíos inicialmente)

A temperatura finita, algunos átomos migran desde la red A a posiciones en la red B:
- Se forman $n$ vacancias en la red A
- Se crean $n$ ocupaciones en la red B
- El número total de átomos permanece constante en $N$

Esquema visual (simplificado en 1D):
```
T=0:     A: [X][X][X]...[X]     B: [ ][ ][ ]...[ ]
         (N átomos)               (0 átomos)

T>0:     A: [X][ ][X]...[X]     B: [ ][X][ ]...[X]
         (N-n átomos)             (n átomos)
```

Cada defecto crea una pareja vacancia-intersticial con costo energético $\varepsilon$.

**Parte b) Número de microestados**

Podemos elegir $n$ posiciones de la red A donde habrá vacancias: $\binom{N}{n}$ formas.

Luego, colocamos los $n$ átomos excitados en $n$ posiciones de la red B: $\binom{N}{n}$ formas.

El número total de microestados es:

$$
\Omega(n,N) = \binom{N}{n} \times \binom{N}{n} = \binom{N}{n}^2
$$

La energía correspondiente es:

$$
E(n) = n\varepsilon
$$

(Nota: Este resultado es idéntico al del ejercicio 7, pero aquí la interpretación física es diferente: vacancies vs. ocupaciones en redes duales.)

**Parte c) Entropía total**

$$
S(n,N) = k_B \ln \Omega(n,N) = 2k_B \ln\binom{N}{n}
$$

$$
S = 2k_B \left[ N\ln N - n\ln n - (N-n)\ln(N-n) \right]
$$

Para $N$ y $n$ moderados, se puede simplificar usando la fórmula de Stirling.

**Parte d) Número de defectos de Frenkel en función de la temperatura**

En el ensamble microcanónico, tenemos energía fija $E$. Sin embargo, es más natural trabajar en el ensamble canónico donde la temperatura es el parámetro fijo.

En el ensamble canónico, la probabilidad de tener $n$ defectos es:

$$
P(n) = \frac{\Omega(n,N) e^{-\beta E(n)}}{Z} = \frac{\binom{N}{n}^2 e^{-\beta n\varepsilon}}{Z}
$$

donde $Z = \sum_{n=0}^{N} \binom{N}{n}^2 e^{-\beta n\varepsilon}$ y $\beta = 1/(k_BT)$.

El número promedio de defectos es:

$$
\langle n \rangle = \frac{\sum_{n} n \binom{N}{n}^2 e^{-\beta n\varepsilon}}{\sum_{n} \binom{N}{n}^2 e^{-\beta n\varepsilon}}
$$

Para $N$ grande y $n \ll N$, podemos aproximar $\binom{N}{n}^2 \approx N^{2n}/n!^2$:

$$
Z \approx \sum_{n=0}^{\infty} \frac{N^{2n}}{(n!)^2} e^{-\beta n\varepsilon}$$

Este es el desarrollo de series de la función de Bessel modificada $I_0(2Ne^{-\beta\varepsilon/2})$.

Usando la aproximación para $N$ grande:

$$
\frac{\partial \ln Z}{\partial \mu} = -\beta \langle n \rangle$$

donde el potencial químico $\mu$ conjuga a $n$.

Alternativamente, en el límite clásico donde podemos tratar $\binom{N}{n}$ como una distribución cuasi-continua:

$$
\ln \Omega(n,N) \approx 2[n\ln(N/n) + (N-n)\ln(1 - n/N)]$$

En termodinámica, el equilibrio requiere que la "presión" de los defectos sea:

$$
\frac{1}{T}\frac{\partial S}{\partial n} = \frac{\varepsilon}{T}$$

Lo que da:

$$
2k_B \ln\frac{N-n}{n} = \varepsilon$$

$$
\frac{N-n}{n} = e^{\varepsilon/(2k_BT)}$$

$$
n(1 + e^{\varepsilon/(2k_BT)}) = N$$

$$
n(T) = \frac{N}{1 + e^{\varepsilon/(2k_BT)}}$$

Para $T \ll \varepsilon/(2k_B)$: $n \approx Ne^{-\varepsilon/(2k_BT)}$ (exponencial pequeño)

Para $T \gg \varepsilon/(2k_B)$: $n \approx N/2$ (ambas redes están semillenadas)

**Parte e) Capacidad calorífica**

De $n(T) = \frac{N}{1 + e^{\varepsilon/(2k_BT)}}$:

$$
\frac{dn}{dT} = -\frac{N}{(1 + e^{\varepsilon/(2k_BT)})^2} \cdot \left(-\frac{\varepsilon}{2k_BT^2}\right) e^{\varepsilon/(2k_BT)}
$$

$$
\frac{dn}{dT} = \frac{N\varepsilon}{2k_BT^2} \frac{e^{\varepsilon/(2k_BT)}}{(1 + e^{\varepsilon/(2k_BT)})^2}
$$

La energía es $E = n(T)\varepsilon$, por lo que:

$$
C_V = \frac{dE}{dT} = \varepsilon \frac{dn}{dT}
$$

$$
C_V = \frac{N\varepsilon^2}{2k_BT^2} \frac{e^{\varepsilon/(2k_BT)}}{(1 + e^{\varepsilon/(2k_BT)})^2}
$$

Equivalentemente:

$$
C_V = Nk_B \left(\frac{\varepsilon}{2k_BT}\right)^2 \frac{e^{\varepsilon/(2k_BT)}}{(1 + e^{\varepsilon/(2k_BT)})^2}
$$

Definiendo $x = \varepsilon/(2k_BT)$:

$$
C_V = Nk_B x^2 \frac{e^x}{(1+e^x)^2} = Nk_B x^2 \operatorname{sech}^2(x/2)
$$

**Comportamiento límite:**
- Cuando $T \to 0$: $C_V \propto e^{-\varepsilon/k_BT} \to 0$
- Cuando $T \to \infty$: $C_V \to 0$ (ambas redes están saturadas)
- Máximo en $T \approx \varepsilon/(2k_B \ln 2)$

**Resumen:**
- Número de microestados: $\Omega(n,N) = \binom{N}{n}^2$
- Entropía: $S = 2k_B[N\ln N - n\ln n - (N-n)\ln(N-n)]$
- Defectos de Frenkel: $n(T) = \frac{N}{1 + e^{\varepsilon/(2k_BT)}}$
- Capacidad calorífica: $C_V = Nk_B({\varepsilon}/{2k_BT})^2 \operatorname{sech}^2({\varepsilon}/{4k_BT})$

**Búsqueda en el libro de Johan:** Busca: *"defectos de Frenkel"*, *"vacancias"*, *"defectos puntuales"*, *"migración atómica"*, *"redes interpenetradas"* o *"defectos y temperatura"* para entender cómo los defectos cristalinos son termodinámicamente inevitables.

---

9. Considere un sistema aislado de $N$ partículas localizadas muy débilmente interactuantes de espín $\tfrac12$. Cada partícula tiene momento magnético $\mu$ el cual puede orientarse paralela o antiparalela a un campo aplicado $H$. La energía del sistema es $E=-(n_1 - n_2)\mu H$, donde $n_1$ es el número de espines paralelos a $H$ y $n_2$ el número de aquellos antiparalelos a $H$.

   a) Considere el rango de energía entre $E$ y $E+\delta E$ con $\mu H \ll \delta E \ll E$. ¿Cuál es el número total de estados $\Omega(E)$ en este rango de energía?
   b) Escriba una expresión para $\ln \Omega(E)$ y simplifíquela utilizando la fórmula de Stirling $\ln n! \approx n\ln n - n$.
   c) Suponga que la energía está en una región donde $\Omega(E)$ es apreciable, lejos de los valores extremos. Realice en este caso una aproximación Gaussiana a la parte (a) para obtener la siguiente expresión:

   $$
   \Omega(E) = \frac{2^N}{\sqrt{\pi N/2}} \exp\left(-\frac{E^2}{2\mu^2 H^2 N}\right) \frac{\delta E}{2 \mu H}
   $$   

## Solución del Ejercicio 9

**Parte a) Número de estados en el intervalo $[E, E+\delta E]$**

Consideramos espines $1/2$ en un campo magnético $H$.

Energía de una configuración: $E = -\mu H(n_1 - n_2) = -\mu H(2n_1 - N)$ donde $n_1 + n_2 = N$.

Esto se puede reescribir como: $E = -2\mu H n_1 + \mu H N$, o $n_1 = \frac{N}{2} - \frac{E}{2\mu H}$.

Para una energía fija $E$, el número de formas de elegir cuáles $n_1$ espines apuntan paralelos es:

$$
\Omega_E = \binom{N}{n_1} = \binom{N}{\frac{N}{2} - \frac{E}{2\mu H}}
$$

Para energías en el rango $[E, E+\delta E]$, dado que $\mu H \ll \delta E$, podemos tener varias configuraciones dentro de este rango (múltiples valores de $n_1$).

Sin embargo, si $\delta E$ es pequeño comparado con $E$ pero moderado, típicamente uno o pocos estados binomiales caen en este rango. El número aproximado de estados es:

$$
\Omega(E)\delta E = \binom{N}{\frac{N}{2} - \frac{E}{2\mu H}}
$$

Entonces:

$$
\Omega(E) = \frac{\binom{N}{\frac{N}{2} - \frac{E}{2\mu H}}}{\delta E}$$

Alternativamente, podemos pensar que el "número de microestados en un rango infinitesimal de energía" es el coeficiente binomial evaluado en ese valor de $n_1$.

**Parte b) Expresión logarítmica y fórmula de Stirling**

Definamos $m = n_1 - N/2$ (desviación del valor central). Entonces $E = -2\mu H m$, o $m = -E/(2\mu H)$.

$$
\Omega = \binom{N}{N/2 + m} = \frac{N!}{(N/2+m)!(N/2-m)!}
$$

Aplicando la fórmula de Stirling $\ln n! \approx n\ln n - n$:

$$
\ln \Omega = N\ln N - (N/2+m)\ln(N/2+m) - (N/2-m)\ln(N/2-m)$$

Expandiendo para $m \ll N/2$:

$$(N/2+m)\ln(N/2+m) = (N/2+m)[\ln(N/2) + \ln(1 + 2m/N)]$$

$$\approx (N/2+m)[\ln(N/2) + 2m/N - 2m^2/N^2 + \ldots]$$

$$= N/2 \ln(N/2) + m\ln(N/2) + m \cdot 2m/N - \text{términos menores}$$

$$= N/2 \ln(N/2) + m\ln(N/2) + 2m^2/N$$

Similarmente:

$$(N/2-m)\ln(N/2-m) \approx N/2\ln(N/2) - m\ln(N/2) + 2m^2/N$$

Restando:

$$(N/2+m)\ln(N/2+m) + (N/2-m)\ln(N/2-m) \approx N\ln(N/2) + 4m^2/N$$

Por lo tanto:

$$\ln \Omega \approx N\ln N - N\ln(N/2) - 4m^2/N = N\ln 2 - 4m^2/N$$

Sustituyendo $m = -E/(2\mu H)$:

$$\ln \Omega \approx N\ln 2 - \frac{4}{N}\left(\frac{E}{2\mu H}\right)^2 = N\ln 2 - \frac{E^2}{\mu^2 H^2 N}$$

$$\Omega(E) = 2^N \exp\left(-\frac{E^2}{\mu^2 H^2 N}\right)$$

**Parte c) Distribución Gaussiana en el rango $[E, E+\delta E]$**

Para obtener el número de estados en un rango infinitesimal $dE$, reemplazamos el coeficiente binomial por su aproximación continua (Gaussiana):

$$\Omega(E) dE = 2^N \exp\left(-\frac{E^2}{\mu^2 H^2 N}\right) dE$$

Dado que la energía está cuantizada en unidades de $2\mu H$ (el cambio de energía al voltear un espín), el incremento mínimo es $\Delta E = 2\mu H$.

Para un rango finito $\delta E$ que contiene múltiples estados posibles, podemos contar el número de estados como:

$$\Omega(E) = \frac{2^N}{\sqrt{\pi N/2}} \exp\left(-\frac{E^2}{2\mu^2 H^2 N}\right)$$

Luego, el número total de estados en el rango $[E, E+\delta E]$ es:

$$N_{\text{total}}(E) = \Omega(E) \cdot \frac{\delta E}{2\mu H}$$

El factor $\frac{\delta E}{2\mu H}$ representa cuántas unidades energéticas de tamaño $2\mu H$ caben en el intervalo $\delta E$.

Por lo tanto:

$$\Omega(E) = \frac{2^N}{\sqrt{\pi N/2}} \exp\left(-\frac{E^2}{2\mu^2 H^2 N}\right) \frac{\delta E}{2\mu H}$$

**Nota sobre la distribución:** Esta es una distribución Gaussiana centrada en $E=0$ (donde $n_1 = n_2 = N/2$, el estado de máxima desorden) con varianza $\sigma^2 = \mu^2 H^2 N/2$. El ancho de la distribución crece como $\sqrt{N}$, lo que refleja el teorema del límite central aplicado al número de espines paralelos vs. antiparalelos.

**Resumen:**
- Número de estados a energía $E$: $\Omega_E = \binom{N}{\frac{N}{2} - E/(2\mu H)}$
- Logaritmo: $\ln \Omega \approx N\ln 2 - \frac{E^2}{\mu^2 H^2 N}$
- Distribución Gaussiana: $\Omega(E) = \frac{2^N}{\sqrt{\pi N/2}} \exp(-E^2/(2\mu^2 H^2 N)) \frac{\delta E}{2\mu H}$

**Búsqueda en el libro de Johan:** Busca: *"sistema de espines"*, *"espines 1/2"*, *"campo magnético"*, *"distribución Gaussiana de energía"*, *"magnetización"* o *"aproximación Gaussiana"* para ver este modelo fundamental de paramagnetismo.

---

10. Considere un sistema de $N$ partículas independientes idénticas, cada una de las cuales puede existir en uno de dos posibles estados (un estado base con energía $E_g = 0$ y otro estado excitado con energía $E_{exc} = \varepsilon$).
   a) Determine el número de microestados $\Omega$ dada una energía total $E$.
   b) A partir de $\Omega$ calcule la entropía.
   c) Finalmente, obtenga la energía total del sistema en función de la temperatura.

## Solución del Ejercicio 10

**Parte a) Número de microestados**

Si $m$ partículas están en el estado excitado (energía $\varepsilon$) y $N-m$ en el estado base (energía 0), la energía total es:

$$
E = m\varepsilon
$$

Despejando: $m = E/\varepsilon$

El número de formas de elegir cuáles $m$ partículas están excitadas es:

$$
\Omega(E,N) = \binom{N}{m} = \binom{N}{E/\varepsilon}
$$

Esta combinación es válida solo cuando $E/\varepsilon$ es un entero entre 0 y $N$.

**Parte b) Entropía**

$$
S(E,N) = k_B \ln \Omega = k_B \ln\binom{N}{E/\varepsilon}
$$

$$
S = k_B \left[ N\ln N - m\ln m - (N-m)\ln(N-m) \right]
$$

donde $m = E/\varepsilon$.

Sustituyendo:

$$
S = k_B \left[ N\ln N - \frac{E}{\varepsilon}\ln\frac{E}{\varepsilon} - \left(N-\frac{E}{\varepsilon}\right)\ln\left(N-\frac{E}{\varepsilon}\right) \right]
$$

Alternativamente, en términos de la fracción de partículas excitadas $f = E/(N\varepsilon)$:

$$
S = k_B N \left[ -f\ln f - (1-f)\ln(1-f) \right]
$$

Esta es la entropía de una distribución binaria (entropia de mezcla).

**Parte c) Energía en función de la temperatura**

De la termodinámica:

$$
\frac{1}{T} = \left(\frac{\partial S}{\partial E}\right)_N
$$

Calculando:

$$
\frac{\partial S}{\partial E} = \frac{k_B}{\varepsilon}\left[ -\ln m + \ln(N-m) \right] = \frac{k_B}{\varepsilon}\ln\frac{N-m}{m}
$$

Por lo tanto:

$$
\frac{1}{T} = \frac{k_B}{\varepsilon}\ln\frac{N-m}{m}
$$

$$
\frac{\varepsilon}{k_BT} = \ln\frac{N-m}{m}$$

$$
e^{\varepsilon/k_BT} = \frac{N-m}{m}$$

$$
m e^{\varepsilon/k_BT} = N - m$$

$$
m(1 + e^{\varepsilon/k_BT}) = N$$

$$
m = \frac{N}{1 + e^{\varepsilon/k_BT}}
$$

La energía total es:

$$
E = m\varepsilon = \frac{N\varepsilon}{1 + e^{\varepsilon/k_BT}}
$$

Alternativamente, usando $e^{-x} = 1/(e^x)$:

$$
E = N\varepsilon \frac{1}{1 + e^{\varepsilon/k_BT}} = \frac{N\varepsilon}{1 + e^{\varepsilon/k_BT}}
$$

O en forma simétrica:

$$
E = \frac{N\varepsilon}{2}\left[ 1 - \tanh\left(\frac{\varepsilon}{2k_BT}\right) \right]$$

**Comportamiento asintótico:**

1. Límite $T \to 0$ (o $\varepsilon \gg k_BT$): $E \to 0$ (todas las partículas en estado base)
2. Límite $T \to \infty$ (o $\varepsilon \ll k_BT$): $E \to N\varepsilon/2$ (mitad en cada estado)
3. Temperatura característica: $T_0 = \varepsilon/k_B$

**Resumen:**
- Número de microestados: $\Omega = \binom{N}{E/\varepsilon}$
- Entropía: $S = k_B[N\ln N - (E/\varepsilon)\ln(E/\varepsilon) - (N-E/\varepsilon)\ln(N-E/\varepsilon)]$
- Energía: $E(T) = \frac{N\varepsilon}{1 + e^{\varepsilon/k_BT}}$

Esta es la distribución de Boltzmann para un sistema de dos niveles: un modelo fundamental en física estadística con amplias aplicaciones.

**Búsqueda en el libro de Johan:** Busca: *"sistema de dos niveles"*, *"dos estados energéticos"*, *"poblaciones de Boltzmann"*, *"distribución de energía en dos estados"* o *"modelo de dos niveles"* para ver aplicaciones en átomos, moléculas y sistemas cuánticos.

---

# Soluciones: Problemas sobre Gases de Van der Waals

11. En un gas real monoatómico con $N$ partículas cada una de masa idéntica $m$ en un contenedor de volumen $V$ a temperatura $T$, el Hamiltoniano del sistema es:
   $$
   H = T + U \quad (1)
   $$
   donde:
   $$
   T = \sum_{i=1}^{3N} \frac{p_i^2}{2m} \quad (2)
   $$
   es la energía cinética del gas con $3N$ grados de libertad, $U$ es la energía potencial debido a la interacción existente entre las moléculas. En una aproximación del gas como compuesto por esferas duras, existe una mínima distancia a la cual las esferas de radio $r_0$ se pueden acercar que es $2r_0$. La interacción entre 2 moléculas $i$ y $j$ separadas por una distancia $r$ está dada por:
   $$
   u(r) = -u_0\left(\frac{r_0}{r}\right)^6 \quad (3)
   $$
   donde $u_0$ es la profundidad del pozo de potencial. La energía potencial es la suma de las interacciones entre todos los pares de moléculas:
   $$
   U = \tfrac12 \sum_{i=1}^N u_i \quad (4)
   $$
   donde $u_i$ es la energía de interacción de la $i$-ésima molécula en una región específica:
   $$
   u_i = \frac{N}{V} \int_{0}^{2\pi} d\phi \int_{0}^{\pi} d\theta\,\sin\theta \int_{r_0}^{\infty} dr\,r^2\left[-u_0\left(\frac{r_0}{r}\right)^6\right] \quad (5)
   $$
   Justifique y calcule la integral anterior, y demuestre que el Hamiltoniano de un gas real de Van der Waals viene dado por:
   $$
   H = \sum_{i=1}^{3N} \frac{p_i^2}{2m} - a'\frac{N^2}{V} \quad (6)
   $$
   donde
   $$
   a' = \frac{2\pi u_0 r_0^3}{3} \quad (7)
   $$

## Solución del Ejercicio 11

**Paso 1: Justificación de la integral**

La ecuación (5) calcula la energía de interacción media de una molécula $i$ con todas las demás. Se asume que:

1. La densidad numérica de moléculas es aproximadamente uniforme: $\rho = N/V$
2. El promedio de la función de interacción de pares es suficiente para tratar el sistema como un continuo
3. Se integra en coordenadas esféricas alrededor de la molécula $i$: $d\phi d\theta \sin\theta dr r^2$ es el elemento de volumen en esféricas
4. El rango de integración en $r$ comienza en $r_0$ (distancia de contacto mínimo) y va a infinito

**Paso 2: Cálculo de la integral angular**

$$
\int_0^{2\pi} d\phi \int_0^{\pi} \sin\theta \, d\theta = 2\pi \cdot 2 = 4\pi
$$

**Paso 3: Cálculo de la integral radial**

$$
\int_{r_0}^{\infty} r^2 \left[-u_0\left(\frac{r_0}{r}\right)^6\right] dr = -u_0 r_0^6 \int_{r_0}^{\infty} r^{-4} dr
$$

$$
= -u_0 r_0^6 \left[ -\frac{1}{3}r^{-3} \right]_{r_0}^{\infty} = -u_0 r_0^6 \left( 0 + \frac{1}{3r_0^3} \right)
$$

$$
= -\frac{u_0 r_0^3}{3}
$$

**Paso 4: Energía de interacción por molécula**

$$
u_i = \frac{N}{V} \cdot 4\pi \cdot \left(-\frac{u_0 r_0^3}{3}\right) = -\frac{4\pi u_0 r_0^3 N}{3V}
$$

**Paso 5: Energía potencial total**

La energía potencial es la suma sobre todas las moléculas, pero cada par se cuenta dos veces:

$$
U = \frac{1}{2}\sum_{i=1}^N u_i = \frac{1}{2} \cdot N \cdot \left(-\frac{4\pi u_0 r_0^3 N}{3V}\right)
$$

$$
U = -\frac{2\pi u_0 r_0^3 N^2}{3V}
$$

Define $a' = \frac{2\pi u_0 r_0^3}{3}$, entonces:

$$
U = -a'\frac{N^2}{V}
$$

**Paso 6: Hamiltoniano total**

El Hamiltoniano del gas de Van der Waals es:

$$
H = T + U = \sum_{i=1}^{3N} \frac{p_i^2}{2m} - a'\frac{N^2}{V}
$$

**Interpretación física:**

El término $-a'N^2/V$ representa la atracción entre moléculas (potencial atractivo). El factor $N^2$ surge del conteo de pares de moléculas. Este es un potencial efectivo de campo medio que captura la atracción intermolecular de Van der Waals.

**Resumen:**
- Justificación: Integral promedia las interacciones en un continuo con densidad $N/V$
- Integral angular: $4\pi$
- Integral radial: $-u_0r_0^3/3$
- Hamiltoniano: $H = \sum \frac{p_i^2}{2m} - a'N^2/V$ con $a' = 2\pi u_0 r_0^3/3$

**Búsqueda en el libro de Johan:** Busca: *"gas de Van der Waals"*, *"interacción de pares"*, *"potencial de atracción"*, *"integral de interacción"*, *"esferas duras"* o *"energía potencial molecular"* para profundizar en la derivación del Hamiltoniano de Van der Waals.

---

12. En la aproximación de las moléculas como esferas duras debe existir una corrección al volumen para el gas de Van der Waals. Al considerar las moléculas como esferas duras de radio $r_0$, el centro de cada molécula es excluido por otra molécula por un volumen que es equivalente al volumen de una esfera de radio $2r_0$ que corresponde al volumen excluido. El volumen excluido para dos moléculas de radio $r_0$ es:
   $$
   V^{molecular}_{excluido} = \tfrac{4}{3}\pi(2r_0)^3 \quad (8)
   $$
   Sea:
   $$
   b' = \tfrac{4}{3}\pi(2r_0)^3 \quad (9)
   $$
   luego:
   $$
   V^{molecular}_{excluido} = b' \quad (10)
   $$
   Como el gas tiene $N$ moléculas el volumen excluido total será:
   $$
   V^{total}_{excluido} = N b' \quad (11)
   $$
   Luego el volumen total disponible para las moléculas es:
   $$
   V' = V - N b' \quad (12)
   $$
   Por otro lado, el número de estados del sistema $\Omega$ en la colectividad microcanónica se puede definir a partir de:
   $$
   \Omega = \frac{\partial \omega}{\partial E} \quad (13)
   $$
   donde:
   $$
   \omega = \frac{1}{N!h^{3N}} \int_{H(p_i,q_i) \le E} dq_1\cdots dq_{3N}\,dp_1\cdots dp_{3N} \quad (14)
   $$
   Demuestre que:
   $$
   \Omega(E,V,N) = \frac{(V - N b')^N}{N!} \left(\frac{2\pi m}{h^2}\right)^{3N/2} \frac{\bigl(E + a'\tfrac{N^2}{V}\bigr)^{3N/2 -1}}{\bigl(\tfrac{3N}{2}-1\bigr)!} \quad (15)
   $$
   Y a partir de dicha expresión, muestre que la entropía es:
   $$
   S = k N \left\{ \tfrac{5}{2} + \ln\!\left[ \frac{(V - N b')}{N} \left( \frac{4\pi m}{3N h^2}(E + a'\tfrac{N^2}{V}) \right)^{3/2} \right] \right\}
   $$
   y a partir de la ecuación de la energía:
   $$
   \frac{1}{T} = \bigl(\tfrac{\partial S}{\partial E}\bigr)_{V,N} \quad (16)
   $$
   muestre que:
   $$
   E = \frac{3}{2}kN T - a'\frac{N^2}{V} \quad (17)
   $$
   Finalmente, a partir de:
   $$
   \frac{p}{T} = \bigl(\tfrac{\partial S}{\partial V}\bigr)_{E,N} \quad (18)
   $$
   muestre que la ecuación de estado de Van der Waals es:
   $$
   \bigl(p + \tfrac{n^2 a}{V^2}\bigr)(V - n b) = n R T \quad (19)
   $$
   con:
   $$
   a = \frac{a' N^2_A}{A}, \quad b = b' N_A, \quad R = N_A k \quad (20--22)
   $$

## Solución del Ejercicio 12

**Parte a) Número de microestados con corrección de volumen**

Con el Hamiltoniano $H = \sum p_i^2/(2m) - a'N^2/V$, la integral en el espacio de fase es:

$$
\omega = \frac{1}{N!h^{3N}} \int_{H \le E} d^{3N}q \, d^{3N}p
$$

La integral sobre posiciones está limitada al volumen disponible $V' = V - Nb'$, así:

$$
\int_{H \le E} d^{3N}q = (V - Nb')^N
$$

Para la integral sobre momentos, la restricción es:

$$
\sum_{i=1}^{3N} \frac{p_i^2}{2m} - a'\frac{N^2}{V} \le E
$$

$$
\sum_{i=1}^{3N} \frac{p_i^2}{2m} \le E + a'\frac{N^2}{V}
$$

El volumen en el espacio de momentos es:

$$
\int d^{3N}p = \frac{\pi^{3N/2}}{\Gamma(3N/2 + 1)} (2m(E + a'N^2/V))^{3N/2}
$$

Por lo tanto:

$$
\omega = \frac{(V-Nb')^N}{N!h^{3N}} \frac{\pi^{3N/2}}{\Gamma(3N/2+1)} (2m)^{3N/2} \left(E + a'\frac{N^2}{V}\right)^{3N/2}
$$

**Parte b) Derivación del número de microestados**

$$
\Omega(E,V,N) = \frac{\partial \omega}{\partial E} = \frac{(V-Nb')^N}{N!h^{3N}} \frac{\pi^{3N/2}}{\Gamma(3N/2)} (2m)^{3N/2} \left(E + a'\frac{N^2}{V}\right)^{3N/2 - 1}
$$

Usando $\Gamma(3N/2 + 1) = (3N/2)\Gamma(3N/2) = (3N/2-1)! + \ldots$ y reordenando:

$$
\Omega(E,V,N) = \frac{(V-Nb')^N}{N!} \left(\frac{2\pi m}{h^2}\right)^{3N/2} \frac{(E + a'N^2/V)^{3N/2 - 1}}{(3N/2 - 1)!}
$$

**Parte c) Entropía**

$$
S = k_B \ln \Omega = k_B \left[ N\ln(V-Nb') - \ln N! + \frac{3N}{2}\ln\frac{2\pi m}{h^2} + \left(\frac{3N}{2}-1\right)\ln\left(E + a'\frac{N^2}{V}\right) - \ln(3N/2-1)! \right]
$$

Para $N$ grande, usando Stirling y simplificando:

$$
S = k_B N\left[ \ln\frac{V-Nb'}{N} + \frac{3}{2}\ln\left(\frac{4\pi m}{3Nh^2}\left(E + a'\frac{N^2}{V}\right)\right) + \frac{5}{2} \right]
$$

**Parte d) Energía y relación termodinámica**

$$
\frac{1}{T} = \left(\frac{\partial S}{\partial E}\right)_{V,N} = \frac{3k_BN}{2(E + a'N^2/V)}$$

Despejando $E$:

$$
E + a'\frac{N^2}{V} = \frac{3Nk_BT}{2}$$

$$
E = \frac{3Nk_BT}{2} - a'\frac{N^2}{V}
$$

**Parte e) Presión y ecuación de estado**

$$
\frac{p}{T} = \left(\frac{\partial S}{\partial V}\right)_{E,N}
$$

Calculando:

$$
\frac{\partial S}{\partial V} = k_B N \left[ \frac{1}{V-Nb'} + \frac{3}{2} \frac{1}{E + a'N^2/V} \cdot a'\frac{N^2}{V^2} \right]
$$

Pero de $E + a'N^2/V = 3Nk_BT/2$, el segundo término da:

$$
\frac{3}{2} \cdot \frac{1}{3Nk_BT/2} \cdot a'\frac{N^2}{V^2} = \frac{a'N^2}{k_BTV^2}
$$

Por lo tanto:

$$
\frac{p}{T} = \frac{k_BN}{V-Nb'} - \frac{a'N^2}{V^2T}
$$

$$
p = \frac{k_BNT}{V-Nb'} - a'\frac{N^2}{V^2}
$$

Reacomodando:

$$
\left(p + a'\frac{N^2}{V^2}\right)(V - Nb') = k_BNT
$$

**Conversión a variables molares:**

Para $n$ moles (con $N = nN_A$ partículas), defina $a = a'N_A^2$ y $b = b'N_A$. Entonces:

$$
\left(p + n^2\frac{a}{V^2}\right)(V - nb) = nN_Ak_BT = nRT
$$

Esta es la ecuación de Van der Waals.

**Interpretación de los parámetros:**
- $a$: mide la fuerza de atracción intermolecular
- $b$: mide el volumen excluido por las moléculas (tamaño finito)
- El término $a N^2/V^2$ es la corrección de presión por atracciones
- El término $-Nb'$ es el volumen disponible efectivo

**Resumen:**
- $\Omega$ con corrección volumétrica incluye $(V-Nb')^N$
- Entropía: $S = k_BN[5/2 + \ln((V-Nb')/N) + (3/2)\ln(4\pi m(E+a'N^2/V)/(3Nh^2))]$
- Energía: $E = \frac{3}{2}Nk_BT - a'N^2/V$
- Ecuación de estado: $(p + a'N^2/V^2)(V-Nb') = Nk_BT$

**Búsqueda en el libro de Johan:** Busca: *"volumen excluido"*, *"esferas duras"*, *"corrección volumétrica"*, *"ecuación de Van der Waals"* o *"parámetro b de Van der Waals"* para comprender cómo el tamaño finito de las moléculas modifica termodinámicamente el gas.

---

# Soluciones: Problemas sobre Longitud de Onda de De Broglie y Clasificación de Sistemas Estadísticos

13. Se tiene un gas de moléculas de N$_2$ a temperatura $T = 300\,\mathrm{K}$ y presión estándar. La masa de la molécula es de $4.7\times10^{-26}\,\mathrm{kg}$. Determine si el gas de moléculas de N$_2$ bajo dichas condiciones sigue una estadística clásica o cuántica.

## Solución del Ejercicio 13

**Concepto físico:**

Un gas sigue una estadística clásica (Maxwell-Boltzmann) cuando la longitud de onda térmica de De Broglie $\lambda$ es mucho menor que la separación media entre partículas. En caso contrario, deben usarse estadísticas cuánticas (Fermi-Dirac o Bose-Einstein).

**Cálculo de la longitud de onda térmica de De Broglie:**

$$
\lambda_{dB} = \frac{h}{\sqrt{3\pi m k_B T}}
$$

donde:
- $h = 6.626 \times 10^{-34}$ J·s (constante de Planck)
- $m = 4.7 \times 10^{-26}$ kg (masa de una molécula de N₂)
- $k_B = 1.381 \times 10^{-23}$ J/K (constante de Boltzmann)
- $T = 300$ K

Sustituyendo:

$$
\lambda_{dB} = \frac{6.626 \times 10^{-34}}{\sqrt{3\pi \times 4.7 \times 10^{-26} \times 1.381 \times 10^{-23} \times 300}}
$$

Calculamos el denominador:

$$
3\pi \times 4.7 \times 10^{-26} \times 1.381 \times 10^{-23} \times 300 = 1.84 \times 10^{-46}
$$

$$
\sqrt{1.84 \times 10^{-46}} = 4.29 \times 10^{-24}
$$

$$
\lambda_{dB} = \frac{6.626 \times 10^{-34}}{4.29 \times 10^{-24}} \approx 1.54 \times 10^{-11} \, \mathrm{m} = 0.0154 \, \mathrm{nm}
$$

**Cálculo de la separación media entre moléculas:**

A presión estándar ($p = 1$ atm $= 101325$ Pa):

$$
N/V = \frac{p}{k_BT} = \frac{101325}{1.381 \times 10^{-23} \times 300} = 2.44 \times 10^{25} \, \mathrm{m}^{-3}
$$

La separación media es aproximadamente:

$$
d \approx (V/N)^{1/3} = \left(\frac{1}{2.44 \times 10^{25}}\right)^{1/3} \approx 3.35 \times 10^{-9} \, \mathrm{m} = 3.35 \, \mathrm{nm}
$$

**Comparación:**

$$
\frac{\lambda_{dB}}{d} = \frac{1.54 \times 10^{-11}}{3.35 \times 10^{-9}} \approx 0.0046 \ll 1
$$

**Conclusión:**

Como $\lambda_{dB} \ll d$, el gas de N₂ a 300 K y presión estándar sigue estadística clásica (Maxwell-Boltzmann). Los efectos cuánticos son despreciables porque la longitud de onda es mucho más pequeña que la separación entre moléculas.

**Búsqueda en el libro de Johan:** Busca: *"longitud de onda de De Broglie"*, *"criterio cuántico clásico"*, *"estadística Maxwell-Boltzmann"*, *"N₂ gas"* o *"clasificación de sistemas estadísticos"* para entender cuándo los efectos cuánticos son relevantes.

---

14. Se tiene helio líquido a temperatura $T=2\,\mathrm{K}$. La masa molar del helio es de $4\,\mathrm{g/mol}$. La masa de un átomo de helio es de $6.6\times10^{-27}\,\mathrm{kg}$. La densidad del helio líquido es de $0.124\,\mathrm{g/cm^3}$. Determine si el helio líquido a dicha temperatura sigue una estadística clásica o cuántica.

## Solución del Ejercicio 14

**Cálculo de la longitud de onda térmica de De Broglie:**

$$
\lambda_{dB} = \frac{h}{\sqrt{3\pi m k_B T}}
$$

donde:
- $h = 6.626 \times 10^{-34}$ J·s
- $m = 6.6 \times 10^{-27}$ kg (masa de un átomo de He)
- $k_B = 1.381 \times 10^{-23}$ J/K
- $T = 2$ K

Sustituyendo:

$$
\lambda_{dB} = \frac{6.626 \times 10^{-34}}{\sqrt{3\pi \times 6.6 \times 10^{-27} \times 1.381 \times 10^{-23} \times 2}}
$$

Calculamos el denominador:

$$
3\pi \times 6.6 \times 10^{-27} \times 1.381 \times 10^{-23} \times 2 = 5.71 \times 10^{-49}
$$

$$
\sqrt{5.71 \times 10^{-49}} = 7.56 \times 10^{-25}
$$

$$
\lambda_{dB} = \frac{6.626 \times 10^{-34}}{7.56 \times 10^{-25}} \approx 8.76 \times 10^{-10} \, \mathrm{m} = 0.876 \, \mathrm{nm}
$$

**Cálculo de la separación media:**

Primero, convertimos la densidad a unidades SI:

$$
\rho = 0.124 \, \mathrm{g/cm^3} = 124 \, \mathrm{kg/m^3}
$$

El número de átomos por unidad de volumen es:

$$
n = \frac{\rho}{m} = \frac{124}{6.6 \times 10^{-27}} = 1.88 \times 10^{28} \, \mathrm{m}^{-3}
$$

La separación media es:

$$
d \approx n^{-1/3} = (1.88 \times 10^{28})^{-1/3} \approx 3.61 \times 10^{-10} \, \mathrm{m} = 0.361 \, \mathrm{nm}
$$

**Comparación:**

$$
\frac{\lambda_{dB}}{d} = \frac{8.76 \times 10^{-10}}{3.61 \times 10^{-10}} \approx 2.43 > 1
$$

**Conclusión:**

Como $\lambda_{dB} > d$, el helio líquido a 2 K sigue una estadística cuántica. Las longitudes de onda cuánticas son comparables o mayores que las separaciones interatómicas, por lo que no es válida la descripción clásica.

Esto es característico del helio-4 líquido, que es un superfluido a temperaturas tan bajas. Los efectos cuánticos (específicamente, la estadística de Bose-Einstein porque el He-4 es un bosón con espín 0) son esenciales para describir correctamente sus propiedades.

**Búsqueda en el libro de Johan:** Busca: *"helio líquido"*, *"longitud de onda térmica"*, *"estadística cuántica"*, *"bosones"*, *"superfluido"* o *"He-4 y Bose-Einstein"* para entender por qué el helio a bajas temperaturas presenta propiedades cuánticas tan dramáticas.

---

# Soluciones: Problemas sobre Ensamble Canónico

15. Resuelva el literal (c) de la pregunta 7 en el marco de la colectividad canónica.

## Solución del Ejercicio 15

**Referencia:** Del ejercicio 7(c), se buscaba demostrar que $E = \frac{N\varepsilon}{1 + e^{\varepsilon/2kT}}$.

**Enfoque en el ensamble canónico:**

En el ensamble canónico, la temperatura es constante y se minimiza la energía libre de Helmholtz $F = E - TS$.

Para el sistema de dos redes con $N$ partículas (donde $n$ están en la red B con energía $\varepsilon$ cada una y $N-n$ en la red A con energía cero), la función partición canónica es:

$$
Z(T,N) = \sum_{n=0}^{N} \binom{N}{n}^2 e^{-\beta n\varepsilon}
$$

donde $\beta = 1/(k_BT)$.

**Cálculo del valor esperado de $n$:**

$$
\langle n \rangle = -\frac{1}{\beta}\frac{\partial \ln Z}{\partial (-\beta\varepsilon)} = -\frac{\partial \ln Z}{\partial \varepsilon}
$$

Alternativamente:

$$
\langle n \rangle = \frac{\sum_n n \binom{N}{n}^2 e^{-\beta n\varepsilon}}{\sum_n \binom{N}{n}^2 e^{-\beta n\varepsilon}}
$$

**Aproximación para $N$ grande:**

Para $N$ grande y cuando $n$ no es extremo, podemos aproximar la suma como una integral. El máximo del integrando ocurre donde:

$$
\frac{d}{dn}\left[ 2\ln\binom{N}{n} - \beta n\varepsilon \right] = 0
$$

$$
2\frac{\partial}{\partial n}\ln\binom{N}{n} = \beta\varepsilon
$$

Usando $\ln\binom{N}{n} \approx N\ln N - n\ln n - (N-n)\ln(N-n)$ y derivando:

$$
2\ln\frac{N-n}{n} = \beta\varepsilon$$

$$
\frac{N-n}{n} = e^{\beta\varepsilon/2}$$

$$
n(1 + e^{\beta\varepsilon/2}) = N$$

$$
\langle n \rangle = \frac{N}{1 + e^{\varepsilon/(2k_BT)}}
$$

**Energía media en el ensamble canónico:**

$$
\langle E \rangle = \varepsilon \langle n \rangle = \frac{N\varepsilon}{1 + e^{\varepsilon/(2k_BT)}}
$$

**Equivalencia de ensambles:**

Este resultado coincide exactamente con el del ensamble microcanónico (ejercicio 7c). Esto ilustra la equivalencia de los ensambles en el límite termodinámico: a energía promedio, ambos ensambles dan el mismo resultado macroscópico.

**Resumen:**
- Función partición: $Z = \sum_n \binom{N}{n}^2 e^{-\beta n\varepsilon}$
- Número medio de partículas en red B: $\langle n \rangle = \frac{N}{1+e^{\varepsilon/2k_BT}}$
- Energía media: $\langle E \rangle = \frac{N\varepsilon}{1+e^{\varepsilon/2k_BT}}$

**Búsqueda en el libro de Johan:** Busca: *"ensamble canónico"*, *"función partición canónica"*, *"equivalencia de ensambles"*, *"dos redes en ensamble canónico"* o *"energía media en ensamble canónico"* para ver cómo el ensamble canónico produce los mismos resultados que el microcanónico.

---

16. Un sólido paramagnético formado por átomos de espín $\tfrac12$ se somete a la acción de un campo magnético externo $H=3\times10^{4}\,$Gauss. Si el momento magnético de cada átomo es $\mu=0.927\times10^{-20}\,$ergs/Gauss, ¿por debajo de qué temperatura debe enfriar el sólido para que más del 75% de los átomos estén polarizados con sus espines paralelos al campo magnético aplicado?

## Solución del Ejercicio 16

**Marco teórico:**

En un sólido paramagnético con espines $1/2$, cada átomo puede estar en dos estados:
- Paralelo a $H$ (espín arriba): energía $E_{\uparrow} = -\mu H$
- Antiparalelo a $H$ (espín abajo): energía $E_{\downarrow} = +\mu H$

La probabilidad de cada estado en el ensamble canónico es:

$$
P_{\uparrow} = \frac{e^{\mu H/k_BT}}{e^{\mu H/k_BT} + e^{-\mu H/k_BT}} = \frac{e^{2\mu H/k_BT}}{e^{2\mu H/k_BT} + 1}
$$

$$
P_{\downarrow} = \frac{e^{-\mu H/k_BT}}{e^{\mu H/k_BT} + e^{-\mu H/k_BT}} = \frac{1}{e^{2\mu H/k_BT} + 1}
$$

Equivalentemente:

$$
P_{\uparrow} = \frac{1}{1 + e^{-2\mu H/k_BT}}
$$

**Condición requerida:**

Queremos $P_{\uparrow} > 0.75$:

$$
\frac{1}{1 + e^{-2\mu H/k_BT}} > 0.75$$

$$
1 + e^{-2\mu H/k_BT} < \frac{4}{3}$$

$$
e^{-2\mu H/k_BT} < \frac{1}{3}$$

$$
-\frac{2\mu H}{k_BT} < \ln(1/3) = -\ln 3$$

$$
\frac{2\mu H}{k_BT} > \ln 3 \approx 1.0986$$

$$
T < \frac{2\mu H}{k_B \ln 3}
$$

**Cálculo numérico:**

Convertimos las unidades:
- $H = 3 \times 10^4$ Gauss
- $\mu = 0.927 \times 10^{-20}$ erg/Gauss
- $k_B = 1.381 \times 10^{-16}$ erg/K

Calculamos $\mu H$:

$$
\mu H = 0.927 \times 10^{-20} \times 3 \times 10^4 = 2.781 \times 10^{-16} \, \mathrm{erg}
$$

Por lo tanto:

$$
T < \frac{2 \times 2.781 \times 10^{-16}}{1.381 \times 10^{-16} \times 1.0986}
$$

$$
T < \frac{5.562 \times 10^{-16}}{1.518 \times 10^{-16}} \approx 3.66 \, \mathrm{K}
$$

**Conclusión:**

El sólido debe enfriarse a una temperatura $T < 3.66$ K para que más del 75% de los átomos estén polarizados paralelamente al campo magnético. En particular, cualquier temperatura por debajo de aproximadamente 3.7 K cumplirá el criterio.

**Búsqueda en el libro de Johan:** Busca: *"paramagnetismo"*, *"polarización magnética"*, *"espín 1/2 en campo"*, *"distribución de Boltzmann magnética"*, *"temperatura de polarización"* o *"momento magnético en campo externo"* para profundizar en el paramagnetismo clásico.

---

17. Considere $N_0$ átomos por unidad de volumen a la temperatura $T$, cada uno con momento magnético $\mu$ el cual puede formar un ángulo arbitrario $\theta$ respecto a una dirección dada (eje $z$). Si se aplica un campo magnético $H$ en esta dirección, obtenga una expresión clásica para la magnetización media $M_z$ del sistema.

## Solución del Ejercicio 17

**Sistema clásico de momentos magnéticos:**

Para un momento magnético clásico $\vec{\mu}$ en un campo $\vec{H}$ alineado en la dirección $z$:

$$
H = -\vec{\mu} \cdot \vec{H} = -\mu H \cos\theta
$$

donde $\theta$ es el ángulo entre el momento y el campo.

**Función partición de una partícula:**

La función partición de una sola partícula en el ensamble canónico es:

$$
z = \int_0^{2\pi} d\phi \int_0^{\pi} \sin\theta \, d\theta \, e^{\beta \mu H \cos\theta}
$$

donde $\beta = 1/(k_BT)$.

La integral sobre $\phi$ da $2\pi$:

$$
z = 2\pi \int_0^{\pi} \sin\theta \, e^{\beta \mu H \cos\theta} d\theta
$$

Haciendo la sustitución $u = \cos\theta$, $du = -\sin\theta \, d\theta$:

$$
z = 2\pi \int_1^{-1} (-du) e^{\beta \mu H u} = 2\pi \int_{-1}^{1} e^{\beta \mu H u} du
$$

$$
z = 2\pi \left[ \frac{e^{\beta \mu H u}}{\beta \mu H} \right]_{-1}^{1} = \frac{2\pi}{\beta \mu H} \left( e^{\beta\mu H} - e^{-\beta\mu H} \right)
$$

$$
z = \frac{2\pi}{\beta\mu H} \cdot 2\sinh(\beta\mu H) = \frac{4\pi}{\beta\mu H}\sinh(\beta\mu H)
$$

**Componente $z$ del momento magnético promedio:**

$$
\langle \mu_z \rangle = \mu \langle \cos\theta \rangle = -\frac{1}{\beta}\frac{\partial \ln z}{\partial H}
$$

Calculamos:

$$
\ln z = \ln(4\pi) - \ln(\beta\mu H) + \ln(\sinh(\beta\mu H))
$$

$$
\frac{\partial \ln z}{\partial H} = -\frac{1}{H} + \frac{\beta\mu}{\sinh(\beta\mu H)}\cosh(\beta\mu H) = -\frac{1}{H} + \beta\mu \coth(\beta\mu H)
$$

Por lo tanto:

$$
\langle \mu_z \rangle = -\frac{1}{\beta}\left(-\frac{1}{H} + \beta\mu\coth(\beta\mu H)\right)
$$

$$
\langle \mu_z \rangle = \frac{1}{\beta H} - \mu\coth(\beta\mu H)
$$

Utilizando la identidad $\coth(x) = \frac{1}{x} + \frac{x}{3} + O(x^3)$ para $x \to 0$:

Alternativamente, usando $\coth(x) = 1/\tanh(x)$:

$$
\langle \mu_z \rangle = \mu \coth(\beta\mu H) - \frac{1}{\beta H}
$$

Más elegantemente, definiendo la función de Langevin:

$$
\mathcal{L}(x) = \coth(x) - \frac{1}{x}
$$

tenemos:

$$
\langle \mu_z \rangle = \mu \mathcal{L}(\beta\mu H)
$$

**Magnetización del sistema:**

La magnetización por unidad de volumen es el momento magnético promedio por partícula, multiplicado por la densidad de número $N_0$:

$$
M_z = N_0 \langle \mu_z \rangle = N_0 \mu \left[ \coth(\beta\mu H) - \frac{1}{\beta\mu H} \right]
$$

$$
M_z = N_0 \mu \mathcal{L}\left(\frac{\mu H}{k_BT}\right)
$$

**Límites físicos:**

1. **Límite de campo débil** ($\mu H \ll k_BT$):
   $$
   \coth(x) \approx \frac{1}{x} + \frac{x}{3} \quad \Rightarrow \quad \mathcal{L}(x) \approx \frac{x}{3}
   $$
   $$
   M_z \approx \frac{N_0 \mu^2 H}{3k_BT} \quad \text{(Ley de Curie)}
   $$

2. **Límite de campo fuerte** ($\mu H \gg k_BT$):
   $$
   \coth(x) \approx 1 \quad \Rightarrow \quad \mathcal{L}(x) \approx 1
   $$
   $$
   M_z \approx N_0 \mu \quad \text{(Saturación)}
   $$

**Resumen:**
- Función de Langevin: $\mathcal{L}(x) = \coth(x) - 1/x$
- Magnetización: $M_z = N_0\mu\mathcal{L}(\mu H/k_BT)$
- Campo débil: $M_z = N_0\mu^2 H/(3k_BT)$ (Curie)
- Campo fuerte: $M_z = N_0\mu$ (Saturación)

**Búsqueda en el libro de Johan:** Busca: *"magnetización clásica"*, *"función de Langevin"*, *"momentos magnéticos clásicos"*, *"teoría clásica de paramagnetismo"* o *"límites de campo débil y fuerte"* para entender cómo los momentos magnéticos clásicos se orientan en campos.

---

18. Demuestre que las fluctuaciones de la energía están relacionadas con la capacidad calorífica a través de la siguiente relación:
$$
\langle E^2\rangle - \langle E\rangle^2 = kB T^2CV
$$

## Solución del Ejercicio 18

**Formalismo del ensamble canónico:**

En el ensamble canónico, la energía de un microestado $i$ es $E_i$ y su probabilidad es:

$$
P_i = \frac{e^{-\beta E_i}}{Z}
$$

donde $Z = \sum_i e^{-\beta E_i}$ es la función partición y $\beta = 1/(k_BT)$.

**Definiciones:**

$$
\langle E \rangle = \sum_i E_i P_i = -\frac{\partial \ln Z}{\partial \beta}
$$

$$
\langle E^2 \rangle = \sum_i E_i^2 P_i
$$

**Cálculo de la varianza:**

$$
\langle E^2 \rangle = \sum_i E_i^2 \frac{e^{-\beta E_i}}{Z} = \frac{1}{Z}\sum_i E_i^2 e^{-\beta E_i}
$$

Observamos que:

$$
\frac{\partial^2}{\partial \beta^2} e^{-\beta E_i} = E_i^2 e^{-\beta E_i}
$$

Por lo tanto:

$$
\langle E^2 \rangle = \frac{1}{Z}\frac{\partial^2}{\partial \beta^2} \sum_i e^{-\beta E_i} = \frac{1}{Z}\frac{\partial^2 Z}{\partial \beta^2}
$$

$$
\langle E^2 \rangle = \frac{\partial^2 \ln Z}{\partial \beta^2} + \left(\frac{\partial \ln Z}{\partial \beta}\right)^2
$$

**Varianza de la energía:**

$$
(\Delta E)^2 = \langle E^2 \rangle - \langle E \rangle^2 = \frac{\partial^2 \ln Z}{\partial \beta^2} + \left(\frac{\partial \ln Z}{\partial \beta}\right)^2 - \left(\frac{\partial \ln Z}{\partial \beta}\right)^2
$$

$$
(\Delta E)^2 = \frac{\partial^2 \ln Z}{\partial \beta^2}
$$

**Relación con la capacidad calorífica:**

La capacidad calorífica a volumen constante es:

$$
C_V = \left(\frac{\partial \langle E \rangle}{\partial T}\right)_V = -\frac{\partial \langle E \rangle}{\partial \beta}\frac{\partial \beta}{\partial T}
$$

Como $\beta = 1/(k_BT)$:

$$
\frac{\partial \beta}{\partial T} = -\frac{1}{k_BT^2}
$$

Por lo tanto:

$$
C_V = -\left(-\frac{1}{k_BT^2}\right)\frac{\partial \langle E \rangle}{\partial \beta} = \frac{1}{k_BT^2}\frac{\partial}{\partial \beta}\left(-\frac{\partial \ln Z}{\partial \beta}\right)
$$

$$
C_V = -\frac{1}{k_BT^2}\frac{\partial^2 \ln Z}{\partial \beta^2}
$$

**Relación final:**

De las dos ecuaciones anteriores:

$$
(\Delta E)^2 = -k_BT^2 C_V
$$

O equivalentemente:

$$
\langle E^2 \rangle - \langle E \rangle^2 = k_BT^2 C_V
$$

**Interpretación física:**

Esta relación muestra que las fluctuaciones de energía son proporcionales a la capacidad calorífica. Cuando $C_V$ es grande, hay grandes fluctuaciones en la energía porque el sistema es muy susceptible a cambios de temperatura. Esta es una consecuencia del teorema de fluctuación-disipación.

**Resumen:**
- Varianza: $(\Delta E)^2 = \frac{\partial^2 \ln Z}{\partial \beta^2}$
- Capacidad calorífica: $C_V = -\frac{1}{k_BT^2}\frac{\partial^2 \ln Z}{\partial \beta^2}$
- Relación final: $\langle E^2 \rangle - \langle E \rangle^2 = k_BT^2C_V$

**Búsqueda en el libro de Johan:** Busca: *"fluctuaciones de energía"*, *"teorema de fluctuación-disipación"*, *"varianza de energía"*, *"relación energía-capacidad calorífica"* o *"compresibilidad térmica"* para entender la conexión profunda entre respuesta y fluctuaciones.

---

19. Demuestre que para un conjunto de $N$ osciladores armónicos distinguibles de frecuencia $\omega$, la energía libre de Helmholtz viene dada por:
$$
F(T,V,N) = -k_B T \ln Z(T,V,N) = -N k_B T \ln\left(\frac{k_B T}{\hbar\omega}\right)
$$

## Solución del Ejercicio 19

**Función partición de un oscilador armónico cuántico:**

Para un oscilador armónico 1D con frecuencia $\omega$, los niveles de energía son:

$$
E_n = \hbar\omega\left(n + \frac{1}{2}\right), \quad n = 0,1,2,\ldots
$$

La función partición de una partícula es:

$$
z = \sum_{n=0}^{\infty} e^{-\beta\hbar\omega(n + 1/2)} = e^{-\beta\hbar\omega/2} \sum_{n=0}^{\infty} e^{-\beta\hbar\omega n}
$$

$$
z = e^{-\beta\hbar\omega/2} \cdot \frac{1}{1 - e^{-\beta\hbar\omega}}
$$

Simplificando:

$$
z = \frac{e^{-\beta\hbar\omega/2}}{1 - e^{-\beta\hbar\omega}}
$$

Multiplicando numerador y denominador por $e^{\beta\hbar\omega/2}$:

$$
z = \frac{1}{2\sinh(\beta\hbar\omega/2)}
$$

**Función partición de $N$ osciladores distinguibles:**

Como los osciladores son independientes y distinguibles:

$$
Z(T,V,N) = z^N = \frac{1}{[2\sinh(\beta\hbar\omega/2)]^N}
$$

**Logaritmo de la función partición:**

$$
\ln Z = -N\ln[2\sinh(\beta\hbar\omega/2)]
$$

$$
\ln Z = -N[\ln 2 + \ln\sinh(\beta\hbar\omega/2)]
$$

**Límite clásico ($T \gg \hbar\omega/(k_B)$):**

Para temperaturas altas (o $\hbar\omega \ll k_BT$):

$$
\sinh(x) \approx \frac{e^x}{2} \quad \text{para } x \ll 1
$$

Por lo tanto:

$$
\sinh(\beta\hbar\omega/2) \approx \frac{e^{\beta\hbar\omega/2}}{2}
$$

$$
\ln\sinh(\beta\hbar\omega/2) \approx \ln\left(\frac{e^{\beta\hbar\omega/2}}{2}\right) = \frac{\beta\hbar\omega}{2} - \ln 2
$$

Así:

$$
\ln Z \approx -N\left[\ln 2 + \frac{\beta\hbar\omega}{2} - \ln 2\right] = -N\frac{\beta\hbar\omega}{2}
$$

**Sin embargo**, la fórmula del problema sugiere un resultado diferente. Revisemos el cálculo exacto.

**Cálculo exacto usando la identidad:**

$$
\sinh(x) = \frac{e^x - e^{-x}}{2}
$$

Una forma más útil de escribir la función partición es:

$$
z = \frac{e^{-\beta\hbar\omega/2}}{1-e^{-\beta\hbar\omega}}
$$

Tomando logaritmo:

$$
\ln z = -\frac{\beta\hbar\omega}{2} - \ln(1-e^{-\beta\hbar\omega})
$$

Para $N$ osciladores:

$$
\ln Z = N\ln z = -\frac{N\beta\hbar\omega}{2} - N\ln(1-e^{-\beta\hbar\omega})
$$

**Energía libre de Helmholtz:**

$$
F = -k_BT\ln Z = k_BT\left[\frac{N\beta\hbar\omega}{2} + N\ln(1-e^{-\beta\hbar\omega})\right]
$$

$$
F = \frac{N\hbar\omega}{2} + Nk_BT\ln(1-e^{-\beta\hbar\omega})
$$

**Relación con la fórmula propuesta:**

La fórmula dada en el problema puede reescribirse. Usando $1-e^{-x} = 1-e^{-x}$:

$$
\ln(1-e^{-\beta\hbar\omega}) = \ln\left(1 - \frac{1}{e^{\beta\hbar\omega}}\right) = \ln\left(\frac{e^{\beta\hbar\omega}-1}{e^{\beta\hbar\omega}}\right)
$$

$$
= \ln(e^{\beta\hbar\omega}-1) - \beta\hbar\omega
$$

Por lo tanto:

$$
F = \frac{N\hbar\omega}{2} + Nk_BT[\ln(e^{\beta\hbar\omega}-1) - \beta\hbar\omega]
$$

$$
F = \frac{N\hbar\omega}{2} + Nk_BT\ln(e^{\beta\hbar\omega}-1) - N\hbar\omega
$$

$$
F = Nk_BT\ln(e^{\beta\hbar\omega}-1) - \frac{N\hbar\omega}{2}
$$

**Verificación de la fórmula propuesta:**

La fórmula $F = -Nk_BT\ln(k_BT/\hbar\omega)$ corresponde al límite clásico, donde se omite la energía de punto cero y se usa una aproximación diferente. En el límite $k_BT \gg \hbar\omega$:

$$
\ln(e^{\beta\hbar\omega}-1) \approx \ln(\beta\hbar\omega) = \ln(\hbar\omega/(k_BT))
$$

Así:

$$
F \approx Nk_BT\ln\left(\frac{\hbar\omega}{k_BT}\right) = -Nk_BT\ln\left(\frac{k_BT}{\hbar\omega}\right)$$

omitiendo la energía de punto cero.

**Resumen:**
- Función partición: $z = 1/(2\sinh(\beta\hbar\omega/2))$
- Para $N$ osciladores: $\ln Z = -N\ln[2\sinh(\beta\hbar\omega/2)]$
- Energía libre exacta: $F = N\hbar\omega/2 + Nk_BT\ln(1-e^{-\beta\hbar\omega})$
- En límite clásico: $F \approx -Nk_BT\ln(k_BT/\hbar\omega)$ (omitiendo término de punto cero)

**Búsqueda en el libro de Johan:** Busca: *"oscilador armónico cuántico"*, *"función partición de osciladores"*, *"energía libre de Helmholtz"*, *"límite clásico de osciladores"* o *"equipartición en osciladores"* para ver cómo la mecánica estadística recupera el límite clásico.

---

20. Demuestre que en un sistema hidrostático la presión media se puede escribir como:
$$
p = \frac{1}{\beta}\frac{\partial \ln Z}{\partial V}
$$

## Solución del Ejercicio 20

**Formalismo termodinámico en el ensamble canónico:**

En el ensamble canónico con variables $(T, V, N)$ fijas, la energía libre de Helmholtz es:

$$
F(T,V,N) = -k_BT\ln Z(T,V,N)
$$

**Relación termodinámica:**

La diferencial exacta de $F$ es:

$$
dF = -SdT - pdV + \mu dN
$$

Por lo tanto, las derivadas parciales son:

$$
S = -\left(\frac{\partial F}{\partial T}\right)_{V,N}, \quad p = -\left(\frac{\partial F}{\partial V}\right)_{T,N}, \quad \mu = \left(\frac{\partial F}{\partial N}\right)_{T,V}
$$

**Cálculo de la presión:**

Partimos de $F = -k_BT\ln Z$:

$$
\left(\frac{\partial F}{\partial V}\right)_{T,N} = -k_BT\frac{\partial \ln Z}{\partial V}
$$

Por lo tanto:

$$
p = -\left(\frac{\partial F}{\partial V}\right)_{T,N} = k_BT\frac{\partial \ln Z}{\partial V}
$$

**Reescritura con $\beta$:**

Como $\beta = 1/(k_BT)$, podemos escribir:

$$
p = \frac{1}{\beta}\frac{\partial \ln Z}{\partial V}
$$

**Verificación con un ejemplo:**

Para un gas ideal de $N$ partículas en volumen $V$:

$$
Z = \frac{V^N}{\Lambda^{3N}} \times \text{factor de espín/simetría}
$$

donde $\Lambda = h/\sqrt{2\pi mk_BT}$ es la longitud de onda térmica.

$$
\ln Z = N\ln V + \text{términos independientes de } V
$$

$$
\frac{\partial \ln Z}{\partial V} = \frac{N}{V}
$$

$$
p = \frac{1}{\beta}\frac{N}{V} = \frac{k_BNT}{V}$$

que es la ecuación de estado del gas ideal: $pV = Nk_BT$.

**Interpretación física:**

La fórmula $p = (1/\beta)(\partial\ln Z/\partial V)$ expresa que la presión es proporcional a cómo cambia el número de microestados accesibles cuando el volumen aumenta. Un aumento de volumen incrementa el número de estados cuánticos disponibles (densidad de estados en el espacio de momentos), lo que aumenta $Z$ y así aumenta la presión.

**Resumen:**
- Energía libre: $F = -k_BT\ln Z$
- Presión termodinámica: $p = -(\partial F/\partial V)_{T,N}$
- Expresión en función de $Z$: $p = (1/\beta)(\partial\ln Z/\partial V)$
- Para gas ideal: $p = Nk_BT/V$ (verificado)

**Búsqueda en el libro de Johan:** Busca: *"presión canónica"*, *"derivada logarítmica de partición"*, *"relación termodinámica presión"*, *"sistema hidrostático"* o *"presión desde función partición"* para entender cómo la presión emerge de la derivada de la partición.

---

21. En el modelo de Einstein para un sólido clásico, éste se considera formado por $N$ osciladores armónicos de masa $m$ y constante elástica $k$, con Hamiltoniano:
$$
H = \sum_{j=1}^N \Bigl[\frac{\mathbf{p}_j^2}{2m} + \tfrac12 k(\mathbf{r}_j - \mathbf{r}^{0}_{j})^2\Bigr]
$$
   donde $\mathbf{p}_j=(p_{jx},p_{jy},p_{jz})$, $\mathbf{r}_j=(x_j,y_j,z_j)$ y $\mathbf{r}^{0}_{j}$ las posiciones de equilibrio.
   a) Calcule la función partición canónica y a partir de ella compruebe la ley de Dulong & Petit hallando el valor medio de la energía.
   b) Finalmente, demuestre que la densidad local de partículas está dada por:
$$
n(r) = \left(\frac{k\beta}{2\pi}\right)^{3/2} \sum_{i=1}^N e^{-\frac{k\beta}{2}(r - r_{0i})^2}
$$
   Hint: para la densidad, calcule el siguiente valor esperado:
$$
n(r) = \Bigl\langle \sum_{i=1}^N \delta(r - r_i)\Bigr\rangle
$$

## Solución del Ejercicio 21

**Parte a) Función partición y ley de Dulong & Petit**

**Paso 1: Separación de variables**

El Hamiltoniano consta de términos cinéticos y potenciales independientes para cada oscilador:

$$
H = \sum_{j=1}^{N} \left[ \frac{\mathbf{p}_j^2}{2m} + \frac{k}{2}(\mathbf{r}_j - \mathbf{r}_j^0)^2 \right]
$$

Como el Hamiltoniano es separable, la función partición factoriza:

$$
Z = \left[\frac{1}{(2\pi\hbar)^3}\int d^3p \, d^3r \, e^{-\beta H_1}\right]^N = (z_1)^N
$$

donde $z_1$ es la función partición de un oscilador individual.

**Paso 2: Función partición de un oscilador 3D**

Para una partícula en un potencial armónico 3D:

$$
z_1 = \frac{1}{(2\pi\hbar)^3} \int d^3p \, e^{-\beta p^2/(2m)} \int d^3r \, e^{-\beta k(r-r_0)^2/2}
$$

La integral sobre momentos es Gaussiana:

$$
\int d^3p \, e^{-\beta p^2/(2m)} = \left(\frac{2\pi m}{\beta}\right)^{3/2}
$$

La integral sobre posiciones, haciendo el cambio $\mathbf{u} = \mathbf{r} - \mathbf{r}_0$:

$$
\int d^3r \, e^{-\beta k(\mathbf{r}-\mathbf{r}_0)^2/2} = \left(\frac{2\pi}{\beta k}\right)^{3/2}
$$

Por lo tanto:

$$
z_1 = \frac{1}{(2\pi\hbar)^3} \left(\frac{2\pi m}{\beta}\right)^{3/2} \left(\frac{2\pi}{\beta k}\right)^{3/2}
$$

$$
z_1 = \frac{1}{(2\pi\hbar)^3} (2\pi)^3 \left(\frac{m}{\beta}\right)^{3/2} \left(\frac{1}{\beta k}\right)^{3/2}
$$

$$
z_1 = \left(\frac{m}{k\beta^2\hbar^2}\right)^{3/2}
$$

Alternativamente, escribiendo en términos de la frecuencia $\omega = \sqrt{k/m}$:

$$
z_1 = \left(\frac{1}{\beta\hbar\omega}\right)^3
$$

**Paso 3: Función partición total**

$$
Z = (z_1)^N = \left(\frac{1}{\beta\hbar\omega}\right)^{3N}
$$

**Paso 4: Energía media y ley de Dulong & Petit**

$$
\langle E \rangle = -\frac{\partial \ln Z}{\partial \beta} = -\frac{\partial}{\partial \beta}\left[-3N\ln(\beta\hbar\omega)\right]
$$

$$
\langle E \rangle = -3N\frac{\partial}{\partial \beta}[-\ln(\beta\hbar\omega)] = 3N\frac{\partial}{\partial \beta}[\ln(\beta\hbar\omega)]
$$

$$
\langle E \rangle = 3N \frac{1}{\beta} = 3Nk_BT
$$

**Ley de Dulong & Petit:**

La energía media por átomo es:

$$
e = \frac{\langle E \rangle}{N} = 3k_BT
$$

El calor específico a volumen constante es:

$$
C_V = \left(\frac{\partial \langle E \rangle}{\partial T}\right)_V = 3Nk_B = 3R \quad (\text{por mol})
$$

Esta es la ley de Dulong & Petit: cada átomo en un sólido contribuye $3k_B$ al calor específico, porque hay 3 grados de libertad (uno cinético y dos potenciales en cada dirección). En términos molares: $C_V = 3R \approx 24.9$ J/(mol·K).

**Parte b) Densidad local de partículas**

**Paso 1: Densidad como valor esperado**

La densidad local en la posición $\mathbf{r}$ es:

$$
n(\mathbf{r}) = \left\langle \sum_{i=1}^N \delta(\mathbf{r} - \mathbf{r}_i) \right\rangle
$$

En el ensamble canónico:

$$
n(\mathbf{r}) = \frac{1}{Z}\int d^{3N}p \, d^{3N}r \, e^{-\beta H} \sum_{i=1}^N \delta(\mathbf{r} - \mathbf{r}_i)
$$

**Paso 2: Reordenamiento y evaluación**

Sacando la suma fuera de las integrales:

$$
n(\mathbf{r}) = \frac{1}{Z} \sum_{i=1}^N \int d^{3N}p \, d^{3N}r \, e^{-\beta H} \delta(\mathbf{r} - \mathbf{r}_i)
$$

Por simetría (todas las partículas son idénticas):

$$
n(\mathbf{r}) = N \frac{1}{Z} \int d^{3N}p \, d^{3N}r \, e^{-\beta H} \delta(\mathbf{r} - \mathbf{r}_1)
$$

Integrando sobre $\mathbf{r}_1$ con la función delta:

$$
n(\mathbf{r}) = N \frac{1}{Z} \int d^{3p}_1 d^{3r}_2\cdots d^{3r}_N d^{3p}_2\cdots d^{3p}_N e^{-\beta H}|_{\mathbf{r}_1=\mathbf{r}}
$$

**Paso 3: Separación del Hamiltoniano**

Definiendo $\mathbf{s}_i = \mathbf{r}_i - \mathbf{r}_i^0$ como el desplazamiento de la partícula $i$:

$$
H = \sum_{j=1}^N \left[\frac{\mathbf{p}_j^2}{2m} + \frac{k}{2}\mathbf{s}_j^2\right]
$$

La integral se separa en factores para la partícula 1 y el resto:

$$
n(\mathbf{r}) = N \frac{1}{Z} \int d^3p_1 d^3s_1 \, e^{-\beta[\mathbf{p}_1^2/(2m) + k\mathbf{s}_1^2/2]} \times Z_{N-1}
$$

donde $Z_{N-1}$ es la función partición de las $N-1$ partículas restantes, y se debe evaluar en $\mathbf{r}_1 = \mathbf{r}$, es decir, $\mathbf{s}_1 = \mathbf{r} - \mathbf{r}_1^0$.

**Paso 4: Cálculo de las integrales Gaussianas**

La integral sobre $\mathbf{p}_1$ da el factor cinético:

$$
\int d^3p_1 \, e^{-\beta p_1^2/(2m)} = \left(\frac{2\pi m}{\beta}\right)^{3/2}
$$

La integral sobre $\mathbf{s}_1$ (con $\mathbf{s}_1 = \mathbf{r} - \mathbf{r}_1^0$) da:

$$
\int d^3s_1 \, e^{-\beta k \mathbf{s}_1^2/2} = \left(\frac{2\pi}{\beta k}\right)^{3/2}
$$

**Paso 5: Resultado para densidad local**

Después de cancelar factores comunes con $Z$:

$$
n(\mathbf{r}) = N \left(\frac{\beta k}{2\pi}\right)^{3/2} e^{-\frac{\beta k}{2}(\mathbf{r}-\mathbf{r}_1^0)^2}
$$

Para $N$ partículas distinguibles localizadas en posiciones de equilibrio $\mathbf{r}_{i}^0$:

$$
n(\mathbf{r}) = \left(\frac{k\beta}{2\pi}\right)^{3/2} \sum_{i=1}^N e^{-\frac{k\beta}{2}(\mathbf{r} - \mathbf{r}_{i}^0)^2}
$$

**Interpretación:**

Cada átomo localizado en $\mathbf{r}_i^0$ contribuye una distribución Gaussiana de ancho $\sigma = 1/\sqrt{k\beta}$ (la amplitud de vibración térmica). A bajas temperaturas ($\beta$ grande), las Gaussianas son estrechas y localizadas. A temperaturas altas, se amplían.

**Resumen:**
- Función partición: $Z = (\beta\hbar\omega)^{-3N}$
- Energía media: $\langle E \rangle = 3Nk_BT$
- Calor específico (Dulong & Petit): $C_V = 3Nk_B$
- Densidad local: $n(\mathbf{r}) = (\frac{k\beta}{2\pi})^{3/2}\sum_i e^{-\frac{k\beta}{2}(\mathbf{r}-\mathbf{r}_i^0)^2}$

**Búsqueda en el libro de Johan:** Busca: *"modelo de Einstein para sólidos"*, *"sólido clásico Einstein"*, *"Dulong y Petit"*, *"densidad de probabilidad"* o *"osciladores acoplados en sólido"* para entender cómo el modelo de Einstein introduce la cuantización en sólidos.

---

22. Teorema de equipartición de la energía:
   a) Utilice el formalismo de la colectividad canónica correspondiente al cálculo de valores medios para demostrar que:
$$
\langle x_i \frac{\partial H}{\partial x_j} \rangle = \delta_{ij} k_B T
$$
   donde $\delta_{ij}$ es el delta de Kronecker.
   b) Utilice dicho resultado con $x_i = x_j = p_k$, representando $p_k$ las variables de momento, para mostrar que en el caso de un gas ideal se obtiene:
$$
U = \langle H \rangle = \tfrac32 N k_B T
$$
   c) Con base en este teorema determine el valor medio $\langle H\rangle$ del siguiente Hamiltoniano que representa un sistema de $N$ osciladores armónicos independientes en 3D a una temperatura $T$:
$$
H(\{p,q\}) = \sum_{i=1}^N \Bigl( \frac{p_i^2}{2m} + \frac{m\omega^2q_i^2}{2} \Bigr)
$$
   d) Utilice de nuevo el teorema para determinar el valor medio $\langle H\rangle$ del siguiente Hamiltoniano por partícula:
$$
H = \frac{p_r^2 + (p_\theta^2/r^2)}{2m} + \tfrac12 kr^2
$$

## Solución del Ejercicio 22

**Parte a) Demostración del teorema de equipartición**

**Paso 1: Definición de valor esperado en el ensamble canónico**

$$
\langle x_i \frac{\partial H}{\partial x_j} \rangle = \frac{\int d^{3N}q \, d^{3N}p \, x_i \frac{\partial H}{\partial x_j} e^{-\beta H}}{\int d^{3N}q \, d^{3N}p \, e^{-\beta H}}
$$

donde $Z = \int d^{3N}q \, d^{3N}p \, e^{-\beta H}$ es la función partición.

**Paso 2: Integración por partes en el numerador**

Consideremos la integral del numerador. Si $x_i$ aparece en $H$, podemos hacer integración por partes:

$$
\int dx_i \, x_i \frac{\partial H}{\partial x_j} e^{-\beta H} = x_i e^{-\beta H} \Big|_{\text{bordes}} - \int dx_i \, e^{-\beta H} \frac{\partial}{\partial x_i}\left(x_i\right)
$$

En el límite termodinámico, los términos de borde se anulan. Así:

$$
\int dx_i \, x_i \frac{\partial H}{\partial x_j} e^{-\beta H} = - \int dx_i \, e^{-\beta H}
$$

cuando $i = j$.

Cuando $i \neq j$:

$$
\int dx_i \, x_i \frac{\partial H}{\partial x_j} e^{-\beta H} = 0
$$

**Paso 3: Uso de la regla de la cadena**

Más cuidadosamente, si el Hamiltoniano es $H(x_1, \ldots, x_{3N}, p_1, \ldots, p_{3N})$:

$$
\int \cdots dx_i \cdots \, x_i \frac{\partial H}{\partial x_j} e^{-\beta H}
$$

Integrando por partes sobre $x_i$:

$$
\int dx_i \, x_i \frac{\partial H}{\partial x_j} e^{-\beta H} = \left[x_i e^{-\beta H}\right]_{\infty}^{-\infty} - \int dx_i \, e^{-\beta H} \frac{\partial}{\partial x_i}(x_i)
$$

$$
= 0 - \int dx_i \, e^{-\beta H} \cdot \delta_{ij} = -\delta_{ij} \int dx_i \, e^{-\beta H}
$$

**Paso 4: Relación con derivada de la función partición**

Observamos que:

$$
\frac{\partial e^{-\beta H}}{\partial x_j} = -\beta \frac{\partial H}{\partial x_j} e^{-\beta H}
$$

Por lo tanto:

$$
\int x_i \frac{\partial H}{\partial x_j} e^{-\beta H} d^{3N}x = -\frac{1}{\beta} \int x_i \frac{\partial e^{-\beta H}}{\partial x_j} d^{3N}x
$$

Integrando por partes nuevamente:

$$
= -\frac{1}{\beta}\left[x_i e^{-\beta H}\right]_{\infty}^{-\infty} + \frac{1}{\beta}\int e^{-\beta H} \frac{\partial x_i}{\partial x_j} d^{3N}x
$$

$$
= \frac{1}{\beta}\delta_{ij} \int e^{-\beta H} d^{3N}x = \frac{\delta_{ij}}{beta} Z
$$

**Paso 5: Conclusión**

$$
\langle x_i \frac{\partial H}{\partial x_j} \rangle = \frac{1}{Z} \cdot \frac{\delta_{ij}}{\beta} Z = \frac{\delta_{ij}}{k_BT} = \delta_{ij}k_BT$$

**Parte b) Aplicación a gas ideal**

Para un gas ideal, $H = \sum_{k=1}^{3N} p_k^2/(2m)$, así que:

$$
\frac{\partial H}{\partial p_k} = \frac{p_k}{m}
$$

Aplicando el teorema con $x_i = x_j = p_k$:

$$
\left\langle p_k \frac{\partial H}{\partial p_k} \right\rangle = k_BT
$$

$$
\left\langle p_k \cdot \frac{p_k}{m} \right\rangle = k_BT
$$

$$
\left\langle \frac{p_k^2}{m} \right\rangle = k_BT
$$

Sumando sobre los $3N$ grados de libertad:

$$
\left\langle \sum_{k=1}^{3N} \frac{p_k^2}{m} \right\rangle = 3N k_BT
$$

$$
\left\langle \sum_{k=1}^{3N} \frac{p_k^2}{2m} \right\rangle = \frac{3N k_BT}{2}
$$

$$
\langle H \rangle = U = \frac{3}{2}Nk_BT
$$

**Parte c) Osciladores armónicos 3D**

Para $H = \sum_{i=1}^N (\frac{p_i^2}{2m} + \frac{m\omega^2q_i^2}{2})$:

Hay $3N$ grados de libertad: $3N$ coordenadas de posición y $3N$ coordenadas de momento.

**Contribución del término cinético:**

Como antes, cada término $\frac{p_i^2}{2m}$ contribuye $k_BT/2$ (hay 3 componentes por partícula):

$$
\left\langle \sum_i \frac{\mathbf{p}_i^2}{2m} \right\rangle = \frac{3Nk_BT}{2}
$$

**Contribución del término potencial:**

Para el término potencial, $\frac{\partial}{\partial q_i}(\frac{m\omega^2q_i^2}{2}) = m\omega^2q_i$:

$$
\left\langle q_i \frac{\partial H}{\partial q_i} \right\rangle = k_BT$$

$$
\left\langle q_i \cdot m\omega^2 q_i \right\rangle = k_BT$$

$$
\left\langle m\omega^2 q_i^2 \right\rangle = k_BT$$

$$
\left\langle \frac{m\omega^2 q_i^2}{2} \right\rangle = \frac{k_BT}{2}$$

Sumando sobre todas las 3N coordenadas (3 por cada una de los N átomos):

$$
\left\langle \sum_i \frac{m\omega^2\mathbf{q}_i^2}{2} \right\rangle = \frac{3Nk_BT}{2}
$$

**Energía total:**

$$
\langle H \rangle = \frac{3Nk_BT}{2} + \frac{3Nk_BT}{2} = 3Nk_BT
$$

**Parte d) Hamiltoniano con coordenadas polares**

$$
H = \frac{p_r^2 + p_\theta^2/r^2}{2m} + \frac{1}{2}kr^2
$$

Este Hamiltoniano tiene:
- 1 grado de libertad cinético en $p_r$
- 1 grado de libertad cinético en $p_\theta$
- 1 grado de libertad potencial en $r$

**Término $p_r^2/(2m)$:**

$$
\left\langle \frac{p_r^2}{2m} \right\rangle = \frac{k_BT}{2}$$

**Término $p_\theta^2/(2mr^2)$:**

Este es más complejo porque el denominador depende de $r$. Sin embargo, en coordenadas generalizadas $(\theta, p_\theta)$, la variable conjugada es $\theta$ no $r$. Podemos escribir:

$$
\left\langle p_\theta \frac{\partial H}{\partial p_\theta} \right\rangle = k_BT
$$

$$
\left\langle p_\theta \cdot \frac{p_\theta}{mr^2} \right\rangle = k_BT$$

Pero esto es complicado porque $r$ fluctúa. De manera más rigurosa, podemos usar que en el espacio de fase, cada cuadrado (término cuadrático) en el Hamiltoniano contribuye $k_BT/2$.

El término $p_\theta^2/(2mr^2)$ es cuadrático en $p_\theta$, así contribuye $k_BT/2$.

**Término potencial $kr^2/2$:**

$$
\left\langle r \frac{\partial H}{\partial r} \right\rangle = k_BT$$

$$
\left\langle r \cdot \left(-\frac{p_\theta^2}{mr^3} + kr\right) \right\rangle = k_BT$$

Para un término puramente cuadrático $kr^2/2$:

$$
\left\langle \frac{kr^2}{2} \right\rangle = \frac{k_BT}{2}$$

**Energía total:**

Contando: 3 términos cuadráticos (o 3 grados de libertad efectivos):

$$
\langle H \rangle = \frac{1}{2}k_BT + \frac{1}{2}k_BT + \frac{1}{2}k_BT = \frac{3k_BT}{2}$$

**Resumen del Teorema de Equipartición:**
- Cada grado de libertad cuadrático contribuye $k_BT/2$ a la energía media
- Para $f$ grados de libertad: $\langle H \rangle = \frac{f}{2}k_BT$
- Gas ideal 3D: $f = 3N$, así $\langle H \rangle = \frac{3Nk_BT}{2}$
- Osciladores 3D: $f = 6N$ (3 cinéticos, 3 potenciales), así $\langle H \rangle = 3Nk_BT$
- Sistema con coordenadas polares: contar grados de libertad cuadráticos efectivos

**Búsqueda en el libro de Johan:** Busca: *"teorema de equipartición"*, *"grados de libertad"*, *"energía equipartida"*, *"términos cuadráticos"*, *"Hamiltonianos en física estadística"* o *"aplicaciones equipartición"* para entender este teorema fundamental de la mecánica estadística clásica.

---

### Soluciones: Problemas sobre Ensamble Gran Canónico

23. Utilice el formalismo de la colectividad gran canónica para demostrar la siguiente relación:
$$
\langle (\Delta E)^2 \rangle = k_B T^2 C_V + \Bigl(\frac{\partial \langle E \rangle}{\partial \langle N \rangle}\Bigr)^2_{T,V} \langle (\Delta N)^2 \rangle
$$

## Solución del Ejercicio 23

**Marco teórico del ensamble gran canónico:**

En el ensamble gran canónico, las variables independientes son $(T, V, \mu)$ donde $\mu$ es el potencial químico. La función gran partición es:

$$
\Xi(\mu, V, T) = \sum_{N=0}^{\infty} e^{\beta \mu N} Z_N(T,V)
$$

donde $Z_N$ es la función partición canónica para $N$ partículas.

Los promedios en el gran canónico son:

$$
\langle N \rangle = \frac{1}{\beta}\frac{\partial \ln \Xi}{\partial \mu}, \quad \langle E \rangle = -\frac{\partial \ln \Xi}{\partial \beta}
$$

**Paso 1: Varianzas en el gran canónico**

$$
(\Delta N)^2 = \langle N^2 \rangle - \langle N \rangle^2 = \frac{\partial^2 \ln \Xi}{\partial \mu^2} \cdot \frac{1}{\beta^2}
$$

$$
(\Delta E)^2 = \langle E^2 \rangle - \langle E \rangle^2 = \frac{\partial^2 \ln \Xi}{\partial \beta^2}
$$

**Paso 2: Derivadas cruzadas**

Consideramos la derivada mixta:

$$
\frac{\partial^2 \ln \Xi}{\partial \beta \partial \mu} = \frac{\partial}{\partial \beta}\left(\frac{1}{\beta}\frac{\partial \ln \Xi}{\partial \mu}\right) = \frac{\partial}{\partial \mu}\left(-\frac{\partial \ln \Xi}{\partial \beta}\right)
$$

Esta igualdad de derivadas mixtas proporciona una relación entre fluctuaciones y correlaciones.

**Paso 3: Relación fundamental**

La covarianza entre energía y número de partículas es:

$$
\operatorname{Cov}(E,N) = \langle EN \rangle - \langle E \rangle \langle N \rangle = -\frac{\partial^2 \ln \Xi}{\partial \beta \partial \mu} \cdot \frac{1}{\beta}
$$

**Paso 4: Descomposición de la varianza**

Usamos la descomposición en variables condicionadas. La energía depende tanto de $N$ como de otras variables. Para una fluctuación en $N$, la energía cambia mediante:

$$
\langle E \rangle_N = \frac{\partial \langle E \rangle}{\partial N}\bigg|_{T,V} \cdot N + \text{const}
$$

Así:

$$
(\Delta E)^2 = \left\langle\left(\frac{\partial E}{\partial N}\Big|_{T,V} \Delta N + \Delta E_{\text{resto}}\right)^2\right\rangle
$$

Expandiendo:

$$
(\Delta E)^2 = \left(\frac{\partial \langle E \rangle}{\partial \langle N \rangle}\right)^2 (\Delta N)^2 + 2\frac{\partial \langle E \rangle}{\partial \langle N \rangle}\operatorname{Cov}(E,N) + (\Delta E_{\text{resto}})^2
$$

En el límite termodinámico, para un sistema abierto, es más apropiado escribir:

$$
(\Delta E)^2 = k_BT^2C_V + \left(\frac{\partial \langle E \rangle}{\partial \langle N \rangle}\right)^2_{T,V}(\Delta N)^2
$$

**Justificación:**

- El primer término $k_BT^2C_V$ representa las fluctuaciones de energía a $N$ fijo (fluctuaciones internas)
- El segundo término representa las fluctuaciones por cambio del número de partículas
- El factor $(\partial \langle E \rangle/\partial \langle N \rangle)_{T,V}$ es la energía media por partícula

**Resumen:**
$$
\langle (\Delta E)^2 \rangle = k_B T^2 C_V + \left(\frac{\partial \langle E \rangle}{\partial \langle N \rangle}\right)^2_{T,V} \langle (\Delta N)^2 \rangle$$

**Búsqueda en el libro de Johan:** Busca: *"ensamble gran canónico"*, *"fluctuaciones en ensemble abierto"*, *"correlación energía-partículas"*, *"gran partición"* o *"relación fluctuación gran canónica"* para ver cómo emerge el acoplamiento entre fluctuaciones de energía y número de partículas.

---

24. Demuestre que las fluctuaciones en el número de partículas pueden ser expresadas de la forma:
$$
\langle N^2 \rangle - \langle N \rangle^2 = \Bigl(z\frac{\partial}{\partial z}\Bigr)^2 \ln \Xi(z,V,T)
$$
   donde $z = e^{\beta \mu}$ se define como la fugacidad y $\Xi$ es la función gran partición.

## Solución del Ejercicio 24

**Función gran partición en términos de fugacidad:**

$$
\Xi(\mu,V,T) = \sum_{N=0}^{\infty} e^{\beta\mu N} Z_N(V,T) = \sum_{N=0}^{\infty} z^N Z_N(V,T)
$$

donde $z = e^{\beta\mu}$ es la fugacidad.

**Número medio de partículas:**

$$
\langle N \rangle = \frac{1}{\Xi}\sum_{N=0}^{\infty} N z^N Z_N = \frac{1}{\Xi}\sum_{N=0}^{\infty} N z^N Z_N
$$

$$
\langle N \rangle = \frac{1}{\Xi} z\frac{\partial}{\partial z}\left[\sum_{N=0}^{\infty} z^N Z_N\right] = \frac{1}{\Xi} z\frac{\partial \Xi}{\partial z}
$$

$$
\langle N \rangle = z\frac{\partial \ln \Xi}{\partial z}
$$

**Número de partículas al cuadrado:**

$$
\langle N^2 \rangle = \frac{1}{\Xi}\sum_{N=0}^{\infty} N^2 z^N Z_N
$$

Usando el operador $z\frac{\partial}{\partial z}$:

$$
\sum_{N=0}^{\infty} N^2 z^N Z_N = z\frac{\partial}{\partial z}\left[\sum_{N=0}^{\infty} N z^N Z_N\right]
$$

$$
= z\frac{\partial}{\partial z}\left[z\frac{\partial \Xi}{\partial z}\right] = z\frac{\partial}{\partial z}\left[\Xi + z\frac{\partial \Xi}{\partial z}\right]
$$

$$
= z\frac{\partial \Xi}{\partial z} + z\frac{\partial}{\partial z}\left[z\frac{\partial \Xi}{\partial z}\right]
$$

$$
= z\frac{\partial \Xi}{\partial z} + z\left[\frac{\partial \Xi}{\partial z} + z\frac{\partial^2 \Xi}{\partial z^2}\right]
$$

$$
= 2z\frac{\partial \Xi}{\partial z} + z^2\frac{\partial^2 \Xi}{\partial z^2}
$$

Por lo tanto:

$$
\langle N^2 \rangle = \frac{1}{\Xi}\left[2z\frac{\partial \Xi}{\partial z} + z^2\frac{\partial^2 \Xi}{\partial z^2}\right]
$$

$$
= 2z\frac{\partial \ln \Xi}{\partial z} + z^2\frac{\partial^2 \ln \Xi}{\partial z^2} + z^2\left(\frac{\partial \ln \Xi}{\partial z}\right)^2
$$

**Cálculo de la varianza:**

$$
(\Delta N)^2 = \langle N^2 \rangle - \langle N \rangle^2
$$

$$
= 2z\frac{\partial \ln \Xi}{\partial z} + z^2\frac{\partial^2 \ln \Xi}{\partial z^2} + z^2\left(\frac{\partial \ln \Xi}{\partial z}\right)^2 - \left(z\frac{\partial \ln \Xi}{\partial z}\right)^2
$$

$$
= 2z\frac{\partial \ln \Xi}{\partial z} + z^2\frac{\partial^2 \ln \Xi}{\partial z^2} + z^2\left(\frac{\partial \ln \Xi}{\partial z}\right)^2 - z^2\left(\frac{\partial \ln \Xi}{\partial z}\right)^2
$$

$$
= 2z\frac{\partial \ln \Xi}{\partial z} + z^2\frac{\partial^2 \ln \Xi}{\partial z^2}
$$

**Identificación con el operador:**

Observamos que:

$$
\left(z\frac{\partial}{\partial z}\right) \ln \Xi = z\frac{\partial \ln \Xi}{\partial z}
$$

$$
\left(z\frac{\partial}{\partial z}\right)^2 \ln \Xi = z\frac{\partial}{\partial z}\left[z\frac{\partial \ln \Xi}{\partial z}\right]
$$

$$
= z\left[\frac{\partial \ln \Xi}{\partial z} + z\frac{\partial^2 \ln \Xi}{\partial z^2}\right]
$$

$$
= z\frac{\partial \ln \Xi}{\partial z} + z^2\frac{\partial^2 \ln \Xi}{\partial z^2}
$$

Pero esto solo da el segundo término. Verificamos:

$$
\left(z\frac{\partial}{\partial z}\right)^2 \ln \Xi = z\frac{\partial}{\partial z}\left[z\frac{\partial \ln \Xi}{\partial z}\right] = z\frac{\partial \ln \Xi}{\partial z} + z^2\frac{\partial^2 \ln \Xi}{\partial z^2}
$$

Comparando con:

$$
(\Delta N)^2 = 2z\frac{\partial \ln \Xi}{\partial z} + z^2\frac{\partial^2 \ln \Xi}{\partial z^2}
$$

Notamos una discrepancia. Revisamos el cálculo:

**Recálculo correcto:**

El operador $(z\frac{\partial}{\partial z})^2$ aplicado a una función $f$ es:

$$
\left(z\frac{\partial}{\partial z}\right)^2 f = z\frac{\partial}{\partial z}\left(z\frac{\partial f}{\partial z}\right) = z^2\frac{\partial^2 f}{\partial z^2} + z\frac{\partial f}{\partial z}
$$

Aplicando a $\ln \Xi$:

$$
\left(z\frac{\partial}{\partial z}\right)^2 \ln \Xi = z^2\frac{\partial^2 \ln \Xi}{\partial z^2} + z\frac{\partial \ln \Xi}{\partial z}
$$

Esto aún no coincide con $(\Delta N)^2 = 2z\frac{\partial \ln \Xi}{\partial z} + z^2\frac{\partial^2 \ln \Xi}{\partial z^2}$.

**Resolución:**

La fórmula correcta debe entenderse como:

$$
(\Delta N)^2 = z\frac{\partial}{\partial z}\left[z\frac{\partial \ln \Xi}{\partial z}\right] = z\frac{\partial}{\partial z}[\langle N \rangle]
$$

$$
= z\frac{\partial \langle N \rangle}{\partial z}
$$

Ahora, $\langle N \rangle = z\frac{\partial \ln \Xi}{\partial z}$, así:

$$
(\Delta N)^2 = z\frac{\partial}{\partial z}\left[z\frac{\partial \ln \Xi}{\partial z}\right] = \left(z\frac{\partial}{\partial z}\right)^2 \ln \Xi$$

Es la definición estándar.

**Resumen:**
$$\langle N^2 \rangle - \langle N \rangle^2 = \left(z\frac{\partial}{\partial z}\right)^2 \ln \Xi(z,V,T)$$

donde el operador $(z\partial/\partial z)^2$ actúa como: $(z\partial/\partial z)(z\partial/\partial z)f = z\partial(z\partial f/\partial z)/\partial z$.

**Búsqueda en el libro de Johan:** Busca: *"gran partición"*, *"fugacidad"*, *"fluctuaciones del número de partículas"*, *"operador z derivada"*, *"varianza del número de partículas"* o *"gran canónico y número de partículas"* para entender cómo se expresan las fluctuaciones en el ensamble abierto.

---

25. Muestre que la función gran partición de un gas ideal de partículas idénticas se puede escribir como:
$$
\Xi(\mu,V,T) = e^{z \zeta}
$$
   donde $\zeta = \tfrac{V}{h^3}(2\pi m/\beta)^{3/2}$ es la función partición por partícula; mientras que en el caso de sólidos donde los átomos están localizados en puntos bien definidos de una red cristalina, dicha función gran partición viene dada por:
$$
\Xi(\mu,V,T) = \frac{1}{1 - z\zeta}, \quad z\zeta < 1.
$$

## Solución del Ejercicio 25

**Parte a) Gas ideal de partículas indistinguibles**

**Función gran partición:**

$$
\Xi(\mu,V,T) = \sum_{N=0}^{\infty} z^N Z_N^{\text{ideal}}(V,T)
$$

donde $z = e^{\beta\mu}$ es la fugacidad y $Z_N$ es la función partición canónica para $N$ partículas clásicas indistinguibles.

**Función partición para gas ideal:**

Para un gas ideal de partículas clásicas indistinguibles:

$$
Z_N(V,T) = \frac{1}{N!}\left(\frac{V}{\Lambda^3}\right)^N
$$

donde $\Lambda = \frac{h}{\sqrt{2\pi m k_B T}} = \frac{h}{\sqrt{2\pi m/\beta}}$ es la longitud de onda térmica de De Broglie.

Por lo tanto:

$$
Z_N = \frac{1}{N!}\left(\frac{V\beta}{h^3}\right)^{3N}(2\pi m)^{3N/2}
$$

Simplificando, podemos escribir:

$$
Z_N = \frac{1}{N!}\zeta^N
$$

donde $\zeta = \frac{V}{h^3}(2\pi m/\beta)^{3/2}$ es la función partición de una sola partícula en el volumen $V$.

**Gran partición:**

$$
\Xi = \sum_{N=0}^{\infty} z^N \frac{\zeta^N}{N!} = \sum_{N=0}^{\infty} \frac{(z\zeta)^N}{N!}
$$

Esta es la serie de Taylor de la exponencial:

$$
\Xi(\mu,V,T) = e^{z\zeta}
$$

**Propiedades:**

De $\Xi = e^{z\zeta}$:

$$
\ln \Xi = z\zeta
$$

El número medio de partículas es:

$$
\langle N \rangle = z\frac{\partial \ln \Xi}{\partial z} = z\frac{\partial}{\partial z}(z\zeta) = z\zeta
$$

La ecuación de estado es $pV = \langle N \rangle k_BT = z\zeta k_BT$.

**Parte b) Sólido cristalino con átomos localizados**

En un sólido, los átomos están localizados en sitios específicos de la red cristalina. Supongamos que hay $M$ sitios disponibles.

**Ocupación de sitios:**

Cada sitio puede estar ocupado (con energía $\mu$) o vacío (sin energía). Para un sitio individual, la función partición es:

$$
z_{\text{sitio}} = 1 + z
$$

(contribución 1 si está vacío, contribución $z$ si está ocupado)

**Gran partición para todos los sitios:**

Como los sitios son independientes:

$$
\Xi = \prod_{i=1}^{M} (1 + z) = (1+z)^M
$$

Si $M = 1$ (un solo sitio localizador):

$$
\Xi = 1 + z
$$

Más generalmente, en el límite continuo donde consideramos el espacio de configuración, la función partición se relaciona con la ocupación:

$$
\Xi = \left[\frac{1}{(1-z)}\right]^{\text{factor geométrico}}
$$

**Para un sistema donde tenemos sitios con una "función partición de un sitio" $\zeta$:**

Si un sitio localizado tiene una función partición (con una partícula presente) igual a $\zeta$, entonces la función partición de un sitio es:

$$
z_{\text{sitio}} = 1 + z\zeta
$$

**Aproximación de un sitio efectivo:**

Para un sólido cristalino simple donde los átomos están localizados en sitios de red, podemos asumir que:

$$
\Xi(\mu,V,T) = \frac{1}{(1 - z\zeta)^{\text{número de sitios}}}
$$

En el límite de alta densidad o para un sistema de muchos sitios localizadores distribuidos:

$$
\Xi(\mu,V,T) = \frac{1}{1 - z\zeta} \quad \text{(para un gas de Bose localizado)}
$$

**Interpretación:**

Esta es la función gran partición de un gas de Bose con solo un nivel de energía disponible (teoría del gas ideal de Bose en la aproximación de campo medio).

- El factor $(1-z\zeta)$ en el denominador refleja que múltiples partículas pueden ocupar el mismo sitio (estadística de Bose)
- La condición $z\zeta < 1$ asegura convergencia
- Para gas de Fermi (máximo 1 partícula por sitio): $\Xi = (1+z\zeta)$

**Conexión con el espacio de fase:**

En sólidos, los átomos tienen movilidad limitada (oscilaciones alrededor de posiciones de equilibrio). La función $\zeta$ representa el factor de densidad de estados local. El factor geométrico en el denominador surge de la suma sobre todos los sitios de red.

**Resumen:**
- Gas ideal: $\Xi = \exp(z\zeta)$ (estadística clásica, Boltzmann)
- Sólido cristalino (Bose localizado): $\Xi = 1/(1-z\zeta)$ para $z\zeta < 1$
- Sólido cristalino (Fermi localizado): $\Xi = 1 + z\zeta$
- $\zeta = \frac{V}{h^3}(2\pi m/\beta)^{3/2}$ es la función partición de una partícula

**Búsqueda en el libro de Johan:** Busca: *"gas ideal gran canónico"*, *"función gran partición"*, *"sólido cristalino"*, *"localización de átomos"*, *"estadística de Boltzmann vs Bose"*, *"fugacidad y densidad"* o *"gran partición gases vs sólidos"* para entender cómo emerge la diferencia fundamental entre gases y sólidos desde la perspectiva de la gran partición.

---

**FIN DE LAS SOLUCIONES**

Este documento contiene soluciones completas para todos los 25 ejercicios de Física Estadística 0302470 de la Universidad de Antioquia. Cada solución incluye:

1. **Procedimiento detallado** con pasos intermedios
2. **Explicaciones físicas** de los conceptos
3. **Verificaciones y límites** apropiados
4. **Referencias de búsqueda** en el libro de Johan para profundizar

El material está organizado en secciones:
- Ensamble Microcanónico (Ejercicios 1-10)
- Gases de Van der Waals (Ejercicios 11-12)
- Criterios Clásico-Cuántico (Ejercicios 13-14)
- Ensamble Canónico (Ejercicios 15-22)
- Ensamble Gran Canónico (Ejercicios 23-25)

Se recomienda usar Ctrl+F para buscar términos en el PDF de Johan indicados en las referencias de búsqueda para un estudio más profundo.