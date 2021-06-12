from pulp import *

# Definicion de parametros
# d = COMPLETE_AQUI
F = [0,2,3,5,11,15,30,35,40]
h = [0,6,4,3,1,2,4,7,8]
M = 30
indices = range(1,9,1)

#Definicion de variables: 
I = LpVariable.dicts("I",indices,None, None, LpContinuous)
y = LpVariable.dicts("y",indices,None, None, LpInteger)
#x = COMPLETE_AQUI

#Restriccion variables
for i in indices:
  I[i].bounds(0, None)
  y[i].bounds(0, 1)  
  #x[i]... = COMPLETE_AQUI

#Creación de problema
prob = LpProblem("Tarea_Optimizacion", LpMinimize)

#Creacion funcion objetivo 
prob += lpSum([F[i] * y[i] for i in indices]) + lpSum([h[i] * I[i] for i in indices]) , "Costo Total"

#Creacion restricciones
# COMPLETE_AQUI
# for i in indices:
#   prob += x[i] <= M * y[i], ("Restriccion costo fijo" + str(i))

    

# Problema a un archivo .lp
prob.writeLP("ProblemaInventario.lp")

# Resolucion de problema 
prob.solve()

# Imprimir el Status del problema
print("Status:", LpStatus[prob.status])

# Parte II, MODIFIQUE_AQUI 
# Imprimir cada variable con su optimo
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Parte II, MODIFIQUE_AQUI 
# Imprimir el optimo de la funcion objetivo   
print(value(prob.objective))


