# Checklist de entrega

Este documento resume los criterios de verificación para el componente computacional y para la propuesta experimental conceptual. Está diseñado para revisar la entrega sin reconstruir toda la estructura del proyecto.

## Checklist computacional

| Criterio | Peso | Cobertura en notebook/README | Criterio de aceptación |
|---|---:|---|---|
| Enunciado | 15% | `Python/electrodos/Electro2/Problema_computacional.ipynb`, celda 1; `README.md`, secciones “Pregunta central” y “Qué calcula”. | El problema directo e inverso está formulado como diagnóstico de haces a partir de patrón angular y escala espectral. |
| Teoría | 25% | Celdas 4, 8, 10, 14, 16 y 24; `README.md`, “Advertencias físicas”. | El notebook explica modelo angular, potencia absoluta, escala espectral y límites físicos del enfoque. |
| Solución | 40% | Celdas 6 a 24; figuras listadas en `README.md`, “Figuras actuales”. | El notebook ejecuta completo; existen problema directo e inverso; la reconstrucción de energía incluye tabla; la sección de divergencia angular existe. |
| Análisis/aplicaciones | 10% | Celdas 22, 24, 26 y 28; `README.md`, filas “Problema inverso”, “Divergencia del haz” y “CRT”. | La FFT se trata como cualitativa; el CRT aparece como aplicación/apéndice conceptual, no como fuente práctica de radiación sincrotrón. |
| Referencias | 10% | `README.md`, sección “Referencias”; citas y contexto del notebook. | Las referencias cubren electrodinámica clásica, radiación de cargas aceleradas y diagnóstico conceptual de haces. |
| Validación técnica | No aplica | `README.md`, sección “Uso”. | El notebook ejecuta completo con `jupyter nbconvert --to notebook --execute Python/electrodos/Electro2/Problema_computacional.ipynb --output /tmp/electro2-diagnostic.ipynb`. |
| Calibración FWHM | No aplica | Celda 10; `README.md`, fila “Calibración angular”. | El FWHM usa ajuste `A_fit/gamma`, no la predicción falsa `2/gamma`. |
| Escala espectral y FFT | No aplica | Celdas 16, 18 y 20; `README.md`, filas “Escala espectral” y “FFT cualitativa”. | La FFT se presenta solo como visualización fenomenológica/cualitativa. |
| Reconstrucción y divergencia | No aplica | Celdas 22 y 24; `README.md`, filas “Problema inverso” y “Divergencia del haz”. | Existe tabla de reconstrucción de energía y sección de divergencia angular del haz. |

## Checklist experimental conceptual

| Punto de rúbrica | Cobertura en reporte | Diapositiva asociada | Criterio de aceptación |
|---|---|---:|---|
| Título y pregunta | `propuesta_experimental.tex`, “Título específico y pregunta experimental”. | 1 | El título identifica metasuperficie reconfigurable, microondas, parámetros `S` y control de reflexión, transmisión y absorción. |
| Alcance | Sección “Alcance y carácter propositivo de la propuesta”. | 2 | Declara que es una propuesta experimental conceptual y que no está destinada a ejecutarse durante el curso. |
| Motivación y aplicaciones | Sección “Utilidad tecnológica y aplicaciones”. | 3 | Incluye absorbedores, cámaras anecoicas, shielding, telecomunicaciones, sensores, radar, THz, control de polarización y reducción de reflexiones. |
| Objetivos | Sección “Objetivos generales y específicos”. | 4 | El objetivo general comienza con “Proponer y diseñar un experimento de caracterización electromagnética” e incluye diseño, observables, procedimiento, incertidumbres y aplicaciones. |
| Teoría detallada | Sección “Fundamento teórico”. | 5, 6, 7 | Explica parámetros `S`, `R`, `T`, `A`, impedancia efectiva, condición de absorción, resonancia LC, dispersión y scattering. |
| Materiales/adquisición | Sección “Materiales y recursos propuestos”. | 8 | Lista recursos moderados y avanzados: VNA, antenas, PCB, absorbentes, cámara anecoica, posicionadores, fabricación de precisión y simulación. |
| Montaje | Sección “Montaje propuesto y procedimiento de medición”. | 8 | Describe el montaje propuesto con VNA, dos antenas, metasuperficie y geometría de incidencia. |
| Procedimiento | Sección “Montaje propuesto y procedimiento de medición”. | 8 | El procedimiento es secuencial y reproducible aunque no se ejecute materialmente. |
| Toma de datos | Sección “Datos esperados y visualizaciones previstas”. | 9 | La toma de datos se entiende como datos esperados, simulados o planificados, no como datos reales medidos. |
| Incertidumbres | Sección “Análisis de incertidumbres y errores”. | 9 | Propone incertidumbres de calibración, cables, alineación, polarización, distancia, reflexiones y difracción. |
| Discusión | Secciones “Datos esperados y visualizaciones previstas” y “Conclusiones esperadas”. | 9, 10 | La discusión interpreta comportamiento esperado y aplicaciones, no resultados ejecutados. |
| Conclusiones | Sección “Conclusiones esperadas”. | 10 | Presenta conclusiones esperadas de la propuesta: relación entre parámetros `S`, absorción, impedancia, resonancia y aplicaciones. |
| Seguridad | Sección “Seguridad y buenas prácticas”. | 10 | Advierte sobre potencia de microondas, conectores RF, límites de sesgo y registro de configuración. |
| Bibliografía | Sección “Bibliografía”; `references.bib`. | No aplica | Incluye referencias formales sobre microondas, antenas, metasuperficies, metamateriales y absorbedores. |
| Validación de compilación | `propuesta_experimental.tex`, `slides_propuesta_experimental.tex`. | Todas | Ambos documentos compilan con `latexmk`; el texto mantiene alcance conceptual y no afirma ejecución material. |
