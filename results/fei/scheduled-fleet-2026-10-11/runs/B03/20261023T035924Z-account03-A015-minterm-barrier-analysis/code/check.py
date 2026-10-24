"""A015-SUBPROB-TRANSPORT-AND-CENTRAL-REVIEW@1; source-independent checker."""
from fractions import Fraction as F
from pathlib import Path
from math import comb, lcm
from itertools import combinations, permutations
import argparse
import hashlib
import json
import time

ROOT=Path(__file__).resolve().parents[1]
START=time.monotonic();COUNT=0
def ck(x,why):
    global COUNT
    COUNT+=1
    if not x:raise AssertionError(why)
    if time.monotonic()-START>55:raise RuntimeError('Frozen55-second runtime limit')

def walsh(v):
    a=v[:];h=1
    while h<len(a):
        for start in range(0,len(a),2*h):
            for j in range(start,start+h):
                x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
        h*=2
    return [F(x,len(v)) for x in a]

def put(out,base,weight):
    if weight and base!=1:
        out[base]=out.get(base,F(0))+weight
        if not out[base]:del out[base]
def entropy_terms(probs):
    out={}
    for p in probs:
        if p:put(out,1/p,p)
    return out
def combine(*parts):
    out={}
    for terms,factor in parts:
        for base,w in terms.items():put(out,base,w*factor)
    return out
def exp_exact(terms):
    den=1
    for v in terms.values():den=lcm(den,v.denominator)
    out=F(1)
    for base,exponent in terms.items():
        ck(base>0,'positive logarithm base')
        out*=base**int(exponent*den)
    return out,den
def ce(p,q):
    v=1-p.get(0,F(0));out=entropy_terms([v,1-v])
    for A,w in p.items():
        if A and w:put(out,1/q[A],w)
    return out
def project(q,i):
    bit=1<<i;qi=q[bit];out={}
    for A,mass in q.items():
        T=A&~bit
        if T:out[T]=out.get(T,F(0))+mass/(1-qi)
    return out
def embed(mask,i):
    return (mask&((1<<i)-1))|((mask>>i)<<(i+1))

def transport(pilot):
    refs=[{A:F(1,7) for A in range(1,8)},
          {A:F(1,14) for A in range(1,8)},
          {A:F(3*A,112) for A in range(1,8)},
          {A:F(3,4)*(F(1023,1024)*(F(1,4) if A in [1,2,4,7] else F(0))+F(1,7168)) for A in range(1,8)}]
    population=[0,1,7,23,105,150,232,255] if pilot else range(256)
    negative_control=None
    for table in population:
        values=[1 if table>>x&1 else -1 for x in range(8)]
        coeff=walsh(values);p={A:c*c for A,c in enumerate(coeff)}
        for i in range(3):
            children=[]
            for b in range(2):
                cv=[values[embed(x,i)|(b<<i)] for x in range(4)]
                childcoeff=walsh(cv)
                cp={embed(A,i):c*c for A,c in enumerate(childcoeff)}
                for A,c in enumerate(childcoeff):
                    T=embed(A,i)
                    ck(c==coeff[T]+(-1)**b*coeff[T|(1<<i)],('restriction coefficients',table,i,b,A))
                children.append(cp)
            v=1-p[0];w=p[1<<i];V=v-w
            v0,v1=[1-c[0] for c in children]
            ck((v0+v1)/2==V,('averaged variance',table,i))
            for ri,q in enumerate(refs):
                qp=project(q,i)
                ck(sum(qp.values())==(sum(q.values())-q[1<<i])/(1-q[1<<i]),'cemetery mass')
                parent=ce(p,q);c0=ce(children[0],qp);c1=ce(children[1],qp)
                delta=combine((parent,1),(c0,F(-1,2)),(c1,F(-1,2)))
                E,den=exp_exact(delta)
                ck(E>=1,('complete monotonicity',table,i,ri))
                independent=combine((entropy_terms([v,1-v]),1),
                                    (entropy_terms([v0,1-v0]),F(-1,2)),
                                    (entropy_terms([v1,1-v1]),F(-1,2)))
                put(independent,1/q[1<<i],w);put(independent,1/(1-q[1<<i]),V)
                for T in qp:
                    pair=q[T]+q[T|(1<<i)]
                    put(independent,pair/q[T],p[T]);put(independent,pair/q[T|(1<<i)],p[T|(1<<i)])
                residual=combine((delta,1),(independent,-1))
                ck(exp_exact(residual)[0]==1,('independent signed identity',table,i,ri))
                G=combine((entropy_terms([1-v,w,V]),1),(entropy_terms([V,1-V]),-1))
                J=combine((entropy_terms([V,1-V]),1),(entropy_terms([v0,1-v0]),F(-1,2)),(entropy_terms([v1,1-v1]),F(-1,2)))
                ck(exp_exact(G)[0]>=1,'categorical coarsening')
                ck(exp_exact(J)[0]>=1,'child binary Jensen')
                if table==232 and i==0 and ri==3:
                    wrong={T:(q[T]+q[T|1]) for T in qp}
                    bad=combine((parent,1),(ce(children[0],wrong),F(-1,2)),(ce(children[1],wrong),F(-1,2)))
                    bad_exp,bad_den=exp_exact(bad)
                    ck(bad_exp<1,'LIVE NEGATIVE CONTROL: unconditioned projection must fail')
                    negative_control={'table':232,'function':'Maj3','reference':3,'wrong_exp':str(bad_exp),'power':bad_den,'correct_exp':str(E),'correct_power':den}
    for q in refs:
        for order in permutations(range(3)):
            inherited=q.copy();D=0
            for i in order[:2]:
                inherited=project(inherited,i);D|=1<<i
                erased=sum(m for A,m in q.items() if A&~D==0)
                direct={}
                for A,m in q.items():
                    T=A&~D
                    if T:direct[T]=direct.get(T,F(0))+m/(1-erased)
                ck(inherited==direct,('original source order',order,D))
                ck(1-sum(inherited.values())==(1-sum(q.values()))/(1-erased),'original cemetery law')
    ck(negative_control is not None,'negative-control case read')
    return {'functions':len(population),'queries':len(population)*12,'source_orders':24,'negative_control':negative_control}

