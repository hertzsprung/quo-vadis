#/bin/bash
set -e

rm -f plot*.png plot.gif

for i in $(seq 0 119);
do
	./surface-fit-visualisation.py 60 $((30 + $i * 3)) $(printf "%03g" $i) | gnuplot5
done
for i in $(seq 0 30);
do
	cp plot000.png plot$(printf "%03g" $(($i + 119))).png
done

convert -delay 5 -loop 0 plot*.png plot.gif
