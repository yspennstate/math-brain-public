from fractions import Fraction as F
from collections import defaultdict
from itertools import product
from pathlib import Path
import json,math,time
ROOT=Path(__file__).resolve().parent
def vectors(q,b,n,L,D):
    if n==0:return [tuple(int(i==j) for i in range(q)) for j in range(q)]
    prev=vectors(q,b,n-1,L,D)
    msg=[tuple((D-L)*sum(v)+L*q*x for x in v) for v in prev]
    return [tuple(math.prod(v[i] for v in vs) for i in range(q)) for vs in product(msg,repeat=b)]
def histogram(q,b,n,L,D):
    start=time.monotonic()
    prev=vectors(q,b,n-1,L,D)
    messages=[tuple((D-L)*sum(v)+L*q*x for x in v) for v in prev]
    hist=defaultdict(int); total1=total2=0
    for vs in product(messages,repeat=b):
        a=math.prod(v[0] for v in vs); d=math.prod(v[1] for v in vs)
        total1+=a;total2+=d;hist[F(abs(a-d),a+d)]+=a+d
    den=(D*q)**sum(b**j for j in range(1,n+1))
    assert total1==total2==den
    out={z:F(w,2*den) for z,w in hist.items()}
    assert sum(out.values())==1
    print('histogram',q,b,n,str(F(L,D)),'knots',len(out),'seconds',round(time.monotonic()-start,2),flush=True)
    return out
def compare(q,r,b,n,L,D,hq,hr):
    knots=sorted(set(hq)|set(hr)|{F(0),F(1)})
    massq=massr=F(1); momq=sum(z*w for z,w in hq.items());momr=sum(z*w for z,w in hr.items())
    smallest=F(0);witness=F(0)
    for t in knots:
        massq-=hq.get(t,0);momq-=t*hq.get(t,0)
        massr-=hr.get(t,0);momr-=t*hr.get(t,0)
        diff=(momr-t*massr)-(momq-t*massq)
        if diff<smallest:smallest=diff;witness=t
    result={'q':q,'r':r,'b':b,'depth':n,'lambda':str(F(L,D)),
            'min_stop_loss_difference':str(smallest),'threshold':str(witness),
            'larger_dominates_binary_Blackwell':smallest>=0,
            'TV_q':str(sum(z*w for z,w in hq.items())),'TV_r':str(sum(z*w for z,w in hr.items()))}
    with (ROOT/'blackwell_results.jsonl').open('a',encoding='utf8') as f:f.write(json.dumps(result)+'\n')
    if smallest<0:
        payload={'comparison':result,'hist_q':{str(z):str(w) for z,w in hq.items()},'hist_r':{str(z):str(w) for z,w in hr.items()}}
        (ROOT/'blackwell_witness.json').write_text(json.dumps(payload,indent=2),encoding='utf8')
        print('EXACT BLACKWELL OBSTRUCTION',json.dumps(result),flush=True)
    else:print('dominance passes',q,r,b,n,str(F(L,D)),flush=True)
    return smallest<0
def main():
    found=False
    for b,n,qs,parameters in [
        (2,2,range(2,9),[(1,5),(2,5),(1,2),(3,5),(4,5)]),
        (2,3,range(2,6),[(1,2),(3,5),(2,3)]),
        (3,2,range(2,5),[(1,3),(1,2)])]:
        for L,D in parameters:
            old=None
            for q in qs:
                hist=histogram(q,b,n,L,D)
                if old:
                    if compare(q-1,q,b,n,L,D,old,hist): found=True;break
                old=hist
            if found:break
        if found:break
    print('search finished; obstruction found:',found,flush=True)
if __name__=='__main__':main()
