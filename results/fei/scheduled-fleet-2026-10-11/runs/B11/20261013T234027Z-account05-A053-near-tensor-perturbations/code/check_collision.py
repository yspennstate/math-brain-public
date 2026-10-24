from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,hashlib
RUN=Path(__file__).resolve().parents[1]
START=time.perf_counter(); assertions=0; comparisons=0
def check(ok):
    global assertions
    assertions+=1
    assert ok, assertions
    if time.perf_counter()-START>55: raise RuntimeError('55-second frozen guard')
def save(name,obj): (RUN/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
@lru_cache(None)
def ln_unit(x):
    z=(x-1)/(x+1); zz=z*z; power=z; value=F(0)
    for k in range(24): value+=2*power/(2*k+1); power*=zz
    tail=2*abs(power)/(49*(1-zz))
    return value-tail,value+tail
LN2=ln_unit(F(2))
@lru_cache(None)
def log2(x):
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    scale=F(2)**k; r=x/scale
    if r<1:k-=1;r*=2
    if r>=2:k+=1;r/=2
    lo,hi=ln_unit(r)
    return F(k)+lo/LN2[1],F(k)+hi/LN2[0]
def add(*es):
    out={}
    for e in es:
        for x,c in e.items():out[x]=out.get(x,F(0))+c
    return {x:c for x,c in out.items() if c and x!=1}
def mul(e,c):return {x:v*c for x,v in e.items() if v*c}
def bounds(e):
    lo=hi=F(0)
    for x,c in e.items():
        a,b=log2(x)
        lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
    return lo,hi
def entropy(ps):return add(*[{p:-p} for p in ps if p])
def walsh(table):
    size=len(table)
    return [F(sum(table[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(size)),size) for s in range(size)]
def data(table):
    n=(len(table)-1).bit_length(); c=walsh(table); ps=[x*x for x in c]
    inf=[F(sum(table[x]!=table[x^(1<<i)] for x in range(len(table))),len(table)) for i in range(n)]
    check(sum(ps)==1)
    for i in range(n):check(inf[i]==sum(ps[s] for s in range(len(ps)) if s>>i&1))
    return c,ps,inf,entropy(ps)
def embed(x,coords):return sum(((x>>j)&1)<<i for j,i in enumerate(coords))
def block(table,mask):
    n=(len(table)-1).bit_length(); A=[i for i in range(n) if mask>>i&1];C=[i for i in range(n) if not(mask>>i&1)]
    d=1<<len(A); e=1<<len(C);c,ps,inf,H=data(table)
    children=[[table[embed(x,A)|embed(y,C)] for y in range(e)] for x in range(d)]
    cds=[data(t) for t in children];rows=[[cds[x][0][t] for x in range(d)] for t in range(e)]
    qs=[sum(w*w for w in row)/d for row in rows]
    qdirect=[sum(ps[embed(u,A)|embed(t,C)] for u in range(d)) for t in range(e)]
    check(qs==qdirect);check(sum(qs)==1)
    joint=[[w*w/d for w in row] for row in rows]
    Gamma={}
    for q,row in zip(qs,rows):
        if q:
            rat=sum(w**4 for w in row)/d/q**2
            check(1<=rat<=d)
            Gamma=add(Gamma,{rat:q})
    B=add(H,mul(entropy(qs),-1));childH=add(*[mul(z[3],F(1,d)) for z in cds])
    J=add(entropy(qs),mul(childH,-1));L=add(H,mul(childH,-1))
    IA=sum(inf[i] for i in A);I=sum(inf)
    check(I==IA+sum(sum(z[2]) for z in cds)/d)
    return dict(H=H,I=I,IA=IA,B=B,J=J,L=L,Gamma=Gamma,V=add(B,Gamma),joint=joint,rows=rows,qs=qs,children=cds,a=len(A),n=n)
def sqrt_compare(left,coefficient,q):
    # left <= coefficient*sqrt(q), exactly, without evaluating a square root.
    if coefficient>=0:
        return left<=0 or left*left<=coefficient*coefficient*q
    return left<0 and left*left>=coefficient*coefficient*q
def compare(f,g,mask,product_h=None):
    global comparisons
    b=block(f,mask);c=block(g,mask);a=b['a'];n=b['n'];m=n-a;p=F(1,1<<n)
    delta=sum(abs(x-y) for row,row2 in zip(b['joint'],c['joint']) for x,y in zip(row,row2))/2
    check(delta**2<=F(4,1<<(2*a+m))*(1-F(1,1<<m)))
    diff=add(c['Gamma'],mul(b['Gamma'],-1));lo,hi=bounds(diff)
    if delta:
        # Rational overestimate of sqrt(d) and 1/ln 2, used only for validation.
        lip=F(a)+F(3,2)*((1<<((a+1)//2))+1)
        check(lo>=-lip*delta and hi<=lip*delta)
    else:check(b['joint']==c['joint'] and not diff)
    maxdiff=max(abs(lo),abs(hi))
    check(maxdiff**2<=100*p)
    check(abs(c['IA']-b['IA'])<=2*a*p)
    if product_h is not None:
        sqerr=F(0)
        for row,oldrow,q,oq in zip(c['rows'],b['rows'],c['qs'],b['qs']):
            if not q:continue
            # Old rows equal +/-sqrt(oq) h. Zero rows use h.
            r=sum(x*y for x,y in zip(oldrow,product_h))/(1<<a)
            phase=[v*(1 if r>=0 else -1) for v in product_h]
            check(all(w==abs(r)*v for w,v in zip(oldrow,phase)))
            err=sum((w-v)**2 for w,v in zip(row,oldrow))/(1<<a)
            overlap=sum(w*v for w,v in zip(row,phase))/(1<<a)
            check(sqrt_compare(2*q-4*err,2*overlap,q))
            sqerr+=err
        check(sqerr==4*p)
        check(not b['Gamma'])
    comparisons+=1
    return b,c,delta
def nandtree(tree,bits):
    if tree==():return next(bits)
    vals=[nandtree(t,bits) for t in tree]
    return -1 if all(v==1 for v in vals) else 1
def serexpr(e):return {str(x):str(c) for x,c in e.items()}
def interval(e):return [str(v) for v in bounds(e)]
def run():
    small=0
    for n in (2,3):
        for code in range(1<<(1<<n)):
            f=[-1 if code>>x&1 else 1 for x in range(1<<n)];g=f.copy();g[0]*=-1
            for mask in range(1,(1<<n)-1):compare(f,g,mask);small+=1
    products=0
    for hcode in range(1,15):
        h=[-1 if hcode>>x&1 else 1 for x in range(4)]
        for kcode in range(1,15):
            k=[-1 if kcode>>x&1 else 1 for x in range(4)]
            f=[h[x&3]*k[x>>2] for x in range(16)];g=f.copy();g[0]*=-1
            compare(f,g,3,h);products+=1
    tree=((((((),()),(),()),()),()))
    f=[nandtree(tree,iter([1 if x>>i&1 else -1 for i in range(6)])) for x in range(64)]
    # Signs/bit orientation must match the pinned source; validate its selected row coefficients.
    base=block(f,48)
    check(base['rows'][0]==[F(1),F(1),F(-1),F(5,8)])
    check(base['I']==F(5,4) and base['IA']==1)
    check(bounds(base['V'])[1]<F(47,20))
    check(bounds(add(base['H'],mul({F(2):F(12,5)},-base['I'])))[0]>0)
    cases=[];cheap=0;debt=0
    for v in range(64):
        g=f.copy();g[v]*=-1
        selected=None;singletons=[]
        for mask in (48,1,2,4,8,16,32):
            b,c,delta=compare(f,g,mask)
            residual=add(mul(c['V'],c['I']),mul(c['H'],-c['IA']))
            lo,hi=bounds(residual)
            if mask==48:
                childres=[add(mul(z[3],c['I']),mul(c['H'],-sum(z[2]))) for z in c['children']]
                positive=[i for i,e in enumerate(childres) if bounds(e)[0]>0]
                if hi<0:cheap+=1;check(bool(positive));debt+=1
                selected={'cost_minus_root_times_I':interval(residual),'positive_child_assignments':positive,'Gamma':serexpr(c['Gamma']),'joint_TV':str(delta),'V':interval(c['V']),'I_A':str(c['IA']),'H':interval(c['H']),'I':str(c['I'])}
            else:singletons.append({'mask':mask,'cost_minus_root_times_I':interval(residual)})
        cases.append({'edited_vertex':v,'selected':selected,'singletons':singletons})
        save('NAND_SURGERIES.json',{'status':'IN_PROGRESS','completed':v+1,'cases':cases})
    save('NAND_SURGERIES.json',{'status':'PASS','selected_mask':48,'strictly_affordable_surgeries':cheap,'affordable_with_positive_child_debt':debt,'cases':cases})
    save('EXACT_CHECK.json',{'status':'PASS','assertions':assertions,'comparisons':comparisons,'small_cut_comparisons':small,'product_phase_comparisons':products,'NAND_surgery_cut_comparisons':448,'strictly_affordable_NAND_surgeries':cheap,'runtime_seconds':time.perf_counter()-START,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic':'integer character sums, Fraction, 24-term rational atanh enclosures with explicit tail; no floating sign decisions'})
    print((RUN/'out'/'EXACT_CHECK.json').read_text())
if __name__=='__main__':run()
