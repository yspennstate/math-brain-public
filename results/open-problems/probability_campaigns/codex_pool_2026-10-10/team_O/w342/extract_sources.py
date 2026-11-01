"""Bounded excerpts only, from the exact primary papers named in this packet."""
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parent
base=Path('~/Downloads')
old=base/'Probability_1000_20h_20260906/sources'
claude=base/'Probability_1000_intake_claude_20260907/sources'
jobs=[
 ('P0289',old/'queues_ross_second_2022/text.txt',r'Problem\s*1|necessary and sufficient'),
 ('C0035',claude/'lyons_determinantal_2014/text.txt',r'block.factor|Question\s*5\.?4'),
 ('P0001',old/'grimmett_2022_selected/text.txt',r'Conjecture\s*4\.?2|uniform forest'),
 ('P0133',old/'schramm_2006_v2/text.txt',r'Problem\s*6\.?2|homotopy'),
 ('C0002',claude/'biskup_dgff_extrema_2020/text.txt',r'Problem\s*16\.?2|rate of convergence'),
 ('C0059',claude/'curien_peeling_2019/text.txt',r'Let q be of type a.*2.*5/2'),
 ('C0083',claude/'heydenreich_hofstad_highd_2017/text.txt',r'Open Problem\s*15\.?10|a1\(d\)'),
 ('C0128',claude/'kosygina_zerner_erw_2012/text.txt',r'Problem\s*3\.?5|Theorem\s*3\.?10'),
 ('P0015',old/'randomstrasse_2025_v1/text.txt',r'Conjecture\s*19|4M.*5|phaseless'),
 ('P0044',old/'lyons_peres_20260819/text.txt',r'Question\s*10\.?6|Lyons and Thom'),
]
out=[]
for problem,path,pattern in jobs:
    regex=re.compile(pattern,re.IGNORECASE)
    ring=[]
    found=[]
    remaining=0
    with path.open(encoding='utf-8',errors='replace') as handle:
        for number,line in enumerate(handle,1):
            if remaining:
                found.append((number,line.rstrip()))
                remaining-=1
                if not remaining:
                    break
            elif regex.search(line):
                found.extend(ring[-3:])
                found.append((number,line.rstrip()))
                remaining=14
            ring.append((number,line.rstrip()))
            if len(ring)>3:
                ring.pop(0)
    record={'problem_id':problem,'path':str(path),'excerpts':found}
    out.append(record)
    print(json.dumps(record,ensure_ascii=False))
(ROOT/'source_excerpts.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
