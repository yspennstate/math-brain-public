"""Read only bounded excerpts around the cited primary-source locators."""
from pathlib import Path
import json
import re

here=Path(__file__).resolve().parent
campaign=Path("~/Downloads/Probability_1000_20h_20260906/sources")
intake=Path("~/Downloads/Probability_1000_intake_claude_20260907/sources")
requests=[
 ("P0193",campaign/"free_positive_unimodality_2020_correct/text.txt", [r"(?m)^Lemma\s+4\s*\.\s*1[.\s]"]),
 ("P0411",campaign/"ideal_voronoi_2023/text.txt", [r"(?m)^Proposition\s+5\s*\.\s*1[.\s]"]),
 ("C0072",intake/"heydenreich_hofstad_highd_2017/text.txt", [r"(?m)^Open\s+Problem\s+13\s*\.\s*6[.\s]"]),
 ("P0039",campaign/"lyons_peres_20260819/text.txt", [r"(?m)^Conjecture\s+6\s*\.\s*45[.\s]"]),
]
out=[]
for pid,path,patterns in requests:
    raw=path.read_bytes()
    if raw.startswith((b'\xff\xfe',b'\xfe\xff')):
        text=raw.decode("utf-16")
    else:
        text=raw.decode("utf-8-sig",errors="replace")
    lines=text.splitlines()
    # Some extracted PDFs are one paragraph per line; bound by characters.
    excerpts=[]
    for pattern in patterns:
        matches=list(re.finditer(pattern,text,re.I))
        for match in matches[:1]:
            left=max(0,match.start()-100)
            right=min(len(text),match.end()+2700)
            excerpts.append({"pattern":pattern,"character":match.start(),"text":text[left:right]})
    row={"problem_id":pid,"path":str(path),"bytes":len(raw),"characters":len(text),"excerpts":excerpts}
    if not excerpts:
        row["head"]=text[:800]
    out.append(row)
    print(json.dumps(row,ensure_ascii=False))
(here/"primary_source_excerpts.json").write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding="utf-8")
