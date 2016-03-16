set term svg size 1600,1200 font "sans-serif,40"
set output "timesteps.svg"
#set style data histogram
set boxwidth 0.75 relative
set style fill solid border -1
set ylabel "Timestep (s)" offset 2
set yrange [0:22]
set mytics 5
set xtics nomirror

plot 'timesteps.dat' using 2:xtic(1) lc '#d2002e' notitle with boxes
