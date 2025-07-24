% Animación 3D del Trompo - Teoría de Landau
% Desarrollado para la Tarea 2 - Mecánica Teórica
% Script adaptado para usar datos exportados desde Python
% Autor: Juan J27
% Fecha: Julio 2025

clear all; close all; clc;

%% Cargar datos exportados desde Python
fprintf('Cargando datos del trompo...\n');
try
    load('dataTrompo.mat');
    fprintf('✓ Datos cargados exitosamente\n');
    fprintf('  - Trompo simétrico: %d puntos temporales\n', length(t));
    fprintf('  - Trompo asimétrico: %d puntos temporales\n', length(t_asym));
catch
    error('Error: No se pudo cargar dataTrompo.mat. Asegúrate de ejecutar el notebook Python primero.');
end

%% Configuración de visualización
set(groot,'defaultAxesTickLabelInterpreter','latex');
set(groot,'defaultLegendInterpreter','latex');
set(groot,'defaultTextInterpreter','latex');

% Parámetros de visualización
txtsize = 20;
linesize = 2;
lgndsize = 14;

%% Selección del tipo de trompo para animar
fprintf('\nSelecciona el tipo de trompo para animar:\n');
fprintf('1. Trompo Simétrico\n');
fprintf('2. Trompo Asimétrico\n');
fprintf('3. Comparación lado a lado\n');
choice = input('Opción (1-3): ');

switch choice
    case 1
        animateSymmetricTop();
    case 2
        animateAsymmetricTop();
    case 3
        animateComparison();
    otherwise
        fprintf('Opción no válida. Animando trompo simétrico por defecto.\n');
        animateSymmetricTop();
end

%% Función para animar trompo simétrico
function animateSymmetricTop()
    fprintf('\n=== ANIMANDO TROMPO SIMÉTRICO ===\n');
    
    % Cargar modelo STL
    try
        piao = stlread('trompo.stl');
        fprintf('✓ Modelo STL cargado\n');
    catch
        error('Error: No se pudo cargar trompo.stl');
    end
    
    % Crear figura para animación
    fig = figure('Position',[100 100 1200 800]);
    fig.WindowState = 'maximized';
    
    % Configurar transformación del modelo STL
    to = hgtransform;
    piaoMalha = trimesh(piao,'FaceColor',[0.2 0.6 0.8],...
        'EdgeColor','none','Parent',to,'FaceAlpha',0.9);
    
    % Transformación para centrar el modelo
    T1 = makehgtform('translate',[-mean(piao.Points(:,1))...
        -mean(piao.Points(:,2)) -min(piao.Points(:,3))]);
    T2 = makehgtform('scale', 0.1); % Escalar el modelo
    TCorrective = T2*T1;
    
    % Configurar ejes y vista
    axis equal
    axis([-0.5 0.5 -0.5 0.5 -0.2 0.5])
    view(3)
    grid on
    set(gca,'Color',[0.05 0.05 0.05],'GridColor',[0.3 0.3 0.3],...
        'GridAlpha',0.6,'fontsize',16)
    
    % Configurar iluminación
    piaoMalha.FaceLighting = 'gouraud';
    camlight('headlight');
    material('shiny');
    
    % Crear líneas para trayectoria
    trajectory_line = animatedline('MaximumNumPoints',200,'Color',...
        [1 1 0 0.7],'LineWidth',2);
    
    % Crear archivos de video
    vidname = 'TrompoSimetrico_Landau_3D.mp4';
    vidfile = VideoWriter(vidname, 'MPEG-4');
    vidfile.FrameRate = 30;
    vidfile.Quality = 95;
    open(vidfile);
    
    fprintf('Generando animación...\n');
    
    % Factor de submuestreo para suavizar animación
    step = max(1, floor(length(t)/500)); % Máximo 500 frames
    
    for ii = 1:step:length(t)
        % Limpiar y reconfigurar
        cla;
        
        % Recrear mesh del trompo
        piaoMalha = trimesh(piao,'FaceColor',[0.2 0.6 0.8],...
            'EdgeColor','none','Parent',to,'FaceAlpha',0.9);
        piaoMalha.FaceLighting = 'gouraud';
        
        % Aplicar rotaciones usando ángulos de Euler
        R = makehgtform('zrotate',psi_t(ii),'xrotate',theta_t(ii),...
            'zrotate',phi_t(ii));
        to.Matrix = R*TCorrective;
        
        % Agregar punto en la trayectoria
        addpoints(trajectory_line, x_t(ii), y_t(ii), z_t(ii));
        
        % Dibujar línea del punto fijo al extremo
        line([0 x_t(ii)], [0 y_t(ii)], [0 z_t(ii)],...
            'Color',[1 0.2 0.2],'LineWidth',3);
        
        % Punto fijo
        scatter3(0, 0, 0, 100, [1 0 0], 'filled', 'MarkerEdgeColor', 'k');
        
        % Extremo del trompo
        scatter3(x_t(ii), y_t(ii), z_t(ii), 80, [1 1 0], 'filled');
        
        % Configurar ejes
        axis equal
        axis([-0.5 0.5 -0.5 0.5 -0.2 0.5])
        view(3)
        grid on
        
        % Título dinámico
        title(sprintf('Trompo Simétrico - Teoría de Landau\\newlinet = %.2f s', t(ii)),...
            'FontSize',18,'FontWeight','bold','Color','white');
        xlabel('X','FontSize',14,'Color','white');
        ylabel('Y','FontSize',14,'Color','white');
        zlabel('Z','FontSize',14,'Color','white');
        
        % Configurar colores
        set(gca,'Color',[0.05 0.05 0.05],'XColor','white','YColor','white',...
            'ZColor','white','GridColor',[0.3 0.3 0.3],'GridAlpha',0.6);
        
        % Iluminación
        camlight('headlight');
        material('shiny');
        
        drawnow;
        
        % Capturar frame
        writeVideo(vidfile, getframe(gcf));
        
        % Mostrar progreso
        if mod(ii, 50) == 0
            fprintf('Progreso: %.1f%%\n', (ii/length(t))*100);
        end
    end
    
    close(vidfile);
    fprintf('✓ Animación guardada como: %s\n', vidname);
    
    % Reproducir sonido de finalización
    try
        load handel;
        sound(y, Fs);
    catch
        fprintf('(Sonido no disponible)\n');
    end
