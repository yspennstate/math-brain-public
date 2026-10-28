#!/usr/bin/env python3
"""lean_check.py - machine-check a mathematical step with Lean 4 + Mathlib, one command, from any agent runtime.

    python lean_check.py --stmt "example (x : Real) (hx : 0 <= x) : Real.exp (-x) <= 1 / (1 + x) := by nlinarith [Real.add_one_le_exp x]"
    python lean_check.py --file Step.lean          (a whole file; add your own imports)
    python lean_check.py --selftest                (a true step must PASS, a false step must FAIL)

Prints PASS or FAIL plus Lean's own messages and the seconds it took. Exit 0 on PASS, 1 on FAIL, 2 on a broken setup.
A FAIL is evidence about the STEP only when the statement was formalised faithfully; an "unsolved goals" on a true
statement means the tactic was too weak (try nlinarith with the needed facts as hints, gcongr, positivity,
field_simp, exact?), not that the mathematics is wrong. A PASS is a proof.

Setup (verified 2026-09-07): toolchain <HOME>/.elan/bin (not on PATH); the BUILT Mathlib project is
<HOME>/phase_retrieval_omega/lean/omega_comb (Lean 4.29.1). `import Mathlib` costs about five minutes cold;
--stmt uses narrow imports (Mathlib.Tactic + the analysis/probability basics) and checks in about 30 s. The check
runs BelowNormal and never touches the project's own files: the temp file lives in your scratch directory.
"""
import argparse, io, os, subprocess, sys, tempfile, time

LEAN = r"<HOME>\.elan\bin\lean.exe"
LAKE = r"<HOME>\.elan\bin\lake.exe"
PROJECT = r"<HOME>\phase_retrieval_omega\lean\omega_comb"
IMPORTS = ("import Mathlib.Tactic\nimport Mathlib.Analysis.SpecialFunctions.Exp\nimport Mathlib.Analysis.SpecialFunctions.Log.Basic\n"
           "import Mathlib.Probability.Independence.Basic\nimport Mathlib.MeasureTheory.Integral.Bochner.Basic\n")


def run_file(path, timeout=900):
    if not (os.path.exists(LEAN) and os.path.exists(LAKE) and os.path.isdir(PROJECT)):
        return 2, "lean setup missing (LEAN/LAKE/PROJECT paths)", 0.0
    t0 = time.time()
    try:
        proc = subprocess.Popen([LAKE, "env", LEAN, path], cwd=PROJECT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                text=True, encoding="utf-8", errors="replace")
        try:
            import psutil; psutil.Process(proc.pid).nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        except Exception:
            pass
        out, _ = proc.communicate(timeout=timeout)
        rc = proc.returncode
    except subprocess.TimeoutExpired:
        subprocess.run(["taskkill", "/F", "/T", "/PID", str(proc.pid)], capture_output=True)
        return 2, "TIMEOUT after %ds" % timeout, time.time() - t0
    return (0 if rc == 0 and "error" not in out.lower() else 1), out, time.time() - t0


def check_stmt(stmt, imports=IMPORTS):
    d = os.environ.get("LEAN_CHECK_DIR") or os.path.join(tempfile.gettempdir(), "lean_check")
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, "Check_%d.lean" % int(time.time() * 1000))
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(imports + "\n" + stmt.strip() + "\n")
    return run_file(p)


def selftest():
    true_stmt = "example (x : ℝ) (hx : 0 ≤ x) : Real.exp (-x) ≤ 1 / (1 + x) := by\n  rw [Real.exp_neg, inv_eq_one_div, div_le_div_iff₀ (Real.exp_pos x) (by linarith)]\n  nlinarith [Real.add_one_le_exp x]\nexample : (2:ℝ)^3 = 8 := by norm_num"
    false_stmt = "example : (2:ℝ)^3 = 9 := by norm_num\nexample (x : ℝ) (hx : 0 < x) : 1 / (1 + x) ≤ Real.exp (-x) := by\n  nlinarith [Real.add_one_le_exp x]"
    rc1, out1, t1 = check_stmt(true_stmt)
    rc2, out2, t2 = check_stmt(false_stmt)
    ok = (rc1 == 0) and (rc2 == 1)
    print("true step  -> %s in %.0fs" % ("PASS" if rc1 == 0 else "FAIL", t1))
    print("false step -> %s in %.0fs (%s)" % ("FAIL" if rc2 == 1 else "PASS", t2, (out2.strip().splitlines() or [""])[0][:120]))
    print("lean_check selftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stmt"); ap.add_argument("--file"); ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--full-mathlib", action="store_true", help="use `import Mathlib` (about five minutes cold)")
    a = ap.parse_args()
    if a.selftest:
        raise SystemExit(selftest())
    if a.file:
        rc, out, dt = run_file(a.file)
    elif a.stmt:
        rc, out, dt = check_stmt(a.stmt, imports="import Mathlib\n" if a.full_mathlib else IMPORTS)
    else:
        print(__doc__); raise SystemExit(2)
    print("PASS" if rc == 0 else ("FAIL" if rc == 1 else "SETUP"), "in %.0fs" % dt)
    if out.strip():
        print(out.strip()[:4000])
    raise SystemExit(rc)


if __name__ == "__main__":
    main()
