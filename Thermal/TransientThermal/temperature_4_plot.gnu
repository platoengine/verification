set terminal png
set output "TransientThermal_4_comparison.png"
set ylabel "Temperature (C)"
set xlabel "Position (m)"
set yrange[-100: 100]
plot 'temperature_4.data' u 1:2 w l lw 6 title "numerical", \
     'temperature_4.data' u 1:3 w l lw 3 title "analytical"

set terminal postscript color eps
set output "TransientThermal_4_comparison.eps"
set ylabel "Temperature (C)"
set xlabel "Position (m)"
set yrange[-100: 100]
plot 'temperature_4.data' u 1:2 w l lw 6 title "numerical", \
     'temperature_4.data' u 1:3 w l lw 3 title "analytical"
