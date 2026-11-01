from pathlib import Path
from fractions import Fraction as F
import json
import check_transport as p
import independent_transport as z
import independent_arithmetic as a
ROOT=Path(__file__).resolve().parent.parent
out=[];checks=0
for k,labels in [(2,[3,5]),(3,[3,5,6])]:
    N=1<<(k+3);t=[]
    for x in range(N):
        data=x&((1<<k)-1);tags=x>>k
        bits=[((data>>i)&1)^((tags&lab).bit_count()%2) for i,lab in enumerate(labels)]
        t.append(int(any(bits)))
    t=tuple(t);g=p.diagnostic(t)
    w=[int(N*v) for v in a.direct_coeffs(t)];O,R,T=z.diag_integer(w)
    assert T==g['T']==g['I'] and sum(R.values())==0;checks+=1
    support=[s for s,v in enumerate(w) if v]
    assert all((u^v).bit_count()>=3 for j,u in enumerate(support) for v in support[:j]);checks+=1
    padded=tuple(t[x&((1<<(k+3))-1)] for x in range(4*N));edited=list(padded);edited[0]=1-edited[0];edited=tuple(edited)
    q=p.diagnostic(edited);NN=len(edited);n=k+5;eps=F(1,NN)
    ew=[int(NN*v) for v in a.direct_coeffs(edited)];EO,ER,ET=z.diag_integer(ew)
    assert ET==q['T'];checks+=1
    assert (sum(EO)-g['I'])**2<=16*n*n*eps;checks+=1
    assert sum(ER.values())<=16*F(n*(n-1),2)*eps;checks+=1
    assert abs(q['I']-g['I'])<=2*n*eps;checks+=1
    assert all(v for v in ew) and sum(1-v for v in edited)%2==1;checks+=1
    out.append({'seed':'PD'+str(k),'coded_n':k+3,'coded_T':str(g['T']),'coded_I':str(g['I']),'coded_Theta':'1','punctured_n':n,'punctured_T':str(q['T']),'punctured_I':str(q['I']),'punctured_Theta':str(q['T']/q['I']),'orientation':str(sum(EO)),'total_refund':str(sum(ER.values())),'all_fourier_nonzero':True})
result={'assertions':checks,'diagnostic_internal_assertions':p.checks,'independent_internal_assertions':z.checks,'cases':out}
(ROOT/'out/CODE_GUARD.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
