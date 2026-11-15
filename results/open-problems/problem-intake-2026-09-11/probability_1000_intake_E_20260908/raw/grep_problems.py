"""Find numbered open-problem/conjecture/question statements with their PDF page."""
import re, sys, json
from pathlib import Path
OUT = Path.home()/"Downloads"/"Probability_1000_intake_E_20260908"/"sources"
PAT = re.compile(r"^\s*((?:Open\s+)?(?:Problem|Conjecture|Question|Open Question|Open Problem|Challenge)\s*\.?\s*[0-9]+(?:\.[0-9]+)*\.?)", re.I|re.M)
def pages(t):
    parts = re.split(r"===== PDF PAGE (\d+) =====", t)
    out=[]
    for i in range(1,len(parts),2):
        out.append((int(parts[i]), parts[i+1]))
    return out
def scan(sid, ctx=0):
    t=(OUT/sid/"text.txt").read_text(encoding="utf-8",errors="replace")
    hits=[]
    for pg, body in pages(t):
        for m in PAT.finditer(body):
            snippet=" ".join(body[m.start():m.start()+ (600 if ctx else 160)].split())
            hits.append((pg, snippet))
    return hits
if __name__=="__main__":
    if len(sys.argv)>1 and sys.argv[1]!="ALL":
        for pg,s in scan(sys.argv[1], ctx=len(sys.argv)>2):
            print(f"[p{pg}] "+s.encode("ascii","replace").decode())
    else:
        for d in sorted(OUT.iterdir()):
            if d.is_dir():
                h=scan(d.name)
                print(f"{d.name}\t{len(h)}")
