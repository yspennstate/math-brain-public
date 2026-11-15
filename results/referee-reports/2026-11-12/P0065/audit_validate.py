"""Final artifact and arithmetic cross-checks, independent of the report builder."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
import signal
signal.alarm(280)
import ast
import hashlib
import json
from pathlib import Path
import math


def load(path): return json.loads(Path(path).read_text())


def main():
    for script in Path('.').glob('audit_*.py'):
        ast.parse(script.read_text(),filename=str(script))
    for row in load('exact_results.json')['exact_trees']:
        assert row['linear']==row['recursion']
    for run in load('contraction_results.json'):
        for row in run['rows']:
            assert row['delta']<=row['delta_bound']+2e-14
            assert row['eta']<=row['eta_bound']+2e-14
    seeds=range(101,105)
    constants=load('exact_results.json')['constants']
    for law in ('12','24','123','geom'):
        for seed in seeds:
            result=load(f'pool_{law}_{seed}.json')
            assert result['seconds']<280
            assert result['pool']==40000 and result['sweeps']==180
            idx=[result['ratios'].index(i/10) for i in range(10)]
            values=[result['d'][i] for i in idx]
            assert all(a<b for a,b in zip(values,values[1:]))
            assert max(values)<float(constants[law]['logm'])
            assert all(math.isfinite(v) for v in result['derivative'])
    for seed in range(201,205):
        result=load(f'ray_{seed}.json')
        assert result['seconds']<280
        for paths in result['paths']:
            assert all(0<values['root']<math.log(2) for values in paths.values())
    text=Path('REPORT.md').read_text()
    for label in ('lem:rec','lem:lower','prop:C1','eq:lin','thm:main','cor:mono','rem:tilt','tab:slope','tab:dim'):
        assert label in text
    for section in range(1,10):
        assert f'## {section}.' in text
    assert 'in progress' not in text
    assert 'in preparation' not in text
    digest=hashlib.sha256(Path('PAPER.tex').read_bytes()).hexdigest()
    output={'status':'PASS','paper_sha256':digest,
            'checks':'Python syntax; 25 exact identities; all sampled contraction inequalities; 16 pool outputs; 4 ray outputs; finite values; grid monotonicity and upper bounds; all requested sections in final report',
            'note':'Source hash identifies the audited version; no pre-run hash comparison is claimed.'}
    Path('validation_results.json').write_text(json.dumps(output,indent=2))
    print(json.dumps(output,indent=2))


if __name__=='__main__': main()
