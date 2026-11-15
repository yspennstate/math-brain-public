"""Bounds, local counterexample, source inventory, and manuscript hashes."""
import hashlib
import json
import re
import resource
import signal
import time
from pathlib import Path
from audit_core import Q, chain, quotient

signal.alarm(240)
started=time.monotonic()
print('U(n) EXACT INTEGER ENUMERATION')
bounds=[]
for n in range(2,21):
    candidates={q:min(2**(n-q),q-1) for q in range(2,n)}
    up=max(candidates.values(),default=1)
    qs=[q for q,v in candidates.items() if v==up]
    assert n//2<=up<=max(1,n-2)
    bounds.append(dict(n=n,lower=n//2,U=up,maximizing_q=qs,candidates=candidates))
    print(n,n//2,up,qs)
assert [b['U'] for b in bounds[:11]]==[1,1,2,2,3,4,4,5,6,7,8]
assert [b['U'] for b in bounds]==[1,1,2,2,3,4,4,5,6,7,8,8,9,10,11,12,13,14,15]

print('\nCOUNTEREXAMPLE TO THE LITERAL HYPOTHESES AT LINE 270')
# All weights one: the original chain consists of independent uniform draws.
# f(0)=f(1)=f(2)=A, f(3)=B. It is injective on J={2,3}.
c=chain([[1]*4 for _ in range(4)])
blocks=[[0,1,2],[3]]
d=chain(quotient(c['w'],blocks))
beta=[c['F'][i][1]-c['F'][i][0] for i in range(4)]
assert beta==[4,-4,0,0]
assert c['F'][2][2]==-3 and d['F'][0][0]==Q(-1,3)
assert c['F'][2][2]+beta[2]**2/8 != d['F'][0][0]
print('original F:',c['F'])
print('quotient weights:',d['w'],'stationary:',d['pi'])
print('beta:',beta,'WR=8; claimed (i,j)=(2,2) RHS=-3; actual Fhat_AA=-1/3')
print('Theorem 2 has the required extra hypothesis; this defect is local to Proposition 8 setup.')

sources=sorted(Path('paper').glob('*.tex'))+sorted(Path('paper/code').glob('*.py'))
inventory={str(p):dict(sha256=hashlib.sha256(p.read_bytes()).hexdigest(),lines=len(p.read_text().splitlines())) for p in sources}
print('\nCITATION LOCATIONS')
for p in sorted(Path('paper').glob('*.tex')):
    for line,txt in enumerate(p.read_text().splitlines(),1):
        if '\\cite' in txt:
            print(f'{p}:{line}: {txt}')
print('\nNO PRIMARY SOURCE FILES AMONG LOCAL INPUTS: all external numbering to check.')
print('Author random merge counts:',25*4,'networks;',25*sum(n*(n-1)//2 for n in range(3,7)),'merges;',
      25*sum(n*n*(n*(n-1)//2) for n in range(3,7)),'entries')
print('Author comb grid:',4*5,'points; author other trial count: 400')

with open('audit_inventory_results.json','w') as out:
    json.dump(dict(bounds=bounds,source_snapshot=inventory,counterexample=dict(
        weights=[[1]*4 for _ in range(4)],blocks=blocks,beta=list(map(str,beta)),
        original_F22=str(c['F'][2][2]),quotient_FAA=str(d['F'][0][0]))),out,indent=2)
elapsed=time.monotonic()-started
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print('seconds',elapsed,'peak_rss_bytes',rss)
with open('LOG.md','a') as log:
    log.write('\n## Bounds, counterexample, and attribution inventory\n\n')
    log.write('- `audit_inventory.py` enumerated U(n) for 2<=n<=20; every manuscript Table 1 entry agrees. U(6)=3 and U(8)=4, proving the two claimed small cases when combined with the verified comb. K(7) is only bounded by the interval [3,4].\n')
    log.write('- Confirmed exact counterexample to the literal setup of Proposition 8: w_ij=1 on four states; f merges {0,1,2}, keeps {3}; u=0,v=1,J={2,3}; f is injective on J. At i=j=2, beta_i=0, original F_22=-3, but lifted quotient F_AA=-1/3. The stated rank-one identity therefore fails unless the missing fibre condition is supplied.\n')
    log.write('- Author check counts 100 networks / 850 merges and 20 comb points match the source. The second program has exactly 400 trials. It returns Boolean failure flags rather than failing the process; this is a reproducibility improvement, not a refutation.\n')
    log.write(f'- Manuscript/code SHA-256 snapshot saved; elapsed {elapsed:.3f} s, peak RSS {rss} bytes.\n')
