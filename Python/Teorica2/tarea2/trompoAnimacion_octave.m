%% ANIMACIÓN DEL TROMPO 3D - ECUACIONES DE LANDAU (Octave Compatible)
% Desarrollado para Tarea 2 - Mecánica Teórica
% Compatible con GNU Octave

function trompoAnimacion_octave()
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
    
    %% Verificar disponibilidad del modelo STL
    if exist('trompo.stl', 'file')
        fprintf('✓ Modelo STL encontrado: trompo.stl\n');
        use_stl = true;
    else
        fprintf('⚠ Modelo STL no encontrado, usando esfera simple\n');
        use_stl = false;
    end
    
    %% Menú de selección
    fprintf('\n🎯 Selecciona el tipo de animación:\n');
    fprintf('1. Trompo Simétrico\n');
    fprintf('2. Trompo Asimétrico\n');
    fprintf('3. Comparación lado a lado\n');
    fprintf('4. Solo visualización de trayectorias\n');
    
    choice = input('Selección (1-4): ');
    
    switch choice
        case 1
            animarTrompoSimetrico();
        case 2
            animarTrompoAsimetrico();
        case 3
            animarComparacion();
        case 4
            visualizarTrayectorias();
        otherwise
            fprintf('Opción no válida, mostrando trayectorias...\n');
            visualizarTrayectorias();
    end
    
    %% Función: Animación Trompo Simétrico
    function animarTrompoSimetrico()
        fprintf('\n🔄 Animando trompo simétrico...\n');
        
        figure('Position', [100, 100, 800, 600]);
        
        % Configurar la animación
        skip = max(1, floor(length(t)/200)); % Máximo 200 frames
        frames = 1:skip:length(t);
        
        % Variables locales para evitar problemas de scope
        x_local = x_t;
        y_local = y_t;
        z_local = z_t;
        t_local = t;
        
        for i = frames
            clf;
            
            % Configurar vista 3D
            subplot(1,1,1);
            hold on;
            
            % Dibujar trayectoria hasta el punto actual
            if i > 1
                plot3(x_local(1:i), y_local(1:i), z_local(1:i), 'b-', 'LineWidth', 1.5);
            end
            
            % Posición actual del trompo
            if use_stl && exist('stlread', 'file')
                % Usar modelo STL si está disponible
                try
                    [faces, vertices] = stlread('trompo.stl');
                    % Escalar y posicionar
                    vertices = vertices * 0.1; % Escalar
                    vertices(:,1) = vertices(:,1) + x_local(i);
                    vertices(:,2) = vertices(:,2) + y_local(i);
                    vertices(:,3) = vertices(:,3) + z_local(i);
                    patch('Faces', faces, 'Vertices', vertices, 'FaceColor', 'red', 'EdgeColor', 'none');
                catch
                    % Fallback a esfera
                    [xs, ys, zs] = sphere(20);
                    surf(xs*0.1 + x_local(i), ys*0.1 + y_local(i), zs*0.1 + z_local(i), ...
                         'FaceColor', 'red', 'EdgeColor', 'none');
                end
            else
                % Usar esfera simple
                [xs, ys, zs] = sphere(20);
                surf(xs*0.1 + x_local(i), ys*0.1 + y_local(i), zs*0.1 + z_local(i), ...
                     'FaceColor', 'red', 'EdgeColor', 'none');
            end
            
            % Configuración de ejes
            axis equal;
            grid on;
            xlabel('X (m)');
            ylabel('Y (m)');
            zlabel('Z (m)');
            title(sprintf('Trompo Simétrico - t = %.2f s', t_local(i)));
            
            % Vista isométrica
            view(45, 30);
            
            % Límites dinámicos
            margin = 0.5;
            xlim([min(x_local) - margin, max(x_local) + margin]);
            ylim([min(y_local) - margin, max(y_local) + margin]);
            zlim([min(z_local) - margin, max(z_local) + margin]);
            
            lighting gouraud;
            light('Position', [1, 1, 1]);
            
            drawnow;
            pause(0.05);
        end
        
        fprintf('✅ Animación simétrica completada\n');
    end
    
    %% Función: Animación Trompo Asimétrico
    function animarTrompoAsimetrico()
        fprintf('\n🔄 Animando trompo asimétrico...\n');
        
        figure('Position', [100, 100, 800, 600]);
        
        % Configurar la animación
        skip = max(1, floor(length(t_asym)/200)); % Máximo 200 frames
        frames = 1:skip:length(t_asym);
        
        for i = frames
            clf;
            
            % Configurar vista 3D
            subplot(1,1,1);
            hold on;
            
            % Dibujar trayectoria hasta el punto actual
            if i > 1
                plot3(x_t_asym(1:i), y_t_asym(1:i), z_t_asym(1:i), 'r-', 'LineWidth', 1.5);
            end
            
            % Posición actual del trompo
            [xs, ys, zs] = sphere(20);
            surf(xs*0.1 + x_t_asym(i), ys*0.1 + y_t_asym(i), zs*0.1 + z_t_asym(i), ...
                 'FaceColor', 'blue', 'EdgeColor', 'none');
            
            % Configuración de ejes
            axis equal;
            grid on;
            xlabel('X (m)');
            ylabel('Y (m)');
            zlabel('Z (m)');
            title(sprintf('Trompo Asimétrico - t = %.2f s', t_asym(i)));
            
            % Vista isométrica
            view(45, 30);
            
            % Límites dinámicos (con protección contra valores extremos)
            if max(abs(x_t_asym(1:i))) < 100 % Evitar valores extremos
                margin = 0.5;
                xlim([min(x_t_asym(1:i)) - margin, max(x_t_asym(1:i)) + margin]);
                ylim([min(y_t_asym(1:i)) - margin, max(y_t_asym(1:i)) + margin]);
                zlim([min(z_t_asym(1:i)) - margin, max(z_t_asym(1:i)) + margin]);
            else
                xlim([-2, 2]);
                ylim([-2, 2]);
                zlim([-2, 2]);
            end
            
            lighting gouraud;
            light('Position', [1, 1, 1]);
            
            drawnow;
            pause(0.05);
        end
        
        fprintf('✅ Animación asimétrica completada\n');
    end
    
    %% Función: Comparación lado a lado
    function animarComparacion()
        fprintf('\n🔄 Animando comparación...\n');
        
        figure('Position', [100, 100, 1200, 500]);
        
        % Sincronizar frames
        max_frames = min(length(t), length(t_asym));
        skip = max(1, floor(max_frames/150));
        frames = 1:skip:max_frames;
        
        for i = frames
            clf;
            
            % Subplot izquierdo - Simétrico
            subplot(1, 2, 1);
            hold on;
            plot3(x_t(1:i), y_t(1:i), z_t(1:i), 'b-', 'LineWidth', 1.5);
            [xs, ys, zs] = sphere(20);
            surf(xs*0.1 + x_t(i), ys*0.1 + y_t(i), zs*0.1 + z_t(i), ...
                 'FaceColor', 'red', 'EdgeColor', 'none');
            axis equal; grid on;
            xlabel('X (m)'); ylabel('Y (m)'); zlabel('Z (m)');
            title(sprintf('Simétrico - t = %.2f s', t(i)));
            view(45, 30);
            
            % Subplot derecho - Asimétrico
            subplot(1, 2, 2);
            hold on;
            if max(abs(x_t_asym(1:i))) < 100 % Solo si valores son razonables
                plot3(x_t_asym(1:i), y_t_asym(1:i), z_t_asym(1:i), 'r-', 'LineWidth', 1.5);
                surf(xs*0.1 + x_t_asym(i), ys*0.1 + y_t_asym(i), zs*0.1 + z_t_asym(i), ...
                     'FaceColor', 'blue', 'EdgeColor', 'none');
            else
                text(0, 0, 0, 'Valores extremos detectados', 'HorizontalAlignment', 'center');
            end
            axis equal; grid on;
            xlabel('X (m)'); ylabel('Y (m)'); zlabel('Z (m)');
            title(sprintf('Asimétrico - t = %.2f s', t_asym(i)));
            view(45, 30);
            
            drawnow;
            pause(0.05);
        end
        
        fprintf('✅ Comparación completada\n');
    end
    
    %% Función: Solo visualización de trayectorias
    function visualizarTrayectorias()
        fprintf('\n📊 Generando visualización de trayectorias...\n');
        
        figure('Position', [100, 100, 1200, 900]);
        
        % Trayectorias 3D
        subplot(2, 2, 1);
        plot3(x_t, y_t, z_t, 'b-', 'LineWidth', 2);
        hold on;
        plot3(x_t(1), y_t(1), z_t(1), 'go', 'MarkerSize', 8, 'MarkerFaceColor', 'g');
        plot3(x_t(end), y_t(end), z_t(end), 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r');
        axis equal; grid on;
        xlabel('X (m)'); ylabel('Y (m)'); zlabel('Z (m)');
        title('Trayectoria Trompo Simétrico');
        legend('Trayectoria', 'Inicio', 'Final');
        view(45, 30);
        
        % Ángulos de Euler simétrico
        subplot(2, 2, 2);
        plot(t, theta_t*180/pi, 'r-', 'LineWidth', 2); hold on;
        plot(t, phi_t*180/pi, 'g-', 'LineWidth', 2);
        plot(t, psi_t*180/pi, 'b-', 'LineWidth', 2);
        grid on;
        xlabel('Tiempo (s)');
        ylabel('Ángulo (grados)');
        title('Ángulos de Euler - Simétrico');
        legend('\theta', '\phi', '\psi');
        
        % Trayectoria asimétrica (solo si valores son razonables)
        subplot(2, 2, 3);
        if max(abs(x_t_asym)) < 100
            plot3(x_t_asym, y_t_asym, z_t_asym, 'r-', 'LineWidth', 2);
            hold on;
            plot3(x_t_asym(1), y_t_asym(1), z_t_asym(1), 'go', 'MarkerSize', 8, 'MarkerFaceColor', 'g');
            plot3(x_t_asym(end), y_t_asym(end), z_t_asym(end), 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r');
            axis equal; grid on;
            xlabel('X (m)'); ylabel('Y (m)'); zlabel('Z (m)');
            title('Trayectoria Trompo Asimétrico');
            legend('Trayectoria', 'Inicio', 'Final');
            view(45, 30);
        else
            text(0.5, 0.5, 'Trayectoria asimétrica\ncontiene valores extremos', ...
                 'HorizontalAlignment', 'center', 'Units', 'normalized');
            title('Trompo Asimétrico - Valores Extremos');
        end
        
        % Ángulos de Euler asimétrico
        subplot(2, 2, 4);
        if max(abs(theta_t_asym)) < 100
            plot(t_asym, theta_t_asym*180/pi, 'r-', 'LineWidth', 2); hold on;
            plot(t_asym, phi_t_asym*180/pi, 'g-', 'LineWidth', 2);
            plot(t_asym, psi_t_asym*180/pi, 'b-', 'LineWidth', 2);
            grid on;
            xlabel('Tiempo (s)');
            ylabel('Ángulo (grados)');
            title('Ángulos de Euler - Asimétrico');
            legend('\theta', '\phi', '\psi');
        else
            text(0.5, 0.5, 'Ángulos contienen\nvalores extremos', ...
                 'HorizontalAlignment', 'center', 'Units', 'normalized');
            title('Asimétrico - Valores Extremos');
        end
        
        fprintf('✅ Visualización completada\n');
        fprintf('\n📋 Resumen de datos:\n');
        fprintf('  Simétrico: %d puntos, %.2f segundos\n', length(t), t(end));
        fprintf('  Asimétrico: %d puntos, %.2f segundos\n', length(t_asym), t_asym(end));
    end
    
end
