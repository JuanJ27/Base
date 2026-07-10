from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, FancyArrowPatch, Rectangle


ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)


plt.rcParams.update(
    {
        "figure.dpi": 150,
        "savefig.dpi": 220,
        "font.size": 11,
        "axes.titlesize": 13,
        "axes.labelsize": 11,
        "legend.fontsize": 9,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "axes.grid": True,
        "grid.alpha": 0.22,
        "grid.linestyle": "--",
    }
)


BLUE = "#246BFE"
ORANGE = "#F28E2B"
GREEN = "#1B9E77"
RED = "#D62728"
PURPLE = "#7B2CBF"
GRAY = "#4A5568"
LIGHT = "#F7FAFC"


def absorption_model(f_ghz, f0=10.0, q=18.0, peak=0.78, background=0.06):
    x = (f_ghz - f0) / f0
    return background + peak / (1.0 + 4.0 * q**2 * x**2)


def expected_power_curves(f_ghz):
    line = absorption_model(f_ghz, peak=0.80, background=0.055)
    detune = (f_ghz - 10.0) / 2.0
    ripple = 0.012 * np.sin(2.0 * np.pi * (f_ghz - 8.0) / 1.7)
    reflectance = 0.39 - 0.335 * (line - line.min()) / (line.max() - line.min()) + ripple
    transmittance = 0.50 - 0.385 * (line - line.min()) / (line.max() - line.min()) - 0.012 * detune
    reflectance = np.clip(reflectance, 0.035, 0.55)
    transmittance = np.clip(transmittance, 0.08, 0.58)
    absorption = np.clip(1.0 - reflectance - transmittance, 0.0, 1.0)
    return reflectance, transmittance, absorption


def save(fig, name):
    fig.savefig(FIGURES / name, bbox_inches="tight")
    plt.close(fig)


def figure_expected_sparameters_absorption():
    f = np.linspace(8.0, 12.0, 600)
    r, t, a = expected_power_curves(f)
    s11_db = 10.0 * np.log10(r)
    s21_db = 10.0 * np.log10(t)

    fig, ax = plt.subplots(figsize=(8.4, 4.8))
    ax.plot(f, s11_db, color=BLUE, lw=2.4, label=r"$|S_{11}|$ dB esperado")
    ax.plot(f, s21_db, color=ORANGE, lw=2.4, label=r"$|S_{21}|$ dB esperado")
    ax.set_xlabel("frecuencia (GHz)")
    ax.set_ylabel("parametro S (dB)")
    ax.set_xlim(8, 12)
    ax.set_ylim(-16, -1)
    ax.axvline(10.0, color=GRAY, lw=1.1, ls=":")
    ax.text(10.05, -2.3, r"$f_0 \approx 10$ GHz", color=GRAY)

    ax2 = ax.twinx()
    ax2.plot(f, a, color=GREEN, lw=2.8, label=r"$A(f)$ esperada")
    ax2.fill_between(f, a, color=GREEN, alpha=0.12)
    ax2.set_ylabel("absorcion esperada")
    ax2.set_ylim(0, 1.02)

    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines + lines2, labels + labels2, loc="lower right", frameon=True)
    ax.set_title("Parametros S y absorcion resonante esperada")
    fig.tight_layout()
    save(fig, "expected_sparameters_absorption.png")


def figure_resonance_shift_bias():
    v = np.linspace(0.0, 20.0, 160)
    c0 = 0.90e-12
    v0 = 8.0
    inductance = 0.32e-9
    capacitance = c0 / np.sqrt(1.0 + v / v0)
    f0 = 1.0 / (2.0 * np.pi * np.sqrt(inductance * capacitance)) / 1e9

    fig, ax = plt.subplots(figsize=(7.4, 4.6))
    ax.plot(v, f0, color=PURPLE, lw=2.7)
    ax.scatter(v[::16], f0[::16], color=PURPLE, s=34, zorder=3)
    ax.set_xlabel(r"$V_{bias}$ (V)")
    ax.set_ylabel(r"$f_0$ esperado (GHz)")
    ax.set_title("Desplazamiento esperado de resonancia por sesgo DC")
    ax.text(
        0.04,
        0.92,
        r"$C(V)=C_0/\sqrt{1+V/V_0}$" + "\n" + r"$f_0=1/(2\pi\sqrt{LC})$",
        transform=ax.transAxes,
        va="top",
        bbox={"facecolor": "white", "edgecolor": "#CBD5E0", "boxstyle": "round,pad=0.4"},
    )
    fig.tight_layout()
    save(fig, "resonance_shift_bias.png")


