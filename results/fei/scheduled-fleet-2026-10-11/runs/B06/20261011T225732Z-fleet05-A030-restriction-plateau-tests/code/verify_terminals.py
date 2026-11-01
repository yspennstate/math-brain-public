from pathlib import Path
from itertools import combinations,product
import json,time
START=time.perf_counter(); count=0
for n in (1,2,3):
    for mask in range(1,(1<<(1<<n))-1):
        seed=[-1 if mask>>x&1 else 1 for x in range(1<<n)]
        for L in ([2,3] if n<=2 else [2]):
            N=n*L
            table=[seed[sum(((x>>(i*L)&((1<<L)-1)).bit_count()%2)<<i for i in range(n))] for x in range(1<<N)]
            for k in range(L-1):
                for A in combinations(range(N),k):
                    free=[i for i in range(N) if i not in A]
                    for bits in product((0,1),repeat=k):
                        base=sum(v<<i for i,v in zip(A,bits))
                        child=[table[base|sum(((x>>j)&1)<<i for j,i in enumerate(free))] for x in range(1<<len(free))]
                        unate=True
                        for j in range(len(free)):
                            signs={child[x^(1<<j)]-child[x] for x in range(len(child)) if not x>>j&1}
                            if -2 in signs and 2 in signs: unate=False; break
                        assert not unate
                        count+=1
                        assert time.perf_counter()-START<59
assert count==466
out=dict(status='PASS',helper_version='A030-terminal-unateness-v1',exact_nonunate_nodes=count,elapsed_seconds=time.perf_counter()-START)
(Path(__file__).resolve().parents[1]/'out/terminal_validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
