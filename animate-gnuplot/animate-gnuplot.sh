#/bin/bash
for i in $(seq 0 119);
do
	./surface-fit-visualisation.py 60 $((30 + $i * 3)) $(printf "%03g" $i) | gnuplot5
done
for i in $(seq 0 40);
do
	./surface-fit-visualisation.py 60 30 $(printf "%03g" $(($i + 119))) | gnuplot5
done


