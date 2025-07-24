%% VISUALIZACIÓN SIMPLE DEL TROMPO (Octave Compatible)
% Script básico para probar la visualización

clear all; close all; clc;

fprintf('🎪 Cargando datos del trompo...\n');

% Cargar datos
load('dataTrompo.mat');
fprintf('✓ Datos cargados:\n');
fprintf('  - Variables simétricas: %d puntos\n', length(t));
fprintf('  - Variables asimétricas: %d puntos\n', length(t_asym));

% Crear figura con 4 subplots
figure('Position', [100, 100, 1200, 800]);

%% 1. Trayectoria 3D Simétrica
subplot(2, 2, 1);
plot3(x_t, y_t, z_t, 'b-', 'LineWidth', 2);
hold on;
plot3(x_t(1), y_t(1), z_t(1), 'go', 'MarkerSize', 10, 'MarkerFaceColor', 'g');
plot3(x_t(end), y_t(end), z_t(end), 'ro', 'MarkerSize', 10, 'MarkerFaceColor', 'r');
axis equal;
grid on;
xlabel('X (m)');
ylabel('Y (m)');
zlabel('Z (m)');
title('Trayectoria Trompo Simétrico');
legend('Trayectoria', 'Inicio', 'Final', 'Location', 'best');
view(45, 30);

%% 2. Ángulos de Euler Simétrico
subplot(2, 2, 2);
plot(t, theta_t*180/pi, 'r-', 'LineWidth', 2); hold on;
plot(t, phi_t*180/pi, 'g-', 'LineWidth', 2);
plot(t, psi_t*180/pi, 'b-', 'LineWidth', 2);
grid on;
xlabel('Tiempo (s)');
ylabel('Ángulo (grados)');
title('Ángulos de Euler - Simétrico');
legend('theta', 'phi', 'psi', 'Location', 'best');

%% 3. Trayectoria 3D Asimétrica (con verificación)
subplot(2, 2, 3);
if max(abs(x_t_asym)) < 100  % Verificar valores razonables
    plot3(x_t_asym, y_t_asym, z_t_asym, 'r-', 'LineWidth', 2);
    hold on;
    plot3(x_t_asym(1), y_t_asym(1), z_t_asym(1), 'go', 'MarkerSize', 10, 'MarkerFaceColor', 'g');
    plot3(x_t_asym(end), y_t_asym(end), z_t_asym(end), 'ro', 'MarkerSize', 10, 'MarkerFaceColor', 'r');
    axis equal;
    grid on;
    xlabel('X (m)');
    ylabel('Y (m)');
    zlabel('Z (m)');
    title('Trayectoria Trompo Asimétrico');
    legend('Trayectoria', 'Inicio', 'Final', 'Location', 'best');
    view(45, 30);
    fprintf('✓ Trayectoria asimétrica: valores normales\n');
else
    text(0.5, 0.5, 'Trayectoria asimétrica contiene valores extremos', ...
         'HorizontalAlignment', 'center', 'Units', 'normalized', 'FontSize', 12);
    title('Trompo Asimétrico - Valores Extremos Detectados');
    fprintf('⚠ Trayectoria asimétrica: valores extremos detectados\n');
    fprintf('  Max |x|: %.2e, Max |y|: %.2e, Max |z|: %.2e\n', ...
            max(abs(x_t_asym)), max(abs(y_t_asym)), max(abs(z_t_asym)));
end

%% 4. Comparación de energías o parámetros
subplot(2, 2, 4);
% Mostrar información de los parámetros
text(0.1, 0.8, 'PARÁMETROS DEL SISTEMA:', 'FontSize', 14, 'FontWeight', 'bold');
text(0.1, 0.7, sprintf('Masa simétrica: %.3f kg', m_sym), 'FontSize', 12);
text(0.1, 0.6, sprintf('Masa asimétrica: %.3f kg', m_asym), 'FontSize', 12);
text(0.1, 0.5, sprintf('I simétrico: %.6f kg⋅m²', I_sym), 'FontSize', 12);
text(0.1, 0.4, sprintf('I_z simétrico: %.6f kg⋅m²', I_z_sym), 'FontSize', 12);
text(0.1, 0.3, sprintf('Altura simétrica: %.3f m', h_sym), 'FontSize', 12);
text(0.1, 0.2, sprintf('Altura asimétrica: %.3f m', h_asym), 'FontSize', 12);
text(0.1, 0.1, sprintf('Gravedad: %.2f m/s²', g), 'FontSize', 12);
axis off;
title('Parámetros del Sistema');

fprintf('\n✅ Visualización completada!\n');
fprintf('📊 Estadísticas:\n');
fprintf('  Simétrico - Rango X: [%.3f, %.3f] m\n', min(x_t), max(x_t));
fprintf('  Simétrico - Rango Y: [%.3f, %.3f] m\n', min(y_t), max(y_t));
fprintf('  Simétrico - Rango Z: [%.3f, %.3f] m\n', min(z_t), max(z_t));

if max(abs(x_t_asym)) < 100
    fprintf('  Asimétrico - Rango X: [%.3f, %.3f] m\n', min(x_t_asym), max(x_t_asym));
    fprintf('  Asimétrico - Rango Y: [%.3f, %.3f] m\n', min(y_t_asym), max(y_t_asym));
    fprintf('  Asimétrico - Rango Z: [%.3f, %.3f] m\n', min(z_t_asym), max(z_t_asym));
end
