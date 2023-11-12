#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Uso: $0 <nombre_directorio> <numero_tareas_reduccion>"
  exit 1
fi

exercise_name="$1"
reduce_tasks="$2"
base_dir="/MapReduce/$exercise_name"

if [ "$exercise_name" == "ejemplo" ]; then
  display_name="Ejemplo"
else
  display_name="Ejercicio ${exercise_name##*[!0-9]}"
fi

hdfs dfs -test -e data && hdfs dfs -rm -r data

hdfs dfs -test -e output && hdfs dfs -rm -r output
rm -rf $base_dir/output/*

hdfs dfs -put $base_dir/data data

/usr/bin/hadoop \
  jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
  -D mapreduce.job.reduces=$reduce_tasks \
  -input data/ \
  -output output/ \
  -mapper $base_dir/src/mapper.py \
  -reducer $base_dir/src/reducer.py

hdfs dfs -get output $base_dir/output

cat $base_dir/output/part-* >> $base_dir/output/${exercise_name}_output.txt
python $base_dir/src/parser.py

echo "$display_name completado con $reduce_tasks tareas de reducción en el directorio $exercise_name!"
