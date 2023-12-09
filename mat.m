
    % 
    % Archivo de script para graficar en MATLAB

    % Cargar datos desde el archivo
    datos = load('datos_mat3.txt');

    % Separar datos_x y datos_y
    datos_x = datos(:, 1);
    datos_y = datos(:, 2);

    %Graficar
    %figure;
    %plot(datos_x);
    %figure;
    %plot(datos_y);
    figure;
    hold on;
    %plot(datos_x);
    plot(datos_y);%plot(-0.5*datos_y+0.011);


datos2 = load('datos_mat2.txt');
datos_x1 = datos2(:, 2);

datos3 = load('datos_mat.txt');
datos_x2 = datos3(:, 2);

% Concatenar los datos verticalmente
datos_concatenados = cat(1, datos_x1, datos_x2);

figure;
hold on;
%plot(datos_x1, 'r'); % Graficar datos_x1 en rojo
%plot(datos_x2, 'b'); % Graficar datos_x2 en azul
plot(datos_concatenados, 'g');  % Graficar la concatenación en verde

xlabel('Índice de Datos');
ylabel('Valor');
legend('datos_x1', 'datos_x2', 'Concatenados');
title('Comparación de Datos Concatenados');
grid on;


%COMPARACION
figure;
hold on;
plot(datos_concatenados, 'g');  % Graficar la concatenación en verde
plot(datos_y);%plot(-0.5*datos_y+0.011);




    