end

%% Función para animar trompo asimétrico
function animateAsymmetricTop()
    fprintf('\n=== ANIMANDO TROMPO ASIMÉTRICO ===\n');
    
    % Similar al simétrico pero usando datos _asym
    try
        piao = stlread('trompo.stl');
        fprintf('✓ Modelo STL cargado\n');
    catch
        error('Error: No se pudo cargar trompo.stl');
    end
    
    fig = figure('Position',[100 100 1200 800]);
    fig.WindowState = 'maximized';
    
    to = hgtransform;
    piaoMalha = trimesh(piao,'FaceColor',[0.8 0.2 0.2],...
        'EdgeColor','none','Parent',to,'FaceAlpha',0.9);
    
    T1 = makehgtform('translate',[-mean(piao.Points(:,1))...
        -mean(piao.Points(:,2)) -min(piao.Points(:,3))]);
    T2 = makehgtform('scale', 0.1);
    TCorrective = T2*T1;
    
    axis equal
    axis([-1 1 -1 1 -0.2 1])
    view(3)
    grid on
    set(gca,'Color',[0.05 0.05 0.05],'GridColor',[0.3 0.3 0.3],...
        'GridAlpha',0.6,'fontsize',16)
    
    piaoMalha.FaceLighting = 'gouraud';
    camlight('headlight');
    material('shiny');
    
    trajectory_line = animatedline('MaximumNumPoints',200,'Color',...
        [1 0.5 0 0.7],'LineWidth',2);
    
    vidname = 'TrompoAsimetrico_Landau_3D.mp4';
    vidfile = VideoWriter(vidname, 'MPEG-4');
    vidfile.FrameRate = 30;
    vidfile.Quality = 95;
    open(vidfile);
    
    fprintf('Generando animación...\n');
    
    step = max(1, floor(length(t_asym)/500));
    
    for ii = 1:step:length(t_asym)
        cla;
        
        piaoMalha = trimesh(piao,'FaceColor',[0.8 0.2 0.2],...
            'EdgeColor','none','Parent',to,'FaceAlpha',0.9);
        piaoMalha.FaceLighting = 'gouraud';
        
        R = makehgtform('zrotate',psi_t_asym(ii),'xrotate',theta_t_asym(ii),...
            'zrotate',phi_t_asym(ii));
        to.Matrix = R*TCorrective;
        
        addpoints(trajectory_line, x_t_asym(ii), y_t_asym(ii), z_t_asym(ii));
        
        line([0 x_t_asym(ii)], [0 y_t_asym(ii)], [0 z_t_asym(ii)],...
            'Color',[1 0.2 0.2],'LineWidth',3);
        
        scatter3(0, 0, 0, 100, [1 0 0], 'filled', 'MarkerEdgeColor', 'k');
        scatter3(x_t_asym(ii), y_t_asym(ii), z_t_asym(ii), 80, [1 0.5 0], 'filled');
        
        axis equal
        axis([-1 1 -1 1 -0.2 1])
        view(3)
        grid on
        
        title(sprintf('Trompo Asimétrico - Teoría de Landau\\newlinet = %.2f s', t_asym(ii)),...
            'FontSize',18,'FontWeight','bold','Color','white');
        xlabel('X','FontSize',14,'Color','white');
        ylabel('Y','FontSize',14,'Color','white');
        zlabel('Z','FontSize',14,'Color','white');
        
        set(gca,'Color',[0.05 0.05 0.05],'XColor','white','YColor','white',...
            'ZColor','white','GridColor',[0.3 0.3 0.3],'GridAlpha',0.6);
        
        camlight('headlight');
        material('shiny');
        
        drawnow;
        writeVideo(vidfile, getframe(gcf));
        
        if mod(ii, 50) == 0
            fprintf('Progreso: %.1f%%\n', (ii/length(t_asym))*100);
        end
    end
    
    close(vidfile);
    fprintf('✓ Animación guardada como: %s\n', vidname);
    
    try
        load handel;
        sound(y, Fs);
    catch
        fprintf('(Sonido no disponible)\n');
    end
