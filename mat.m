
    % Archivo de script para graficar en MATLAB

    % Cargar datos desde el archivo
    datos = load('datos_mat2.txt');

    % Separar datos_x y datos_y
    datos_x = datos(:, 1);
    datos_y = datos(:, 2);

    %Graficar
    figure;
    plot(datos_x);
    figure;
    plot(datos_y);
    figure;
    hold on;
    plot(datos_x);
    plot(-0.5*datos_y+0.011);




