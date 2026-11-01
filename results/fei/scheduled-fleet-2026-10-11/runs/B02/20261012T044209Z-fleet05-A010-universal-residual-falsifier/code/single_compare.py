from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations
import reference_v1 as ref
import json,time,hashlib,sys,math

RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out'
OLD=RUN.parents[0]/'20261011T225444Z-fleet05-A010-universal-residual-falsifier'

def factors(x):
    result={}; d=2
    while d*d<=x:
        while x%d==0: result[d]=result.get(d,0)+1; x//=d
        d+=1
    if x>1: result[x]=result.get(x,0)+1
    return result

def addlog(coeff,x,weight):
    for prime,power in factors(x).items(): coeff[prime]=coeff.get(prime,Q(0))+power*weight

def interval(coeff):
    lo=hi=Q(0)
    for p,w in coeff.items():
        a,b=ref.log_interval(Q(p))
        if w>=0: lo+=w*a; hi+=w*b
        else: lo+=w*b; hi+=w*a
    return lo,hi

def closed_spectrum(t,n):
    a=ref.walsh(t,n); den=(1<<n)**2
    p=[Q(v*v,den) for v in a]
    influences=[sum(p[A] for A in range(1<<n) if A>>j&1) for j in range(n)]
    relevant=[j for j in range(n) if influences[j]]
    order=sorted(relevant,key=lambda j:(-influences[j],j)); I=sum(influences)
    def formula(ordr):
        c={}
        for rank,j in enumerate(ordr,1): addlog(c,rank,Q(6,5)*influences[j]/I)
        for A,prob in enumerate(p):
            if prob: addlog(c,math.factorial(A.bit_count()),-Q(6,5)*prob/I)
        return {k:v for k,v in c.items() if v}
    coeff=formula(order); lo,hi=interval(coeff)
    # Independent direct rank sum on every full relevant order.
    checked=0
    for ordr in permutations(relevant):
        direct={}
        for A,prob in enumerate(p):
            selected=0
            for rank,j in enumerate(ordr,1):
                if A>>j&1:
                    selected+=1; addlog(direct,rank,Q(6,5)*prob/I); addlog(direct,selected,-Q(6,5)*prob/I)
        direct={k:v for k,v in direct.items() if v}
        assert direct==formula(ordr)
        # Certify rearrangement by every inversion swap: rank odds and influence.
        assert sum(influences[j] for j in ordr)==I
        d=formula(ordr)
        diff={q:d.get(q,Q(0))-coeff.get(q,Q(0)) for q in set(d)|set(coeff)}
        dl,dh=interval(diff)
        assert dl>=0 or all(v==0 for v in diff.values()),(t,n,ordr,dl,dh)
        checked+=1
    return {'n':n,'truth':t,'relevant':relevant,'order':order,'influences':[str(x) for x in influences],'I':str(I),'variance':str(1-p[0]),'coefficients':{str(k):str(v) for k,v in coeff.items()},'single_lo':str(lo),'single_hi':str(hi),'single_ratio':float((lo+hi)/2),'orders_checked':checked,'integer_walsh':a}

def main():
    started=time.monotonic(); max_n=int(sys.argv[1]); data=json.loads((OLD/'out/results.json').read_text()); rows=[]
    for baseline in data['rows']:
        if baseline['n']>max_n: continue
        assert time.monotonic()-started<60
        r=closed_spectrum(baseline['truth'],baseline['n'])
        r.update(prime_baseline_lo=baseline['ratio_lo'],prime_baseline_hi=baseline['ratio_hi'],prime_baseline_ratio=baseline['ratio'],representative=baseline['representative'],orbit_size=baseline['orbit_size'],prime_gates=baseline['gates'],prime_read=baseline['read'])
        slo,shi=Q(r['single_lo']),Q(r['single_hi']); plo,phi=Q(baseline['ratio_lo']),Q(baseline['ratio_hi'])
        r['menu_upper']=str(min(shi,phi)); r['menu_midpoint']=min(r['single_ratio'],r['prime_baseline_ratio']); rows.append(r)
        (OUT/'single_checkpoint.json').write_text(json.dumps({'completed':len(rows),'rows':rows},indent=2))
    rows.sort(key=lambda x:x['menu_midpoint'],reverse=True)
    result={'max_n':max_n,'elapsed_seconds':time.monotonic()-started,'rows':rows,'orders_checked':sum(r['orders_checked'] for r in rows),'source_sha256':hashlib.sha256((OLD/'out/results.json').read_bytes()).hexdigest()}
    (OUT/f'single_n{max_n}.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({'elapsed_seconds':result['elapsed_seconds'],'rows':len(rows),'orders_checked':result['orders_checked'],'top':[{k:r[k] for k in ['n','truth','single_ratio','prime_baseline_ratio','menu_midpoint','coefficients']} for r in rows[:12]]},indent=2))

if __name__=='__main__': main()
