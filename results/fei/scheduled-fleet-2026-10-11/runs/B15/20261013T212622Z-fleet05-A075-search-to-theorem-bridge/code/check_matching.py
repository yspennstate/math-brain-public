from pathlib import Path
from fractions import Fraction as Q
from math import comb, isqrt
from functools import lru_cache
import json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0
def ck(x):
    global checks
    assert x
    checks+=1
def add(a,b,c=Q(1)):
    r=a.copy()
    for x,v in b.items():
        r[x]=r.get(x,Q(0))+c*v
        if not r[x]: del r[x]
    return r
@lru_cache(None)
def logform(z):
    if z<=1: return {}
    # Small integers are prime-factorized; large integers remain explicit log arguments.
    if z>1000000:
        a=isqrt(z)
        if a*a==z: return {x:2*c for x,c in logform(a).items()}
        return {z:Q(1)}
    r={}; p=2
    while p*p<=z:
        while z%p==0: r[p]=r.get(p,Q(0))+1; z//=p
        p+=1
    if z>1: r[z]=r.get(z,Q(0))+1
    return r
def G(a,b):
    r={}
    for z,c in [(a+b,a+b),(a,-a),(b,-b)]:
        if z: r=add(r,logform(z),Q(c))
    return r
def entropy(W):
    D=len(W)**2; out={2:Q(2*((len(W)-1).bit_length()))}
    for w in W:
        if w: out=add(out,logform(w*w),-Q(w*w,D))
    return out
