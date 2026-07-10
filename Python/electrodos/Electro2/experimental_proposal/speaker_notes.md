# Notas de exposición: propuesta conceptual de metasuperficie

Duración objetivo: 10 a 15 minutos. Cada entrada corresponde a una diapositiva del deck de 20 slides. El mensaje central debe repetirse con claridad: la propuesta es conceptual, los datos son esperados y las figuras sintéticas ilustran cómo se evaluaría la relación entre teoría y datos esperados.

## Diapositiva 1: Título técnico y pregunta experimental

Presentar el título completo y ubicar el tema en microondas. La pregunta guía es cómo cambiarían la reflexión, la transmisión y la absorción cuando una onda incide sobre una metasuperficie reconfigurable. Aclarar que las magnitudes clave serían `S11`, `S21`, `R`, `T`, `A`, `f0`, `Delta f` y `Q`. La diapositiva abre con la rúbrica de título y deja claro el objeto físico.

Referencia de apoyo: Holloway et al. para metasuperficies; Pozar para parámetros `S`.

## Diapositiva 2: Alcance conceptual

Decir explícitamente que es una propuesta conceptual, no destinada a ser ejecutada durante el curso. Explicar que no se presentan mediciones reales; se propone un montaje y se muestran datos esperados para ilustrar el análisis. Esta aclaración protege la interpretación del informe: todo está escrito en condicional. También prepara al evaluador para leer las gráficas como herramientas metodológicas.

Referencia de apoyo: Pozar para caracterización en microondas mediante VNA y parámetros `S`.

## Diapositiva 3: Motivación

Explicar que una metasuperficie funciona como una frontera artificial diseñada. En vez de aceptar la reflexión o transmisión natural de un material, se diseña una geometría para controlar amplitud, fase y absorción. La idea conecta electrodinámica clásica con tecnología moderna. Esta motivación justifica por qué los parámetros `S` son observables adecuados.

Referencia de apoyo: Yu & Capasso para metasuperficies de fase diseñada; Holloway et al. para la formulación general.

## Diapositiva 4: Aplicaciones tecnológicas

Recorrer las aplicaciones sin extenderse demasiado: absorbentes, cámaras anecoicas, blindaje, telecomunicaciones, superficies inteligentes, sensores, radar, THz y polarización. La clave es que todas esas aplicaciones se pueden discutir mediante magnitudes verificables. Reforzar que no se venden resultados, sino un método de caracterización. La diapositiva conecta la discusión con utilidad real.

Referencia de apoyo: Watts et al. para absorbentes; Cui et al. para metamateriales programables.

## Diapositiva 5: Objetivo general

Leer el objetivo general de forma natural: proponer un experimento conceptual para caracterizar la metasuperficie mediante parámetros `S`. Luego explicar el mapa de magnitudes: desde `S11` y `S21` se derivan `R`, `T`, `A`, frecuencia de resonancia, ancho de banda y factor de calidad. Esto muestra que la propuesta tiene variables medibles y análisis definido.

Referencia de apoyo: Pozar para parámetros `S`; Landy et al. para su uso en absorbentes metamateriales.

## Diapositiva 6: Objetivos específicos

Presentar los objetivos como una ruta de trabajo: definir observables, proponer montaje, calcular balance de potencia, extraer parámetros resonantes, ajustar un modelo y evaluar errores. Recordar que objetivos vale 15% en la rúbrica, por eso están separados del objetivo general. La diapositiva debe sonar como checklist verificable, no como lista decorativa.

Referencia de apoyo: Milton & Schwinger, Jackson y Griffiths para el marco de electrodinámica del curso.

## Diapositiva 7: Parámetros S

Explicar que en microondas se trabaja con ondas incidentes y salientes, por eso `Sij` es complejo: tiene módulo y fase. `S11` describe reflexión hacia el puerto de entrada; `S21` describe transmisión hacia el puerto de salida. La fase importa porque cerca de una resonancia la respuesta dispersiva cambia rápido. Este es el primer bloque fuerte de teoría.

Referencia de apoyo: Pozar para parámetros `S`; Landy para su uso experimental en absorbentes.

## Diapositiva 8: Reflexión, transmisión y absorción

Derivar verbalmente el balance: `R = |S11|^2`, `T = |S21|^2` y `A = 1 - R - T`. La advertencia es fundamental: ese `A` solo representa absorción si no se pierde potencia por scattering lateral o caminos no capturados. Si no se controla el entorno, el cálculo puede sobreestimar la absorción. Esta diapositiva anticipa el análisis de errores.

Referencia de apoyo: Landy et al. y Watts et al. para absorción obtenida desde parámetros `S` bajo condiciones controladas.

## Diapositiva 9: Impedancia efectiva

Explicar que `Z0` es la impedancia del espacio libre y vale aproximadamente 377 ohm. La reflexión depende de la diferencia entre `Zeff` y `Z0`; si son muy distintos, la onda rebota. Para una absorción alta se necesita adaptación de impedancia y pérdidas internas. Esa combinación es la interpretación física del pico esperado de absorción.

Referencia de apoyo: Milton & Schwinger para impedancia y fronteras; Landy et al. para adaptación en absorbentes.

## Diapositiva 10: Modelo LC

Presentar cada celda como resonador sublongitud de onda, con `p << lambda`. La geometría metálica aporta inductancia efectiva y las brechas o varactores aportan capacitancia. La ecuación `f0 = 1/(2*pi*sqrt(LC))` explica por qué cambiar la capacitancia desplaza la resonancia. `Q = f0/Delta f` resume qué tan estrecha o ancha sería la respuesta.

Referencia de apoyo: Engheta & Ziolkowski para metamateriales; Holloway et al. para metasuperficies sublongitud de onda.