def fifth_root(x):
    scale=1<<32;lo=0;hi=scale
    while lo+1<hi:
        mid=(lo+hi)//2
        if mid**5*x.denominator<=x.numerator*scale**5:lo=mid
        else:hi=mid
    return F(lo,scale),F(hi,scale)
def visit_table(W):
    result={}
    for d in range(1,W+1):
        theta=[fifth_root(min(F(1),F(d,r))**6) for r in range(1,W+1)]
        subs={}
        for positions in combinations(range(W),d):
            lo=hi=F(1);mask=0
            for j in positions:lo*=theta[j][0];hi*=theta[j][1];mask|=1<<j
            subs[mask]=(lo,hi)
        zl=sum(v[0] for v in subs.values());zh=sum(v[1] for v in subs.values())
        for mask,(lo,hi) in subs.items():result[mask]=(lo/zh/F(2*d*(d+1)),hi/zl/F(2*d*(d+1)))
    return result

def central(pilot):
    physical=[];queue=[]
    for k in range(1,2 if pilot else 4):
        m=2*k;n=2*m;L=1<<n;side=(1<<m)-1
        vals=[2*int((x&side).bit_count()>=k and (x>>m).bit_count()>=k)-1 for x in range(L)]
        coeff=walsh(vals);p=[c*c for c in coeff]
        q=F(sum(comb(m,j) for j in range(k,m+1)),1<<m)
        a=F(comb(m,k),1<<m);vg=4*q*(1-q);ig=m*a
        infl=F(sum(vals[x]!=vals[x^(1<<i)] for i in range(n) for x in range(L)),L)
        ck(infl==2*q*ig,('central influence',k))
        sectors=[p[0],sum(p[A] for A in range(1,1<<m)),sum(p[A<<m] for A in range(1,1<<m)),sum(p[A] for A in range(L) if A&side and A>>m)]
        ck(sectors==[(2*q*q-1)**2,q*q*vg,q*q*vg,vg*vg/4],('sector masses',k))
        ck(2*(q*q*vg+vg*vg/4)==2*q*vg,('conditional entropy coefficient',k))
        if k<=2:
            for A,c in enumerate(coeff):
                direct=sum(v*(-1)**((A&x).bit_count()) for x,v in enumerate(vals))
                ck(c==F(direct,L),('independent character',k,A))
        # Independently factor every physical coefficient through threshold blocks.
        block=walsh([2*int(x.bit_count()>=k)-1 for x in range(1<<m)])
        for A,c in enumerate(coeff):
            u=A&side;v=A>>m
            if not A:pred=2*q*q-1
            elif not u:pred=q*block[v]
            elif not v:pred=q*block[u]
            else:pred=block[u]*block[v]/2
            ck(c==pred,('tensor spectrum',k,A))
        physical.append({'k':k,'n':n,'I':str(infl),'sectors':[str(x) for x in sectors]})
        if k>2:continue
        parts=[sum(1<<i for i in c) for c in combinations(range(m),k)]
        gates=[a|(b<<m) for a in parts for b in parts];N=len(gates);W=m;z=F(1,N*(1<<W));D=(1+z)**N-1
        visits=visit_table(W)
        orders=[]
        for j,g in enumerate(gates):
            order=[i for i in range(n) if g>>i&1];rot=j%W;orders.append(order[rot:]+order[:rot])
        def vv(j,B):
            local=sum(1<<r for r,i in enumerate(orders[j]) if B>>i&1)
            return visits[local]
        e0=sum(1<<i for i in range(k));e0|=e0<<m
        e1=((1<<n)-1)^e0
        r0=gates.index(e0);r1=gates.index(e1)
        total_hi=F(0);ngood=nbad=0
        for A in range(1,L):
            a=(A&side).bit_count();b=(A>>m).bit_count();d=a+b
            compatible=[j for j,g in enumerate(gates) if A&~g==0]
            good=(a<=k and b<=k)
            ck(len(compatible)==(comb(m-a,k-a)*comb(m-b,k-b) if good else 0),('actual prime count',k,A))
            if good:
                ngood+=1;lo=sum(vv(j,A)[0] for j in compatible)*z/D;hi=sum(vv(j,A)[1] for j in compatible)*z/D
                ck(lo**5>=F(d,W)**(6*d)*F(1,1<<(55*d)),('full compatible good lower bound',k,A))
            else:
                nbad+=1;b0=A&e0;b1=A&e1
                ck(b0>0 and b1>0,'disjoint original roots own nonempty sets')
                lo=z*z/D*vv(r0,b0)[0]*vv(r1,b1)[0];hi=z*z/D*vv(r0,b0)[1]*vv(r1,b1)[1]
                ck(lo>=F(1,1<<(1+13*m)),('full bad lower bound',k,A))
                ck(1+13*m<26*d,('fallback paid by size',k,A))
            ck(lo>0 and lo<=hi,'positive bounded selected event')
            total_hi+=hi
        ck(total_hi<=1,'all output-event upper sum is subprobability')
        queue.append({'k':k,'outputs':L-1,'good':ngood,'bad':nbad,'selected_mass_upper':str(total_hi)})
    if not pilot:
        for k in range(1,13):
            m=2*k;N=comb(m,k)**2
            for a in range(k+1):
                for b in range(k+1):
                    G=comb(m-a,k-a)*comb(m-b,k-b)
                    ck(F(G,N)==F(comb(k,a),comb(m,a))*F(comb(k,b),comb(m,b)),'compatible fraction identity')
                    if a:ck(F(comb(k,a))>=F(k,a)**a,'binomial lower bound')
                    if b:ck(F(comb(k,b))>=F(k,b)**b,'binomial lower bound')
                    ck(F(G,N)>=F(1,6**(a+b)),'rational compatible-name envelope')
    return {'physical':physical,'queue':queue,'threshold_FEI_dependency':'Established threshold Theorem A, Creg<9; analytic review is conditional only on this accepted source baseline'}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');args=ap.parse_args()
    result={'helper':'A015-SUBPROB-TRANSPORT-AND-CENTRAL-REVIEW@1','pilot':args.pilot,
            'transport':transport(args.pilot),'central':central(args.pilot)}
    result['assertions']=COUNT;result['elapsed_seconds']=round(time.monotonic()-START,4)
    result['script_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out=ROOT/'out';out.mkdir(exist_ok=True)
    dest=out/('pilot.json' if args.pilot else 'checks.json')
    dest.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'PASS','assertions':COUNT,'elapsed_seconds':result['elapsed_seconds'],'output':dest.name}))
if __name__=='__main__':main()
