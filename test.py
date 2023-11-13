import matplotlib
import matplotlib.pyplot as plt 

datos_despues_coma = []

try:
    with open('datos.txt', 'r') as archivo:
        lineas = archivo.readlines()  # Lee todas las líneas del archivo y las almacena en una lista
        ##como saber que lineas es un lista

        # Inicializa dos listas para almacenar los datos antes y después de la coma 
        #datos_despues_coma = []
        
        # Procesar cada línea para obtener los datos antes y después de la coma:
        for linea in lineas:
            partes = linea.split(',')  # Divide la línea en función de la coma
            if len(partes) == 2:  # Asegurarse de que haya dos partes (antes y después de la coma)
                #datos_antes_coma.append( partes[0].strip())  # Obtiene la parte antes de la coma y elimina espacios en blanco
                dato_despues_de_coma = float(partes[1].strip())  # Obtiene la parte después de la coma y elimina espacios en blanco
                
                
                    ##Al convertir los valores a números con float(), el eje y respetará los valores numéricos y no los tratará como cadenas de texto


                # Agrega los datos a las listas respectivas
                #datos_antes_coma.append(dato_antes_de_coma)
                datos_despues_coma.append(dato_despues_de_coma)
                
except FileNotFoundError:
    print("El archivo no se encontró")
except IOError:
    print("Ocurrió un error al leer el archivo")

plt.figure(figsize=(10, 5))  # Tamaño de la figura
#plt.plot(range(len(datos_despues_coma)), datos_despues_coma, label='Datos',marker='*')
        
        # Puedes graficar los datos después de la coma si lo deseas
        # plt.plot(datos_despues_coma, label='Datos después de la coma')
        
        # Configuración de la leyenda y etiquetas de los ejes
plt.legend()
plt.xlabel('Índice de Datos')
plt.ylabel('Valor')
plt.title('Gráfico de Datos antes de la Coma')
        
        # Mostrar el gráfico
#plt.show()  # Usar 'block=False' para que el gráfico no bloquee la ejecución
#print(datos_despues_coma)

maximo_valor = max(datos_despues_coma)
print(maximo_valor)

numeros_despues_coma_normalizados = [valor / maximo_valor for valor in datos_despues_coma]
#####
# FIN CAPTURA DE DATOS
######

import tensorflow as tf
import numpy as np
np.random.seed(0)
tf.random.set_seed(0)
#datos_despues_coma = np.arange(0,1399)

datos = np.array(numeros_despues_coma_normalizados, dtype=float)
datos2 = np.arange(0, 5865)

print("los datos:")
print(datos)
print(datos2)


# Definir el modelo secuencial
modelo = tf.keras.Sequential()

# Agregar la primera capa oculta
modelo.add(tf.keras.layers.Dense(units=1, input_shape=[1], activation='linear', kernel_initializer='he_normal'))

# Agregar la segunda capa oculta
#modelo.add(tf.keras.layers.Dense(units=35, activation='linear'))

#relu linear tanh

modelo.add(tf.keras.layers.Dense(units=5, activation='linear'))


# Agregar la capa de salida
modelo.add(tf.keras.layers.Dense(units=1, activation='linear'))


# Resumen del modelo
modelo.summary()


modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.01),
    loss='mean_squared_error'
    #mean_absolute_error
    #mean_squared_error
)
print("aca entreno")
#plt.close('all')
#matplotlib.use('Agg')
historial = modelo.fit(datos2, datos, epochs=15, verbose= True)
print("entrenado")
plt.xlabel("n mediciones")
plt.ylabel("potencia")
#plt.plot(historial.history["loss"])
plt.show(block=False)

##
# PREDICCIONES
##


evaluacion = modelo.evaluate(datos2, datos)
print("Pérdida en datos de prueba:", evaluacion)

datos3 = np.arange(1400, 2799)
datos3 = numeros_despues_coma_normalizados
# Realizar predicciones en los datos de prueba
predicciones = modelo.predict(datos3)

print("le mande hacer predicciones con:")
print(datos2)


# Crear un gráfico de dispersión para comparar las predicciones con los valores reales
plt.plot(datos2, datos, label='Valores reales entrenados')
#plt.scatter(datos2, datos3, label='Valores reales sin entrenar', marker='+')
plt.plot(datos2, predicciones, label='Predicciones', marker='.')

plt.xlabel("Índice de Datos")
plt.ylabel("Valor")
plt.legend()
plt.title('Comparación de Predicciones en Datos de Prueba')
plt.show()

resultado = modelo.predict(np.array([1]).reshape(-1, 1))
print("El resultado es " + str(resultado[0][0]) + " watts")

resultado2 = modelo.predict(np.array([2]).reshape(-1, 1))
print("El resultado es " + str(resultado2[0][0]) + " watts")

resultado2 = modelo.predict(np.array([8000]).reshape(-1, 1))
print("El resultado es " + str(resultado2[0][0]) + " watts")