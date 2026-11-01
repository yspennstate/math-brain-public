import json, glob, os, sys
root = r'~/brain_workers/FEI100_20261011/agents'
out = []
for cj in sorted(glob.glob(root + '/*/runs/*/CLAIMS.json')):
    p = cj.replace(os.sep, '/')
    agent = p.split('/')[-4]
    run = p.split('/')[-2]
    try:
        d = json.load(open(cj, encoding='utf-8-sig'))
    except Exception as e:
        out.append((agent, run, 'PARSE_ERROR', str(e)[:100], '')); continue
    claims = d if isinstance(d, list) else d.get('claims', d.get('Claims', []))
    if isinstance(claims, dict): claims = [claims]
    for c in claims:
        if not isinstance(c, dict): continue
        out.append((agent, run[:40], str(c.get('status')), str(c.get('claim_id')), str(c.get('exact_statement'))[:420].replace('\n',' ')))
with open(sys.argv[1], 'w', encoding='utf-8') as f:
    for r in out:
        f.write(' | '.join(r) + '\n')
from collections import Counter
print(len(out), 'claims;', Counter(r[2] for r in out))
