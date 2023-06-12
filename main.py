import pandas as pd
from helpers.creartablashtml import creartabla
from helpers.crearBarras import graficarPromedioSalarial
from helpers.crearTorta import calcularPromediSalariosPorEdad
from data.data1 import apartamento1,apartamento2



tabla1=pd.DataFrame(apartamento1,columns=['edad'])
tabla2=pd.DataFrame(apartamento2,columns=['edad'])
tabla3=pd.read_csv("./data/empleados.csv")

#Filters
empleadosJovenesAnalistas1 = tabla3.query('cargo=="analista1"')
empleadosSalarioBajoAnalistas2 = tabla3.query('salario<5000000 and cargo== "analista2"')
empleadosDespedir = tabla3.query('edad>=50')
#create table with dataframe
creartabla(empleadosSalarioBajoAnalistas2, "TablaBajosSalarios")
creartabla(empleadosJovenesAnalistas1, "TablaJovenes")
creartabla(empleadosDespedir, "TablaDespedir")
#graficamos 
graficarPromedioSalarial(empleadosDespedir, 'cargo', 'salario', 'graficaDespedidos')
calcularPromediSalariosPorEdad(empleadosJovenesAnalistas1, [20,30,40,50,60], 'edad', 'salario', 'graicaTortaAnalista1')


