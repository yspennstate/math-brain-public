#!/bin/bash
# queue_coinp.sh - coin searches at biased inputs with fei_coinp (run on the Mac: bash queue_coinp.sh MODE SEED0 [WFILE]).
#   MODE hot   every base of hot_bases.txt (tags in hot_bases.tags) and the record's labels, at 14 biases
#   MODE lib   every gate with 7..13 inputs of keep5.txt and zoo_lib.txt, at 14 biases
# One job covers one base and one half of the bias list; it runs run_cp.sh, which writes one file per bias:
#   cp_<tag>_p<bias>_<seed>.txt in ~/fei_agent.
Q=~/fillq/queue
D=~/fei_agent
mode=${1:-hot}
s=${2:-7000}
W=${3:-W_run6.txt}
LOW="0.30 0.34375 0.381966 0.42 0.45 0.47 0.49"
HIGH="0.51 0.53 0.55 0.58 0.618034 0.65625 0.70"
cat > "$D/run_cp.sh" <<'EOF'
#!/bin/bash
# run_cp.sh tag m k seconds iters seed wfile init p1 p2 ...
cd ~/fei_agent || exit 1
tag=$1; m=$2; k=$3; sec=$4; it=$5; seed=$6; w=$7; init=$8; shift 8
for p in "$@"; do
  ./fei_coinp "$p" "$m" "$k" "$sec" "$seed" "cp_${tag}_p${p}_${seed}.txt" "$w" "$init" "$it" 0.01 0.00002
done
EOF
chmod +x "$D/run_cp.sh"
mk() {  # prefix tag m k seconds iters seed init half biases...
  local pre=$1 tag=$2 m=$3 k=$4 sec=$5 it=$6 seed=$7 init=$8 half=$9
  shift 9
  local f="$Q/${pre}_${tag}_${half}_${seed}.job"
  printf '#!/bin/bash\n# cores: 1\n# mem_mb: 80\ncd %s || exit 1\nexec nice -n 10 bash run_cp.sh %s %s %s %s %s %s %s %s %s\n' \
    "$D" "$tag" "$m" "$k" "$sec" "$it" "$seed" "$W" "$init" "$*" > "$f.tmp"
  chmod +x "$f.tmp" && mv "$f.tmp" "$f"
}
budget() {  # m -> sets sec, it
  if [ "$1" -le 10 ]; then sec=240; it=300000; elif [ "$1" -le 12 ]; then sec=400; it=150000; else sec=600; it=80000; fi
}
if [ "$mode" = hot ]; then
  i=-1
  while read -r m hx; do
    i=$((i+1)); s=$((s+1))
    tag=$(sed -n "$((i+1))p" "$D/hot_bases.tags")
    budget "$m"
    mk 30_agent_cp "$tag" "$m" 24 $sec $it $s "hex:hot_bases.txt:$i" lo $LOW
    mk 30_agent_cp "$tag" "$m" 24 $sec $it $s "hex:hot_bases.txt:$i" hi $HIGH
  done < "$D/hot_bases.txt"
  s=$((s+1))
  mk 30_agent_cp rec 9 24 240 300000 $s "lab:rec18.lab" lo $LOW
  mk 30_agent_cp rec 9 24 240 300000 $s "lab:rec18.lab" hi $HIGH
fi
if [ "$mode" = lib ]; then
  for lib in keep5 zoo_lib; do
    [ -f "$D/$lib.txt" ] || { echo "no $lib.txt"; continue; }
    i=-1
    while read -r n hx rest; do
      case "$n" in ''|\#*) continue;; esac
      i=$((i+1)); s=$((s+1))
      [ "$n" -ge 7 ] && [ "$n" -le 13 ] || continue
      budget "$n"
      mk 31_agent_cl "${lib}_${i}_n${n}" "$n" 24 $sec $it $s "hex:$lib.txt:$i" lo $LOW
      mk 31_agent_cl "${lib}_${i}_n${n}" "$n" 24 $sec $it $s "hex:$lib.txt:$i" hi $HIGH
    done < "$D/$lib.txt"
  done
fi
ls $Q | grep -c 'agent_c[pl]_'
