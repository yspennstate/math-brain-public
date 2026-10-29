import json, collections
rows = [json.loads(l) for l in open('cert_out.jsonl', encoding='utf-8') if l.strip()]
cnt = collections.Counter(); bad = []; spot = 0; ctrl_neg = 0; gam_needed_ctrl = []
for r in rows:
    spot += r.get('spot') == 'ok'
    for m, x in r['m'].items():
        if not x['pass']:
            bad.append((r['cell'], m, x['tried'])); continue
        cnt[(x['gamma'], x['e'])] += 1
        ctrl_neg += x['ctrl_g24_min'] < 0
        if x['gamma'] != '0':
            gam_needed_ctrl.append((r['cell'], m, x['tried'].get('0|1'), x['tried'].get('0|2')))
print('cells', len(rows), 'cases', 2 * len(rows), 'spot ok', spot)
print('(gamma, e) counts:', dict(cnt))
print('failures:', bad[:5], len(bad))
print('g24 -1/10 control: cases with a negative coefficient', ctrl_neg)
print('gamma>0 cases (gamma=0 min at e=1, e=2):', gam_needed_ctrl[:6], len(gam_needed_ctrl))
