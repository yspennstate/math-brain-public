from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import itertools,json,sys,time,hashlib
import exact_math as a

ROOT=Path(__file__).resolve().parents[1]
COUNT=0
def ck(x):
    global COUNT
    COUNT+=1
    assert x,COUNT
def bounded(e,c):ck(a.nonneg(a.add(a.constant(c),a.scale(e,-1))))
def lower(e,c):ck(a.nonneg(a.add(e,a.constant(-c))))
def truth(k,r):
    g=[];h=[]
    for bits in range(1<<(k+1+r)):
        s=bits&((1<<k)-1);x=(bits>>k)&1;active=(bits>>(k+1))==0
        g.append(-1 if active and s==0 and x==0 else 1)
        parity=sum(((s>>j)&1)*((s>>(j+1))&1) for j in range(0,k,2))
        h.append((-1)**parity if active else 1)
    return tuple(g),tuple(h)
def restricted(vals,pattern):
    for i in range(len(pattern)-1,-1,-1):
        if pattern[i]!=-1: vals=a.restrict(vals,i,pattern[i])
    return vals
class Family:
    def __init__(self,k,r):
        self.k=k;self.r=r
        self.g,self.h=truth(k,r);self.w=a.wrap(self.g,self.h)
        self.bg,self.bh=truth(k,0)
        self.n=k+r+2
    @lru_cache(None)
    def state(self,p):
        free=tuple(i for i,b in enumerate(p) if b==-1)
        w=restricted(self.w,p)
        g=restricted(self.g,p[1:]);h=restricted(self.h,p[1:])
        bg=restricted(self.bg,p[1:self.k+2]);bh=restricted(self.bh,p[1:self.k+2])
        alive=not any(b==1 for b in p[self.k+2:])
        eligible=(p[0]==-1 and alive and a.influence(bg)>0 and a.influence(bh)>0)
        delta=F(sum(x!=y for x,y in zip(g,h)),len(g)) if p[0]==-1 else F(0)
        mark=12*delta if eligible else F(0)
        bank=mark+10*delta
        return free,w,g,h,eligible,delta,mark,bank
    def child(self,p,i,b):
        return p[:i]+(b,)+p[i+1:]
    def influences(self,p):
        free,w,*_=self.state(p)
        data=sum((a.inf(w,j) for j,i in enumerate(free) if i!=0),F(0))
        z=a.inf(w,free.index(0)) if 0 in free else F(0)
        return data,z
    def bad(self,p,i):
        free,w,g,h,eligible,*_=self.state(p)
        if not eligible or i==0:return False
        datafree=tuple(j for j in free if j!=0)
        t=datafree.index(i)
        return a.inf(g,t)>0 and a.inf(h,t)==0
    def node(self,p):
        free,w,g,h,eligible,delta,mark,bank=self.state(p)
        if 0 in free:
            ck(a.inf(w,free.index(0))==delta)
            sg,sh=a.spectrum(g),a.spectrum(h)
            potential=a.add(*(a.add(a.phi((x+y)**2/4),a.phi((x-y)**2/4),
                                      a.scale(a.phi(x*x),F(-1,2)),a.scale(a.phi(y*y),F(-1,2))) for x,y in zip(sg,sh)))
            ck(a.H(w)==a.add(a.scale(a.add(a.H(g),a.H(h)),F(1,2)),potential))
        private=sharp=0
        for j,i in enumerate(free):
            children=[self.state(self.child(p,i,b)) for b in (0,1)]
            avgmark=sum((c[6]/2 for c in children),F(0))
            avgbank=sum((c[7]/2 for c in children),F(0))
            ck(bank>=avgbank)
            jj=a.inf(w,j);bb=a.B(w,j)
            allowance=(10*jj if i!=0 else 0)+bank-avgbank
            bounded(bb,allowance)
            ck(all(not c[4] or eligible for c in children))
            if self.bad(p,i):
                private+=1
                ck(avgmark<=F(2,3)*mark)
                ck(mark-avgmark>=4*delta)
                di=tuple(u for u in free if u!=0).index(i)
                remainder=a.add(bb,a.scale(a.B(g,di),F(-1,4)))
                lower(remainder,0)
                bounded(remainder,4*delta)
                bounded(remainder,mark-avgmark)
                ck(a.inf(g,di)==2*jj)
                bounded(a.B(g,di),3*a.inf(g,di))
                if avgmark==F(2,3)*mark:sharp+=1
            if i==0:bounded(bb,10*delta)
        return len(free),private,sharp
    def tree(self,p,policy,depth=0):
        free,w,*tail=self.state(p);bank=tail[-1]
        if not free or a.influence(w)==0 or (policy=='stop2' and depth>=2) or (policy=='stop3' and depth>=3):
            data,z=self.influences(p)
            return (),F(0),F(0),data,z,bank,a.H(w)
        if policy=='first':i=free[0]
        elif policy=='last':i=free[-1]
        elif policy=='stop2':i=min(free,key=lambda i:(i==0,i))
        elif policy in ('bad','stop3'):
            i=max(free,key=lambda i:(self.bad(p,i),a.inf(w,free.index(i)),-i))
        else:i=max(free,key=lambda i:(a.inf(w,free.index(i)),-i))
        children=[self.tree(self.child(p,i,b),policy,depth+1) for b in (0,1)]
        j=free.index(i);jj=a.inf(w,j)
        bill=a.add(a.B(w,j),*(a.scale(c[0],F(1,2)) for c in children))
        pd=(jj if i!=0 else 0)+sum((c[1]/2 for c in children),F(0))
        pz=(jj if i==0 else 0)+sum((c[2]/2 for c in children),F(0))
        ld=sum((c[3]/2 for c in children),F(0));lz=sum((c[4]/2 for c in children),F(0))
        lk=sum((c[5]/2 for c in children),F(0))
        lh=a.add(*(a.scale(c[6],F(1,2)) for c in children))
        di,zi=self.influences(p)
        ck(pd+ld==di);ck(pz+lz==zi)
        bounded(bill,10*pd+bank-lk)
        return bill,pd,pz,ld,lz,lk,lh
