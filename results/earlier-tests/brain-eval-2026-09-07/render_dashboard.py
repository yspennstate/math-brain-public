"""Render aggregate campaign status; no private question text is read."""
import hashlib
import json
from pathlib import Path

def render(status_path):
    data=status_path.read_bytes();s=json.loads(data)
    c=s['accepted_inventory'];a=c['summary']['calibration'];h=c['summary']['heldout_provisional_not_certified']
    lines=['# Brain evaluation campaign', '', 'Generated from STATUS.json at '+s['as_of']+'.', '',
        'Clock: '+s['campaign_start']+' through '+s['campaign_deadline']+'. State: '+s['campaign_state']+'.', '',
        '| Inventory | Forms | Distinct proofs | Paper families |','|---|---:|---:|---:|',
        f"| Accepted private calibration | {a['accepted_forms']} | {a['distinct_source_proofs']} | {a['paper_families']} |",
        f"| Provisional heldout, not certified untouched | {h['accepted_forms']} | {h['distinct_source_proofs']} | {h['paper_families']} |", '',
        'This campaign added 20 independently reviewed calibration forms from 10 proofs in 9 families. '
        'The recovered inventory has '+str(c['solver_transport_verified_forms'])+' forms with verified transport. '
        'Brain utility is '+c['brain_utility']+'.', '',
        '| Solver | Registered primary tier | Brain / none | Pairs / target |', '|---|---|---|---|']
    for name,v in s['primary_reconstruction'].items():
        p=v['primary'][0]
        lines.append(f"| {name} | {v['primary_tier']} | {p['correct'][0]}/{p['n']} versus {p['correct'][1]}/{p['n']} | {p['n']}/{v['planned_primary_flawed_pairs']} |")
    lines.extend(['', 'The primary comparisons do not establish benefit, equivalence, or general harm. Pooled results are descriptive.', '', *['- '+x for x in s['limitations']], '', 'Status SHA-256: '+hashlib.sha256(data).hexdigest(), ''])
    return '\n'.join(lines)

if __name__=='__main__':
    folder=Path(__file__).resolve().parent
    (folder/'DASHBOARD.md').write_text(render(folder/'STATUS.json'),encoding='utf-8')
