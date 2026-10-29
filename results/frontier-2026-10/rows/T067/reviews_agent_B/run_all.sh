cd (local dir)
for a in "76 5/43 16" "79 31/272 16" "83 35/313 66" "88 37/339 19" "90 529999/5000000 11"; do
  set -- $a; e=$(echo $2 | tr / -)
  (timeout 7200 python -X utf8 uf_engine.py $1 $2 $3 interleave 96 32 run_d$1_$e.json > run_d$1.log 2>&1) &
done
wait
