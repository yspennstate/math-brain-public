"""Run the complete certificate with the cancellation-keeping enclosures, each part as its own process, and write a
summary.  Parts: lemmas, T2, T3 (fei_cert23, unchanged), region 1 and region 2 (fei_cert_r1x, the exact enclosures),
region 3 (fei_cert23, unchanged).  A part that prints no RESULTS line, prints False in it, or exits non-zero is not
counted as passing, and the summary's all_ok is the conjunction over all six.
usage: run_cert_all_x.py <npz> <c> <max_depth> <tag>"""
import subprocess, sys, os, time, json
here = os.path.dirname(os.path.abspath(__file__))
src, c, depth, tag = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
NOWIN = 0x08000000
PARTS = [
    ("lemmas", [sys.executable, "-X", "utf8", os.path.join(here, "fei_cert23.py"), src, c, depth, "lemmas"]),
    ("T2",     [sys.executable, "-X", "utf8", os.path.join(here, "fei_cert23.py"), src, c, depth, "T2"]),
    ("T3",     [sys.executable, "-X", "utf8", os.path.join(here, "fei_cert23.py"), src, c, depth, "T3"]),
    ("R1x",    [sys.executable, "-X", "utf8", os.path.join(here, "fei_cert_r1x.py"), src, c, depth]),
    ("R2x",    [sys.executable, "-X", "utf8", os.path.join(here, "run_r2x.py"), src, c, depth]),
    ("R3",     [sys.executable, "-X", "utf8", os.path.join(here, "fei_cert23.py"), src, c, depth, "R3"]),
]
summary = {}
for part, cmd in PARTS:
    out = os.path.join(here, "certx_%s_%s.out" % (tag, part))
    t0 = time.time()
    with open(out, "w", encoding="utf-8") as f:
        rc = subprocess.call(cmd, stdout=f, stderr=subprocess.STDOUT, cwd=here, creationflags=NOWIN)
    txt = open(out, encoding="utf-8", errors="replace").read()
    tail = txt.split("RESULTS")[-1] if "RESULTS" in txt else ""
    ok = bool(txt.count("RESULTS")) and ("False" not in tail) and rc == 0
    summary[part] = {"ok": bool(ok), "rc": rc, "seconds": round(time.time() - t0), "log": os.path.basename(out)}
    print("%-6s %s  rc=%d  %ds" % (part, "OK " if ok else "NOT", rc, summary[part]["seconds"]), flush=True)
    with open(os.path.join(here, "certx_%s_SUMMARY.json" % tag), "w", encoding="utf-8") as f:
        json.dump({"candidate": src, "c": float(c), "max_depth": int(depth), "parts": summary,
                   "all_ok": all(v["ok"] for v in summary.values()) and len(summary) == len(PARTS)}, f, indent=1)
allok = all(v["ok"] for v in summary.values()) and len(summary) == len(PARTS)
print(json.dumps(summary))
print("ALL SIX PARTS VERIFIED" if allok else "NOT all parts verified")
sys.exit(0 if allok else 1)
