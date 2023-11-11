#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Uso: $0 <nombre_directorio> <numero_tareas_reduccion>"
  exit 1
fi

exercise_name="$1"
reduce_tasks="$2"
input_dir="$exercise_name/data"
output_dir="$exercise_name/output"

if [ "$exercise_name" == "ejemplo" ]; then
  display_name="Ejemplo"
else
  display_name="Ejercicio ${exercise_name##*[!0-9]}"
fi

clean_hdfs_dir() {
  hdfs dfs -test -e "$1" && hdfs dfs -rm -r "$1"
}

clean_hdfs_dir "$input_dir"

clean_hdfs_dir "$output_dir"

hdfs dfs -put "$input_dir"

/usr/bin/hadoop \
  jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
  -D mapreduce.job.reduces="$reduce_tasks" \
  -input "$input_dir/" \
  -output "$output_dir/" \
  -mapper "$exercise_name/src/mapper.py" \
  -reducer "$exercise_name/src/reducer.py"

hdfs dfs -get "$output_dir"

cat "$output_dir/part-*" >> "${exercise_name}_output.txt"
python "$exercise_name/src/parser.py"
rm "${exercise_name}_output.txt"

echo "$display_name completado con $reduce_tasks tareas de reducción en el directorio $exercise_name!"
