import re, sys
from pathlib import Path
OUT = Path.home()/"Downloads"/"Probability_1000_intake_E_20260908"/"sources"
PAT = re.compile(r"(?:^|\n)\s*(\(?(?:Open\s+)?(?:Problem|Conjecture|Question|Challenge)\s*\.?\s*(?:[0-9]+(?:\.[0-9]+)*|[A-Z])?\)?\s*[.:)]?)(?=[\s(\[]|$)", re.I)
def pages(t):
    parts = re.split(r"===== PDF PAGE (\d+) =====", t)
    return [(int(parts[i]), parts[i+1]) for i in range(1,len(parts),2)]
def scan(sid, n=200):
    t=(OUT/sid/"text.txt").read_text(encoding="utf-8",errors="replace")
    hits=[]
    for pg, body in pages(t):
        for m in PAT.finditer(body):
            hits.append((pg, " ".join(body[m.start():m.start()+n].split())))
    return hits
if __name__=="__main__":
    a=sys.argv[1]
    if a=="ALL":
        for d in sorted(OUT.iterdir()):
            if d.is_dir(): print(f"{d.name}\t{len(scan(d.name))}")
    else:
        n=int(sys.argv[2]) if len(sys.argv)>2 else 200
        for pg,s in scan(a,n): print(f"[p{pg}] "+s.encode("ascii","replace").decode())
