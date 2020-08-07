import line
import math

def displacement(x):
  # t = 1e-7
  return 0.001*math.sin(3.14159264*(x-501840.435*math.pow(10,-7)))



# OBLIGATORY:  the test harness looks for '#L2_error_norm_tolerance' 
tolerance = 1e-2
print "#L2_error_norm_tolerance:", tolerance

variable = {'name': 'Displacements', 'time': 1.0}

# get x, y data from results
x_data, y_data = line.getLineData('./output_data/steps.pvd', [-0.5, 0, 0], [0.5, 0, 0], variable)


# sample analytical displacement solution
a_data = [displacement(x_data[i]) for i in range(len(x_data))]

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
