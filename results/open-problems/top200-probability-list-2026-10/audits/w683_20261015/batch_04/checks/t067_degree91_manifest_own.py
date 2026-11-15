"""Bind degree91 supplied sources and the independent finite gate."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
root=Path('~/brain_workers/w682')
manifest_path=root/'checks/extensions91_submission.json'
manifest=json.loads(manifest_path.read_text())
gate_path=root/'checks/compensated91_gate.json';gate=json.loads(gate_path.read_text())
checked={};size=0
for rel,digest in {**manifest['hashes'],**gate['endpoint_hashes']}.items():
    path=root/rel.replace('\\','/')
    assert path.resolve().is_relative_to(root.resolve())
    raw=path.read_bytes();size+=len(raw)
    assert sha256(raw).hexdigest()==digest,rel
    checked[str(path.relative_to(root))]=digest
constants=json.loads(Path('checks/t067_compensated_constants_own.json').read_text())['rows'][1]
for key in ['alpha','B']:
    assert F(constants[key])==F(gate[key])
assert F(constants['curvature'])==F(gate['curvature_upper'])
assert [F(constants[k]) for k in ['fU','fM']]==list(map(F,gate['F_constants']))
assert [F(constants[k]) for k in ['qU','qM']]==list(map(F,gate['Q_constants']))
assert F(constants['positive_denominator'])==F(gate['positive_replacement_denominator'])
assert F(constants['monotonicity_margin'])==F(gate['positive_d_monotonicity_coefficient'])
assert F(gate['minimum_exact_margin'])>F(3,200)
own=json.loads(Path('checks/t067_compensated_gaussian_own.json').read_text())
assert own['complete'] and len(own['endpoints'])==86
newgate=next(g for g in own['gates'] if g['degree']==91)
assert F(newgate['minimum_interval_margin'])>F(3,200)
out={'complete':True,'manifest_sha256':sha256(manifest_path.read_bytes()).hexdigest(),'source_gate_sha256':sha256(gate_path.read_bytes()).hexdigest(),'checked_files':len(checked),'checked_bytes':size,'hashes':checked,'own_gate_margin':newgate['minimum_interval_margin'],'author_gate_margin':gate['minimum_exact_margin'],'all_constants_match':True}
Path('checks/t067_degree91_manifest_own.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({'complete':True,'checked_files':len(checked),'checked_bytes':size,'all_constants_match':True}))
