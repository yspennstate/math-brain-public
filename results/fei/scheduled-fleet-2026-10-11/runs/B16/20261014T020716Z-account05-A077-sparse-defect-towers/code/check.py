from pathlib import Path
from fractions import Fraction as R
import json, sys, time, itertools, hashlib
import exact_math as m

ROOT=Path(__file__).resolve().parents[1]
COUNT=0
def ck(ok):
    global COUNT
    COUNT+=1
    assert ok, COUNT
def S(u,d,v):
    return m.add(m.scale(m.add(m.Phi((u+v)**2,d*d),m.Phi((u-v)**2,d*d)),R(1,4)),m.scale(m.Phi(u*u,d*d),R(-1,2)))
def pos(e): return m.nonneg(e)
def bounded(e,c):
    ck(pos(m.add(m.constant(c),m.scale(e,-1))))
def rare(k,r):
    n=k+1+r
    g=[];h=[]
    for bits in range(1<<n):
        ss=bits&((1<<k)-1)
        x=(bits>>k)&1
        active=(bits>>(k+1))==0
        hh=(-1)**sum(((ss>>i)&1)*((ss>>(i+1))&1) for i in range(0,k,2))
        g.append(-1 if active and ss==0 and x==0 else 1)
        h.append(hh if active else 1)
    return tuple(g),tuple(h),tuple([f's{i}' for i in range(k)]+['x']+[f't{i}' for i in range(r)])
def tree(g,h,tags,phase='paid'):
    w=m.wrap(g,h)
    if m.influence(w)==0:
        return (),R(0),m.influence(w),m.H(w),R(0),R(0)
    if not tags:
        if phase=='gate_stop':
            return (),R(0),m.influence(w),m.H(w),R(0),R(0)
        ck(m.H(w)==());ck(m.B(w,0)==())
        final=m.inf(w,0)
        return (),final,R(0),(),R(0),final
    gates=[i for i,t in enumerate(tags) if t.startswith('t')]
    if gates: i=gates[0];gate=True
    elif phase=='gate_stop':
        return (),R(0),m.influence(w),m.H(w),R(0),R(0)
    else:
        live=[i for i in range(len(tags)) if m.inf(h,i)]
        if live:
            i=live[0];gate=False
            ck(m.inf(h,i)>=R(1,2))
        else:
            live=[i for i in range(len(tags)) if m.inf(g,i)]
            if not live:
                ck(m.H(w)==())
                ck(m.B(w,0)==())
                final=m.inf(w,0)
                return (),final,R(0),(),R(0),final
            i=live[0];gate=False
    j=m.inf(w,i+1);b=m.B(w,i+1)
    ck(j==(m.inf(g,i)+m.inf(h,i))/2)
    bounded(b,(4 if gate else 5)*j)
    if gate:
        exact=m.add(m.Phi((1-j)**2,j*j),m.constant(2*j*(1-j)))
        ck(b==exact)
    children=[tree(m.restrict(g,i,v),m.restrict(h,i,v),tags[:i]+tags[i+1:],phase) for v in (0,1)]
    bill=m.add(b,*(m.scale(c[0],R(1,2)) for c in children))
    spent=j+sum((c[1]/2 for c in children),R(0))
    leafI=sum((c[2]/2 for c in children),R(0))
    leafH=m.add(*(m.scale(c[3],R(1,2)) for c in children))
    gateI=(j if gate else 0)+sum((c[4]/2 for c in children),R(0))
    dataI=(0 if gate else j)+sum((c[5]/2 for c in children),R(0))
    ck(spent+leafI==m.influence(w))
    ck(spent==gateI+dataI)
    bounded(bill,4*gateI+5*dataI)
    return bill,spent,leafI,leafH,gateI,dataI
