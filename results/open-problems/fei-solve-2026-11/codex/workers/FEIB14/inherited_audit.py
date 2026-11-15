"""Read-only replay of the finite ledger behind the inherited symmetric coefficient."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,time
root=Path('../../inputs/fsym44_cert');start=time.time();sources={}
def read(p):
    q=root/p;b=q.read_bytes();sources[str(q)]=hashlib.sha256(b).hexdigest();return json.loads(b)
out=read(Path('ledger_certificate.json'));raw=read(Path('census/certified_maxima.json'));scaled=[F(0),F(0)]
for n in range(2,25):
    scaled.append(min(scaled[n-r['k']]+r['k']*F(r['certified_ratio_upper']) for r in raw if r['n']==n))
    assert scaled[n]/n==F(out['small_dimensions'][str(n)])
assert scaled[24]==24*F(out['base_ratio'])
base=Path('v4/computations/restriction_v4');finite=read(base/'finite_certificate.json')['dimensions'];blocks=read(base/'blocks_certificate.json')['blocks'];ext=read(Path('extension/block_certificate.json'));tail=read(Path('extension/tail_certificate.json'))
segments=[(r['n'],r['n'],F(r['rational_upper'])) for r in finite if r['n']>24]+[(r['L'],r['U'],F(r['rational_upper'])) for r in blocks]+[(ext['L'],ext['U'],F(ext['rational_upper']))]
acc=scaled[24];peak=max((scaled[n]/n,n) for n in range(1,25));cursor=25
for j,(L,U,B) in enumerate(segments):
    assert L==cursor;cursor=U+1;peak=max(peak,(acc/(L-1),L-1),((acc+(U-L+1)*B)/U,U));acc+=(U-L+1)*B
    assert acc==F(out['segments'][j]['cumulative_sum_end'])
assert peak[0]==F(out['finite_maximum_rational']) and peak[1]==out['binding_dimension']
assert cursor-1==tail['n0']==out['cutoff'];maximum=max(peak[0],F(tail['rational_upper']));safe=F(out['safe_rational']);assert maximum<=safe and maximum>safe-F(1,10**6)
paper=Path('../FSYM47/repository/paper/main.tex');text=paper.read_text();assert '4650431/1000000=4.650431' in text
z=dict(passed=True,safe_rational=str(safe),maximum_rational=str(maximum),binding_dimension=peak[1],sources=sources,paper_source=str(paper),paper_sha256=hashlib.sha256(paper.read_bytes()).hexdigest(),scope='Exact seed and rational-ledger replay; does not independently reprove analytic envelopes or rerun the large block census.',elapsed_seconds=time.time()-start)
Path('inherited_audit.json').write_text(json.dumps(z,indent=2)+'\n');print('INHERITED LEDGER PASS',str(safe),peak[1])
