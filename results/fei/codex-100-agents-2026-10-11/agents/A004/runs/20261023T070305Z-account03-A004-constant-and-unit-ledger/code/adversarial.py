from pathlib import Path
from fractions import Fraction as F
import json,time
import check as c
import exact as e

RUN=Path(__file__).resolve().parents[1]
def run():
    start=time.perf_counter();sector=rows=funded=matched=nonzero_mean=0
    counts={};sample=None
    for mask in range(256):
        h=tuple(1 if mask>>t&1 else -1 for t in range(8));p=e.spec(h);co=c.coeff(h);a0=1-p[0]
        for j in range(3):
            if not a0 or co[1<<j] or any(co[e.insert(t,j)]*co[e.insert(t,j)|(1<<j)] for t in range(4)):continue
            sector+=1;nonzero_mean+=int(co[0]!=0)
            for atom in [None]+[k for k in range(1,8) if k!=1<<j]:
                r=p if atom is None else (p[0],)+tuple((p[t]+a0*F(t==atom))/2 for t in range(1,8))
                eta,W,delta,rc,rho,k=c.nullstep(h,r,j);rows+=1;matched+=int(eta==0)
                if eta>=F(1,63):
                    funded+=1
                    # A deliberately sparse target, including actual-zero labels.
                    target=(F(1),F(0),F(0));rn=(rc[0],)+tuple(F(63,64)*rc[t]+F(1,64)*a0*target[t-1] for t in range(1,4))
                    pp=e.marginal(p,j)
                    inc=e.add((1,e.B(p,j)),(1,e.CE(pp,rn)),(-1,e.CE(p,r)))
                    z=e.add((1,e.CE(pp,rn)),(-1,e.CE(pp,rc)))
                    c.ck(inc==e.add((-1,rho),(-1,k),(1,z)))
                    c.ck(e.bounds(inc)[1]<0)
                    if co[0] and sample is None:
                        sample={'mask':mask,'query':j,'reference_extra_atom':atom,'mean':str(co[0]),'eta':str(eta),'increment':e.rec(inc)}
                c.ck(time.perf_counter()-start<55)
    c.ck(sector>0 and nonzero_mean>0 and matched>0 and funded>0 and sample is not None)
    out={'status':'PASS','seconds':time.perf_counter()-start,'assertions':e.COUNT,'all_labelled_3bit_functions':256,'eligible_physical_queries':sector,'eligible_queries_with_nonzero_mean':nonzero_mean,'reference_rows':rows,'funded_fixed_strength_rows':funded,'exact_matched_null_rows':matched,'nonzero_mean_sample':sample,'scope':'Exhaustion of exact isospectral double-null query sector on n3 only; no all-dimensional extrapolation.'}
    (RUN/'out/ADVERSARIAL.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out))
if __name__=='__main__':run()
