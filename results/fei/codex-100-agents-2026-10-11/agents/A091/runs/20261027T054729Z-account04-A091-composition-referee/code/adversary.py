from fractions import Fraction as Q
from pathlib import Path
import json,time
start=time.perf_counter(); N=0
A=Q(9,2); k=Q(29,13)
for I in [Q(0),Q(1,8),Q(1),Q(3),Q(8)]:
    for pf in range(9):
        p=I*pf/8; J=I-p
        for df in range(17):
            D=k*I*df/16
            if not J:
                assert A*I-D>=0; N+=1; continue
            qstar=min(Q(1),(A*I-D)/(A*J)); assert 0<=qstar<=1
            O=max(Q(0),D-A*p)
            assert (1-qstar)*A*J==O
            assert A*I-D-qstar*A*J==max(Q(0),A*p-D)
            assert qstar>=1-k/A
            for qn in range(17):
                q=Q(qn,16)
                assert (A*I-D-q*A*J>=0)==(q<=qstar)
                N+=1
            N+=3
from check import edge,stats,add,mul,num,eq,bounds
policies=0
for mask in range(256):
    tab=tuple(1 if (mask>>x)&1 else -1 for x in range(8)); H,I=stats(tab)
    for i in range(3):
        D,p,I,J,kids=edge(tab,i)
        # STOP or either remaining coordinate may be chosen independently in each actual child.
        for j0 in [-1,0,1]:
            for j1 in [-1,0,1]:
                hterms=[]; cterms=[]
                for kid,j in zip(kids,[j0,j1]):
                    if j<0: cterms.append({}); hterms.append(stats(kid)[0]); continue
                    D2,p2,I2,J2,grand=edge(kid,j)
                    cterms.append(D2); hterms.append(mul(Q(1,2),add(*(stats(t)[0] for t in grand))))
                total=add(D,mul(Q(1,2),add(*cterms)))
                terminal=mul(Q(1,2),add(*hterms))
                assert eq(add(total,terminal),H)
                # The two original tickets, including second-ticket release through first split.
                assert bounds(add(num(2*k*I),mul(-1,total)))[0]>=0
                policies+=1
result=dict(status='PASS',scalar_assertions=N,two_query_policies=policies,two_query_assertions=2*policies,seconds=time.perf_counter()-start)
Path(__file__).resolve().parents[1].joinpath('out/ADVERSARY.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
