"""Read-only final artifact and exact-output validation."""
import hashlib
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def load(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
for item in load(R/'out/PERSISTENCE_RECEIPTS.json')['files']:
    p=R/item['path']
    assert p.stat().st_size==item['bytes'] and sha(p)==item['sha256'],p
for stem in ['orbits','tetra','independent','tangent','block']:
    spec=load(R/f'out/{stem}_spec.json')
    assert sha(R/f'code/{stem}.py')==spec['helper_sha256'],stem
    cert=load(R/f'out/{stem}_certificate.json') if stem!='orbits' else load(R/'out/orbits.json')
    assert cert['status']=='PASS',stem
t=load(R/'out/tetra_certificate.json')
i=load(R/'out/independent_certificate.json')
assert i['independent_parent_cases']==57344
assert i['actual_parent_generator_checks']==11264
assert i['entropy_histogram_classes']==540
assert int(t['maximum']['P'])*int(i['maximum']['Q'])==int(i['maximum']['P'])*int(t['maximum']['Q'])
assert int(i['maximum']['P'])<=2**128*int(i['maximum']['Q'])
b=load(R/'out/block_certificate.json')
assert b['all_clean_half_inside_subsets']==65536 and b['assertions']==262144
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
c=load(R/'CLAIMS.json')[0]
assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
print('PASS: saved hashes, five frozen helper hashes, exact matching maxima, full-case counts, statement hash and packet compatibility.')
