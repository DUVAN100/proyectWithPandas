import pandas as pd
import matplotlib.pyplot as plt
def calcularPromediSalariosPorEdad(dataframe, rangos, columnaDeInteres, columnaAPromediar, nombreGrafica):
    plt.figure()
    #crear coluna nueva por rangos de edad 
    dataframe['rangosEdad'] = pd.cut(dataframe[columnaDeInteres], bins=rangos)
    #calcular la suma de los salarios pr rango de edad
    salarioPorRango = dataframe.groupby('rangosEdad')[columnaAPromediar].sum()
    #defiinmos lo datos da graficar
    salario = salarioPorRango.values
    rangosEdad = salarioPorRango.index
    plt.pie(salario, labels = rangosEdad, autopct = '%1.1f%%')    
    plt.title('Salarios por rango de edad')
    plt.savefig(f'./assets/img/{nombreGrafica}.png')