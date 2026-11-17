"""The health check fails when the hook itself fails, whatever it printed (scheduled audit).

    python test_math_sense_healthcheck_exit.py [OLD_HEALTHCHECK.py]

A fake hook, selected with MATH_SENSE_HOOK, answers every row the way a healthy hook would: a block
naming every required title for a must-speak prompt, nothing for the rest. Each case then breaks one
thing - the exit status, the output, the time - and the health check must go red. H1 is the positive
control: the same fake with nothing broken must pass, or the other cases prove nothing. N1 (when the
pre-fix health check is given) runs H2 and H3 on it and shows both green, which is the finding.
"""
import json
import os
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
CHECK = os.path.join(HERE, "math_sense_healthcheck.py")
FAILS = []

FAKE = r'''
import json, os, sys, time
prompt = json.loads(sys.stdin.read() or "{}").get("prompt", "")
speak = prompt in json.load(open(os.environ["FAKE_SPEAK_FILE"], encoding="utf-8"))
mode = os.environ.get("FAKE_MODE", "")
if mode == "hang":
    time.sleep(30)
if speak:
    block = "[math-brain] fake block\n- Hoeffding, Turan and Sylow are all named here " + "x" * 150
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": block}}))
elif mode == "garbled":
    print("Traceback (most recent call last): not the hook protocol")
if mode == "noisy":
    sys.stderr.write("e" * 5000)
rc = int(os.environ.get("FAKE_RC", "0"))
if mode == "crash_silent_only":
    rc = 0 if speak else 7
sys.exit(rc)
'''


def check(name, ok, detail=""):
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, (": " + detail) if detail else ""))
    if not ok:
        FAILS.append(name)


def run(script, tmp, **env):
    e = dict(os.environ)
    e.update({"MATH_SENSE_HOOK": os.path.join(tmp, "fake_hook.py"),
              "FAKE_SPEAK_FILE": os.path.join(tmp, "speak.json")})
    e.update({k: str(v) for k, v in env.items()})
    t0 = time.time()
    r = subprocess.run([sys.executable, script], capture_output=True, text=True, env=e, timeout=300)
    return r.returncode, r.stdout + r.stderr, time.time() - t0


def main():
    sys.path.insert(0, HERE)
    import math_sense_healthcheck as hc
    with tempfile.TemporaryDirectory(prefix="hc_exit_") as tmp:
        with open(os.path.join(tmp, "fake_hook.py"), "w", encoding="utf-8") as fh:
            fh.write(FAKE)
        with open(os.path.join(tmp, "speak.json"), "w", encoding="utf-8") as fh:
            json.dump([entry[1] for entry in hc.MUST_SPEAK], fh)

        rc, out, _ = run(CHECK, tmp)
        check("H1 positive control: the fake with nothing broken passes", rc == 0, "rc %s" % rc)
        rc, out, _ = run(CHECK, tmp, FAKE_RC=7)
        check("H2 every row printed right but the hook exited 7: red", rc == 1 and "hook failed (exit 7" in out,
              "rc %s" % rc)
        rc, out, _ = run(CHECK, tmp, FAKE_MODE="crash_silent_only")
        check("H3 the hook crashed with no output on the silent rows only: red, not correct silence",
              rc == 1 and "where silence was required" in out and "hook failed (exit 7" in out, "rc %s" % rc)
        rc, out, _ = run(CHECK, tmp, FAKE_MODE="garbled")
        check("H4 exit 0 but output that is not the hook's JSON on a silent row: red",
              rc == 1 and "not the hook's JSON" in out, "rc %s" % rc)
        rc, out, dt = run(CHECK, tmp, FAKE_MODE="hang", MATH_SENSE_HEALTHCHECK_TIMEOUT=1)
        check("H5 a hung hook: red within one timeout, the later rows not asked",
              rc == 1 and "timed out after 1 s" in out and "not asked" in out and dt < 20, "rc %s, %.1f s" % (rc, dt))
        rc, out, _ = run(CHECK, tmp, FAKE_MODE="noisy", FAKE_RC=7)
        longest = max(len(line) for line in out.splitlines())
        check("H6 5,000 characters of stderr stay bounded in the report", rc == 1 and longest < 400,
              "longest line %d" % longest)

        if len(sys.argv) > 1:
            rc2, _, _ = run(sys.argv[1], tmp, FAKE_RC=7)
            rc3, _, _ = run(sys.argv[1], tmp, FAKE_MODE="crash_silent_only")
            check("N1 the health check before the fix calls both H2 and H3 healthy (the finding)",
                  rc2 == 0 and rc3 == 0, "rc %s and %s" % (rc2, rc3))
    print("%d failed" % len(FAILS))
    return 1 if FAILS else 0


if __name__ == "__main__":
    raise SystemExit(main())
