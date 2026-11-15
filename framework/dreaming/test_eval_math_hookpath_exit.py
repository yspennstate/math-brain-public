"""eval_math_hookpath scores a block only from a hook call that finished and exited 0 (account02/B07,
B07-R79-MATH-HOOKPATH-EVALUATOR-IGNORES-CHILD-EXIT-056, 30 Sep 2026).

    python test_eval_math_hookpath_exit.py [EVALUATOR_BEFORE_THE_FIX.py]

A fake hook prints a current-format card (or an old-format one, nothing, or garbage) and exits with the code asked
for. C23-C26 are the auditor's cases; P1-P3 add unreadable output, a double timeout and a launch error. N6 runs the
evaluator given on the command line and shows it scoring an exit-7 call exactly like an exit-0 one (the finding).
"""
import importlib.util
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
FAILS = []

FAKE = r'''
import json, os, sys, time
sys.stdin.read()
mode = os.environ.get("FAKE_MODE", "new")
new = ("[math-brain] leads, not verdicts - check each result's hypotheses.\n"
       "- Spectral theorem [theorem]: Every self-adjoint operator on a finite-dimensional space is diagonalizable.\n"
       "    (claim_" + "a" * 64 + " | theorem; draft; unreviewed; unverified)\n")
old = ("[math-brain] the math brain holds material that may bear on this - a hint, not a verdict.\n"
       "- Spectral theorem [theorem, score 12.5]: Every self-adjoint operator on a finite-dimensional space is ...\n"
       "    (source-id: claim_" + "b" * 64 + ")\n"
       "    (hint: unverified)\n")
if mode == "sleep":
    time.sleep(float(os.environ.get("FAKE_SLEEP", "3")))
if mode == "garbage":
    sys.stdout.write("Traceback (most recent call last): not the hook's JSON")
elif mode != "silent":
    sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit",
                                                         "additionalContext": old if mode == "old" else new}}))
sys.stdout.flush()
sys.exit(int(os.environ.get("FAKE_RC", "0")))
'''


def check(name, ok, detail=""):
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, (": " + str(detail)[:300]) if detail else ""))
    if not ok:
        FAILS.append(name)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def row(mod, kind, form, env, stems=("spectral",)):
    """One scored row, the way the evaluator's run() makes it."""
    r = mod.ask("what does the spectral theorem say", env)
    r.update({"kind": kind, "key": "k", "area": "a", "form": form, "prompt_chars": 30})
    if kind == "answerable":
        r["hit"] = mod.stem_hit(r["titles"], list(stems))
        r["rank1"] = bool(r["titles"]) and mod.stem_hit(r["titles"][:1], list(stems))
    else:
        r["target_served"] = bool(r["titles"]) and mod.stem_hit(r["titles"], ["pinsker"])
    return r


def main():
    tmp = tempfile.mkdtemp(prefix="emh_exit_")
    fake = os.path.join(tmp, "fake_hook.py")
    with open(fake, "w", encoding="utf-8") as fh:
        fh.write(FAKE)
    new = load(os.path.join(HERE, "eval_math_hookpath.py"), "emh_new")
    new.HOOK = fake
    ok0 = new.ask("q", {"FAKE_RC": "0"})
    bad7 = new.ask("q", {"FAKE_RC": "7"})
    check("C24 exit 0 with a current-format card is scored: its title and id are read",
          ok0["titles"] == ["Spectral theorem"] and ok0["ids"] == ["claim_" + "a" * 64] and new.valid(ok0)
          and ok0.get("hook_rc") == 0, ok0)
    check("C23 the same output with exit 7 is invalid, its content is not scored, and the exit code is kept",
          bad7["titles"] == [] and bad7["ids"] == [] and not new.valid(bad7) and bad7.get("invalid") == "hook exited 7"
          and bad7.get("hook_rc") == 7, bad7)
    old0 = new.ask("q", {"FAKE_MODE": "old"})
    check("C25 the evaluator reads blocks with the shared parser (no private pattern left) and reads the old format too",
          not hasattr(new, "TITLE_RE") and not hasattr(new, "SRC_RE") and old0["titles"] == ["Spectral theorem"]
          and old0["ids"] == ["claim_" + "b" * 64], old0)
    garbage = new.ask("q", {"FAKE_MODE": "garbage"})
    check("P1 output that is not the hook's JSON is invalid, not silence",
          not new.valid(garbage) and "not the hook's JSON" in garbage.get("invalid", ""), garbage)
    silent = new.ask("q", {"FAKE_MODE": "silent"})
    check("P1b a hook that prints nothing and exits 0 is a valid silence", new.valid(silent) and silent["titles"] == [],
          silent)
    saved_timeout = new.CALL_TIMEOUT_S
    new.CALL_TIMEOUT_S = 1
    slow = new.ask("q", {"FAKE_MODE": "sleep", "FAKE_SLEEP": "3"})
    new.CALL_TIMEOUT_S = saved_timeout
    check("P2 a call that times out twice is marked and not scored", slow.get("timed_out") and not new.valid(slow), slow)
    saved_call = new._call

    def boom(prompt, e):
        raise OSError("no interpreter")
    new._call = boom
    launch = new.ask("q", {})
    new._call = saved_call
    check("P3 a launch error is invalid and named", not new.valid(launch) and launch.get("invalid", "").startswith(
        "launch error"), launch)
    rows = [row(new, "answerable", "q_content", {"FAKE_RC": "0"}),
            row(new, "answerable", "q_content", {"FAKE_RC": "7"}),
            row(new, "answerable", "q_hinted", {"FAKE_RC": "0"}),
            row(new, "unanswerable", "q", {"FAKE_RC": "7"}),
            row(new, "unanswerable", "q", {"FAKE_MODE": "silent"})]
    summary, lines = new.summarize(rows, {}, "bank.json")
    qc, un = summary["q_content"], summary["unanswerable"]
    check("C26 rates are over the scored rows only; the invalid rows are counted apart and fire nothing",
          qc == {"n": 1, "hit": 1, "rank1": 1, "silent": 0, "not_scored": 1}
          and un["n"] == 1 and un["false_fire"] == 0 and un["not_scored"] == 1 and summary["invalid"] == 2
          and summary["invalid_reasons"] == {"hook exited 7": 2}
          and any("not delivered whole: 2" in x for x in lines), summary)
    if len(sys.argv) > 1:
        old = load(sys.argv[1], "emh_old")
        old.HOOK = fake
        o0, o7 = old.ask("q", {"FAKE_RC": "0"}), old.ask("q", {"FAKE_RC": "7"})
        og = old.ask("q", {"FAKE_MODE": "garbage"})
        check("N6 the evaluator before the fix reads exit 7 exactly as exit 0, and garbage as silence (the finding)",
              o0["titles"] == o7["titles"] == ["Spectral theorem"] and o0["ids"] == o7["ids"] and og["titles"] == []
              and "invalid" not in o7, (o0, o7))
    print("%d failed" % len(FAILS))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
