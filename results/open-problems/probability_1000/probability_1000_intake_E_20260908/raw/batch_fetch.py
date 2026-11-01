import subprocess, sys, time, json
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
rows = [json.loads(l) for l in Path(sys.argv[1]).read_text(encoding='utf-8').splitlines() if l.strip() and not l.startswith('#')]
for r in rows:
    sid, aid, title = r
    out = HERE/"intake_tools.py"
    cmd = [sys.executable, str(out), "fetch", "--id", sid, "--url", f"https://arxiv.org/pdf/{aid}",
           "--kind", "pdf", "--title", title, "--access", f"arXiv {aid} (API listing, title-confirmed)"]
    p = subprocess.run(cmd, capture_output=True, text=True)
    print(sid, "->", (p.stdout or p.stderr).strip().splitlines()[-1] if (p.stdout or p.stderr).strip() else "??")
    time.sleep(3)