def expected_fit_data():
    rng = np.random.default_rng(42)
    f_points = np.linspace(8.25, 11.75, 42)
    theory = absorption_model(f_points, f0=10.0, q=16.0, peak=0.76, background=0.065)
    sigma = 0.018 + 0.010 * np.exp(-((f_points - 10.0) / 0.45) ** 2)
    expected = np.clip(theory + rng.normal(0.0, sigma * 0.65), 0.0, 1.0)
    f_dense = np.linspace(8.0, 12.0, 600)
    fit = absorption_model(f_dense, f0=10.01, q=15.7, peak=0.755, background=0.067)
    fit_at_points = absorption_model(f_points, f0=10.01, q=15.7, peak=0.755, background=0.067)
    return f_points, expected, sigma, f_dense, fit, fit_at_points


def figure_theory_vs_expected_experiment():
    f_points, expected, sigma, f_dense, fit, _ = expected_fit_data()
    fig, ax = plt.subplots(figsize=(8.2, 4.8))
    ax.plot(f_dense, fit, color=BLUE, lw=2.6, label="modelo resonante / ajuste")
    ax.errorbar(
        f_points,
        expected,
        yerr=sigma,
        fmt="o",
        ms=4.8,
        color=RED,
        ecolor="#9CA3AF",
        capsize=2.5,
        label="datos esperados simulados",
    )
    ax.set_xlabel("frecuencia (GHz)")
    ax.set_ylabel("absorcion")
    ax.set_ylim(0, 1.02)
    ax.set_xlim(8, 12)
    ax.set_title("Comparacion esperada teoria vs experimento")
    ax.legend(loc="upper right")
    fig.tight_layout()
    save(fig, "theory_vs_expected_experiment.png")


def figure_residuals_expected_fit():
    f_points, expected, sigma, _, _, fit_at_points = expected_fit_data()
    residual = expected - fit_at_points

    fig, ax = plt.subplots(figsize=(8.2, 3.8))
    ax.axhline(0.0, color=GRAY, lw=1.2)
    ax.errorbar(
        f_points,
        residual,
        yerr=sigma,
        fmt="o",
        ms=4.8,
        color=PURPLE,
        ecolor="#A0AEC0",
        capsize=2.3,
    )
    ax.set_xlabel("frecuencia (GHz)")
    ax.set_ylabel("residual de absorción")
    ax.set_title("Residuales esperados del ajuste resonante")
    ax.set_xlim(8, 12)
    ax.set_ylim(-0.075, 0.075)
    fig.tight_layout()
    save(fig, "residuals_expected_fit.png")


def figure_error_budget():
    labels = [
        "calibracion\nVNA",
        "alineacion",
        "repetibilidad",
        "scattering\nlateral",
        "resolucion\nde frecuencia",
    ]
    values = np.array([0.030, 0.024, 0.016, 0.026, 0.010])
    colors = [BLUE, ORANGE, GREEN, RED, PURPLE]

    fig, ax = plt.subplots(figsize=(7.8, 4.7))
    bars = ax.bar(labels, values, color=colors, alpha=0.88)
    ax.set_ylabel(r"contribucion a $\sigma_A$")
    ax.set_title("Presupuesto de incertidumbre esperado")
    ax.set_ylim(0, 0.04)
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 0.001, f"{value:.3f}", ha="center", va="bottom")
    fig.tight_layout()
    save(fig, "error_budget.png")


def draw_box(ax, xy, width, height, label, fc="white", ec=GRAY, lw=1.8, fontsize=10):
    patch = Rectangle(xy, width, height, linewidth=lw, edgecolor=ec, facecolor=fc, joinstyle="round")
    ax.add_patch(patch)
    ax.text(xy[0] + width / 2, xy[1] + height / 2, label, ha="center", va="center", fontsize=fontsize)
    return patch


def add_arrow(ax, start, end, color=GRAY, lw=2.1, text=None, text_xy=None, connectionstyle="arc3,rad=0"):
    arrow = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=14,
        linewidth=lw,
        color=color,
        connectionstyle=connectionstyle,
    )
    ax.add_patch(arrow)
    if text is not None and text_xy is not None:
        ax.text(text_xy[0], text_xy[1], text, color=color, ha="center", va="center", fontsize=10)


