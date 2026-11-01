"""run the complete certificate for one candidate and margin, each part as its own process (so a crash in one part
does not lose the others), and write a summary.  usage: run_cert_all.py <npz> <c> <max_depth> <tag>"""
import subprocess, sys, os, time, json
here = os.path.dirname(os.path.abspath(__file__))
src, c, depth, tag = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
NOWIN = 0x08000000
parts = ["lemmas", "T2", "T3", "R1", "R2", "R3"]
summary = {}
for part in parts:
    out = os.path.join(here, "cert_%s_%s.out" % (tag, part))
    t0 = time.time()
    with open(out, "w", encoding="utf-8") as f:
        rc = subprocess.call([sys.executable, "-X", "utf8", os.path.join(here, "fei_cert23.py"), src, c, depth, part], stdout=f, stderr=subprocess.STDOUT, cwd=here, creationflags=NOWIN)
    txt = open(out, encoding="utf-8", errors="replace").read()
    ok = ("RESULTS" in txt) and ("False" not in txt.split("RESULTS")[-1]) and rc == 0
    summary[part] = {"ok": bool(ok), "rc": rc, "seconds": round(time.time() - t0)}
    with open(os.path.join(here, "cert_%s_SUMMARY.json" % tag), "w", encoding="utf-8") as f:
        json.dump({"candidate": src, "c": float(c), "parts": summary, "all_ok": all(v["ok"] for v in summary.values()) and len(summary) == len(parts)}, f, indent=1)
print(json.dumps(summary))