P=192; SCALE=1<<P; TERMS=80
def ceildiv(a,b): return -(-a//b)
@lru_cache(None)
def ln_unit(a,b):
    ck(b<=a<=2*b)
    zn=a-b; zd=a+b
    zl=zn*SCALE//zd; zu=ceildiv(zn*SCALE,zd)
    z2l=zl*zl//SCALE; z2u=ceildiv(zu*zu,SCALE)
    tl,tu=zl,zu; lo=hi=0
    for j in range(TERMS):
        lo+=2*tl//(2*j+1); hi+=ceildiv(2*tu,2*j+1)
        tl=tl*z2l//SCALE; tu=ceildiv(tu*z2u,SCALE)
    hi+=ceildiv(2*SCALE*9,161*3**161*8)
    return Q(lo,SCALE),Q(hi,SCALE)
LN2=ln_unit(2,1)
@lru_cache(None)
def log_interval(z):
    if z==1: return Q(0),Q(0)
    e=z.bit_length()-1
    if z==1<<e: return Q(e),Q(e)
    lo,hi=ln_unit(z,1<<e)
    return e+lo/LN2[1],e+hi/LN2[0]
def enclose(expr):
    lo=hi=Q(0)
    for z,c in expr.items():
        a,b=log_interval(z)
        lo+=c*(a if c>=0 else b); hi+=c*(b if c>=0 else a)
    return lo,hi
def scale(expr,c): return {x:v*c for x,v in expr.items() if v*c}
def forms(expr): return {str(x):str(c) for x,c in sorted(expr.items())}
def packet_hist_add(hist,a,b,m=1):
    pair=tuple(sorted((a*a,b*b)))
    hist[pair]=hist.get(pair,0)+m
def compressed(k,l,typ):
    r=2*k+l; a=1+3*k+l; N=1<<r
    hist={}
    if typ=='paired':
        ck(k>0); delta=a-4
        for u in range(k):
            for v in range(l+1):
                mult=comb(k-1,u)*3**u*comb(l,v)
                L=a-4*u-2*v
                if u==v==0: packet_hist_add(hist,N-2*a,-2*(L-4))
                else: packet_hist_add(hist,-2*L,-2*(L-4),mult)
                packet_hist_add(hist,-2*(L-4),-2*(L-4),mult)
    else:
        ck(l>0); delta=a-2
        for u in range(k+1):
            for v in range(l):
                mult=comb(k,u)*3**u*comb(l-1,v)
                L=a-4*u-2*v
                if u==v==0: packet_hist_add(hist,N-2*a,-2*(L-2))
                else: packet_hist_add(hist,-2*L,-2*(L-2),mult)
    ck(sum(hist.values())==N//2)
    B={}
    for (x,y),m in hist.items(): B=add(B,G(x,y),Q(m,N*N))
    d=Q(2*delta,N)
    return hist,B,d
def Aset(k,l):
    r=2*k+l
    return {0}|{1<<i for i in range(r)}|{(1<<(2*j))|(1<<(2*j+1)) for j in range(k)}
def fwht(t):
    a=list(t); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for x in range(j,j+h): a[x],a[x+h]=a[x]+a[x+h],a[x]-a[x+h]
        h*=2
    return a
def certify_table(t):
    W=fwht(t); N=len(t); r=(N-1).bit_length()
    ck(sum(w*w for w in W)==N*N)
    ds=[]; bs=[]; hs=[]
    for i in range(r):
        direct=Q(2*sum(t[x]!=t[x|(1<<i)] for x in range(N) if not(x>>i&1)),N)
        spectral=Q(sum(W[x]**2 for x in range(N) if x>>i&1),N*N)
        ck(direct==spectral); ds.append(direct)
        hist={}
        for x in range(N):
            if not(x>>i&1): packet_hist_add(hist,W[x],W[x|(1<<i)])
        hs.append(hist)
        B={}
        for (a,b),m in hist.items(): B=add(B,G(a,b),Q(m,N*N))
        bs.append(B)
    return W,ds,bs,hs
def restriction_kind(A,r,i,value):
    free=[j for j in range(r) if j!=i]
    Ar={sum(((x>>j)&1)<<s for s,j in enumerate(free)) for x in A if (x>>i&1)==value}
    if not Ar or len(Ar)==1<<(r-1): return 'constant'
    if value:
        ck(Ar=={0} or (len(Ar)==2 and 0 in Ar and max(Ar).bit_count()==1))
        return 'point-defect-with-possible-dummy'
    ck(0 in Ar and all(x.bit_count()<=2 for x in Ar))
    edges=[x for x in Ar if x.bit_count()==2]
    ck(all(not(a&b) for s,a in enumerate(edges) for b in edges[s+1:]))
    ck({x for x in Ar if x.bit_count()==1}=={1<<j for j in range(r-1)})
    return 'partial-matching'

finite=[]; child_count=0; parameter_count=0; all_ratio_upper=Q(0); worst_row=None
for r in range(10):
    for k in range(r//2+1):
        l=r-2*k; A=Aset(k,l); N=1<<r
        t=[-1 if x in A else 1 for x in range(N)]
        W,ds,bs,hists=certify_table(t); a=len(A)
        ck(a==1+3*k+l)
        for s,w in enumerate(W):
            u=sum(bool(s & (3<<(2*j))) for j in range(k))
            v=sum(bool(s>>j&1) for j in range(2*k,r))
            ck(w==(N-2*a if s==0 else -2*(a-4*u-2*v)))
        ratios=[]
        for i in range(r):
            typ='paired' if i<2*k else 'isolated'
            hist,B,d=compressed(k,l,typ)
            ck(hist==hists[i]); ck(B==bs[i]); ck(d==ds[i])
            if d:
                e=scale(B,1/d); low,high=enclose(e)
                ck(high<4)
                ratios.append({'i':i,'type':typ,'I_i':str(d),'ratio_form':forms(e),'lo':str(low),'hi':str(high)})
                if high>all_ratio_upper: all_ratio_upper=high; worst_row=(r,k,l,i,float((low+high)/2))
            for val in [0,1]:
                kind=restriction_kind(A,r,i,val)
                free=[j for j in range(r) if j!=i]
                child=[t[(val<<i)|sum(((y>>j)&1)<<bit for j,bit in enumerate(free))] for y in range(N//2)]
                cw,cd,cb,ch=certify_table(child)
                # Independently check true physical entropy decrement identity.
                ck(all(2*cw[y]==W[sum(((y>>j)&1)<<bit for j,bit in enumerate(free))]+(1 if val==0 else -1)*W[sum(((y>>j)&1)<<bit for j,bit in enumerate(free))|(1<<i)] for y in range(N//2)))
                child_count+=1
        finite.append({'r':r,'k':k,'l':l,'a':a,'ratios':ratios}); parameter_count+=1
ck(parameter_count==30)
(ROOT/'out'/'FINITE_HEREDITARY.json').write_text(json.dumps({'parameter_pairs':parameter_count,'physical_children':child_count,'all_coordinate_upper_below_four':True,'worst_row_display_only':worst_row,'roots':finite},indent=2)+'\n',encoding='utf-8')

point_defects=[]
for r in range(1,10):
    t=[-1]+[1]*((1<<r)-1); W,ds,bs,hs=certify_table(t)
    if ds[0]:
        expr=scale(bs[0],1/ds[0]); lo,hi=enclose(expr); ck(hi<4)
        point_defects.append({'dimension':r,'ratio_form':forms(expr),'lo':str(lo),'hi':str(hi)})
(ROOT/'out'/'POINT_DEFECTS.json').write_text(json.dumps(point_defects,indent=2)+'\n',encoding='utf-8')

roots=[]; incumbent=None
for k in range(2,33):
    l=0; r=2*k; N=1<<r; a=3*k+1; delta=a-4
    hist,B,d=compressed(k,0,'paired'); E=scale(B,1/d); lo,hi=enclose(E)
    spectrum={}
    for u in range(k+1):
        count=comb(k,u)*3**u; L=a-4*u
        if u==0: spectrum[(N-2*a)**2]=spectrum.get((N-2*a)**2,0)+1
        else: spectrum[4*L*L]=spectrum.get(4*L*L,0)+count
    ck(sum(spectrum.values())==N); ck(sum(sq*m for sq,m in spectrum.items())==N*N)
    H={2:Q(2*r)}
    for sq,m in spectrum.items():
        if sq: H=add(H,logform(sq),-Q(sq*m,N*N))
    HI=scale(H,1/(r*d)); hlo,hhi=enclose(HI)
    lower=Q(2*a,delta)-Q(2*(a*a+delta*delta),delta*N)-Q(8,delta)/LN2[0]
    upper=Q(2*a,delta)+Q(2*delta,N)*(2*r+Q(3,2))
    ck(lo>=lower); ck(hi<=upper)
    row={'k':k,'dimension':r,'a':a,'I_i':str(d),'E_form':forms(E),'E_interval':[str(lo),str(hi)],'E_display':float((lo+hi)/2),'H_over_I_interval':[str(hlo),str(hhi)],'H_over_I_display':float((hlo+hhi)/2),'analytic_E_lower':str(lower),'analytic_E_upper':str(upper)}
    roots.append(row)
    if incumbent is None or lo>Q(incumbent['E_interval'][1]): incumbent=row
    (ROOT/'out'/'MATCHING_ROOTS.json').write_text(json.dumps({'frozen_domain':'k=2,...,32; no claim of all-k maximum','incumbent':incumbent,'roots':roots},indent=2)+'\n',encoding='utf-8')
expected={2:Q(16,3),3:Q(-21,8),5:Q(95,24),11:Q(-121,24),13:Q(65,24)}
ck({int(x):Q(v) for x,v in roots[1]['E_form'].items()}==expected)
ck(all(Q(incumbent['E_interval'][0])>Q(row['E_interval'][1]) for row in roots if row['k']!=incumbent['k']))
ck(Q(368,125)<Q(roots[1]['E_interval'][0]))
# All-dimensional rough bound at r=10 and monotonic polynomial tail.
ck(2+Q(8,7)+Q(43,64)<4)
ck(Q(3,2)>1/LN2[0])
ck(Q(15,4)<4)
out={'helper_version':'A075-matching-v1','exact_assertions':checks,'direct_parameter_pairs':parameter_count,'physical_children_checked':child_count,'compressed_matching_roots':31,'finite_matching_max_dimension':incumbent['dimension'],'finite_matching_max_E_display':incumbent['E_display'],'finite_matching_max_interval':incumbent['E_interval'],'finite_hereditary_max_row_display':worst_row,'all_small_descendant_coordinates_B_over_I_below_four':True,'analytic_limits':{'perfect_matching_E':'2','perfect_matching_H_over_I':'4'},'runtime_seconds':time.perf_counter()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'verdict_arithmetic':'Integer/Fraction and outward fixed-point logarithm enclosures; display floats not used for decisions'}
ck(time.perf_counter()-start<60)
(ROOT/'out'/'VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
