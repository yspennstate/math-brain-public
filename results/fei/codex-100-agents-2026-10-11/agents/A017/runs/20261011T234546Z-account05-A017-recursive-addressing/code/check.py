"""A017-point-surgery-v1.1: exact compressed physical-cube certificates."""
from pathlib import Path
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
import argparse
import hashlib
import json
import time

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
CHECKS=0
ROOT_CASES=0
TREE_CASES=0
DIGEST=hashlib.sha256()
FACTORS={}
LOGS={}

def req(ok, context=''):
    global CHECKS
    CHECKS+=1
    if not ok: raise AssertionError((CHECKS,ROOT_CASES,TREE_CASES,context))

def parity(x): return x.bit_count()&1

def rank(rows):
    piv={}
    for v in rows:
        while v:
            j=v.bit_length()-1
            if j in piv: v^=piv[j]
            else: piv[j]=v; break
    return len(piv)

def kernel(rows,n):
    basis=[]
    for v in range(1<<n):
        if all(parity(v&r)==0 for r in rows) and rank(basis+[v])>len(basis): basis.append(v)
    return basis

def parameters(n,code):
    linear=code&((1<<n)-1)
    polar=[0]*n
    edges=[]
    for t,(i,j) in enumerate(( (i,j) for i in range(n) for j in range(i+1,n))):
        if (code>>(n+t))&1:
            edges.append((i,j)); polar[i]^=1<<j; polar[j]^=1<<i
    return linear,edges,polar

def poly_code(n,edges):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    return sum(1<<(n+pairs.index((i,j))) for i,j in edges)

def graph_codes(n):
    return [poly_code(n,[(i,i+1) for i in range(0,n-1,2)]),
            poly_code(n,[(i,i+1) for i in range(n-1)]),
            poly_code(n,[(0,i) for i in range(1,n)]),
            poly_code(n,[(i,j) for i in range(n) for j in range(i+1,n)])]

def addr(rows,x): return sum(parity(r&x)<<j for j,r in enumerate(rows))

def signs(n,linear,edges):
    return [(-1 if parity(x&linear)^(sum(((x>>i)&(x>>j)&1) for i,j in edges)&1) else 1) for x in range(1<<n)]

def fwht(vals):
    out=list(vals); h=1
    while h<len(out):
        for s in range(0,len(out),2*h):
            for j in range(s,s+h):
                u,v=out[j],out[j+h]; out[j],out[j+h]=u+v,u-v
        h*=2
    return out

def spectrum(g,labels):
    out={}
    for z in set(labels):
        out[z]=fwht([v if label==z else 0 for v,label in zip(g,labels)])
    return out

def factors(v):
    if v in FACTORS:return FACTORS[v]
    ret={}; d=2; x=v
    while d*d<=x:
        while x%d==0:ret[d]=ret.get(d,0)+1; x//=d
        d+=1
    if x>1:ret[x]=ret.get(x,0)+1
    FACTORS[v]=ret
    return ret

class LF:
    """Exact rational linear form in log2 primes; key 1 is a constant."""
    def __init__(self,const=0):self.d={1:F(const)} if const else {}
    def term(self,key,v):
        self.d[key]=self.d.get(key,F(0))+v
        if not self.d[key]:del self.d[key]
        return self
    def log(self,v,weight):
        if v<=1:return self
        for p,e in factors(v).items(): self.term(1 if p==2 else p,weight*e)
        return self
    def add(self,other,scale=1):
        for p,v in other.d.items():self.term(p,v*scale)
        return self
    def times(self,scale):return LF().add(self,scale)
    def __eq__(self,other):return self.d==other.d
    def interval(self):
        lo=hi=F(0)
        for p,c in self.d.items():
            a,b=(F(1),F(1)) if p==1 else log_interval(p)
            lo+=c*(a if c>=0 else b); hi+=c*(b if c>=0 else a)
        return lo,hi
    def json(self):
        lo,hi=self.interval()
        return dict(log2_prime_form={str(p):str(c) for p,c in sorted(self.d.items())},
                    interval=[str(lo),str(hi)],decimal_display=[float(lo),float(hi)])

def ln_interval(x,terms=32):
    z=(x-1)/(x+1); req(0<=z<1,'ln range')
    power=z; total=F(0)
    for j in range(terms):total+=2*power/(2*j+1); power*=z*z
    tail=2*power/((2*terms+1)*(1-z*z))
    return total,total+tail

LN2=ln_interval(F(2))

def log_interval(v):
    if v not in LOGS:
        m=v.bit_length()-1
        a,b=ln_interval(F(v,1<<m)); c,d=LN2
        LOGS[v]=(m+a/d,m+b/c)
    return LOGS[v]

