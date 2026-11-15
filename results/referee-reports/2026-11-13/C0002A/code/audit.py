"""Final reproducible checks of constants, data integrity and resource records."""
import csv
import json
import hashlib
from pathlib import Path
from exact_means import constants, G, C, C0, integrals
from dgff import diagonal
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
out={'bias_derivative':[], 'center_green':[], 'sample_integrity':[]}
for lam in [.2,.4,.6,.8]:
    b=2*lam/np.sqrt(G); step=1e-3
    def m(z):return constants(z*np.sqrt(G)/2,30000)['m']
    dd=(-m(b+2*step)+16*m(b+step)-30*m(b)+16*m(b-step)-m(b-2*step))/(12*step**2)
    value=constants(lam)['B']; alternative=-dd/(2*G)
    assert abs(value-alternative)<1e-7
    out['bias_derivative'].append(dict(lam=lam,B=value,
        B_from_finite_second_derivative=alternative,error=alternative-value))
for N in [64,256,1024]:
    for start,v in diagonal(N):
        if start<=N//2-1<start+v.shape[0]:
            q=v[N//2-1-start,N//2-1]-G*np.log(N)
            predicted=C0+G*np.log(C)
            assert abs(q-predicted)<1/N**2
            out['center_green'].append(dict(N=N,q_center=q,predicted=predicted,error=q-predicted))
for plan in ['main','large','calibration']:
    meta=json.loads((ROOT/'data'/f'metadata_{plan}.json').read_text())
    assert 'finished' in meta and meta['peak_bytes']<4_000_000_000
    assert meta['resources']['nice']>=10 and meta['resources']['threads']==1
    with (ROOT/'data'/f'samples_{plan}.csv').open() as f:rows=list(csv.DictReader(f))
    assert len(rows)==4*sum(count for _,count in meta['plan'])
    for row in rows:
        N=int(row['N']);lam=float(row['lambda']);count=int(row['count'])
        expected=np.sqrt(np.log(N))*N**(2*lam*lam-2)*count
        assert np.isclose(float(row['X']),expected,rtol=1e-12,atol=1e-14)
        assert 0<=count<=(N-1)**2
    out['sample_integrity'].append(dict(plan=plan,fields=len(rows)//4,
                                       rows=len(rows),peak_bytes=meta['peak_bytes']))
assert abs(integrals(0)[0]-1)<1e-8
# Audit all retained paper files as UTF-8 plain text and refresh their hashes.
manifest=json.loads((ROOT/'sources'/'manifest.json').read_text())
by_file={v['file']:v for v in manifest}
for f in (ROOT/'sources').glob('*.txt'):
    raw=f.read_bytes();raw.decode('utf-8')
    assert not raw.startswith(b'%PDF')
    name=str(f.relative_to(ROOT))
    if name in by_file:
        by_file[name].update(sha256_text=hashlib.sha256(raw).hexdigest(),bytes=len(raw),pages=raw.count(b'\x0c'))
for pattern in ['*.pdf','*.PDF','*.jpg','*.jpeg','*.png']:
    assert not list(ROOT.rglob(pattern)),pattern
(ROOT/'sources'/'manifest.json').write_text(json.dumps(list(by_file.values()),indent=2)+'\n')
(ROOT/'data'/'audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