end

%% Función para comparación lado a lado
function animateComparison()
    fprintf('\n=== ANIMANDO COMPARACIÓN LADO A LADO ===\n');
    
    try
        piao = stlread('trompo.stl');
        fprintf('✓ Modelo STL cargado\n');
    catch
        error('Error: No se pudo cargar trompo.stl');
    end
    
    fig = figure('Position',[50 50 1600 800]);
    fig.WindowState = 'maximized';
    
    % Subplot izquierdo - Trompo Simétrico
    subplot(1,2,1);
    to1 = hgtransform;
    piaoMalha1 = trimesh(piao,'FaceColor',[0.2 0.6 0.8],...
        'EdgeColor','none','Parent',to1,'FaceAlpha',0.9);
    
    T1 = makehgtform('translate',[-mean(piao.Points(:,1))...
        -mean(piao.Points(:,2)) -min(piao.Points(:,3))]);
    T2 = makehgtform('scale', 0.1);
    TCorrective = T2*T1;
    
    axis equal
    axis([-0.5 0.5 -0.5 0.5 -0.2 0.5])
    view(3)
    grid on
    set(gca,'Color',[0.05 0.05 0.05],'GridColor',[0.3 0.3 0.3],...
        'GridAlpha',0.6,'fontsize',14)
    title('Trompo Simétrico','FontSize',16,'FontWeight','bold','Color','white');
    
    piaoMalha1.FaceLighting = 'gouraud';
    camlight('headlight');
    material('shiny');
    
    trajectory_line1 = animatedline('MaximumNumPoints',200,'Color',...
        [1 1 0 0.7],'LineWidth',2);
    
    % Subplot derecho - Trompo Asimétrico  
    subplot(1,2,2);
    to2 = hgtransform;
    piaoMalha2 = trimesh(piao,'FaceColor',[0.8 0.2 0.2],...
        'EdgeColor','none','Parent',to2,'FaceAlpha',0.9);
    
    axis equal
    axis([-1 1 -1 1 -0.2 1])
    view(3)
    grid on
    set(gca,'Color',[0.05 0.05 0.05],'GridColor',[0.3 0.3 0.3],...
        'GridAlpha',0.6,'fontsize',14)
    title('Trompo Asimétrico','FontSize',16,'FontWeight','bold','Color','white');
    
    piaoMalha2.FaceLighting = 'gouraud';
    camlight('headlight');
    material('shiny');
    
    trajectory_line2 = animatedline('MaximumNumPoints',200,'Color',...
        [1 0.5 0 0.7],'LineWidth',2);
    
    % Video
    vidname = 'ComparacionTrompos_Landau_3D.mp4';
    vidfile = VideoWriter(vidname, 'MPEG-4');
    vidfile.FrameRate = 30;
    vidfile.Quality = 95;
    open(vidfile);
    
    fprintf('Generando animación comparativa...\n');
    
    % Usar el menor número de puntos para sincronizar
    n_frames = min(length(t), length(t_asym));
    step = max(1, floor(n_frames/500));
    
    for ii = 1:step:n_frames
        % Subplot izquierdo - Simétrico
        subplot(1,2,1);
        cla;
        
        piaoMalha1 = trimesh(piao,'FaceColor',[0.2 0.6 0.8],...
            'EdgeColor','none','Parent',to1,'FaceAlpha',0.9);
        piaoMalha1.FaceLighting = 'gouraud';
        
        R1 = makehgtform('zrotate',psi_t(ii),'xrotate',theta_t(ii),...
            'zrotate',phi_t(ii));
        to1.Matrix = R1*TCorrective;
        
        addpoints(trajectory_line1, x_t(ii), y_t(ii), z_t(ii));
        
        line([0 x_t(ii)], [0 y_t(ii)], [0 z_t(ii)],...
            'Color',[1 0.2 0.2],'LineWidth',3);
        scatter3(0, 0, 0, 80, [1 0 0], 'filled');
        scatter3(x_t(ii), y_t(ii), z_t(ii), 60, [1 1 0], 'filled');
        
        axis equal
        axis([-0.5 0.5 -0.5 0.5 -0.2 0.5])
        view(3)
        grid on
        title(sprintf('Simétrico\\newlinet = %.2f s', t(ii)),...
            'FontSize',14,'FontWeight','bold','Color','white');
        set(gca,'Color',[0.05 0.05 0.05],'XColor','white','YColor','white',...
            'ZColor','white','GridColor',[0.3 0.3 0.3],'GridAlpha',0.6);
        camlight('headlight');
        
        % Subplot derecho - Asimétrico
        subplot(1,2,2);
        cla;
        
        piaoMalha2 = trimesh(piao,'FaceColor',[0.8 0.2 0.2],...
            'EdgeColor','none','Parent',to2,'FaceAlpha',0.9);
        piaoMalha2.FaceLighting = 'gouraud';
        
        R2 = makehgtform('zrotate',psi_t_asym(ii),'xrotate',theta_t_asym(ii),...
            'zrotate',phi_t_asym(ii));
        to2.Matrix = R2*TCorrective;
        
        addpoints(trajectory_line2, x_t_asym(ii), y_t_asym(ii), z_t_asym(ii));
        
        line([0 x_t_asym(ii)], [0 y_t_asym(ii)], [0 z_t_asym(ii)],...
            'Color',[1 0.2 0.2],'LineWidth',3);
        scatter3(0, 0, 0, 80, [1 0 0], 'filled');
        scatter3(x_t_asym(ii), y_t_asym(ii), z_t_asym(ii), 60, [1 0.5 0], 'filled');
        
        axis equal
        axis([-1 1 -1 1 -0.2 1])
        view(3)
        grid on
        title(sprintf('Asimétrico\\newlinet = %.2f s', t_asym(ii)),...
            'FontSize',14,'FontWeight','bold','Color','white');
        set(gca,'Color',[0.05 0.05 0.05],'XColor','white','YColor','white',...
            'ZColor','white','GridColor',[0.3 0.3 0.3],'GridAlpha',0.6);
        camlight('headlight');
        
        drawnow;
        writeVideo(vidfile, getframe(gcf));
        
        if mod(ii, 50) == 0
            fprintf('Progreso: %.1f%%\n', (ii/n_frames)*100);
        end
    end
    
    close(vidfile);
    fprintf('✓ Animación comparativa guardada como: %s\n', vidname);
    
    try
        load handel;
        sound(y, Fs);
    catch
        fprintf('(Sonido no disponible)\n');
    end
end

fprintf('\n🎬 Script de animación completado!\n');
fprintf('Archivos generados en el directorio actual.\n');
