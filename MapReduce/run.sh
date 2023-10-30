#!/bin/bash

# Verificar si se proporcionan los argumentos requeridos
if [ $# -ne 2 ]; then
  echo "Uso: $0 <nombre_directorio> <numero_tareas_reduccion>"
  exit 1
fi

# Variables
exercise_name="$1"
reduce_tasks="$2"
input_dir="$exercise_name/data"
output_dir="$exercise_name/output"

# Determine el nombre de visualización en función del argumento proporcionado
if [ "$exercise_name" == "ejemplo" ]; then
  display_name="Ejemplo"
else
  display_name="Ejercicio ${exercise_name##*[!0-9]}"
fi

# Funciones
remove_hdfs_dir() {
  hdfs dfs -test -e "$1" && hdfs dfs -rm -r "$1"
}

# Eliminar datos si ya existen
remove_hdfs_dir "$output_dir"

# Eliminar el directorio de salida si ya existe
remove_hdfs_dir "$input_dir"

# Colocar los datos del ejercicio en el sistema de archivos distribuido
hdfs dfs -put "$exercise_name/data"

# Ejecutar el trabajo de MapReduce
/usr/bin/hadoop \
    jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar \
    -D mapreduce.job.reduces="$reduce_tasks" \
    -input "$input_dir/" \
    -output "$output_dir/" \
    -mapper "$exercise_name/src/mapper.py" \
    -reducer "$exercise_name/src/reducer.py"

# Subir la carpeta de salida
hdfs dfs -get "$output_dir"

# Combinar y mostrar los resultados
cat "$output_dir/part-*" >> "$exercise_name_results.txt"
python "$exercise_name/src/combiner.py"
rm "$exercise_name_results.txt"

echo "$display_name completado con $reduce_tasks tareas de reducción en el directorio $exercise_name!"
