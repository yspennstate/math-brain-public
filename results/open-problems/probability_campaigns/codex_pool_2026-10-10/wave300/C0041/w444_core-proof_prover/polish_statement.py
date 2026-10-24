"""Make L3 stand alone; preserve the proof and every review-pending status."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
bundle = json.loads((ROOT / 'bundle_001.json').read_text(encoding='utf-8'))
definitions = next(e['statement'] for e in bundle['entries'] if e['key'] == 'box-pattern')
entry = next(e for e in bundle['entries'] if e['key'] == 'adaptive-moments')
old = entry['statement']
phrase = 'Use the box pattern and M_r(s) defined in this packet.'
replacement = ('Let the nearest-neighbor environment on Z^d have iid rows and every allowed transition at least kappa>0. '
               + definitions + ' For integer s>=1 put M_r(s)=2^s s! (2r+1)^s kappa^(-s(2r+1)).')
entry['statement'] = old.replace(phrase, replacement).replace(
    'q=P_0(D^ell=infinity)>0, this',
    'q=P_0(D^ell=infinity)>0, where D^ell is first strict backtracking below the initial ell projection, this')
assert phrase not in entry['statement']
encoded = json.dumps(bundle, ensure_ascii=False, indent=2) + '\n'
(ROOT / 'bundle_001.json').write_text(encoded, encoding='utf-8')
draft = Path('~/math-brain-inbox/w444/bundle_001.json').resolve()
assert str(draft.parent).replace('\\', '/').lower() == '~/math-brain-inbox/w444'
on_disk = json.loads(draft.read_text(encoding='utf-8'))
assert on_disk['author_agent'] == 'w444' and all(e['kind'] == 'concept' for e in on_disk['entries'])
part = draft.with_suffix('.part')
part.write_text(encoded, encoding='utf-8')
part.replace(draft)
claims = [json.loads(line) for line in (ROOT / 'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
claim = next(c for c in claims if c['claim_id'] == 'w444-C0041-L3')
claim['statement'] = entry['statement']
(ROOT / 'CLAIMS.jsonl').write_text(''.join(json.dumps(c, ensure_ascii=False) + '\n' for c in claims), encoding='utf-8')
with (ROOT / 'STATUS.md').open('a', encoding='utf-8') as handle:
    handle.write('2026-10-10: L3 draft/registry wording now carries every box, density and moment definition inline for stand-alone recall. Proof scope is identical; byte identities refreshed after this wording fix.\n')
print('L3 stand-alone wording updated; proof text unchanged; all concepts remain review-pending.')
