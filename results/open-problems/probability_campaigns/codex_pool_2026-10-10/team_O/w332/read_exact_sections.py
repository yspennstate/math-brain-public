from pathlib import Path
import json
import re

root=Path(__file__).resolve().parent
downloads=Path('~/Downloads')
intake=downloads/'Probability_1000_intake_claude_20260907/sources'
campaign=downloads/'Probability_1000_20h_20260906/sources'
jobs=[
 (intake/'levine_peres_sandpiles_2017/text.txt',r'Γ|integer superharmonic matrices|maximal elements',8,6),
 (intake/'heydenreich_hofstad_highd_2017/text.txt',r'Open Problem 13\.2',15,1),
 (intake/'biskup_dgff_extrema_2020/text.txt',r'Problem 16\.10 \(',8,1),
 (intake/'pete_pgg_notes/text.txt',r'Question 14\.3',8,1),
 (campaign/'free_unimodality_2018/text.txt',r'Lemma 3\.1|Problem 3\.3|Example 2\.1|Dµ :=|diameter',15,4),
 (campaign/'arw_universality_2024/text.txt',r'Conjecture 27',10,1),
 (campaign/'basdevant_coloring_2023/text.txt',r'Question 1\.4',10,1),
 (campaign/'burdzy_scheutzow_2014/text.txt',r'Problem 7\.[123]',6,3),
 (campaign/'burdzy_open_20260906/text.txt',r'percolation dimension|Jordan arcs',2,2)
]
receipts=[]
for path,pattern,after,limit in jobs:
    info={'path':str(path),'matches':[]}
    if not path.is_file():
        info['availability']='missing';print('MISSING',path);receipts.append(info);continue
    regex=re.compile(pattern)
    remaining=0
    for lineno,line in enumerate(path.open(encoding='utf-8-sig',errors='replace'),1):
        match=regex.search(line)
        if match and len(info['matches'])<limit:
            selection=line[max(0,match.start()-150):match.end()+450] if len(line)>1200 else line
            info['matches'].append({'line':lineno,'text':selection})
            print('MATCH',path.parent.name,lineno,selection.strip());remaining=after
        elif remaining:
            info['matches'][-1]['text']+=line
            print('AFTER',lineno,line[:300].strip());remaining-=1
    receipts.append(info)
(root/'reports/exact_primary_sections.json').write_text(json.dumps(receipts,indent=2,ensure_ascii=False),encoding='utf-8')
print('SAVED',len(receipts),'targeted source receipts')
