"""Only named source pages and a few cited theorem lines are extracted."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
main=Path('~/Downloads/Probability_1000_20h_20260906/sources')
claude=Path('~/Downloads/Probability_1000_intake_claude_20260907/sources')
tasks=[
 ('P0189-brown',main/'rotation_brown_2012/text.txt',[r'12\s*\.\s*2',r'Haar\s+(?:measure|probability)',r'unique\s+trac'],[]),
 ('P0189-scope',main/'strong_convergence_2025/text.txt',[r'6\s*\.\s*9'],[69,70]),
 ('P0390',main/'arw_universality_2024/text.txt',[r'Question\s*28'],[15,16]),
 ('P0031',main/'burdzy_scheutzow_2014/text.txt',[r'Problem\s*7\s*\.\s*4'],[26]),
 ('C0011',claude/'biskup_dgff_extrema_2020/text.txt',[r'Problem\s*16\s*\.\s*11',r'Ray.Knight'],[]),
 ('C0070',claude/'heydenreich_hofstad_highd_2017/text.txt',[r'Open\s+Problem\s*13\s*\.\s*4',r'Hulshof'],[]),
 ('C0153',claude/'pete_pgg_notes/text.txt',[r'14\s*\.\s*19'],[]),
 ('C0100',claude/'levine_peres_sandpiles_2017/text.txt',[r'exactly\s+j',r'fraction\s+of\s+sites'],[27]),
]
rows=[]
for label,path,patterns,pages in tasks:
    content=path.read_text(encoding='utf-8-sig',errors='replace')
    excerpts=[]
    for pattern in patterns:
        matches=list(re.finditer(pattern,content,re.I))
        # Prefer actual text near the end to a contents-list match.
        for match in matches[-2:]:
            excerpts.append({'anchor':pattern,'text':content[max(0,match.start()-200):match.end()+1400]})
    for page in pages:
        pattern=r'===== PDF PAGE\s+'+str(page)+r'\s+=====(.*?)(?=\n===== PDF PAGE|\Z)'
        match=re.search(pattern,content,re.S)
        if match:
            excerpts.append({'anchor':'PDF page '+str(page),'text':match.group(1)[:5200]})
    row={'label':label,'path':path.as_posix(),'excerpts':excerpts}
    rows.append(row)
    print(label,'matches',len(excerpts))
    for excerpt in excerpts:
        if label in ['P0189-brown','C0011','C0070','C0153']:
            print(excerpt['anchor'],excerpt['text'][:1800])
(ROOT/'evidence/source_excerpts.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
