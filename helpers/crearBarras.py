import matplotlib.pyplot as plt

def graficarPromedioSalarial(dataFrame, campoX, campoY, nombreGrafica):
     colores = ['red', 'green', 'blue', 'orange']
     salarioPromedio = dataFrame.groupby(campoX)[campoY].mean()
     
     #Generar la grafca
     plt.bar(salarioPromedio.index, salarioPromedio, color = colores)
     plt.title("PROMEDIO SALARIAL")
     plt.xlabel("Cargos")
     plt.ylabel("SALARIO MENSUAL")
     plt.savefig(f'./assets/img/{nombreGrafica}.png')