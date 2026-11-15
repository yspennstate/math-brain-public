#!/bin/zsh
# STRAT21 foreground Codex run, for heavy_lock_run.sh (the lock is held for exactly the run's life).
cd ~/agent_run/STRAT21 || exit 1
export PATH=/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin; export OMP_NUM_THREADS=1; export OPENBLAS_NUM_THREADS=1; export CODEX_HOME=$HOME/.codex-acc2
echo $$ > run.pid
/usr/local/bin/codex exec --skip-git-repo-check -s workspace-write -m gpt-6.1-sol -c model_reasoning_effort="high" -c service_tier="default" -c features.fast_mode=false -c features.ultrafast_mode=false -C "$HOME/agent_run/STRAT21" - < PROMPT.md > codex.log 2>&1
echo "exit $? $(date)" >> run.exit
