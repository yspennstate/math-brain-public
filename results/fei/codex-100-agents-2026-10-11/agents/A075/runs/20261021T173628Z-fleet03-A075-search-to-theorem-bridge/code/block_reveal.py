from pathlib import Path
from fractions import Fraction as Q
import json,time,sys
import arithmetic as ar
sys.set_int_max_str_digits(100000)
ROOT=Path(__file__).resolve().parents[1]
def logq(x):return ar.add(ar.logform(x.numerator),ar.logform(x.denominator),Q(-1))
def hm(x):return ar.scale(logq(x),-x) if x else {}
def h2(x):return ar.add(hm(x),hm(1-x))
def val(e):
    l,u=ar.enclose(e)
    return {'form':ar.forms(e),'lower':str(l),'upper':str(u),'display':[float(l),float(u)]}
H=[-1 if x in {0,1,2,4,8,16,32,6,17,40} else 1 for x in range(64)]
J=[-H[x^1] for x in range(64)]
W=ar.fwht(J)
def outer(ps):
    ms=[1-2*p for p in ps];vs=[4*p*(1-p) for p in ps]
    masses=[];entropy={};qs=[]
    for T in range(64):
        c=Q(0)
        for U,w in enumerate(W):
            if U&T!=T:continue
            z=Q(w,64)
            for j in range(6):
                if (U^T)>>j&1:z*=ms[j]
            c+=z
        v=Q(1)
        for j in range(6):
            if T>>j&1:v*=vs[j]
        mass=v*c*c;masses.append(mass);entropy=ar.add(entropy,hm(mass))
    ar.ck(sum(masses)==1)
    for j in range(6):
        q=Q(0)
        for x in range(64):
            if x>>j&1:continue
            prob=Q(1)
            for l in range(6):
                if l!=j:prob*=ps[l] if x>>l&1 else 1-ps[l]
            if J[x]!=J[x^(1<<j)]:q+=prob
        if vs[j]:ar.ck(sum(masses[T] for T in range(64) if T>>j&1)==q*vs[j])
        qs.append(q)
        entropy=ar.add(entropy,h2(vs[j]),-q)
    return entropy,qs,masses
def core(n):
    N=1<<n;p=Q(3,N);I=Q(6*n-8,N)
    hg=hm((1-2*p)**2)
    hg=ar.add(hg,hm(Q(36,N*N)),Q(N//4-1))
    hg=ar.add(hg,hm(Q(4,N*N)),Q(3*N//4))
    ar.ck((1-2*p)**2+(N//4-1)*Q(36,N*N)+3*N//4*Q(4,N*N)==1)
    if n<=12:
        truth=[-1 if x<3 else 1 for x in range(N)]
        w=ar.fwht(truth)
        ar.ck(ar.entropy(w)==hg)
        ar.ck(sum(Q(t*t,N*N)*x.bit_count() for x,t in enumerate(w))==I)
    return p,I,hg,ar.add({2:4*I},hg,Q(-1))
def record(n):
    p,I,hg,S=core(n);C,qs,_=outer([p]*6)
    Cp,qp,_=outer([Q(0)]+[p]*5);Cm,qm,_=outer([Q(1)]+[p]*5)
    ar.ck(qs[0]==qp[0]==qm[0])
    for j in range(1,6):ar.ck(qs[j]==(1-p)*qp[j]+p*qm[j])
    delta=ar.add(ar.add(C,Cp,-(1-p)),Cm,-p)
    bank=ar.scale(S,qs[0]);excess=ar.add(delta,bank,Q(-1))
    fullS=ar.add(ar.scale(S,sum(qs)),C,Q(-1))
    Mp=ar.add(ar.scale(S,sum(qp[1:])),Cp,Q(-1))
    Mm=ar.add(ar.scale(S,sum(qm[1:])),Cm,Q(-1))
    meanM=ar.add(ar.scale(Mp,1-p),Mm,p)
    ar.ck(ar.add(ar.add(meanM,fullS,Q(-1)),excess,Q(-1))=={})
    bounds=[ar.enclose(x) for x in [excess,Mp,Mm,fullS,meanM]]
    ar.ck(bounds[0][0]>0 and bounds[3][0]>0 and bounds[4][0]>0)
    e_lo,e_hi=bounds[0];b_lo,b_hi=bounds[4]
    fraction={'lower':str(e_lo/b_hi),'upper':str(e_hi/b_lo),'display':[float(e_lo/b_hi),float(e_hi/b_lo)]}
    out={'n':n,'physical_dimension':6*n,'p':str(p),'I_core':str(I),'q0':str(qs[0]),'core_S4':val(S),'root_full_S4':val(fullS),'full_block_delta_C':val(delta),'selected_initial_bank':val(bank),'signed_full_block_K4_excess':val(excess),'delta_C_over_p2':val(ar.scale(delta,1/(p*p))),'excess_over_p2':val(ar.scale(excess,1/(p*p)))}
    out.update({'endpoint_other_owner_M_plus':val(Mp),'endpoint_other_owner_M_minus':val(Mm),'mean_endpoint_other_owner_M':val(meanM),'aggregate_signed_ratio_NOT_feasible_donation':fraction,'donation_rule':'A positive mean bank alone is insufficient: each full endpoint surplus must be nonnegative. Raw endpoint signs are archived; no endpoint donor repair is asserted.'})
    (ROOT/'out'/f'BLOCK_n{n}.json').write_text(json.dumps(out,indent=2)+'\n')
    return out
if __name__=='__main__':
    start=time.perf_counter();spec=json.loads((ROOT/'out'/('FOLLOWUP_SPEC.json' if '--followup' in sys.argv else 'FROZEN_SPEC.json')).read_text())
    rows=[record(n) for n in spec['domain']]
    out={'domain':spec['domain'],'rows':[{'n':r['n'],'excess':r['signed_full_block_K4_excess']['display'],'delta_C_over_p2':r['delta_C_over_p2']['display'],'core_S4':r['core_S4']['display'],'full_S4':r['root_full_S4']['display']} for r in rows],'checks':ar.checks,'runtime_seconds':time.perf_counter()-start}
    assert out['runtime_seconds']<spec['maximum_runtime_seconds']
    (ROOT/'out'/('FOLLOWUP.json' if '--followup' in sys.argv else 'PILOT.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
