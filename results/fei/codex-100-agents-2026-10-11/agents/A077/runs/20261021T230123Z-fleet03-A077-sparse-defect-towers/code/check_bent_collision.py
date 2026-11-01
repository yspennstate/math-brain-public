from fractions import Fraction as Q
from pathlib import Path
import json,sys,time
import check_profiles as C
start=time.monotonic(); pilot='--pilot' in sys.argv; count=0
def plus(*xs):return sum((x[0] for x in xs),Q(0)),sum((x[1] for x in xs),Q(0))
def scale(c,x):return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def gi(x):
    if not x:return Q(0),Q(0)
    x=abs(Q(x)); l,u=C.ln_interval(x); l2,u2=C.ln_interval(Q(2))
    # log2 interval with the sign of ln(x) respected.
    candidates=[l/l2,l/u2,u/l2,u/u2]
    return scale(-2*x*x,(min(candidates),max(candidates)))
def ki(a,b):return plus(scale(Q(1,2),plus(gi(a+b),gi(a-b))),scale(-1,plus(gi(a),gi(b))))
def outward(x):
    D=1<<80; l,u=x
    return [str(Q(l.numerator*D//l.denominator,D)),str(Q(-((-u.numerator*D)//u.denominator),D))]
rows=[]
for k in ([4] if pilot else [4,6,8,10,16,32,48,64]):
    a=Q(1,1<<k); b=Q(1,1<<(k//2))
    ratio=scale(((1/a)-1)/a,plus(ki(b,a),scale(Q(-1,2),ki(b,2*a))))
    assert ratio[0]>=(k-6 if k>=6 else -2); count+=1
    if k>=8:assert ratio[0]>4; count+=1
    extra=plus(ki(b,1-a),scale(Q(-1,2),plus(ki(b,1-2*a),ki(b,1))))
    guarded=plus(ratio,scale(1/a,extra))
    assert guarded[0]>=(k-6 if k>=6 else -2);count+=1
    if k>=8:assert guarded[0]>4;count+=1
    donor=Q(3*k,2)+5
    assert donor-4>=7;count+=1
    rows.append({'k':k,'ratio_interval':outward(ratio),'guarded_ratio_interval':outward(guarded),'linear_lower_bound':k-6,'price4_refuted':ratio[0]>4,'guarded_price4_refuted':guarded[0]>4,'C5_original_donor_over_e':str(donor),'remaining_donor_over_e':str(donor-4)})
truth=[]
for k in ([2] if pilot else [2,4]):
    N=1<<k; a=Q(1,N); b=Q(1,1<<(k//2))
    V=[];W=[]
    for x in range(2*N):
        z=x&(N-1); phase=sum(((z>>j)&1)*((z>>(j+1))&1) for j in range(0,k,2))%2
        V.append(1-2*phase);W.append(-1 if x==0 else 1)
    t=C.wrapper((1,1),V,W); i=k
    check_delta=C.add(C.xi(C.fw(V),C.fw(W),Q(1,2)),C.mul(Q(-1,2),C.add(*(C.xi(C.fw(C.restrict(V,i,q)),C.fw(C.restrict(W,i,q)),Q(1,2)) for q in [0,1]))))
    model=C.mul(Q(N-1,2),C.add(C.mul(Q(1,2),C.add(C.g(b+a),C.g(b-a))),C.mul(-1,C.add(C.g(b),C.g(a))),C.mul(Q(-1,2),C.add(C.mul(Q(1,2),C.add(C.g(b+2*a),C.g(b-2*a))),C.mul(-1,C.add(C.g(b),C.g(2*a)))))))
    assert model==check_delta;count+=1
    assert C.inf(t,k+1)==a/2;count+=1
    assert all(len(set(C.restrict(t,k+1,q)))==2 for q in [0,1]);count+=1
    assert C.fw(t)==C.direct_fw(t);count+=1
    truth.append({'k':k,'n':k+2,'all_coefficients_directly_checked':len(t),'exact_ratio_interval':outward(C.interval(C.mul(2/a,check_delta)))})
    Vg=V+[-x for x in V];Wg=W+[-x for x in W]
    tg=C.wrapper((1,1),Vg,Wg)
    guarded_delta=C.add(C.xi(C.fw(Vg),C.fw(Wg),Q(1,2)),C.mul(Q(-1,2),C.add(*(C.xi(C.fw(C.restrict(Vg,i,q)),C.fw(C.restrict(Wg,i,q)),Q(1,2)) for q in [0,1]))))
    guarded_model=C.add(model,C.mul(Q(1,2),C.add(C.mul(Q(1,2),C.add(C.g(b+1-a),C.g(b-1+a))),C.mul(-1,C.add(C.g(b),C.g(1-a))),C.mul(Q(-1,2),C.add(C.mul(Q(1,2),C.add(C.g(b+1-2*a),C.g(b-1+2*a))),C.mul(-1,C.add(C.g(b),C.g(1-2*a))))),C.mul(Q(-1,2),C.add(C.mul(Q(1,2),C.add(C.g(b+1),C.g(b-1))),C.mul(-1,C.add(C.g(b),C.g(Q(1)))))))))
    assert guarded_model==guarded_delta;count+=1
    assert all(C.mean(q)==0 for q in [Vg,Wg]+[C.restrict(f,i,b) for f in [Vg,Wg] for b in [0,1]]);count+=1
    assert all(len(set(C.restrict(f,i,b)))==2 for f in [Vg,Wg] for b in [0,1]);count+=1
    assert C.inf(tg,k+1)==a/2;count+=1
    assert C.fw(tg)==C.direct_fw(tg);count+=1
    donor=Q(1,2)*(5*C.total_inf(Vg)-sum((Q(1) for _ in range(k)),Q(0)))
    assert C.H(Vg)==C.number(k);count+=1
    assert donor==Q(1,2)*(Q(3*k,2)+5);count+=1
    assert donor-2>=(Q(7,2) if k>=4 else 0);count+=1
    truth.append({'k':k,'n':k+3,'guarded':True,'all_coefficients_directly_checked':len(tg),'exact_ratio_interval':outward(C.interval(C.mul(2/a,guarded_delta))),'original_donor':str(donor),'booked_debit':'2','remaining_donor':str(donor-2)})
assert time.monotonic()-start<55
out={'status':'PASS','compressed':rows,'truth_tables':truth,'exact_assertions':count,'elapsed_seconds':time.monotonic()-start,'claim':'DeltaXi/Inf diverges; full FEI OPEN'}
(Path(__file__).resolve().parents[1]/'out'/('bent_pilot.json' if pilot else 'bent_full.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
