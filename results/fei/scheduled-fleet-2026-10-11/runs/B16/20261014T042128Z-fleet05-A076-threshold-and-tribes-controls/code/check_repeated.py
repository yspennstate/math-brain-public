from pathlib import Path
from fractions import Fraction as F
import json,time
ROOT=Path(__file__).resolve().parents[1]
exec(compile((ROOT/'code/arithmetic.py').read_text(encoding='utf-8'),str(ROOT/'code/arithmetic.py'),'exec'))
start=time.perf_counter()
def mux(g):return tuple(v for a in g for v in [a,1])
rows=[]
for m in [1,2,3,4]:
    g=tuple((-1)**((z&1)+sum(((z>>(1+2*j))&1)*((z>>(2+2*j))&1) for j in range(m))) for z in range(1<<(2*m+1)))
    f=mux(g);eq(I(g),m+1);eq(I(f),F(m,2)+1)
    equal_expr(plus((H(g),F(1)),({F(2):F(2*m)},F(-1))))
    equal_expr(plus((H(f),F(1)),({F(2):F(m+2)},F(-1))))
    todo=[(g,list(range(2*m+1)),F(1),0)]
    bg=bf=A={};spent=leafI=F(0);leafH={};nodes=0
    while todo:
        if time.perf_counter()-start>55:raise RuntimeError('frozen repeated-check deadline')
        t,labels,w,j=todo.pop();ft=mux(t)
        if j==m:
            eq(sum(v!=0 for v in coeff(t)),1)
            equal_expr(plus((H(ft),F(1)),({F(2):F(2)},F(-1))))
            leafI+=w*I(ft);leafH=plus((leafH,F(1)),(H(ft),w));continue
        i=labels.index(1+2*j);nodes+=1;cc=coeff(t)
        eq(cc[0],F(0));eq(cc[1<<i],F(0));eq(inf(ft,0),F(1,2));eq(inf(ft,i+1),F(1,4))
        eq(F(sum(ft[z]!=ft[z^(1<<(i+1))] for z in range(len(ft))),len(ft)),F(1,4))
        cost=B(t,i);fcost=B(ft,i+1)
        equal_expr(plus((cost,F(1)),({F(2):F(1)},F(-1))))
        equal_expr(plus((fcost,F(1)),({F(2):F(1,2)},F(-1))))
        bg=plus((bg,F(1)),(cost,w));bf=plus((bf,F(1)),(fcost,w))
        A=plus((A,F(1)),(fcost,w),(cost,-w/4));spent+=w/4
        rem=labels[:i]+labels[i+1:]
        todo.extend((child(t,i,b),rem,w/2,j+1) for b in [0,1])
    equal_expr(plus((bg,F(1)),({F(2):F(m)},F(-1))))
    equal_expr(plus((bf,F(1)),({F(2):F(m,2)},F(-1))))
    equal_expr(plus((A,F(1)),({F(2):F(m,4)},F(-1))))
    eq(spent,F(m,4));eq(leafI,1+F(m,4));eq(spent+leafI,I(f))
    equal_expr(plus((leafH,F(1)),({F(2):F(2)},F(-1))))
    rows.append(dict(m=m,nodes=nodes,admission=str(F(m,4)),selector_influence='1/2',spent=str(spent),leafI=str(leafI)))
for m in [16,32,64,128]:
    eq(F(m,4)+(1+F(m,4)),F(m,2)+1)
    rows.append(dict(m=m,compressed=True,admission=str(F(m,4)),selector_influence='1/2',ratio=F(m,2).numerator))
result=dict(status='PASS',exact_assertions=checks,elapsed_seconds=time.perf_counter()-start,cases=rows)
(ROOT/'out/REPEATED_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
