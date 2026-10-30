from pathlib import Path
from fractions import Fraction as Q
import math,json,time
ROOT=Path(__file__).resolve().parents[1]
NEG={0,1,2,4,8,16,32,6,17,40}
TABLE=[-1 if x in NEG else 1 for x in range(64)]
def walsh(a):
    a=a[:];k=1
    while k<len(a):
        for start in range(0,len(a),2*k):
            for j in range(k):u,v=a[start+j],a[start+j+k];a[start+j]=u+v;a[start+j+k]=u-v
        k*=2
    return a
WH=walsh(TABLE)
def profile(p):
    m=1-2*p;v=4*p*(1-p);rows=[]
    for T in range(0,64,2):
        k=T.bit_count();C=0;d=0
        for W in range(64):
            if W&T==T:C+=WH[W]/64*m**(W.bit_count()-k)
            if W&(T|1)==T|1:d+=WH[W]/64*m**(W.bit_count()-k-1)
        rows.append((v**k*C*C,v**k*d*d))
    return rows
def phi(x,y):
    def a(z):return z*math.log2(z) if z else 0.
    return a(x+y)-a(x)-a(y)
def reserve(p,t,rows=None):
    rows=profile(p) if rows is None else rows
    q=sum(d for u,d in rows)
    return sum(phi(u,t*d) for u,d in rows)-q*phi((1-2*p)**2,t)
def main():
    start=time.perf_counter();bad=[];both=[];safe=[]
    for j in range(1,129):
        p=j/256;tmax=4*p*p;profiles=[profile(p),profile(1-p)]
        vals=[[],[]]
        for k in range(1,17):
            t=tmax*k/16;r=[reserve(p,t,profiles[0]),reserve(1-p,t,profiles[1])]
            vals[0].append(r[0]);vals[1].append(r[1])
            if max(r)<-1e-10:both.append({'p':f'{j}/256','t_fraction_of_max':f'{k}/16','R':r})
        choice=[o for o in [0,1] if min(vals[o])>=-1e-10]
        if not choice:bad.append({'p':f'{j}/256','min_R':[min(v) for v in vals]})
        safe.append({'p':f'{j}/256','orientations_screened_safe':choice,'min_R':[min(v) for v in vals]})
    (ROOT/'out').mkdir(exist_ok=True)
    out={'runtime_seconds':time.perf_counter()-start,'scope':'floating discovery only, not a continuum certificate','no_orientation_rows':bad,'both_negative_at_same_t':both,'all_rows':safe,'outer_uniform_walsh':WH}
    (ROOT/'out'/'PILOT.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({'runtime_seconds':out['runtime_seconds'],'no_orientation_rows':bad,'both_negative_count':len(both),'first_both_negative':both[:8]}),flush=True)
if __name__=='__main__':main()
