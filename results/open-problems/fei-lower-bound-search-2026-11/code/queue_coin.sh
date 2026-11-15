#!/bin/bash
# queue_coin.sh - coin-affine searches with fei_coin (run on the Mac: bash queue_coin.sh MODE [SEED0]).
#   MODE rec   the record's neighbourhood and the bare K33 matching gate, several temperatures
#   MODE lib   every gate with 6..13 inputs of keep5.txt and zoo_lib.txt as the base, 24 coins free
# Output co_<tag>_<seed>.txt in ~/fei_agent.  Prefix 31: ahead of the gate searches.
Q=~/fillq/queue
D=~/fei_agent
W=W_run6.txt
mode=${1:-rec}
s=${2:-800}
mk() {  # tag m k seconds init iters T0 T1 seed
  local name="31_agent_co_$1_$9"
  local f="$Q/$name.job"
  printf '#!/bin/bash\n# cores: 1\n# mem_mb: 60\ncd %s || exit 1\nexec ./fei_coin %s %s %s %s co_%s_%s.txt %s %s %s %s %s 1 1.2 0.9\n' \
    "$D" "$2" "$3" "$4" "$9" "$1" "$9" "$W" "$5" "$6" "$7" "$8" > "$f.tmp"
  chmod +x "$f.tmp" && mv "$f.tmp" "$f"
}
if [ "$mode" = rec ]; then
  for T in 0.005 0.02 0.05; do
    for r in 1 2; do s=$((s+1)); mk rec 9 24 3600 lab:rec18.lab 5000000 $T 0.00002 $s; done
  done
  s=$((s+1)); mk k33 9 24 3600 hex:seed_k33.txt 5000000 0.01 0.00002 $s
  s=$((s+1)); mk k33 9 24 3600 hex:seed_k33.txt 5000000 0.03 0.00002 $s
fi
if [ "$mode" = lib ]; then
  for lib in keep5 zoo_lib; do
    [ -f "$D/$lib.txt" ] || { echo "no $lib.txt"; continue; }
    i=-1
    while read -r n hx rest; do
      case "$n" in ''|\#*) continue;; esac
      i=$((i+1))
      s=$((s+1))
      [ "$n" -ge 6 ] && [ "$n" -le 13 ] || continue
      if [ "$n" -le 10 ]; then sec=900; it=2000000; else sec=1500; it=1000000; fi
      mk "${lib}_${i}_n${n}" "$n" 24 $sec "hex:$lib.txt:$i" $it 0.01 0.00002 $s
    done < "$D/$lib.txt"
  done
fi
if [ "$mode" = big ]; then
  for lib in keep5 zoo_lib; do
    [ -f "$D/$lib.txt" ] || { echo "no $lib.txt"; continue; }
    i=-1
    while read -r n hx rest; do
      case "$n" in ''|\#*) continue;; esac
      i=$((i+1))
      s=$((s+1))
      [ "$n" -ge 14 ] && [ "$n" -le 16 ] || continue
      mk "${lib}_${i}_n${n}" "$n" 24 3600 "hex:$lib.txt:$i" 3000000 0.01 0.00002 $s
    done < "$D/$lib.txt"
  done
fi
ls $Q | grep -c 'agent_co_'
