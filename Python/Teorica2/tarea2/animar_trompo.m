%% ANIMACIÓN SIMPLE DEL TROMPO (Octave Compatible)
% Version simplificada para evitar problemas de scope

clear all; close all; clc;

fprintf('🎪 Iniciando animación del trompo...\n');

%% Carga de datos
fprintf('Cargando datos del trompo...\n');
try
    load('dataTrompo.mat');
    fprintf('✓ Datos cargados exitosamente\n');
    fprintf('  - Trompo simétrico: %d puntos temporales\n', length(t));
    fprintf('  - Trompo asimétrico: %d puntos temporales\n', length(t_asym));
catch
    error('❌ Error al cargar dataTrompo.mat');
end

%% Menú de selección
fprintf('\n🎯 Selecciona el tipo de animación:\n');
fprintf('1. Trompo Simétrico\n');
fprintf('2. Trompo Asimétrico\n');
fprintf('3. Comparación lado a lado\n');
fprintf('4. Solo visualización estática\n');

choice = input('Selección (1-4): ');

%% Ejecutar según selección
switch choice
    case 1
        %% Animación Trompo Simétrico
        fprintf('\n🔄 Animando trompo simétrico...\n');
        
        figure('Position', [100, 100, 800, 600]);
        
        % Configurar la animación
        skip = max(1, floor(length(t)/100)); % Máximo 100 frames para rapidez
        frames = 1:skip:length(t);
        
        for i = frames
            clf;
            hold on;
            
            % Dibujar trayectoria hasta el punto actual
            if i > 10
                plot3(x_t(1:i), y_t(1:i), z_t(1:i), 'b-', 'LineWidth', 1.5);
            end
            
            % Posición actual del trompo (esfera simple)
            [xs, ys, zs] = sphere(20);
            surf(xs*0.05 + x_t(i), ys*0.05 + y_t(i), zs*0.05 + z_t(i), ...
                 'FaceColor', 'red', 'EdgeColor', 'none');
            
            % Configuración de ejes
            axis equal;
            grid on;
            xlabel('X (m)');
            ylabel('Y (m)');
            zlabel('Z (m)');
            title(sprintf('Trompo Simétrico - t = %.2f s', t(i)));
            
            % Vista isométrica
            view(45, 30);
            
            % Límites dinámicos
            margin = 0.3;
            xlim([min(x_t) - margin, max(x_t) + margin]);
            ylim([min(y_t) - margin, max(y_t) + margin]);
            zlim([min(z_t) - margin, max(z_t) + margin]);
            
            drawnow;
            pause(0.02);
        end
        
        fprintf('✅ Animación simétrica completada\n');
        
    case 2
        %% Animación Trompo Asimétrico
        fprintf('\n🔄 Animando trompo asimétrico...\n');
        
        figure('Position', [100, 100, 800, 600]);
        
        % Verificar valores razonables
        if max(abs(x_t_asym)) > 50
            fprintf('⚠ Detectados valores extremos, limitando visualización...\n');
            % Usar solo los primeros puntos donde los valores son razonables
            valid_idx = find(abs(x_t_asym) < 10 & abs(y_t_asym) < 10 & abs(z_t_asym) < 10);
            if isempty(valid_idx)
                valid_idx = 1:min(100, length(x_t_asym));
            end
            x_plot = x_t_asym(valid_idx);
            y_plot = y_t_asym(valid_idx);
            z_plot = z_t_asym(valid_idx);
            t_plot = t_asym(valid_idx);
        else
            x_plot = x_t_asym;
            y_plot = y_t_asym;
            z_plot = z_t_asym;
            t_plot = t_asym;
        end
        
        % Configurar la animación
        skip = max(1, floor(length(x_plot)/100));
        frames = 1:skip:length(x_plot);
        
        for i = frames
            clf;
            hold on;
            
            % Dibujar trayectoria hasta el punto actual
            if i > 10
                plot3(x_plot(1:i), y_plot(1:i), z_plot(1:i), 'r-', 'LineWidth', 1.5);
            end
            
            % Posición actual del trompo
            [xs, ys, zs] = sphere(20);
            surf(xs*0.05 + x_plot(i), ys*0.05 + y_plot(i), zs*0.05 + z_plot(i), ...
                 'FaceColor', 'blue', 'EdgeColor', 'none');
            
            % Configuración de ejes
            axis equal;
            grid on;
            xlabel('X (m)');
            ylabel('Y (m)');
            zlabel('Z (m)');
            title(sprintf('Trompo Asimétrico - t = %.2f s', t_plot(i)));
            
            % Vista isométrica
            view(45, 30);
            
            % Límites dinámicos
            margin = 0.5;
            xlim([min(x_plot) - margin, max(x_plot) + margin]);
            ylim([min(y_plot) - margin, max(y_plot) + margin]);
            zlim([min(z_plot) - margin, max(z_plot) + margin]);
            
            drawnow;
            pause(0.02);
        end
        
        fprintf('✅ Animación asimétrica completada\n');
        
    case 3
        %% Comparación lado a lado
        fprintf('\n🔄 Comparación lado a lado...\n');
        
        figure('Position', [100, 100, 1200, 500]);
        
        % Preparar datos asimétricos
        if max(abs(x_t_asym)) > 50
            valid_idx = find(abs(x_t_asym) < 10 & abs(y_t_asym) < 10 & abs(z_t_asym) < 10);
            if isempty(valid_idx)
                valid_idx = 1:min(100, length(x_t_asym));
            end
            x_asym_plot = x_t_asym(valid_idx);
            y_asym_plot = y_t_asym(valid_idx);
            z_asym_plot = z_t_asym(valid_idx);
            t_asym_plot = t_asym(valid_idx);
        else
            x_asym_plot = x_t_asym;
            y_asym_plot = y_t_asym;
            z_asym_plot = z_t_asym;
            t_asym_plot = t_asym;
        end
        
        max_frames = min(length(t), length(t_asym_plot));
        skip = max(1, floor(max_frames/80));
        frames = 1:skip:max_frames;
        
        for i = frames
            clf;
            
            % Subplot izquierdo - Simétrico
            subplot(1, 2, 1);
            hold on;
            if i > 5
                plot3(x_t(1:i), y_t(1:i), z_t(1:i), 'b-', 'LineWidth', 1.5);
            end
            [xs, ys, zs] = sphere(15);
            surf(xs*0.04 + x_t(i), ys*0.04 + y_t(i), zs*0.04 + z_t(i), ...
                 'FaceColor', 'red', 'EdgeColor', 'none');
            axis equal; grid on;
            xlabel('X (m)'); ylabel('Y (m)'); zlabel('Z (m)');
            title(sprintf('Simétrico - t = %.2f s', t(i)));
            view(45, 30);
            margin = 0.3;
            xlim([min(x_t) - margin, max(x_t) + margin]);
            ylim([min(y_t) - margin, max(y_t) + margin]);
            zlim([min(z_t) - margin, max(z_t) + margin]);
            
            % Subplot derecho - Asimétrico
            subplot(1, 2, 2);
            hold on;
            if i <= length(x_asym_plot)
                if i > 5
                    plot3(x_asym_plot(1:i), y_asym_plot(1:i), z_asym_plot(1:i), 'r-', 'LineWidth', 1.5);
                end
                surf(xs*0.04 + x_asym_plot(i), ys*0.04 + y_asym_plot(i), zs*0.04 + z_asym_plot(i), ...
                     'FaceColor', 'blue', 'EdgeColor', 'none');
                title(sprintf('Asimétrico - t = %.2f s', t_asym_plot(i)));
            else
                text(0, 0, 0, 'Datos limitados', 'HorizontalAlignment', 'center');
                title('Asimétrico - Datos limitados');
            end
            axis equal; grid on;
            xlabel('X (m)'); ylabel('Y (m)'); zlabel('Z (m)');
            view(45, 30);
            
            drawnow;
            pause(0.03);
        end
        
        fprintf('✅ Comparación completada\n');
        
    case 4
        %% Solo visualización estática
        visualizar_simple;
        
    otherwise
        fprintf('Opción no válida, ejecutando visualización estática...\n');
        visualizar_simple;
end

fprintf('\n🎪 Animación completada!\n');
