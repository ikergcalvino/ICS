#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Uso: $0 <nombre_directorio> <numero_tareas_reduccion>"
  exit 1
fi

exercise_name="$1"
reduce_tasks="$2"

if [ "$exercise_name" == "ejemplo" ]; then
  display_name="Ejemplo"
else
  display_name="Ejercicio ${exercise_name##*[!0-9]}"
fi

hdfs dfs -test -e "$exercise_name/" && hdfs dfs -rm -r "$exercise_name/"

hdfs dfs -put "/MapReduce/$exercise_name/"

/usr/bin/hadoop \
  jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
  -D mapreduce.job.reduces="$reduce_tasks" \
  -input "$exercise_name/data/" \
  -output "$exercise_name/output/" \
  -mapper "$exercise_name/src/mapper.py" \
  -reducer "$exercise_name/src/reducer.py"

hdfs dfs -get "$exercise_name/output/"

cat "$exercise_name/output/part-*" >> "${exercise_name}_output.txt"
python "$exercise_name/src/parser.py"
rm "${exercise_name}_output.txt"

echo "$display_name completado con $reduce_tasks tareas de reducción en el directorio $exercise_name!"
