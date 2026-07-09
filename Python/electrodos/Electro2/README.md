# Electro2: diagnóstico de haces relativistas

Notebook académico computacional sobre diagnóstico de haces de electrones mediante la radiación emitida cuando el haz es curvado por un campo magnético.

## Pregunta central

“¿Puede reconstruirse la energía relativista y estimarse la divergencia angular de un haz de electrones a partir del patrón angular y del contenido espectral de la radiación emitida cuando el haz es curvado por un campo magnético?”

## Qué calcula

| Bloque | Resultado |
|---|---|
| Problema directo | Trayectoria, patrón angular, FWHM, potencia absoluta y escala espectral para `20 keV`, `100 keV`, `1 MeV`, `100 MeV` y `1 GeV`. |
| Calibración angular | Medición adaptativa del FWHM y ajuste `A_fit/gamma`, sin asumir `FWHM ~ 2/gamma` como predicción. |
| Potencia SI | Potencia radiada absoluta con `P = e^4 B^2 gamma^2 beta^2 / (6*pi*epsilon0*m_e^2*c)`. |
| Escala espectral | Uso de `m_c = gamma^3` y `omega_c = (3/2)*gamma^3*beta*omega0`. |
| Problema inverso | Reconstrucción sintética de `gamma`, energía cinética y consistencia entre observables angulares y espectrales. |
| Divergencia del haz | Ensanchamiento angular por divergencia gaussiana y estimación por desconvolución cuadrática. |
| CRT | Apéndice conceptual: deflexión de Lorentz e impacto en fósforo, no fuente práctica de radiación sincrotrón. |

## Uso

1. Crear un entorno de Python.
2. Instalar dependencias desde este directorio o desde la raíz del repositorio:

```bash
python -m pip install -r Python/electrodos/Electro2/requirements.txt
```

3. Ejecutar el notebook en Jupyter, JupyterLab o VS Code.

También puede validarse desde la raíz del repositorio:

```bash
python -m json.tool Python/electrodos/Electro2/Problema_computacional.ipynb >/dev/null
jupyter nbconvert --to notebook --execute Python/electrodos/Electro2/Problema_computacional.ipynb --output /tmp/electro2-diagnostic.ipynb
```

## Dependencias

| Paquete | Uso |
|---|---|
| `numpy` | Cálculo numérico y generación de observables sintéticos. |
| `matplotlib` | Figuras reproducibles. |
| `scipy` | Sección opcional con funciones de Bessel; el notebook no falla si no está disponible. |
| `nbformat`, `nbclient` | Validación y ejecución automatizada de notebooks. |

## Advertencias físicas

- La distribución angular usa la fórmula instantánea relativista de Liénard-Wiechert.
- La teoría sincrotrón espectral completa requiere armónicos y funciones de Bessel; la FFT incluida es solo una visualización fenomenológica.
- `m_c = gamma^3` no debe sobreinterpretarse en baja velocidad: es una escala, no un conteo exacto de líneas dominantes.
- Un CRT emite radiación por cargas aceleradas en principio, pero la señal visible real proviene del impacto del haz en el fósforo.

## Figuras actuales

| Archivo | Contenido |
|---|---|
| `trajectory_direct_problem.png` | Trayectorias circulares para energías de 20 keV a 1 GeV con `B_ref` fijo. |
| `angular_model_comparison.png` | Comparación entre patrón `sin^2(theta)` y Liénard-Wiechert relativista. |
| `polar_beaming_energy_comparison.png` | Corte polar del beaming para distintas energías. |
| `angular_heatmap_100MeV.png` | Mapa angular instantáneo para 100 MeV. |
| `fwhm_calibration.png` | FWHM adaptativo, ajuste `A_fit/gamma` y escala `1/gamma`. |
| `forward_backward_asymmetry.png` | Razón `P_forward/P_backward`. |
| `absolute_power_si.png` | Potencia radiada absoluta en SI. |
| `critical_frequency_scale.png` | Escalas `m_c` y `omega_c`. |
| `fft_qualitative_harmonics.png` | FFT fenomenológica para energías moderadas. |
| `bessel_optional_harmonics.png` | Figura opcional si `scipy` está disponible. |
| `inverse_diagnostic_reconstruction.png` | Reconstrucción inversa de `gamma` con observables sintéticos. |
| `beam_divergence_broadening.png` | Ensanchamiento angular por divergencia del haz. |
| `crt_schematic.png` | Esquema conceptual de un CRT. |
| `crt_screen_heatmap.png` | Mapa conceptual de impactos en pantalla CRT. |

## Referencias

Milton/Schwinger, *Classical Electrodynamics*, caps. 35, 38, 41 y 43; Jackson, *Classical Electrodynamics*; Griffiths, *Introduction to Electrodynamics*.
