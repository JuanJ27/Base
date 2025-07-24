% Script de verificación y carga de datos - Trompo Landau
% Verificar que los datos se cargan correctamente desde Python

clear all; close all; clc;

fprintf('=== VERIFICACIÓN DE DATOS DEL TROMPO ===\n\n');

%% 1. Cargar y verificar datos
try
    load('dataTrompo.mat');
    fprintf('✓ Archivo dataTrompo.mat cargado exitosamente\n');
catch ME
    fprintf('❌ Error cargando dataTrompo.mat:\n');
    fprintf('   %s\n', ME.message);
    fprintf('   Asegúrate de ejecutar el notebook Python primero.\n');
    return;
end

%% 2. Mostrar información de los datos
fprintf('\n--- INFORMACIÓN DE LOS DATOS ---\n');
fprintf('Trompo Simétrico:\n');
fprintf('  • Puntos temporales: %d\n', length(t));
fprintf('  • Tiempo total: %.2f segundos\n', max(t));
fprintf('  • Parámetros: I=%.2f, I_z=%.2f, m=%.2f kg, h=%.3f m\n', I_sym, I_z_sym, m_sym, h_sym);

fprintf('\nTrompo Asimétrico:\n');
fprintf('  • Puntos temporales: %d\n', length(t_asym));
fprintf('  • Tiempo total: %.2f segundos\n', max(t_asym));
fprintf('  • Masa: %.2f kg, h=%.3f m\n', m_asym, h_asym);

fprintf('\nTensor de inercia asimétrico:\n');
disp(I_matrix_asym);

%% 3. Verificar modelo STL
fprintf('--- VERIFICACIÓN DEL MODELO STL ---\n');
try
    piao = stlread('trompo.stl');
    fprintf('✓ Modelo STL trompo.stl cargado exitosamente\n');
    fprintf('  • Número de caras: %d\n', size(piao.ConnectivityList, 1));
    fprintf('  • Número de vértices: %d\n', size(piao.Points, 1));
    
    % Mostrar dimensiones del modelo
    x_range = [min(piao.Points(:,1)), max(piao.Points(:,1))];
    y_range = [min(piao.Points(:,2)), max(piao.Points(:,2))];
    z_range = [min(piao.Points(:,3)), max(piao.Points(:,3))];
    
    fprintf('  • Dimensiones X: [%.2f, %.2f]\n', x_range);
    fprintf('  • Dimensiones Y: [%.2f, %.2f]\n', y_range);
    fprintf('  • Dimensiones Z: [%.2f, %.2f]\n', z_range);
    
    stl_loaded = true;
catch ME
    fprintf('❌ Error cargando trompo.stl:\n');
    fprintf('   %s\n', ME.message);
    stl_loaded = false;
end

%% 4. Crear gráficos de verificación
fprintf('\n--- GENERANDO GRÁFICOS DE VERIFICACIÓN ---\n');

% Gráfico 1: Comparación de trayectorias
figure('Position', [100, 100, 1200, 600]);

subplot(2,3,1);
plot(t, rad2deg(theta_t), 'b-', 'LineWidth', 2); hold on;
plot(t_asym, rad2deg(theta_t_asym), 'r-', 'LineWidth', 2);
xlabel('Tiempo (s)'); ylabel('Ángulo θ (°)');
title('Nutación'); legend('Simétrico', 'Asimétrico');
grid on;

subplot(2,3,2);
plot(t, rad2deg(phi_t), 'b-', 'LineWidth', 2); hold on;
plot(t_asym, rad2deg(phi_t_asym), 'r-', 'LineWidth', 2);
xlabel('Tiempo (s)'); ylabel('Ángulo φ (°)');
title('Precesión'); legend('Simétrico', 'Asimétrico');
grid on;

subplot(2,3,3);
plot(t, rad2deg(psi_t), 'b-', 'LineWidth', 2); hold on;
plot(t_asym, rad2deg(psi_t_asym), 'r-', 'LineWidth', 2);
xlabel('Tiempo (s)'); ylabel('Ángulo ψ (°)');
title('Spin'); legend('Simétrico', 'Asimétrico');
grid on;