## Diapositiva 11: Lorentz y supuestos

Explicar el modelo de Lorentz como una forma macroscópica de representar dispersión y pérdidas cerca de una frecuencia resonante. La parte real se relaciona con fase y dispersión; la parte imaginaria con pérdidas. Mencionar los supuestos: campo lejano, incidencia aproximadamente plana, régimen lineal, muestra suficientemente grande y calibración válida. Sin esos supuestos, la interpretación de parámetros efectivos pierde fuerza.

Referencia de apoyo: Milton & Schwinger y Jackson para medios dispersivos; Smith et al. para la cautela al extraer parámetros efectivos.

## Diapositiva 12: Materiales y adquisición

Indicar que el reporte tiene una tabla completa y la diapositiva resume categorías. VNA, antenas, cables y kit de calibración sostienen la medición; PCB, sustrato y elementos reconfigurables sostienen la muestra; absorbentes, cámara y software sostienen control y análisis. Los costos son rangos, no precios inventados. Todo quedaría a confirmar con laboratorio o proveedor.

Referencia de apoyo: Pozar para instrumentación de microondas; Balanis para antenas.

## Diapositiva 13: Montaje propuesto

Usar el diagrama para narrar el camino físico de la señal. El VNA alimentaría la antena TX por puerto 1, la onda incidiría en la metasuperficie, `S21` correspondería a la transmisión hacia RX y `S11` a la reflexión de vuelta hacia TX. Los absorbentes reducen reflexiones parásitas y la distancia `d` se relaciona con campo lejano. El plano metálico es opcional para estudiar absorción con transmisión suprimida.

Referencia de apoyo: Landy para VNA 8--12 GHz y antenas horn; Balanis para alineación y campo lejano.

## Diapositiva 14: Procedimiento

Presentar el procedimiento como una secuencia futura: calibrar, alinear, registrar referencias, barrer frecuencia, repetir configuraciones y estimar incertidumbres. No usar lenguaje de ejecución material; mantener condicional. Explicar que la repetición por `V_bias` permite estudiar reconfiguración. El procedimiento muestra que la propuesta sería reproducible en principio.

Referencia de apoyo: Pozar para calibración y barrido de parámetros `S`.

## Diapositiva 15: Toma de datos

Explicar que la tabla define qué columnas debería tener un archivo de datos: frecuencia, módulos, fases, estado de sesgo, absorción e incertidumbre. La inclusión de fase evita perder información compleja. Las unidades ordenadas reducen ambigüedad al analizar. Esta diapositiva ayuda al evaluador a ver que la toma de datos está pensada antes del análisis.

Referencia de apoyo: Pozar para módulo/fase de parámetros `S`; Smith et al. para usar reflexión y transmisión en extracción efectiva.

## Diapositiva 16: Resultados esperados S y absorción

Decir de entrada que la figura usa datos esperados sintéticos. La curva muestra el patrón que se buscaría: un mínimo en reflexión, una reducción de transmisión y un pico de absorción cerca de 10 GHz. La figura ayuda porque convierte la teoría en señales observables. También permite discutir qué pasaría si el pico fuera más bajo, más ancho o estuviera desplazado.

Referencia de apoyo: Landy et al. y Watts et al. para firmas espectrales de absorbentes metamateriales.

## Diapositiva 17: Reconfiguración

Explicar que la gráfica `f0` versus `V_bias` ilustra el mecanismo de reconfiguración. En el modelo, la capacitancia depende del voltaje y por eso cambia la frecuencia resonante. La curva no afirma datos reales; muestra qué tendencia esperada permitiría comprobar que el sesgo DC modifica la respuesta. Esta figura conecta el modelo `LC` con un observable directo.

Referencia de apoyo: Cui et al. para respuesta programable; Zheludev & Kivshar para el paso de metamateriales a metadevices.

## Diapositiva 18: Ajuste y residuales

Explicar que la comparación teoría versus datos esperados es el puente entre el fundamento y el análisis cuantitativo. La curva representa un ajuste resonante y los puntos son datos esperados sintéticos con barras de incertidumbre. Los residuales muestran si el modelo deja estructura sistemática sin explicar. Si los residuales quedan centrados alrededor de cero, el modelo sería compatible dentro de la incertidumbre esperada.

Referencia de apoyo: Smith para extracción/ajuste de parámetros efectivos; Pozar para interpretación de datos `S`.

## Diapositiva 19: Errores, incertidumbres y seguridad

Presentar el presupuesto de error como una forma de priorizar qué controla la calidad del montaje. Calibración, alineación, repetibilidad, scattering lateral y resolución afectan directamente `A`, `f0` y `Q`. Luego conectar con seguridad: baja potencia no elimina buenas prácticas, especialmente con RF, conectores y sesgo DC. Esta diapositiva cubre errores y seguridad de manera compacta.

Referencia de apoyo: Balanis para alineación/campo lejano; Pozar para limitaciones de medición en microondas.

## Diapositiva 20: Discusión, conclusiones y bibliografía

Cerrar interpretando los casos principales: un pico de absorción apuntaría a adaptación de impedancia más pérdidas; `A < 1` puede venir de reflexión, transmisión o pérdidas insuficientes; un `f0` desplazado puede indicar tolerancias o sustrato real distinto. Repetir que la propuesta no demuestra resultados reales, sino que diseña una ruta conceptual completa. Mencionar la bibliografía mínima como soporte académico: Pozar, Balanis, Holloway, Landy y Watts.

Referencia de apoyo: Milton & Schwinger, Pozar, Holloway, Landy, Yu & Capasso y Watts como bibliografía mínima de cierre.
