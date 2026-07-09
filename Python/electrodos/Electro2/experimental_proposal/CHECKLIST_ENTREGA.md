# Checklist de entrega: propuesta experimental conceptual

Este checklist verifica que la propuesta sea inequívocamente conceptual: no se ejecutará durante el curso, no reporta datos medidos y organiza el reporte según los 13 criterios de la rúbrica del profesor.

| # | Criterio de rúbrica | Cobertura en reporte | Diapositiva asociada | Criterio de aceptación |
|---:|---|---|---:|---|
| 1 | Título del experimento | `\section{Título del experimento}` | 1 | Usa el título técnico sobre metasuperficie reconfigurable, microondas, parámetros `S`, reflexión, transmisión y absorción resonante. |
| 2 | Objetivos generales y específicos | `\section{Objetivos generales y específicos}` | 4 | El objetivo general empieza con proponer y diseñar un experimento conceptual; los objetivos incluyen `S11`, `S21`, `R`, `T`, `A`, `f0`, `Delta f`, `Q`, incertidumbres, errores, aplicaciones y reproducibilidad en principio. |
| 3 | Fundamento teórico detallado | `\section{Fundamento teórico detallado}` | 5, 6, 7 | Incluye régimen sublongitud de onda, parámetros `S`, absorción, advertencia por scattering lateral, plano metálico, impedancia efectiva, modelo LC, modelo de Lorentz, scattering colectivo y campo lejano. |
| 4 | Materiales, equipos y adquisición | `\section{Materiales, equipos y adquisición}` | 8 | Tabla con elemento, función, recursos moderados, recursos avanzados, adquisición/disponibilidad y costo estimado a confirmar. |
| 5 | Descripción del montaje experimental | `\section{Descripción del montaje experimental}` | 8 | El esquema muestra Tx -> metasuperficie, metasuperficie -> Rx como transmisión `S21`, reflexión `S11` hacia Tx, absorbentes, distancia `d` y plano metálico opcional. |
| 6 | Procedimiento experimental | `\section{Procedimiento experimental}` | 8 | Procedimiento numerado con lenguaje condicional: banda, calibración, referencias, alineación, absorbentes, medición propuesta, CSV, cálculo y repetibilidad. |
| 7 | Toma de datos y resultados esperados | `\section{Toma de datos y resultados esperados}` | 9 | Declara datos esperados, no datos medidos; incluye tabla con frecuencia, módulos, fases, `R`, `T`, `A`, configuración e incertidumbre. |
| 8 | Análisis de datos e incertidumbres | `\section{Análisis de datos e incertidumbres}` | 9 | Propaga incertidumbres para `R`, `T`, `A` y `Q`; conserva datos complejos antes de suavizado. |
| 9 | Análisis de errores | `\section{Análisis de errores}` | 9 | Clasifica errores aleatorios, sistemáticos e instrumentales, incluyendo calibración, acoplamiento directo, bordes, polarización, campo lejano y rango dinámico. |
| 10 | Discusión de resultados | `\section{Discusión de resultados}` | 3, 9, 10 | Interpreta `A < 1`, desplazamiento de `f0`, `S21` no despreciable, reflexión alta y compara recursos moderados versus avanzados. Incluye aplicaciones tecnológicas. |
| 11 | Conclusiones | `\section{Conclusiones}` | 10 | Responde a los objetivos con lenguaje de propuesta: se esperaría, la propuesta permitiría, el diseño conceptual muestra. |
| 12 | Seguridad y buenas prácticas | `\section{Seguridad y buenas prácticas}` | 10 | Incluye baja potencia, cuidado con antenas activas, conectores sin señal, límites DC, calentamiento, soldadura y cámara anecoica. |
| 13 | Bibliografía | `\section{Bibliografía}` | No aplica | Hay citas reales con `\citep{}` en el texto y BibTeX compila sin depender solo de `\nocite{*}`. |

## Verificaciones críticas

- El reporte incluye `\section*{Nota de alcance}` antes de las secciones numeradas.
- La nota de alcance dice: `Esta es una propuesta experimental conceptual, no destinada a ser ejecutada durante el curso.`
- La toma de datos se presenta como datos esperados, no datos medidos.
- La discusión incluye `\subsection{Utilidad tecnológica y aplicaciones}`.
- No se usa el tema experimental anterior.
- No se afirma ejecución experimental material.
- Las diapositivas conservan 10 slides.
- La diapositiva 2 dice `NO se ejecutará durante el curso.`
