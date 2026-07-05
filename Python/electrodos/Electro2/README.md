# Electro2: transición de régimen CRT-sincrotrón

Notebook académico computacional sobre la transición desde la deflexión de un haz electrónico tipo CRT hasta la radiación de sincrotrón relativista.

## Problema

Un electrón de carga `-e` y masa `m_e` se acelera con `V_acc`, entra perpendicularmente en un campo magnético uniforme `B` y describe una órbita circular. El notebook estudia cómo cambian la trayectoria, el patrón angular de radiación, el ancho del lóbulo principal y el contenido espectral al aumentar la energía cinética desde `20 keV` hasta `1 GeV`.

La pregunta central es: ¿cuándo la radiación deja de parecer dipolar/no relativista y empieza a concentrarse en un cono estrecho con armónicos altos?

## Qué calcula

| Bloque | Resultado |
|---|---|
| Cinemática | `gamma`, `beta`, `omega0`, radio orbital, `m_c ~ gamma^3`, `omega_c`. |
| Radiación angular | Superficies 3D, mapa angular y cortes polares usando la fórmula relativista instantánea. |
| FWHM | Ancho completo a media altura del lóbulo principal y comparación con `2/gamma`. |
| Movimiento circular | Órbitas para un `B_ref` fijo y crecimiento de las escalas críticas. |
| Tiempo retardado | Solución numérica de `t_obs = t_ret + R(t_ret)/c` por bisección. |
| FFT proxy | Modelo fenomenológico de pulsos estrechos para visualizar armónicos altos; no reemplaza el espectro sincrotrón completo con funciones de Bessel. |
| CRT | Deflexión de pantalla y comparación conceptual con sincrotrón. |

## Uso

1. Instalar dependencias: `numpy`, `matplotlib` y Jupyter.
2. Abrir `electro2.ipynb` con Jupyter, JupyterLab o VS Code.
3. Ejecutar las celdas en orden.
4. Revisar las figuras regeneradas en `figures/`.

También puede ejecutarse desde terminal:

```bash
jupyter nbconvert --to notebook --execute Python/electrodos/Electro2/electro2.ipynb --output /tmp/electro2-executed.ipynb
```

## Figuras actuales

El notebook genera salidas reproducibles en `figures/` para revisión o presentación:

| Archivo | Contenido |
|---|---|
| `angular_3d_20keV.png`, `angular_3d_1MeV.png`, `angular_3d_100MeV.png` | Patrones angulares 3D por energía. |
| `angular_heatmap_100MeV.png` | Mapa angular normalizado para alta energía. |
| `polar_beaming_energy_comparison.png` | Corte polar comparativo por energía. |
| `fwhm_vs_gamma.png` | FWHM adaptativo del lóbulo principal frente a `2/gamma`. |
| `circular_motion_frequency_scales.png` | Órbitas y escalas críticas para `B` fijo. |
| `retarded_time_vs_beta.png`, `retarded_position_geometry.png` | Tiempo retardado y geometría de emisión observada. |
| `fft_harmonics_beaming.png` | Proxy fenomenológico de pulsos y armónicos. |
| `crt_vs_synchrotron_gamma.png`, `crt_schematic.png` | Comparación conceptual CRT/sincrotrón y escala de potencia para `B` fijo. |

La FFT es una ayuda cualitativa: muestra que pulsos más angostos exigen armónicos más altos, pero no calcula la distribución espectral sincrotrón completa con funciones de Bessel.

## Referencias

La referencia principal es Schwinger/Milton, *Classical Electrodynamics*: cap. 34 para tiempo retardado y funciones de Green; cap. 35 para campo radiativo; cap. 38 para espectro; caps. 41--43 para sincrotrón, beaming y altas energías.

## Advertencia CRT

El CRT es una analogía de deflexión de haz. Para `20 kV`, `gamma ≈ 1.039` y `beta ≈ 0.27`; no es una fuente de radiación sincrotrón fuerte ni medible en condiciones comunes de laboratorio.