def figure_montaje_metasuperficie():
    fig, ax = plt.subplots(figsize=(11.0, 5.4))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 5.4)
    ax.axis("off")

    ax.add_patch(Rectangle((0.2, 4.75), 10.6, 0.34, facecolor="#F6AD55", edgecolor="#C05621", hatch="//", alpha=0.65))
    ax.add_patch(Rectangle((0.2, 0.35), 10.6, 0.34, facecolor="#F6AD55", edgecolor="#C05621", hatch="//", alpha=0.65))
    ax.text(5.5, 5.21, "absorbentes RF", ha="center", va="center", fontsize=10, color="#7B341E")
    ax.text(5.5, 0.17, "absorbentes RF", ha="center", va="center", fontsize=10, color="#7B341E")

    draw_box(ax, (0.45, 1.65), 1.25, 1.05, "VNA\n2 puertos", fc=LIGHT, ec="#2D3748", fontsize=10)
    ax.text(1.78, 2.50, "Puerto 1", fontsize=9, color=GRAY)
    ax.text(1.78, 1.66, "Puerto 2", fontsize=9, color=GRAY)

    draw_box(ax, (2.75, 2.20), 1.10, 0.88, "antena\nTX", fc="#EBF8FF", ec=BLUE, fontsize=10)
    ax.add_patch(Rectangle((5.32, 1.48), 0.20, 2.34, facecolor="#BEE3F8", edgecolor=BLUE, linewidth=2.0))
    ax.text(5.42, 3.97, "metasuperficie", ha="center", fontsize=10, color=BLUE)
    ax.add_patch(Rectangle((5.72, 1.48), 0.12, 2.34, facecolor="#E2E8F0", edgecolor="#718096", linewidth=1.5, linestyle="--"))
    ax.text(6.22, 3.70, "plano metalico\nopcional", ha="left", va="center", fontsize=9, color=GRAY)
    draw_box(ax, (7.75, 2.20), 1.10, 0.88, "antena\nRX", fc="#F0FFF4", ec=GREEN, fontsize=10)

    add_arrow(ax, (1.70, 2.48), (2.75, 2.64), color="#2D3748", lw=1.9, text=None)
    add_arrow(
        ax,
        (1.70, 1.82),
        (7.75, 2.26),
        color="#2D3748",
        lw=1.7,
        connectionstyle="angle3,angleA=-90,angleB=180",
    )
    ax.text(4.85, 1.08, "cables coaxiales calibrados", ha="center", fontsize=9, color=GRAY)

    add_arrow(ax, (3.85, 2.64), (5.32, 2.64), color=BLUE, lw=2.8, text="onda incidente", text_xy=(4.58, 2.95))
    add_arrow(ax, (5.84, 2.64), (7.75, 2.64), color=GREEN, lw=2.8, text=r"transmision $S_{21}$", text_xy=(6.83, 2.96))
    add_arrow(
        ax,
        (5.32, 3.22),
        (3.85, 3.20),
        color=RED,
        lw=2.6,
        text=r"reflexion $S_{11}$",
        text_xy=(4.58, 3.82),
        connectionstyle="arc3,rad=0.42",
    )

    ax.annotate("", xy=(3.85, 1.55), xytext=(5.32, 1.55), arrowprops={"arrowstyle": "<->", "color": GRAY, "lw": 1.5})
    ax.annotate("", xy=(5.84, 1.55), xytext=(7.75, 1.55), arrowprops={"arrowstyle": "<->", "color": GRAY, "lw": 1.5})
    ax.text(4.58, 1.33, r"distancia $d$", ha="center", fontsize=10, color=GRAY)
    ax.text(6.78, 1.33, r"distancia $d$", ha="center", fontsize=10, color=GRAY)

    ax.add_patch(Arc((5.42, 2.64), 1.05, 2.65, theta1=-72, theta2=72, color="#90CDF4", lw=1.1, ls=":"))
    ax.set_title("Montaje experimental propuesto para caracterizacion por parametros S", pad=10)
    save(fig, "montaje_metasuperficie.png")


def main():
    figure_expected_sparameters_absorption()
    figure_resonance_shift_bias()
    figure_theory_vs_expected_experiment()
    figure_residuals_expected_fit()
    figure_error_budget()
    figure_montaje_metasuperficie()


if __name__ == "__main__":
    main()