def review():
    cases=0
    for n in (1,2,3):
        for gm in range(1<<(1<<n)):
            g=tuple(1 if gm>>x&1 else -1 for x in range(1<<n))
            for hm in range(1<<(1<<(n-1))):
                h=tuple(1 if hm>>(x&((1<<(n-1))-1))&1 else -1 for x in range(1<<n))
                w=a.wrap(g,h);d=a.inf(g,n-1)
                delta=F(sum(x!=y for x,y in zip(g,h)),len(g))
                rem=a.add(a.B(w,n),a.scale(a.B(g,n-1),F(-1,4)))
                ck(a.inf(h,n-1)==0);ck(a.inf(w,0)==delta)
                ck(a.inf(w,n)==d/2);ck(d<=2*delta)
                ug=a.spectrum(g);vh=a.spectrum(h)
                E=sum(((ug[t]-vh[t])**2 for t in range(1<<(n-1))),F(0))
                ck(E==4*delta-d)
                lower(rem,0)
                bounded(rem,4*delta)
                upper=a.add(a.constant(d),a.scale(a.Phi(E,d),F(1,2)))
                ck(a.nonneg(a.add(upper,a.scale(rem,-1))))
                cases+=1
    return cases
def main():
    start=time.perf_counter();mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
    if mode=='review':
        cases=review();out={'helper_version':'A077-quarter-admission-review-v1','mode':mode,'actual_wrappers':cases,
                'assertions':COUNT,'elapsed_seconds':time.perf_counter()-start}
    else:
        frozen=[(2,1),(2,2),(4,1),(4,2),(6,1)]
        if mode=='chunk':
            k,r,zpart=map(int,sys.argv[2:5])
            assert (k,r) in frozen and zpart in (-1,0,1)
            domains=[(k,r)]
        else:domains=[(2,1)] if mode=='pilot' else frozen
        totalstates=queries=bad=sharp=0;records=[]
        for k,r in domains:
            ctx=Family(k,r);root=(-1,)*ctx.n
            states=qcount=bcount=scount=0
            patterns=((zpart,)+p for p in itertools.product((-1,0,1),repeat=ctx.n-1)) if mode=='chunk' else itertools.product((-1,0,1),repeat=ctx.n)
            for p in patterns:
                if states%128==0 and time.perf_counter()-start>55:raise RuntimeError('frozen runtime limit')
                q,b,s=ctx.node(p);states+=1;qcount+=q;bcount+=b;scount+=s
            trees=[]
            policies=('first','last','bad','max','stop2','stop3') if mode!='chunk' or zpart==-1 else ()
            for policy in policies:
                tr=ctx.tree(root,policy)
                trees.append({'policy':policy,'consumed_data':str(tr[1]),'consumed_selector':str(tr[2]),
                        'remaining_data':str(tr[3]),'remaining_selector':str(tr[4]),'retained_bank':str(tr[5]),
                        'terminal_entropy':{str(p):str(c) for p,c in tr[6]}})
            totalstates+=states;queries+=qcount;bad+=bcount;sharp+=scount
            records.append({'k':k,'r':r,'states':states,'queries':qcount,'eligible_private_rows':bcount,
                            'sharp_contraction_rows':scount,'policies':trees})
            ctx.state.cache_clear()
        if mode!='chunk' or zpart==-1:
            ck(sharp>0);ck(bad>0)
        out={'helper_version':'A077-geometric-mark-v1','mode':mode,'roots':len(domains),'restriction_states':totalstates,
             'local_queries':queries,'eligible_private_rows':bad,'sharp_contraction_rows':sharp,
             'assertions':COUNT,'elapsed_seconds':time.perf_counter()-start,'records':records}
    out['arithmetic']='exact rational FWHT/edge counts and bank releases; prime-log equalities and certified rational sign intervals'
    filename=f'chunk_k{k}_r{r}_z{zpart}.json' if mode=='chunk' else f'{mode}.json'
    if mode=='chunk':
        out['selector_partition']=zpart
        out['helper_version']='A077-geometric-mark-v1-chunks'
    path=ROOT/'out'/filename;path.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='records'}))
    print('sha256',hashlib.sha256(path.read_bytes()).hexdigest())
if __name__=='__main__':main()
