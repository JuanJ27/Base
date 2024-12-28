"""
Plot of potential, kinetic and total energy of spring-mass system
Autor: [JuanMS]
Fecha: [08/08/2023]
"""
import matplotlib.pyplot as plt
import numpy as np


def x_pos(t):
    return np.cos(t) + np.sin(t)


def x_vel(t):
    return np.cos(t) - np.sin(t)


def total_energy(x_ve, x_posi):
    return 0.5 * (x_ve ** 2 + x_posi ** 2)


def kit_energy(x_ve):
    return 0.5 * (x_ve ** 2)


def pot_energy(x_posi):
    return 0.5 * (x_posi ** 2)


# Genera 1000 valores equidistantes en el rango de 0 a 10
t = np.linspace(0, 10, 70)


# Calcula las energías para cada valor de t
total_energies = total_energy(x_vel(t), x_pos(t))
kinetic_energies = kit_energy(x_vel(t))
potential_energies = pot_energy(x_pos(t))

plt.plot(t, total_energies, label='Energía Total', color='blue')
plt.plot(t, kinetic_energies, label='Energía Cinética', color='green')
plt.plot(t, potential_energies, label='Energía Potencial', color='red')

# Agrega leyendas y título
plt.legend()
plt.title('Energía Total, Cinética y Potencial en función del tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Energía')

plt.show()

# Energia en sistema amortiguado y su version aproximada
t = np.linspace(1, 8, 100)


def energy_decay(t):
    return 0.5*np.exp(-t)*(0.25*(np.cos(t)**2)+np.cos(t)*np.sin(t)+1)


def aprox_energy_decay(t):
    return 0.5*np.exp(-t)


plt.plot(t, energy_decay(t), label='Sin aproximar', color='green')
plt.plot(t, aprox_energy_decay(t), label='Aproximando', color='red')

# Agrega leyendas y título
plt.legend()
plt.title('Comparacion de energia en sistema amortiguado')
plt.xlabel('Tiempo')
plt.ylabel('Energía')

plt.show()
