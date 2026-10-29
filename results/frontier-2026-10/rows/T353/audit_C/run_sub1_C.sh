#!/bin/sh
# T353 sub-1 audit 2 (agent C): all nine PQ certificates + QP spot checks of the duality J_PQ(al) = J_QP(1-al).
for o in 1/4 1/2 3/4; do
  python -X utf8 sub1_cert_C.py 1 $o PQ -2.3 -2.2 400
  python -X utf8 sub1_cert_C.py 2 $o PQ -3.05 -2.95 400
  python -X utf8 sub1_cert_C.py 0.5 $o PQ -2.250001 -2.249999 40
done
python -X utf8 sub1_cert_C.py 1 3/4 QP -2.3 -2.2 400
python -X utf8 sub1_cert_C.py 1 1/4 QP -2.3 -2.2 400
echo done
