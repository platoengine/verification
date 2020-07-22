import line
import math

def sol(x):
  
  # Mass density
  p = 8920.0
  # Specific heat
  s = 385.185433
  # Conductivity
  K = 397.48
  # Length
  L = 2.0 

  c2 = K/(s*p)
  l = c2*math.pow(3.14159,2)*math.pow(2,2)/math.pow(L,2)

  # Looking at t = 1000 sec
  return 100*math.sin(3.14159*2*x/L)*math.exp(-l * 1000)


## Note: this test computes the thermal history from initial conditions to thermal 
#        equilibration then compares against a steady-state solution.  Consequently,
#        the agreement won't be as good as say a steady-state simulation.

# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
tolerance = 1e2
print "#L2_error_norm_tolerance:", tolerance

l = 2.0    ## length
k = 1.0e3  ## thermal conductivity
q = 1.0    ## flux boundary condition
T = 0.0    ## fixed temperature BC

# time step (looking at 100th time step or t = 1000 sec)
variable = {'name': 'Temperature', 'time': 100.0}

# get x, y data from results
x_data, y_data = line.getLineData('./output_data/steps.pvd', [-1.0, 0, 0], [1.0, 0, 0], variable)


# sample analytical solution
a_data = [sol(x_data[i]) for i in range(len(x_data))]

# compute error norm
error_norm = 0.0
for i in range(len(x_data)):
  error_norm += (y_data[i]-a_data[i])*(y_data[i]-a_data[i])

# OBLIGATORY:  the test harness looks for '#L2_error_norm_value' 
error_norm = math.sqrt(error_norm)
print "#L2_error_norm_value: ", error_norm

print "#X, computed, analytical"
for i in range(len(x_data)):
  print x_data[i], y_data[i], a_data[i]
