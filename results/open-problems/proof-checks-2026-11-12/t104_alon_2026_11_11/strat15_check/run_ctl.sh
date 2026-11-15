cd ~/agent_run/strat15_check_claude || exit 1
sed 's/p, used = residual(box, cert\[.lambda.\])/p, used = residual(box, {k: F(v)\/2 for k, v in list(cert["lambda"].items())[:1]})/' my_check1b.py > ctl_halflam.py
echo "control edits: $(grep -c 'list(cert' ctl_halflam.py)"
nice -n 15 python3 ctl_halflam.py ../STRAT15/domain_audit.json 20 11 | tail -1
nohup nice -n 15 python3 my_check1b.py ../STRAT15/domain_audit.json 100000 11 > check1b_full.out 2>&1 &
echo $! > full.pid; echo "full check pid $(cat full.pid)"
