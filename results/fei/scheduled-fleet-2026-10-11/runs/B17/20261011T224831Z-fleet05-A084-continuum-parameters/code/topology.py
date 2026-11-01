from certify import bound,ROOT,R
import json
box=(R(49,100),R(49,100),R(1,4),R(1,4));iv=bound(box)
assert iv[1]<-R(11,100)
out={'point':['49/100','1/4'],'F_interval':[str(x) for x in iv],'certified_upper_bound':'-11/100','consequence':'At p=49/100, at least two zeros in q in (0,1/2), by continuity and the strictly positive analytic neighborhoods of q=0 and q=1/2. For every fixed p>1/2, at least one extra zero in q in (1/2,1), by equation (4) and the negative q=1 edge.'}
(ROOT/'out'/'ZERO_TOPOLOGY.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out),flush=True)
