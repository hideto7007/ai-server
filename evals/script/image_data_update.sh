#!/bin/bash

INPUT="../../evals/input/"
#OUTPUT="./evals/output"


echo 'バッチ実行'
#python ../image_data_update.py $INPUT
python ../../manage.py runscript image_data_update.py --script-args $INPUT

echo 'バッチ終了'
echo $?