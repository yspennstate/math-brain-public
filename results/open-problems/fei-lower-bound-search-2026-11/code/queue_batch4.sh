#!/bin/bash
# queue_batch4.sh - seeded Bellman-step gate searches (run on the Mac: bash queue_batch4.sh WFILE [SEED0]).
# Each job starts fei_bias from a structured gate on its low inputs plus free extra inputs, at a fixed bias p, and
# maximises (G_p(F) + W(p')) / J_p(F) with W from WFILE.  Seeds are files seed_<name>.txt ("n0 hex") in ~/fei_agent.
# Output bs_<name>_k<k>_p<tag>_<seed>.txt.  Prefix 33: these go ahead of the unseeded 35_ searches.
W=${1:-W_run2.txt}
Q=~/fillq/queue
D=~/fei_agent
s=${2:-500}
mk() {  # name k ptag p iters T0 T1 seconds mem
  s=$((s+1))
  [ -f "$D/seed_$1.txt" ] || { echo "no seed_$1.txt"; return; }
  local name="33_agent_bs_$1_k$2_p$3_$s"
  local f="$Q/$name.job"
  printf '#!/bin/bash\n# cores: 1\n# mem_mb: %s\ncd %s || exit 1\nexec ./fei_bias %s 1 1 1 1 %s %s bs_%s_k%s_p%s_%s.txt %s %s %s 0 0 0 0 1 1 %s %s seed_%s.txt\n' \
    "$9" "$D" "$2" "$8" "$s" "$1" "$2" "$3" "$s" "$5" "$6" "$7" "$W" "$4" "$1" > "$f.tmp"
  chmod +x "$f.tmp" && mv "$f.tmp" "$f"
}
# the 18-input record at p = 1/2, cold and warm
mk rec18 18 half 0.5 600000 0.000003 0.00000003 7200 80
mk rec18 18 half 0.5 600000 0.00003 0.0000003 7200 80
# the nine-edge matching gate with free inputs, at 1/2 and at the biases where it comes closest
for k in 12 14; do
  mk k33 $k half 0.5 400000 0.0003 0.000003 5400 60
  mk k33 $k 55 0.55 400000 0.0003 0.000003 5400 60
  mk k33 $k 45 0.45 400000 0.0003 0.000003 5400 60
done
mk k33 16 half 0.5 500000 0.0001 0.000001 7200 70
mk k33 16 55 0.55 500000 0.0001 0.000001 7200 70
# other matching gates
mk cube 14 57 0.57 400000 0.0003 0.000003 5400 60
mk cube 16 57 0.57 500000 0.0001 0.000001 7200 70
mk cube 14 half 0.5 400000 0.0003 0.000003 5400 60
mk octa 14 46 0.46 400000 0.0003 0.000003 5400 60
mk octa 14 half 0.5 400000 0.0003 0.000003 5400 60
mk k44 18 45 0.45 600000 0.00003 0.0000003 7200 80
mk k44 16 45 0.45 500000 0.0001 0.000001 7200 70
mk pmk4 12 58 0.58 400000 0.0003 0.000003 5400 60
mk pmk4 12 half 0.5 400000 0.0003 0.000003 5400 60
# the five-input entry gate and the two-input gate at the golden bias, with free inputs
for k in 10 12 14; do
  mk entry5 $k half 0.5 400000 0.0005 0.000005 5400 60
  mk nor2 $k gold 0.381966011250105 400000 0.0005 0.000005 5400 60
  mk nand2 $k goldc 0.618033988749895 400000 0.0005 0.000005 5400 60
  mk entry5 $k entry 0.34375 400000 0.0005 0.000005 5400 60
done
ls "$Q" | grep -c 33_agent_bs