def exact_rows(k,r):
    a=R(1,1<<k);b=R(1,1<<(k//2));q=R(1,1<<r);j=q*a/2
    ds=m.add(m.scale(S(-a,a,b),q*((1<<k)-1)),m.scale(S(-a,a,b-1),q*(1-q)),S(1-q*a,q*a,1-q+q*b))
    if k>=4:
        ck(pos(m.add(ds,m.constant(-(k-4)*j))))
    return ds
def quadratic_review():
    polys=restrictions=0
    for n in range(4):
        monomials=[0]+[1<<i for i in range(n)]+[(1<<i)|(1<<j) for i in range(n) for j in range(i)]
        for mask in range(1<<len(monomials)):
            vals=tuple((-1)**sum(1 for j,t in enumerate(monomials) if (mask>>j)&1 and x&t==t) for x in range(1<<n))
            for pattern in itertools.product((-1,0,1),repeat=n):
                res=vals
                for i in range(n-1,-1,-1):
                    if pattern[i]>=0:res=m.restrict(res,i,pattern[i])
                for i in range(len(res).bit_length()-1):
                    jj=m.inf(res,i)
                    ck(jj==0 or jj>=R(1,2))
                restrictions+=1
            polys+=1
    return {'quadratic_signs':polys,'labelled_restrictions':restrictions}
def main():
    start=time.perf_counter();mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
    if mode=='review':
        review=quadratic_review()
        result={'helper_version':'A077-independent-quadratic-review-v1','mode':mode,'assertions':COUNT,
            'elapsed_seconds':time.perf_counter()-start,'reviews':review,'arithmetic':'exact rational physical edge influences'}
        path=ROOT/'out'/'review.json';path.write_text(json.dumps(result,indent=2),encoding='utf-8')
        print(json.dumps(result));return
    cases=[(2,1)] if mode=='pilot' else [(2,1),(2,2),(2,4),(4,1),(4,2),(4,4),(6,1),(6,2)]
    records=[]
    for k,r in cases:
        if time.perf_counter()-start>55:raise RuntimeError('frozen limit')
        g,h,tags=rare(k,r);w=m.wrap(g,h)
        a=R(1,1<<k);b=R(1,1<<(k//2));q=R(1,1<<r);c=(1-b+a)/2
        ck(sum(g)/R(len(g))==1-q*a);ck(sum(h)/R(len(h))==1-q*(1-b))
        ck(sum(w)/R(len(w))==1-q*c)
        ck(m.inf(w,0)==q*c)
        for i,t in enumerate(tags):
            expect=q*a/2 if t=='x' else (q*c if t.startswith('t') else q*(a+R(1,2))/2)
            ck(m.inf(w,i+1)==expect)
            ck(expect<=q)
        total=q*(R(k,4)+R(k+1,2)*a+(r+1)*c)
        ck(m.influence(w)==total)
        x=tags.index('x')
        d=m.add(m.B(w,x+1),m.scale(m.B(g,x),R(-1,2)))
        ck(d==exact_rows(k,r))
        paid=tree(g,h,tags)
        stopped=tree(g,h,tags,'gate_stop')
        ck(paid[3]==());ck(paid[2]==m.inf(w,0)*0)
        ck(paid[4]==r*q*c);ck(stopped[4]==r*q*c)
        baseg,baseh,basetags=rare(k,0);base=m.wrap(baseg,baseh)
        ck(paid[5]==q*m.influence(base))
        ck(stopped[2]==q*m.influence(base))
        ck(stopped[3]==m.scale(m.H(base),q))
        # Exact terminal decomposition retains both core entropies and outer potential.
        base_core=m.scale(m.add(m.H(baseg),m.H(baseh)),R(1,2))
        potential=m.add(m.H(base),m.scale(base_core,-1))
        ck(stopped[3]==m.add(m.scale(base_core,q),m.scale(potential,q)))
        bounded(m.H(w),8*total)
        # Independent base-row reconstruction for the scoped A078 review.
        db=m.add(m.B(base,k+1),m.scale(m.B(baseg,k),R(-1,2)))
        ck(db==m.add(m.scale(S(-a,a,b),(1<<k)-1),S(1-a,a,b)))
        if k>=4:ck(pos(m.add(db,m.constant(-(k-4)*a/2))))
        records.append({'k':k,'r':r,'dimension':len(w).bit_length()-1,'I':str(total),'rare_query_influence':str(q*a/2),
            'D_prime_logs':{str(p):str(v) for p,v in d},'D_interval':[str(v) for v in m.enclosure(d)],
            'gate_consumed':str(paid[4]),'base_consumed':str(paid[5]),'terminal_entropy_retained':{str(p):str(v) for p,v in stopped[3]}})
    compressed=aux=0
    if mode=='full':
        for k in (2,4,6,8):
            for r in (1,2,4):
                exact_rows(k,r);compressed+=1
        for k in range(4,65,2):
            a=R(1,1<<k)
            for r in range(1,65):
                q=R(1,1<<r)
                ck(r*q<=R(1,2))
                ck(a*(k-1)+2*q*a*(k+r-R(1,4))<=2*k*a)
                ck(2*k*a<=1);aux+=1
        review=quadratic_review()
    else:review={}
    result={'helper_version':'A077-rare-rare-activation-v1','mode':mode,'actual_roots':len(cases),'compressed_roots':compressed,
        'analytic_auxiliary_pairs':aux,'assertions':COUNT,'elapsed_seconds':time.perf_counter()-start,
        'arithmetic':'exact rational FWHT/edges; prime-log equality and rational certified signs','reviews':review,'records':records}
    path=ROOT/'out'/f'{mode}.json';path.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='records'}))
    print('sha256',hashlib.sha256(path.read_bytes()).hexdigest())
if __name__=='__main__':main()
