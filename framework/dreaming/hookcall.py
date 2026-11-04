"""One way for an evaluator to call a hook process.

    from hookcall import run_hook, cap_for
    r = run_hook([sys.executable, hook], json.dumps({"prompt": q}), env)
    if r.timed_out: ...          # both tries ran past the cap: record the row as timed out, not as a miss
    r.stdout, r.stderr, r.returncode, r.attempts, r.seconds, r.cap

The cap follows the hook's own clock instead of a number fixed in each evaluator. A rehearsal may give the math hook
MATHBRAIN_TIME_BUDGET_S=300 and MATHBRAIN_INTEGRITY_GRACE_S=60; an evaluator with a fixed 90 or 180 s cap then kills slow
but legitimate calls on a loaded machine. Where the evaluator catches the timeout the row reads as a miss, and where it
does not the whole bench dies. The cap is the hook's budget plus its integrity grace plus a margin for interpreter start
and the store load, never under a floor. The defaults when the env says nothing are the math hook's: 30 s and 2 s for an
interactive prompt, and 50 s and 8 s for a prompt opening with the headless-worker marker (MATHBRAIN_HEADLESS_BUDGET_S,
MATHBRAIN_HEADLESS_GRACE_S).

A call past the cap is asked once more (a transient stall on a busy machine is the usual cause); when the second call also
runs past it the result says so, and the caller writes the row as timed out so a scorer can leave it out of both arms instead
of counting a miss.
"""
import os
import subprocess
import time

FLOOR_S = 90.0
MARGIN_S = 60.0
HEADLESS_MARKER = "[headless-worker]"


def _num(env, key, default):
    try:
        v = env.get(key)
        return float(v) if v not in (None, "") else float(default)
    except (TypeError, ValueError):
        return float(default)


def cap_for(env=None, prompt="", floor=FLOOR_S, margin=MARGIN_S):
    """Seconds an evaluator should wait for one hook call: budget + integrity grace + margin, at least `floor`."""
    env = os.environ if env is None else env
    headless = (prompt or "").lstrip().startswith(HEADLESS_MARKER)
    budget = _num(env, "MATHBRAIN_TIME_BUDGET_S",
                  max(30.0, _num(env, "MATHBRAIN_HEADLESS_BUDGET_S", 50)) if headless else 30.0)
    grace = _num(env, "MATHBRAIN_INTEGRITY_GRACE_S", _num(env, "MATHBRAIN_HEADLESS_GRACE_S", 8) if headless else 2.0)
    return max(float(floor), budget + grace + float(margin))


class HookRun:
    """What one hook call returned; stdout and stderr are empty strings when both tries timed out."""
    __slots__ = ("stdout", "stderr", "returncode", "timed_out", "attempts", "seconds", "cap")

    def __init__(self, stdout="", stderr="", returncode=None, timed_out=False, attempts=0, seconds=0.0, cap=0.0):
        self.stdout, self.stderr, self.returncode = stdout, stderr, returncode
        self.timed_out, self.attempts, self.seconds, self.cap = timed_out, attempts, seconds, cap

    @property
    def retried(self):
        return self.attempts > 1

    def row_fields(self):
        """The fields a result row should carry so a scorer can tell a timeout from a miss."""
        return {"timed_out": self.timed_out, "attempts": self.attempts, "seconds": round(self.seconds, 2)}


def run_hook(argv, input_text, env=None, cap=None, retries=1, cwd=None, prompt=None):
    """Run a hook process with `input_text` on stdin. `prompt` (optional) only decides the headless default of the cap."""
    env = dict(os.environ) if env is None else env
    if cap is None:
        cap = cap_for(env, prompt or "")
    t0 = time.time()
    attempts = 0
    for _ in range(1 + max(0, int(retries))):
        attempts += 1
        try:
            p = subprocess.run(argv, input=input_text, capture_output=True, text=True, encoding="utf-8",
                               errors="replace", timeout=cap, env=env, cwd=cwd,
                               creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        except subprocess.TimeoutExpired:
            continue
        return HookRun(p.stdout or "", p.stderr or "", p.returncode, False, attempts, time.time() - t0, cap)
    return HookRun("", "", None, True, attempts, time.time() - t0, cap)
