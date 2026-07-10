# Checklist de entrega: propuesta experimental conceptual

Este checklist permite verificar la entrega contra la rúbrica del profesor. La propuesta es conceptual: no está destinada a ejecutarse durante el curso y las gráficas son datos sintéticos esperados para ilustrar el método de análisis.

| Criterio | Sección informe | Slide(s) | Peso | Verificación |
|---|---|---:|---:|---|
| Título del experimento | `\section{Título del experimento}` | 1 | 5% | El título menciona metasuperficie electromagnética reconfigurable, microondas, parámetros `S`, reflexión, transmisión y absorción resonante. |
| Objetivos generales y específicos | `\section{Objetivos generales y específicos}` | 5, 6 | 15% | El objetivo general y los específicos están separados; incluyen observables, montaje, `R`, `T`, `A`, `f0`, `Delta f`, `Q`, incertidumbres, errores y aplicaciones. |
| Fundamento teórico detallado | `\section{Fundamento teórico detallado}` | 7, 8, 9, 10, 11 | 30% | Es la sección más extensa; incluye ondas planas, `Z0`, `p << lambda`, parámetros `S` complejos, `R/T/A`, advertencia de scattering lateral, plano metálico, impedancia efectiva, modelo `LC`, `Q`, Lorentz, campo lejano y supuestos. |
| Materiales, equipos y adquisición | `\section{Materiales, equipos y adquisición}` | 12 | 5% | La tabla usa las columnas pedidas: Elemento, Función, Especificación técnica, Adquisición/disponibilidad y Costo estimado; no inventa precios exactos. |
| Descripción del montaje experimental | `\section{Descripción del montaje experimental}` | 13 | 5% | El diagrama muestra VNA, puerto 1, antena TX, metasuperficie, antena RX, puerto 2, `S11`, `S21`, absorbentes, distancia `d` y plano metálico opcional sin cruces confusos. |
| Procedimiento experimental | `\section{Procedimiento experimental}` | 14 | 5% | El procedimiento está numerado y mantiene lenguaje condicional: calibración, referencias, alineación, barridos, sesgo, CSV, cálculo y repetibilidad. |
| Toma de datos y resultados | `\section{Toma de datos y resultados}` | 15, 16, 17 | 5% | Se declara que las figuras son datos sintéticos esperados; incluye formato de tabla, curvas de `S`, absorción y desplazamiento de resonancia. |
| Análisis de datos | `\section{Análisis de datos}` | 18 | 5% | Incluye extracción de `f0`, `Delta f`, `Q`, ajuste Lorentziano, residuales, `chi^2_red` y propagación de incertidumbres para `R`, `T`, `A` y `Q`. |
| Análisis de errores | `\section{Análisis de errores}` | 19 | 5% | Se separan errores sistemáticos, aleatorios, instrumentales, resolución de equipos, precisión de fabricante, error total y comparación con teoría; incluye presupuesto de error. |
| Discusión de resultados | `\section{Discusión de resultados}` | 4, 20 | 5% | Interpreta pico de absorción, `Zeff ≈ Z0`, `A < 1`, desplazamiento de `f0`, `S21` no despreciable, calidad del montaje y aplicaciones. |
| Conclusiones | `\section{Conclusiones}` | 20 | 5% | Cierra respondiendo a los objetivos y aclara que las figuras esperadas no son evidencia experimental real. |
| Seguridad y buenas prácticas | `\section{Seguridad y buenas prácticas}` | 19 | 5% | Incluye baja potencia, antenas activas, conectores RF, sesgo DC, calentamiento, soldadura, cámara/caja con absorbentes y trazabilidad. |
| Bibliografía | `\section{Bibliografía}` | 20 | 5% | Las fuentes cubren electrodinámica, microondas, antenas, metamateriales, metasuperficies, absorbentes y medición con VNA. |

## Verificaciones críticas

- El informe contiene exactamente los 13 títulos principales pedidos después de `\section*{Nota de alcance}`.
- La nota de alcance contiene la frase exacta: `Esta es una propuesta experimental conceptual, no destinada a ser ejecutada durante el curso.`
- Las diapositivas tienen exactamente 20 frames.
- Las figuras sintéticas generadas por Python se usan en informe y slides.
- El diagrama del montaje no cruza las flechas principales de onda incidente, reflexión y transmisión.
- No aparece lenguaje que afirme ejecución material o resultados reales.
- No aparece ninguna de las cadenas prohibidas indicadas por la consigna.
