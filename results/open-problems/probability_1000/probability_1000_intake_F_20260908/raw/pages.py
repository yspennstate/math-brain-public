import re, sys
sys.stdout.reconfigure(encoding="utf-8")
sid=sys.argv[1]; want=sys.argv[2:]
t=open(f"~/Downloads/Probability_1000_intake_F_20260908/sources/{sid}/text.txt",encoding="utf-8").read()
parts=re.split(r"===== PDF PAGE (\d+) =====",t)
pages={int(parts[i]):parts[i+1] for i in range(1,len(parts),2)}
for w in want:
    if "-" in w: a,b=map(int,w.split("-")); rng=range(a,b+1)
    else: rng=[int(w)]
    for p in rng:
        print(f"\n=== PAGE {p} ===\n"+pages.get(p,""))
