from pulp import *

# Definicion de parametros
# d = COMPLETE_AQUI
F = [0,2,3,5,11,15,30,35,40]
h = [0,6,4,3,1,2,4,7,8]
M = 30
d = [0,3,4,2,4,3,4,2,4]
indices = range(1,9,1)

#Definicion de variables: 
I = LpVariable.dicts("I",indices,None, None, LpContinuous)
y = LpVariable.dicts("y",indices,None, None, LpInteger)
#x = COMPLETE_AQUI
x = LpVariable.dicts("x",indices,None, None, LpContinuous)

#Restriccion variables
for i in indices:
  I[i].bounds(0, None)
  y[i].bounds(0, 1)  
  #x[i]... = COMPLETE_AQUI
  x[i].bounds(0, None)

#Creación de problema
prob = LpProblem("Tarea_Optimizacion", LpMinimize)

#Creacion funcion objetivo 
prob += lpSum([F[i] * y[i] for i in indices]) + lpSum([h[i] * I[i] for i in indices]) , "Costo Total"

#Creacion restricciones
# COMPLETE_AQUI
for i in indices:
  #x[i]... = COMPLETE_AQUI
  if i == 1:
    prob += x[i] + 0 == I[i] + d[i]
    prob += x[i] <= M * y[i], ("Restriccion costo fijo" + str(i))
    prob += 0 <= y[i] <= 1
  else:
    prob += x[i] + I[i-1] == I[i] + d[i]
    prob += x[i] <= M * y[i], ("Restriccion costo fijo" + str(i))
    prob += 0 <= y[i] <= 1

# Problema a un archivo .lp
prob.writeLP("ProblemaInventario.lp")

# Resolucion de problema 
prob.solve()

# Imprimir el Status del problema
print("Status:", LpStatus[prob.status])


# Parte II, MODIFIQUE_AQUI 
# Imprimir el optimo de la funcion objetivo   
print(f"\nCosto de la solución = {int(value(prob.objective))},")


# Parte II, MODIFIQUE_AQUI 
# Imprimir cada variable con su optimo
vars_x = []
vars_I = []
for v in prob.variables():
  if "x" in v.name:
    vars_x.append(v)
  elif "I" in v.name:
    vars_I.append(v)
for t in range(len(vars_x)):
  print(f"cantidad de inventario período {t+1} = {int(vars_I[t].varValue)}")
  print(f"cantidad producida en período {t+1} = {int(vars_x[t].varValue)}")