subplot(2,3,4);
plot3(x_t, y_t, z_t, 'b-', 'LineWidth', 2); hold on;
plot3(x_t_asym, y_t_asym, z_t_asym, 'r-', 'LineWidth', 2);
scatter3(0, 0, 0, 100, 'k', 'filled');
xlabel('X'); ylabel('Y'); zlabel('Z');
title('Trayectorias 3D'); legend('Simétrico', 'Asimétrico', 'Punto fijo');
grid on; axis equal;

subplot(2,3,5);
plot(x_t, y_t, 'b-', 'LineWidth', 2); hold on;
plot(x_t_asym, y_t_asym, 'r-', 'LineWidth', 2);
scatter(0, 0, 100, 'k', 'filled');
xlabel('X'); ylabel('Y');
title('Proyección XY'); legend('Simétrico', 'Asimétrico', 'Punto fijo');
grid on; axis equal;

subplot(2,3,6);
plot(t, psi_d_t, 'b-', 'LineWidth', 2); hold on;
plot(t_asym, psi_d_t_asym, 'r-', 'LineWidth', 2);
xlabel('Tiempo (s)'); ylabel('Velocidad ψ̇ (rad/s)');
title('Velocidad de Spin'); legend('Simétrico', 'Asimétrico');
grid on;

sgtitle('Verificación de Datos - Trompo Teoría de Landau', 'FontSize', 16, 'FontWeight', 'bold');

fprintf('✓ Gráficos de verificación generados\n');

%% 5. Visualización del modelo STL (si está disponible)
if stl_loaded
    figure('Position', [200, 200, 800, 600]);
    trimesh(piao, 'FaceColor', [0.7, 0.7, 0.9], 'EdgeColor', 'none', 'FaceAlpha', 0.8);
    axis equal; grid on;
    camlight; lighting gouraud; material shiny;
    title('Modelo STL del Trompo', 'FontSize', 14, 'FontWeight', 'bold');
    xlabel('X'); ylabel('Y'); zlabel('Z');
    view(3);
    fprintf('✓ Visualización del modelo STL generada\n');
end

%% 6. Resumen final
fprintf('\n=== RESUMEN DE VERIFICACIÓN ===\n');
fprintf('✓ Datos cargados correctamente\n');
if stl_loaded
    fprintf('✓ Modelo STL disponible\n');
else
    fprintf('⚠ Modelo STL no disponible\n');
end
fprintf('✓ Gráficos de verificación generados\n');
fprintf('\n🎬 Listo para ejecutar animaciones!\n');
fprintf('   Ejecuta: trompoAnimacionLandau.m\n');
fprintf('\nArchivos necesarios:\n');
fprintf('  • dataTrompo.mat (✓ disponible)\n');
if stl_loaded
    fprintf('  • trompo.stl (✓ disponible)\n');
else
    fprintf('  • trompo.stl (❌ no encontrado)\n');
end

%% 7. Verificar dependencias de MATLAB
fprintf('\n--- VERIFICANDO DEPENDENCIAS ---\n');

% Verificar funciones necesarias para Octave
try
    % Verificar si tenemos las funciones básicas de transformación
    eye(4); % Matriz identidad básica
    fprintf('✓ Funciones básicas de matriz disponibles\n');
catch
    fprintf('⚠ Error con funciones básicas de matriz\n');
end

try
    if exist('stlread', 'file') || exist('stlread', 'builtin')
        fprintf('✓ Función stlread disponible\n');
    else
        fprintf('⚠ stlread no disponible - puede necesitar paquete io o geometry\n');
        fprintf('   Instalar con: pkg install -forge io\n');
        fprintf('   Instalar con: pkg install -forge geometry\n');
    end
catch
    fprintf('⚠ Error verificando stlread\n');
end

% En Octave, verificar si podemos crear videos básicos
try
    % Octave puede no tener VideoWriter, pero puede usar otras funciones
    fprintf('ℹ Para videos en Octave, considerar usar:\n');
    fprintf('   - Guardar frames como imágenes y usar ffmpeg\n');
    fprintf('   - Usar paquete video si está disponible\n');
catch
    fprintf('⚠ Capacidades de video limitadas en Octave\n');
end

fprintf('\n✨ Verificación completada!\n');
