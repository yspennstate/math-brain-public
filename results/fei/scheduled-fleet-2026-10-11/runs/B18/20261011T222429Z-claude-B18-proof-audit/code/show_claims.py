import json, glob, os, sys
root = r'~/brain_workers/FEI100_20261011/agents'
want = set(sys.argv[1].split(','))
maxlen = int(sys.argv[2]) if len(sys.argv) > 2 else 1800
seen = set()
for cj in sorted(glob.glob(root + '/*/runs/*/CLAIMS.json')):
    p = cj.replace(os.sep, '/')
    agent = p.split('/')[-4]
    try:
        d = json.load(open(cj, encoding='utf-8-sig'))
    except Exception:
        continue
    claims = d if isinstance(d, list) else d.get('claims', [])
    if isinstance(claims, dict): claims = [claims]
    for c in claims:
        if not isinstance(c, dict): continue
        cid = str(c.get('claim_id'))
        if cid in want and (cid, agent) not in seen and cid not in seen:
            seen.add(cid)
            print('###', cid, '[file of', agent + ']', c.get('status'))
            print('STATEMENT:', str(c.get('exact_statement'))[:maxlen])
            h = c.get('hypotheses')
            print('HYP:', json.dumps(h)[:400])
            print('FIRST_UNPROVED:', str(c.get('first_unproved_line'))[:300])
            print('PROOF_SOURCE:', json.dumps(c.get('proof_source'))[:250])
            print()