def entropy_hist(hist,n):
    ret=LF(2*n)
    for w,count in hist.items():
        if w:ret.log(w,-F(2*count*w*w,1<<(2*n)))
    return ret

def entropy(spec,n):return entropy_hist(Counter(abs(w) for vals in spec.values() for w in vals if w),n)

def erasure(spec,n,i):
    ret=LF(); den=1<<(2*n)
    for vals in spec.values():
        for u in range(1<<n):
            if (u>>i)&1:continue
            a,b=vals[u]**2,vals[u^(1<<i)]**2
            if a and b:
                ret.log(a+b,F(a+b,den)).log(a,-F(a,den)).log(b,-F(b,den))
    return ret

def spectral_metrics(spec,n):
    den=1<<(2*n)
    inf=[0]*n; pairs={(i,j):0 for i in range(n) for j in range(i+1,n)}
    control_charge=[0]*n; data_charge={}
    for z,vals in spec.items():
        degree=0
        for u,w in enumerate(vals):
            if not w:continue
            square=w*w; d=u.bit_count(); degree+=d*square
            ids=[i for i in range(n) if (u>>i)&1]
            for i in ids:inf[i]+=square; control_charge[i]+=2*d*square
            for i,j in ((i,j) for i in ids for j in ids if i<j):pairs[i,j]+=square
        data_charge[z]=F(2*degree,den)
    return [F(v,den) for v in inf],{ij:F(v,den) for ij,v in pairs.items()},[F(v,den) for v in control_charge],data_charge

def physical(g,labels,n):
    size=1<<n; inf=[]; pairs={}; data_charge=defaultdict(F)
    for i in range(n):
        s=F(0)
        for x in range(size):
            v=x^(1<<i)
            if labels[x]!=labels[v]:
                s+=F(1,2)
                data_charge[labels[x]]+=F(1,2*size)
                data_charge[labels[v]]+=F(1,2*size)
            else:
                sq=(g[x]-g[v])**2
                s+=F(sq,4)
                data_charge[labels[x]]+=F(sq,2*size)
        inf.append(s/size)
    for i in range(n):
        for j in range(i+1,n):
            total=0
            for x in range(size):
                coeff=defaultdict(int)
                for v,sgn in [(x,1),(x^(1<<i),-1),(x^(1<<j),-1),(x^(1<<i)^(1<<j),1)]:
                    coeff[labels[v]]+=sgn*g[v]
                total+=sum(v*v for v in coeff.values())
            pairs[i,j]=F(total,16*size)
    return inf,pairs,dict(data_charge)

