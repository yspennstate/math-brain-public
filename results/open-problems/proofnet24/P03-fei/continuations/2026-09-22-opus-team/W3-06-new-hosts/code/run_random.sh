#!/bin/bash
# runs the random-host families one at a time
for spec in "grid:3:3 400 1" "grid:3:4 400 2" "grid:2:5 200 3" "lin:11:5:9 300 4" "lin:12:5:10 300 5" "lin:13:5:11 300 6" "hyp:12:4:8:16 300 7" "hyp:11:3:5:9 300 8" "grid:4:4 60 9" "lin:15:6:12 80 10"; do
  set -- $spec
  timeout 600 python random_hosts.py $1 $2 $3
done
