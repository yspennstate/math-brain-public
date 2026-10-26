"""Re-run the whole verification battery against the CURRENT engine.

The volume engine was given an integer fast path mid-session; this
re-runs every checker end to end so that no result rests on the
pre-optimisation build.  Prints one line per checker plus a final
summary.

Run:  python -u run_all.py
"""
import subprocess, sys, os, time

HERE = os.path.dirname(os.path.abspath(__file__))
ENGINE = os.path.join(HERE, "..", "engine")

CHECKERS = [
    "check_identities.py",
    "verify_order8.py",
    "verify_archived_data.py",
    "check_appendixA_completeness.py",
    "check_peeling.py",
    "check_ehrhart.py",
    "check_extension.py",
    "verify_new_results.py",
    "check_volumes_spot.py",
]

PASS_TOKENS = ("ALL IDENTITY CHECKS PASSED", "ORDER-8 CHECK PASSED",
               "ARCHIVED DATA CHECK PASSED", "COMPLETENESS CHECK PASSED",
               "ALL PEELING CHECKS PASSED", "ALL EHRHART/GORENSTEIN CHECKS PASSED",
               "EXTENSION CHECKS ALL PASS",
               "ALL NEW-RESULT CLAIMS INDEPENDENTLY VERIFIED",
               "ALL VOLUME SPOT CHECKS PASSED")

env = dict(os.environ)
env["PYTHONPATH"] = ENGINE
env["PYTHONIOENCODING"] = "utf-8"

results = []
for c in CHECKERS:
    path = os.path.join(HERE, c)
    if not os.path.exists(path):
        results.append((c, "MISSING", 0.0))
        print(f"MISSING  {c}", flush=True)
        continue
    t0 = time.time()
    p = subprocess.run([sys.executable, "-u", path], cwd=HERE, env=env,
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    dt = time.time() - t0
    out = (p.stdout or "") + (p.stderr or "")
    ok = any(tok in out for tok in PASS_TOKENS) and "FAIL" not in out.replace("FAILURES ***", "")
    if p.returncode != 0:
        ok = False
    verdict = "PASS" if ok else "CHECK"
    results.append((c, verdict, dt))
    print(f"{verdict:5s} {c:38s} {dt:7.1f}s", flush=True)
    if not ok:
        tail = [l for l in out.splitlines() if "FAIL" in l or "Error" in l][:3]
        for l in tail:
            print(f"        {l}", flush=True)

print()
npass = sum(1 for _, v, _ in results if v == "PASS")
print(f"BATTERY: {npass}/{len(results)} checkers pass on the current engine")
