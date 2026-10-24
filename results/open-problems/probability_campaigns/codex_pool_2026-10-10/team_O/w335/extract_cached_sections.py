import json
import pathlib
import re
import subprocess

root=pathlib.Path(__file__).resolve().parent
base=pathlib.Path('~/Downloads/probability_1000_intake_claude_20260907/sources')
requests=[('biskup_dgff_extrema_2020',r'Problem 16\.14|\(13\.13\)'),('heydenreich_hofstad_highd_2017',r'Open Problem 14\.1'),('chatterjee_chaos_2008',r'equivalent.*chaos|equivalent.*superconcentration|^12\.'),('tao_vu_littlewood_offord_2009',r'rate of convergence|convergence rate')]
sections=[]
for source_id,pattern in requests:
    path=base/source_id/'text.txt'
    matched=subprocess.run(['rg','-a','-n','-i','-m','3',pattern,str(path)],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=30)
    hits=[]
    for line in matched.stdout.split('\n'):
        found=re.match(r'^(\d+):',line)
        if found:
            hits.append(int(found.group(1)))
    if hits:
        # rg counts LF lines. PDF text contains other separators that Python's
        # splitlines treats as new lines and would shift quoted source windows.
        lines=path.read_text(encoding='utf-8',errors='replace').split('\n')
        for number in hits:
            assert re.search(pattern,lines[number-1],re.IGNORECASE), (source_id,number)
            fragment='\n'.join(lines[max(0,number-5):number+10]).replace('\x00','')
            sections.append({'source_id':source_id,'path':str(path),'match_line':number,'start_line':max(1,number-4),'match_verified':True,'matched_text':lines[number-1].replace('\x00',''),'text':fragment})
    else:
        sections.append({'source_id':source_id,'path':str(path),'no_match':True,'rg_status':matched.returncode,'stderr':matched.stderr})
(root/'cached_primary_sections.json').write_text(json.dumps(sections,ensure_ascii=False,indent=2),encoding='utf-8')
for section in sections:
    print(json.dumps(section,ensure_ascii=False),flush=True)