def surgery_hist(D,k):
    plus=((1<<k)+(1<<(k//2)))//2
    minus=((1<<k)-(1<<(k//2)))//2
    A=1<<(D-k//2)
    out=Counter()
    for v,count in [(abs(A-2),plus),(A+2,minus),(2,(1<<D)-(1<<k))]:
        if v and count:out[v]+=count
    return out

def root_check(n,rows,qcode,boundary_sample=False):
    global ROOT_CASES
    linear,edges,Q=parameters(n,qcode); r=rank(rows)
    basis=kernel(rows,n)
    restricted=[sum((sum(parity(Q[i]&v) for i in range(n) if (u>>i)&1)&1)<<j for j,v in enumerate(basis)) for u in basis]
    k=rank(restricted); req(k%2==0)
    b=signs(n,linear,edges); labels=[addr(rows,x) for x in range(1<<n)]
    g=b.copy();g[0]=-g[0]
    spec=spectrum(g,labels);size=1<<n
    req(sum(w*w for vals in spec.values() for w in vals)==size*size)
    A=1<<(n-r-k//2)
    expected=Counter({A:((1<<r)-1)*(1<<(r+k))})
    for v,count in surgery_hist(n-r,k).items(): expected[v]+=(1<<r)*count
    expected=+expected
    req(Counter(abs(w) for vals in spec.values() for w in vals if w)==expected,'histogram')
    H=entropy(spec,n); Hfiber=entropy_hist(surgery_hist(n-r,k),n-r)
    target=LF(2*r+k).add(Hfiber,F(1,1<<r)).add(LF(k),-F(1,1<<r))
    req(H==target,'fiber entropy identity')
    inf,pairs,charge,dcharge=spectral_metrics(spec,n)
    p_inf,p_pairs,p_dcharge=physical(g,labels,n)
    req(inf==p_inf and pairs==p_pairs and dcharge==p_dcharge,'physical derivative moments')
    for i in range(n):
        active=any((row>>i)&1 for row in rows)
        base=F(1,2) if active or Q[i] else F((linear>>i)&1)
        expected_i=base if active else base+F(1-2*((linear>>i)&1),1<<(n-1))
        req(inf[i]==expected_i,'physical coordinate influence')
        req(charge[i]==2*(inf[i]+sum(pairs[min(i,j),max(i,j)] for j in range(n) if j!=i)),'boundary charge')
    req(sum(dcharge.values())==2*sum(inf),'data/control boundary sum')
    for z in set(labels):req(F(sum(w*w for w in spec[z]),size*size)==F(1,1<<r),'label normalization')
    ROOT_CASES+=1
    DIGEST.update(json.dumps([n,rows,qcode,{str(p):str(c) for p,c in H.d.items()},[str(v) for v in inf]],sort_keys=True).encode()+b'\n')
    if not boundary_sample:return
    # Matching, even n, prefix address rows: closed physical charge formulas.
    req(n%2==0 and rows==[1<<i for i in range(r)])
    delta=F(1,1<<n);L=n-r;t=r%2
    req(k==n-r-t)
    req(1+sum(inf)==1+F(n,2)+2*L*delta)
    for i in range(n):
        tau=int((i^1)>=r)
        predicted=F(n+1,2)+(2*L*delta if i<r else 2*delta*(n+1+2*tau))
        req(charge[i]==predicted,'closed control charge')
    for z in dcharge:
        w=((z>>(r-1))&1) if r%2 else 0
        predicted=F(r+k+2*w,1<<r)+(4*L*delta if z==0 else 0)
        req(dcharge[z]==predicted,'closed data charge')
    # Taylor approximation and an explicit rational error enclosure.
    D=n-r;p=F(1,1<<D);theta=F(1,1<<t)
    alpha_u_exponent=1-D+k//2
    if alpha_u_exponent<=-1:
        lnlo,lnhi=LN2
        coef=(4-12*theta)*delta
        leading=F(n+r-t)+4*delta*(1-theta)*(D+t-2)
        approx_lo=leading+coef/(lnhi if coef>=0 else lnlo)
        approx_hi=leading+coef/(lnlo if coef>=0 else lnhi)
        error=F(16*(1<<r),1<<(2*n))/lnlo
        hlo,hhi=H.interval()
        req(hlo>=approx_lo-error and hhi<=approx_hi+error,'Taylor enclosure')
    return dict(n=n,r=r,k=k,H=H.json(),I=str(1+sum(inf)),
                control_influence=[str(v) for v in inf],control_boundary=[str(v) for v in charge],
                data_boundary={str(z):str(v) for z,v in dcharge.items()},
                total_root_boundary=str(sum(charge)+sum(dcharge.values())),
                root_bad_boundary_K2='0',root_bad_reason='each control influence >=1/2, B_i<=1; data B_i=0')

def maps(n):
    return [[1<<i for i in range(n) if (mask>>i)&1] for mask in range(1<<n)]+[
        [(1<<n)-1], [sum(1<<i for i in range(n) if i%2==0),sum(1<<i for i in range(n) if i%2)], [(1<<n)-1]*2]

def tree_check(n,rows,qcode):
    global TREE_CASES
    linear,edges,Q=parameters(n,qcode);req(linear==0)
    active=[i for i in range(n) if any((row>>i)&1 for row in rows)]
    orig=signs(n,linear,edges); orig[0]*=-1
    lab=[addr(rows,x) for x in range(1<<n)]
    nodes=0; leaves=0; bad_charge=F(0);spent_I=F(0);spent_H=LF();terminal_I=F(0);terminal_H=LF()
    point_terminal=[]
    def visit(rem,assignment,weight,stage):
        nonlocal nodes,leaves,spent_I,spent_H,terminal_I,terminal_H,bad_charge
        vals=[];labels=[]
        for x in range(1<<len(rem)):
            physical_x=assignment+sum(((x>>j)&1)<<i for j,i in enumerate(rem))
            vals.append(orig[physical_x]);labels.append(lab[physical_x])
        spec=spectrum(vals,labels);D=len(rem)
        inf,_,charges,_=spectral_metrics(spec,D);I=1+sum(inf);H=entropy(spec,D)
        if stage<len(active):pivot=active[stage];next_stage=stage+1
        elif assignment!=0:pivot=None;next_stage=stage
        else:
            candidates=[i for i in rem if Q[i]&sum(1<<j for j in rem)]
            pivot=min(candidates) if candidates else None;next_stage=stage
        if pivot is None:
            leaves+=1;terminal_I+=weight*I;terminal_H.add(H,weight)
            req(len(set(labels))==1,'terminal data reserve')
            if assignment==0:
                req(vals==[-1]+[1]*((1<<D)-1),'point-defect terminal')
                req(I-1==F(2*D,1<<D),'point-defect influence')
                point_terminal.append(dict(remaining_controls=rem,weight=str(weight),H=H.json(),I_minus_1=str(I-1)))
            # H<=4(I-1), certified with an exact interval; constant/equality handled symbolically.
            gap=LF(4*(I-1)).add(H,-1)
            req(not gap.d or gap.interval()[0]>=0,'terminal H payment')
            return H,I
        nodes+=1;j=rem.index(pivot)
        req(inf[j]>=F(1,2),'high-influence pivot')
        B=erasure(spec,D,j)
        gap=LF(2*inf[j]).add(B,-1)
        req(not gap.d or gap.interval()[0]>=0,'exact B bad-node gate')
        # For the nominated gate K=2 no internal node is bad, hence bad_charge stays zero.
        child_rem=[i for i in rem if i!=pivot]
        H0,I0=visit(child_rem,assignment,weight/2,next_stage)
        H1,I1=visit(child_rem,assignment+(1<<pivot),weight/2,next_stage)
        req(I==inf[j]+(I0+I1)/2,'influence telescope')
        drop=LF().add(H).add(H0,-F(1,2)).add(H1,-F(1,2))
        gap=LF(4*inf[j]).add(drop,-1)
        req(not gap.d or gap.interval()[0]>=0,'node entropy payment')
        spent_I+=weight*inf[j];spent_H.add(drop,weight)
        return H,I
    H,I=visit(list(range(n)),0,F(1),0)
    req(H==LF().add(spent_H).add(terminal_H),'full entropy telescope')
    req(I==spent_I+terminal_I,'full influence telescope')
    req(bad_charge==0)
    req(LF(4*(I-1)).add(H,-1).interval()[0]>=0,'strong final payment')
    TREE_CASES+=1
    return dict(n=n,rows=rows,qcode=qcode,internal_nodes=nodes,leaves=leaves,
                spent_influence=str(spent_I),terminal_influence=str(terminal_I),
                bad_boundary_charge_K2=str(bad_charge),point_defect_terminal=point_terminal)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--pilot',action='store_true');args=parser.parse_args()
    planned=4854+8192+4*((16+3)+(32+3)+(64+3))+15
    plan=dict(root_cases=planned,stopping_tree_cases=4*((16+3)+(32+3)+(64+3)),pilot_cases=182)
    # Save the count before any spectrum search.
    (ROOT/'out'/('pilot_plan.json' if args.pilot else 'case_plan.json')).write_text(json.dumps(plan,indent=2)+'\n')
    for n in range(1,4):
        if args.pilot and n==3:break
        for a in range(3):
            for rows in product(range(1<<n),repeat=a):
                for code in range(1<<(n+n*(n-1)//2)):
                    root_check(n,list(rows),code)
                    if time.perf_counter()-START>60:raise RuntimeError('Frozen cap reached')
    samples=[];trees=[]
    if not args.pilot:
        for rows in [[],[1],[15],[1,2],[3,12],[5,10],[15,15],[7,14]]:
            for code in range(1024):
                root_check(4,rows,code)
                if time.perf_counter()-START>60:raise RuntimeError('Frozen cap reached')
        for n in [4,5,6]:
            for code in graph_codes(n):
                for rows in maps(n):
                    root_check(n,rows,code)
                    trees.append(tree_check(n,rows,code))
                    if time.perf_counter()-START>60:raise RuntimeError('Frozen cap reached')
        for n in [2,4,6]:
            code=graph_codes(n)[0]
            for r in range(n+1):samples.append(root_check(n,[1<<i for i in range(r)],code,True))
        req(ROOT_CASES==planned and TREE_CASES==plan['stopping_tree_cases'],'frozen case count')
    else:req(ROOT_CASES==182,'pilot count')
    result=dict(status='PASS',helper_version='A017-point-surgery-v1.1',pilot=args.pilot,
                root_cases=ROOT_CASES,tree_cases=TREE_CASES,exact_assertions=CHECKS,
                runtime_seconds=time.perf_counter()-START,case_digest_sha256=DIGEST.hexdigest(),
                entropy_units='bits',arithmetic='integer Walsh, Fraction, exact log2-prime forms and rational certified intervals',
                log_certificate='ln x=2 sum z^(2j+1)/(2j+1), tail <=2 z^(65)/(65(1-z^2)), z=(x-1)/(x+1), 32 terms; log normalization to x in [1,2]',
                samples=samples,trees=trees)
    outfile='pilot.json' if args.pilot else 'validation.json'
    (ROOT/'out'/outfile).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['samples','trees']},indent=2))

if __name__=='__main__':main()
