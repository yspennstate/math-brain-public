#!/bin/bash
# queue_batch3.sh - Bellman-step gate search on a Mac mini (run there: bash queue_batch3.sh WFILE).
# Each job maximises (G_p(F) + W(p')) / J_p(F) over monotone F on k inputs at a fixed real bias p, with W read from
# WFILE (written by tower_vi.py --dump).  A value above W(p) is a gate that improves the tower at that bias.
# Output ~/fei_agent/bw_k<k>_<tag>_<seed>.txt, one line per run; prefix 35 so these run before the 40/45/50 jobs.
W=${1:-W_run2.txt}
Q=~/fillq/queue
D=~/fei_agent
s=${2:-300}
mk() {  # k tag p iters
  s=$((s+1))
  local name="35_agent_bw_k$1_$2_$s"
  local f="$Q/$name.job"
  printf '#!/bin/bash\n# cores: 1\n# mem_mb: 60\ncd %s || exit 1\nexec ./fei_bias %s 1 1 1 1 3600 %s bw_k%s_%s_%s.txt %s 0.05 0.0005 0 0 0 0 1 1 %s %s\n' \
    "$D" "$1" "$s" "$1" "$2" "$s" "$4" "$W" "$3" > "$f.tmp"
  chmod +x "$f.tmp" && mv "$f.tmp" "$f"
}
for k in ${3:-8 10 12 14}; do
  it=300000; [ $k -ge 12 ] && it=1000000; [ $k -ge 14 ] && it=2000000
  mk $k half 0.5 $it
  mk $k entry 0.34375 $it
  mk $k gold 0.381966011250105 $it
  mk $k goldc 0.618033988749895 $it
done
ls "$Q" | grep -c 35_agent_bw
