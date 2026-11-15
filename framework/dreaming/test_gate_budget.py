"""The gate's run() keeps inside the run's budget. Loads the gate from this folder (its STATE is this folder's state/,
so nothing here touches the real history) and drives run() directly; no stage, no mesh."""
import importlib.util
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "~/.claude/dreaming")   # the gate imports siblings from the live folder
spec =importlib.util.spec_from_file_location("gate_under_test", os.path.join(HERE, "math_brain_regression_gate.py"))
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)
assert gate.STATE.startswith(HERE), gate.STATE
PY = sys.executable
SLEEP = [PY, "-c", "import time; time.sleep(60)"]
fails = []


def check(ok, what):
    print(("PASS " if ok else "FAIL ") + what)
    if not ok:
        fails.append(what)


# no budget set (t0 None): behaves as before
gate._GATE.update(t0=None, skipped=[])
rc, out, err, dt = gate.run([PY, "-c", "print('hello')"], 30)
check(rc == 0 and out.strip() == "hello", "no budget: a stage runs as before (rc %s)" % rc)

# 8 s left in the budget: a 60 s child under a 600 s stage cap is stopped near 8 s
gate._GATE.update(t0=time.time() - (gate.GATE_BUDGET_S - gate.ROW_RESERVE_S - 8), skipped=[])
t0 = time.time()
rc, out, err, dt = gate.run(SLEEP, 600)
took = time.time() - t0
check(rc == 124 and 5 <= took <= 20, "8 s left: the stage is cut at the budget (rc %s after %.1f s)" % (rc, took))
check(gate._GATE["skipped"] == [], "a cut stage is a timeout, not a skip")

# nothing left: the stage is skipped at once and named
gate._GATE.update(t0=time.time() - gate.GATE_BUDGET_S, skipped=[])
t0 = time.time()
rc, out, err, dt = gate.run([PY, os.path.join(HERE, "eval_value_in_block.py"), "--x"], 900)
took = time.time() - t0
check(rc == 124 and took < 2 and "SKIPPED" in err, "no time left: skipped at once (rc %s in %.2f s)" % (rc, took))
check(gate._GATE["skipped"] == ["eval_value_in_block.py"], "the skipped stage is named: %s" % gate._GATE["skipped"])

print("FAILED %d" % len(fails) if fails else "ALL PASS")
sys.exit(1 if fails else 0)
