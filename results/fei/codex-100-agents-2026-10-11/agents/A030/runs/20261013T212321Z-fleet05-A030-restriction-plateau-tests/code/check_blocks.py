"""Exact additional domain for whole-block simulation; no baseline census rerun."""
from pathlib import Path
from itertools import permutations
import json,time,hashlib
HERE=Path(__file__).resolve().parent
# Only the shared, locally owned definition prefix is evaluated; all executed
# operations and arithmetic are the literal audited helper definitions.
source=(HERE/'check.py').read_text(encoding='utf-8').split('for n in (1,2,3):\n')[0]
scope={'__file__':str(HERE/'check.py')}
exec(compile(source,str(HERE/'check.py'),'exec'),scope)
F=scope['F'];const=scope['const'];add=scope['add'];positive=scope['positive']
reserve=scope['reserve'];pairs=scope['pairs'];stats=scope['stats'];ck=scope['ck']
count=0
for n in (1,2,3):
    for mask in range(1<<(1<<n)):
        t=tuple(-1 if mask>>x&1 else 1 for x in range(1<<n))
        parent=pairs(t,n);I=sum(stats(t)[1],F(0))
        for order in permutations(range(n)):
            physical=tuple(j for i in order for j in (2*i,2*i+1))
            for C in (0,1,4):
                q=reserve(t,order,C);q2=reserve(t,order,2*C)
                ck(reserve(parent,physical,C)==q2)
                compression=positive(add((1,q),(-1,const(C*I))))
                ck(positive(add((1,compression),(-1,q2)))==())
                count+=1
assert count==4716
ck(3**9>2**14);ck(3**3<2**5)
out=dict(status='PASS',helper_version='A030-block-simulation-v1',cases=count,
 checks=scope['checks'],certified_nonzero_signs=scope['signs'],exact_zero_signs=scope['zeros'],
 elapsed_seconds=time.perf_counter()-scope['START'],
 witness=dict(core='A_3 data-first',q_expression='(9/32)log2(3)-3/8',strict_lower='1/16',strict_upper='3/32',spectator_parent_q='0',both_child_q='same q'),
 shared_source_sha256=hashlib.sha256(source.encode()).hexdigest(),
 code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(HERE.parent/'out/BLOCK_VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
