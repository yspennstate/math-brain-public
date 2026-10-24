from pathlib import Path
import json
R=Path(__file__).resolve().parent
d=json.loads((R/'bellman_3x3_certificate.json').read_text())
f=d['truth'];T={(k,o):v for k,o,v in d['states']}
assert len(f)==512 and len(T)==3**9
checked=0
for k in range(512):
    o=k
    while True:
        u=511^k
        assert (k,o) in T
        # Explicit completion constancy check, not a monotonicity shortcut.
        possible={f[m] for m in range(512) if m&k==o}
        if len(possible)==1:assert T[k,o]==0
        else:
            assert T[k,o]==(1<<u.bit_count())+min(
              T[k|(1<<i),o]+T[k|(1<<i),o|(1<<i)] for i in range(9) if u&(1<<i))
        checked+=1
        if not o:break
        o=(o-1)&k
first=[512+T[1<<i,0]+T[1<<i,1<<i] for i in range(9)]
assert first==[2468,2312,2220,2312,2252,2312,2220,2312,2468]
assert T[0,0]==2220 and first[4]-T[0,0]==32
result={'verified_states':checked,'root_total':T[0,0],
  'first_query_totals':first,'greedy_center_excess_over_512':32}
(R/'bellman_certificate_check.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(result)
