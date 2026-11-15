set -e
D=~/agent_run/P0220
cd $D
export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH
CODEX=$(command -v codex)
F=$(memory_pressure -Q | tail -1 | tr -dc '0-9'); echo "P0220 referee: free $F pct"
if [ "$F" -lt 25 ]; then echo "memory gate closed, not launched"; exit 0; fi
if [ -f run.pid ] && kill -0 "$(cut -d' ' -f1 run.pid)" 2>/dev/null; then echo "already running"; exit 0; fi
test -s PROMPT.md && test -s PAPER.tex
echo "$(date '+%H:%M') start" >> codex.log
CODEX_HOME=$HOME/.codex-acc2 nohup nice -n 10 $CODEX exec --skip-git-repo-check -s workspace-write -c sandbox_workspace_write.network_access=true -m gpt-6.1-sol -c 'model_reasoning_effort="high"' -c 'service_tier="default"' -c features.fast_mode=false -c features.ultrafast_mode=false -C $D - < PROMPT.md >> codex.log 2>&1 &
echo "$! $(date '+%m-%d %H:%M')" > run.pid
cat run.pid
