"""Fetch a list of (id, url, kind, title, access) through intake_tools.fetch; log outcomes."""
import subprocess, sys, json, time
rows=[json.loads(l) for l in open(sys.argv[1],encoding="utf-8") if l.strip()]
for r in rows:
    cmd=[sys.executable,"intake_tools.py","fetch","--id",r["id"],"--url",r["url"],"--kind",r.get("kind","pdf"),"--title",r["title"],"--access",r.get("access","public web")]
    p=subprocess.run(cmd,capture_output=True,text=True)
    print(r["id"],"->",(p.stdout.strip().splitlines() or [""])[-1][:200], p.stderr.strip().splitlines()[-1][:120] if p.returncode else "")
    time.sleep(2.5)
