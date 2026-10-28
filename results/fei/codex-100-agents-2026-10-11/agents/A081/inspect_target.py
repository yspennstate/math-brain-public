from read_sources import BASE,SUP,CTX,RUN
import json
def scan(x):
    if isinstance(x,dict):
        if x.get('packet_id')=='A081' or x.get('agent_id')=='A081': print('ASSIGNMENT',json.dumps(x,indent=2))
        else:
            for v in x.values(): scan(v)
    elif isinstance(x,list):
        for v in x: scan(v)
scan(json.loads((BASE/'AGENT_ASSIGNMENTS.json').read_text(encoding='utf-8-sig')))
for path,ranges in [(SUP/'baseline/current-threshold-paper.tex',[(1790,1856),(2323,2447)]),(CTX/'percolation_spectral_pivotal_entropy_30pp.txt',[(1,220)]),(CTX/'threshold_paper_29pp_earlier_version.txt',[(1,140)]),(CTX/'percolation_spectral_pivotal_entropy_31pp_other_version.txt',[(1,150)])]:
    lines=path.read_text(encoding='utf-8-sig',errors='replace').splitlines()
    print('\nSOURCE',path)
    for a,b in ranges:
        for i in range(a-1,min(b,len(lines))): print(f'{i+1}: {lines[i]}')
