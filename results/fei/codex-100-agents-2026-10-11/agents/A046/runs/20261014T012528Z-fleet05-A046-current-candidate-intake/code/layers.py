"""A046 layer-v1: exact grouped physical Fourier rows, not a collapsed input law."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,itertools,time,runpy
ROOT=Path(__file__).resolve().parents[1]
old=runpy.run_path(str(ROOT.parent/'20261011T214251Z-fleet05-A046-current-candidate-intake'/'code'/'exact_check.py'))
log= lru_cache(None)(old['log2']); fmt=old['outward']
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(c,a):return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def sub(a,b):return a[0]-b[1],a[1]-b[0]
ZERO=(Q(0),Q(0))
def term(x):return mul(-x,log(x)) if x else ZERO
def phi(a,b):
    if not a or not b:return ZERO
    total=a+b
    return add(mul(a,log(total/a)),mul(b,log(total/b)))
MONOMIALS=((3,1),(5,1),(7,-1),(14,1),(15,-1))
def density(w):return Q(0) if w is None else Q(1,2**w)
def coeff(ws,mask):
    ans=Q(0)
    for mon,c in MONOMIALS:
        if mask&mon!=mask:continue
        a=Q(c)
        for i,w in enumerate(ws):
            if mon>>i&1:a*=density(w)
        ans+=a
    return ans
def rows(ws):
    active=[i for i,w in enumerate(ws) if w is not None and w>0]
    for bits in range(2**len(active)):
        mask=0; count=1
        for k,i in enumerate(active):
            if bits>>k&1:mask|=1<<i;count*=2**ws[i]-1
        yield mask,count
@lru_cache(None)
def H(ws):
    out=ZERO; total=Q(0)
    for mask,count in rows(ws):
        a=coeff(ws,mask)
        for core in (0,1):
            f=a if core else Q(mask==0)-a
            total+=count*f*f;out=add(out,mul(count,term(f*f)))
    assert total==1
    return out
def branch(ws,i,b):
    vv=list(ws);vv[i]=ws[i]-1 if b else None;return tuple(vv)
@lru_cache(None)
def node(ws,i):
    a,b=branch(ws,i,0),branch(ws,i,1)
    residual=list(ws);residual[i]-=1;residual=tuple(residual)
    B=ZERO;hq=ZERO;total=Q(0);d=Q(0)
    for mask,count in rows(residual):
        ca,cb=coeff(a,mask),coeff(b,mask)
        for core in (0,1):
            g=ca if core else Q(mask==0)-ca
            h=cb if core else Q(mask==0)-cb
            u=(g+h)/2;v=(g-h)/2
            x,y=u*u,v*v; q=x+y
            B=add(B,mul(count,phi(x,y)));hq=add(hq,mul(count,term(q)))
            total+=count*q;d+=count*y
    assert total==1
    J=sub(hq,mul(Q(1,2),add(H(a),H(b))))
    return B,J,d
@lru_cache(None)
def tree(ws):
    # Query separator, then conjunction on failure, or U then V on success.
    if ws[0] is not None and ws[0]>0:i=0
    elif ws[0] is None:
        if any(ws[k] is None for k in (1,2,3)):return ZERO,Q(0),ZERO
        i=next((k for k in (3,1,2) if ws[k]>0),None)
    else:
        if ws[1]==0 or ws[2]==0:return ZERO,Q(0),ZERO
        if ws[1] is None and ws[2] is None:return ZERO,Q(0),ZERO
        i=next((k for k in (1,2) if ws[k] is not None and ws[k]>0),None)
    if i is None:return ZERO,Q(0),ZERO
    B,J,d=node(ws,i)
    a,b=tree(branch(ws,i,0)),tree(branch(ws,i,1))
    Js=add(J,mul(Q(1,2),add(a[0],b[0])))
    removed=d+(a[1]+b[1])/2
    Bs=add(B,mul(Q(1,2),add(a[2],b[2])))
    return Js,removed,Bs
def explicit(ws):
    widths=[int(x) for x in ws];n=sum(widths)+1; values=[]
    for x in range(2**n):
        offset=0;pts=[]
        for w in widths:pts.append((x>>offset)&(2**w-1)==0);offset+=w
        S,U,V,W=pts;A=(S and (U or V))or(W and U and V)
        g=-1 if x>>offset&1 else 1;values.append(g if A else 1)
    arr=values[:];h=1
    while h<len(arr):
        for k in range(0,len(arr),2*h):
            for j in range(k,k+h):u,v=arr[j],arr[j+h];arr[j],arr[j+h]=u+v,u-v
        h*=2
    # The common parity sign is irrelevant to all squared row masses.
    for mask,count in rows(ws):
        for core in (0,1):
            inds=[];off=0
            for i,w in enumerate(widths):
                inds.extend([off] if mask>>i&1 else []);off+=w
            if core:inds.append(off)
            freq=sum(1<<i for i in inds);a=coeff(ws,mask)
            expected=a if core else Q(mask==0)-a
            assert Q(arr[freq],len(arr))**2==expected**2
    directI=sum(Q(sum(values[x]!=values[x^(1<<i)] for x in range(len(values))),len(values)) for i in range(n))
    return directI
def main():
    start=time.perf_counter();results=[];checks=0;badcount=0
    for s,L,r in itertools.product((1,4,8),(1,3),(2,4,8)):
        R=T=r; q=Q(1,2**r);eta=Q(1,2**(L+2*r));beta=2*q-q*q;e=beta-eta;alpha=Q(1,2**s)
        JB=(L+2*r)*eta;JC=2*r*q*(1-q);JD=JB+JC;pi=eta+alpha*e
        Isep=s*alpha*e;Iother=(1-alpha)*JB+alpha*JC;Iter=pi
        I=Isep+Iother+Iter
        m=(r+1).bit_length()+2 # ceil(log2(r+2))+2 for integer r+2
        Qbad=Q(0);layers=[]
        for j in range(1,s+1):
            B,J,d=node((j,r,r,L),0);assert d==e/Q(2**j);checks+=1
            margin=sub(B,(4*d,4*d))
            assert margin[0]>0 or margin[1]<0,'unresolved sign'
            bad=margin[0]>0;badcount+=bad
            rho=Q(1,2**(j-1));cost=rho*(JD+(j-1)*e+e)/2
            weight=Q(1,2**(s-j))
            if bad:Qbad+=weight*cost
            if j>m:assert not bad;checks+=1
            layers.append({'j':j,'d':str(d),'B_over_d':fmt(mul(1/d,B)),'B_minus_4d_interval':fmt(margin),'bad':bad,'face_price':str(cost),'reach':str(weight)})
        mm=min(s,m);cap=alpha*(mm*JD+e*mm*(mm-1)/2+mm*e)
        assert Qbad<=cap<=mm*I;checks+=2
        Jtree,removed,Btree=tree((s,r,r,L));assert removed==Isep+Iother;checks+=1
        output_info=sub(old['entropy']([pi/2,1-pi/2]),(pi,pi))
        conversion=sub(Jtree,output_info)
        # Analytic JS payment is checked with strict outward sign here.
        ln2lo,ln2hi=old['ln_unit'](Q(2));paid=(2*removed/ln2hi,2*removed/ln2lo)
        assert sub(paid,Jtree)[0]>=0;checks+=1
        # Direct B+J entropy telescope; interval overlap is corroboration only.
        residual=sub(sub(H((s,r,r,L)),Btree),Jtree)
        assert residual[0]<=0<=residual[1];checks+=1
        results.append({'s':s,'L':L,'R':r,'T':r,'gamma':str(e/2),'cutoff_m':m,'I':str(I),'removed_control_influence':str(removed),'terminal_influence':str(pi),'terminal_entropy_dictator':0,'terminal_entropy_general_balanced_core':'pi H(g), retained analytically','Q_bad':str(Qbad),'cutoff_full_price_cap':str(cap),'conversion_interval':fmt(conversion),'layers':layers})
        (ROOT/'out'/'RESULTS.json').write_text(json.dumps({'status':'IN_PROGRESS','roots':results},indent=2)+'\n',encoding='utf-8')
        if time.perf_counter()-start>55:raise SystemExit('budget stop: results remain partial')
    direct=[]
    for s,L,r in itertools.product((1,2),(1,2),(1,2)):
        q=Q(1,2**r);eta=Q(1,2**(L+2*r));e=2*q-q*q-eta;a=Q(1,2**s)
        I=s*a*e+(1-a)*(L+2*r)*eta+a*2*r*q*(1-q)+eta+a*e
        assert explicit((s,r,r,L))==I;checks+=1;direct.append([s,L,r])
    summary={'status':'PASS','roots':len(results),'separator_node_occurrences':sum(len(x['layers']) for x in results),'bad_separator_occurrences':badcount,'exact_assertions':checks,'direct_truth_table_roots':len(direct),'runtime_seconds':time.perf_counter()-start,'arithmetic':'Fraction grouped Walsh coefficients, exact multiplicities, rational 24-term atanh intervals','results':results}
    (ROOT/'out'/'RESULTS.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in summary.items() if k!='results'},indent=2))
if __name__=='__main__':main()
