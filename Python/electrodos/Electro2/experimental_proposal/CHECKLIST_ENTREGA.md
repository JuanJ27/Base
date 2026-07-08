# Checklist de entrega

Este documento resume los criterios de verificación para el componente computacional y para la propuesta experimental. Está diseñado para revisar la entrega sin reconstruir toda la estructura del proyecto.

## Checklist computacional

| Criterio | Peso | Cobertura en notebook/README | Criterio de aceptación |
|---|---:|---|---|
| Enunciado | 15% | `Python/electrodos/Electro2/electro2.ipynb`, celda 1; `README.md`, secciones “Pregunta central” y “Qué calcula”. | El problema directo e inverso está formulado como diagnóstico de haces a partir de patrón angular y escala espectral. |
| Teoría | 25% | Celdas 4, 8, 10, 14, 16 y 24; `README.md`, “Advertencias físicas”. | El notebook explica modelo angular, potencia absoluta, escala espectral y límites físicos del enfoque. |
| Solución | 40% | Celdas 6 a 24; figuras listadas en `README.md`, “Figuras actuales”. | El notebook ejecuta completo; existen problema directo e inverso; la reconstrucción de energía incluye tabla; la sección de divergencia angular existe. |
| Análisis/aplicaciones | 10% | Celdas 22, 24, 26 y 28; `README.md`, filas “Problema inverso”, “Divergencia del haz” y “CRT”. | La FFT se trata como cualitativa; el CRT aparece como aplicación/apéndice conceptual, no como fuente práctica de radiación sincrotrón. |
| Referencias | 10% | `README.md`, sección “Referencias”; citas y contexto del notebook. | Las referencias cubren electrodinámica clásica, radiación de cargas aceleradas y diagnóstico conceptual de haces. |
| Validación técnica | No aplica | `README.md`, sección “Uso”. | El notebook ejecuta completo con `jupyter nbconvert --to notebook --execute Python/electrodos/Electro2/electro2.ipynb --output /tmp/electro2-diagnostic.ipynb`. |
| Calibración FWHM | No aplica | Celda 10; `README.md`, fila “Calibración angular”. | El FWHM usa ajuste `A_fit/gamma`, no la predicción falsa `2/gamma`. |
| Escala espectral y FFT | No aplica | Celdas 16, 18 y 20; `README.md`, filas “Escala espectral” y “FFT cualitativa”. | La FFT se presenta solo como visualización fenomenológica/cualitativa. |
| Reconstrucción y divergencia | No aplica | Celdas 22 y 24; `README.md`, filas “Problema inverso” y “Divergencia del haz”. | Existe tabla de reconstrucción de energía y sección de divergencia angular del haz. |

## Checklist experimental

| Punto de rúbrica | Cobertura en reporte | Diapositiva asociada | Criterio de aceptación |
|---|---|---:|---|
| Título | `propuesta_experimental.tex`, “Título específico y técnico”. | 1 | El título identifica la medición de `e/m` por deflexión magnética en tubo e/m. |
| Objetivos | Sección “Objetivos generales y específicos”. | 3 | Incluye objetivo general, calibración de campo, medición de radios, estimación de incertidumbres y comparación con valor aceptado. |
| Teoría detallada | Sección “Fundamento teórico detallado”. | 4, 5, 6 | Deriva `eV = 1/2 mv^2`, fuerza de Lorentz, movimiento circular, `e/m = 2V/(B^2 r^2)` y campo de Helmholtz. |
| Materiales/adquisición | Sección “Materiales, equipos y adquisición”. | 6 | Lista tubo e/m, bobinas, fuentes, instrumentos de medición, soporte y seguridad. |
| Montaje | Sección “Descripción del montaje”. | 6 | El montaje ubica el tubo en el centro de bobinas de Helmholtz y define cómo medir `r`. |
| Procedimiento | Sección “Procedimiento experimental”. | 7 | El procedimiento es secuencial, repetible y contempla apagado/descarga segura. |
| Datos/resultados esperados | Sección “Toma de datos y resultados esperados”. | 8 | Incluye variables medidas, tabla de datos y gráficas esperadas para validar el modelo. |
| Incertidumbres | Sección “Análisis de datos e incertidumbres”. | 9 | Incluye propagación relativa de incertidumbre para `e/m`. |
| Análisis de errores | Sección “Análisis de errores”. | 9 | Distingue fuentes aleatorias, sistemáticas e instrumentales. |
| Discusión | Sección “Discusión de resultados”. | 8, 9 | Interpreta desviaciones respecto al valor aceptado y diagnostica posibles causas. |
| Conclusiones | Sección “Conclusiones”. | 10 | Indica qué se mide y cómo se valida la medición. |
| Seguridad | Sección “Seguridad y buenas prácticas”. | 9 | Advierte sobre alta tensión, tubo de vidrio, calentamiento de bobinas y manipulación segura. |
| Bibliografía | Sección “Bibliografía”; `references.bib`. | No aplica | Incluye referencias de electrodinámica, valor CODATA y manual de aparato e/m. |
| Validación de compilación | `experimental_proposal/Makefile`, `propuesta_experimental.tex`, `slides_propuesta_experimental.tex`. | Todas | `propuesta_experimental.tex` compila con `latexmk`; las diapositivas compilan; no hay afirmación de medición de radiación sincrotrón real. |
