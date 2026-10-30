from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache,reduce
import time,json
R=Path(__file__).resolve().parents[1];start=time.perf_counter();nodes=0;signcalls=0
def require(a,b): assert a==b,(a,b)
@lru_cache(None)
def factors(n):
    ans={};p=2
    while p*p<=n:
        while n%p==0: ans[p]=ans.get(p,0)+1;n//=p
        p+=1
    if n>1: ans[n]=ans.get(n,0)+1
    return ans
def combine(*forms):
    result={}
    for form in forms:
        for k,c in form.items(): result[k]=result.get(k,Q(0))+c
    return {k:c for k,c in result.items() if c}
def entropy_atom(q):
    if not q:return {}
    return combine({p:-q*c for p,c in factors(q.numerator).items()},{p:q*c for p,c in factors(q.denominator).items()})
def fwht(tab):
    a=list(tab)
    for bit in range(len(tab).bit_length()-1):
        stride=1<<bit
        for s in range(len(tab)):
            if not s&stride:
                a[s],a[s+stride]=a[s]+a[s+stride],a[s]-a[s+stride]
    return a
def erasure(tab):
    a=fwht(tab);den=len(tab)**2;form={}
    for i in range(0,len(tab),2):
        x=Q(a[i]**2,den);y=Q(a[i+1]**2,den)
        form=combine(form,entropy_atom(x),entropy_atom(y),{p:-c for p,c in entropy_atom(x+y).items()})
    return form
@lru_cache(None)
def logbounds(p):
    k=p.bit_length()-1
    def ln(x):
        z=(x-1)/(x+1);s=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(24)),Q(0))
        return s,s+2*z**49/(49*(1-z*z))
    a,b=ln(Q(p,2**k));c,d=ln(Q(2))
    return Q(k)+a/d,Q(k)+b/c
def positive(form):
    global signcalls
    signcalls+=1
    if not form:return False
    lo=hi=Q(0)
    for p,c in form.items():
        a,b=logbounds(p);lo+=c*(a if c>0 else b);hi+=c*(b if c>0 else a)
    assert lo>0 or hi<0,(form,lo,hi)
    return lo>0
def influence(tab):
    n=len(tab).bit_length()-1
    return Q(2*sum(tab[x]!=tab[x|1<<i] for i in range(n) for x in range(len(tab)) if not x>>i&1),len(tab))
def cmodule():
    out=[]
    for y in range(32):
        x=y>>1;b=(-1)**(((x&1)*((x>>1)&1))+(((x>>2)&1)*((x>>3)&1)))
        out.append(-b if y&1 and x==0 else b)
    return tuple(out)
C=cmodule()
def product(k):return tuple(reduce(lambda a,j:a*C[(x>>(5*j))&31],range(k),1) for x in range(1<<(5*k)))
def reorder(tab,order):return tuple(tab[sum(((x>>i)&1)<<coord for i,coord in enumerate(order))] for x in range(len(tab)))
def runprefix(w,h):
    @lru_cache(None)
    def visit(w):
        global nodes
        nodes+=1;assert time.perf_counter()-start<180
        if all(a==w[0] for a in w): return Q(0),Q(0),Q(w[0]<0)
        # Explicit physical F values, no scalar erasure transport formula.
        f=tuple(-1 if ww<0 and hh<0 else 1 for hh in h for ww in w)
        g0,g1=f[::2],f[1::2]
        d=Q(sum(a!=b for a,b in zip(g0,g1)),len(g0))
        q=influence(tuple(a*b for a,b in zip(g0,g1)))/2
        b=erasure(f);b=combine(b,{2:-4*d})
        bad=positive(b)
        s0,s1=visit(w[::2]),visit(w[1::2])
        return (Q(q if bad else 0)+(s0[0]+s1[0])/2,d+(s0[1]+s1[1])/2,(s0[2]+s1[2])/2)
    return visit(w)
seed={'left':str(2**182*13**156),'right':str(5**210*3**162)}
threshold={'left':str(13**13*499**499),'right':str(2**4517)}
assert int(seed['left'])>int(seed['right']);assert int(threshold['left'])>int(threshold['right'])
(R/'out/K7_INTEGER_CERTIFICATE.json').write_text(json.dumps(threshold,indent=2),encoding='utf-8')
rootrows=json.loads((R/'out/ROOT_PREFIXES.json').read_text());tensorrows=json.loads((R/'out/TENSOR_PREFIXES.json').read_text());out=[]
for mask in [9,27,125,254]:
    w=tuple(1 if mask>>x&1 else -1 for x in range(8))
    for name,h in [('c',C),('-c',tuple(-x for x in C))]:
        bill,spent,term=runprefix(w,h)
        row=next(z for z in rootrows if z['controller_mask']==mask and z['core']==name)
        require(bill,Q(row['prefix_bad_bill']));require(term,Q(row['t']))
        require(spent,(1-Q(sum(h),len(h)))*influence(w)/2)
        out.append({'mask':mask,'core':name,'bill':str(bill),'spent_I':str(spent),'terminal_probability':str(term)})
for l,m in [(1,1),(1,2),(2,1)]:
    w=tuple(-x for x in product(l));h=product(m)
    sel=[5*j for j in range(l)];data=[5*j+i for j in range(l) for i in range(1,5)]
    for name,order in [('selectors-data',sel+data),('data-selectors',data+sel)]:
        bill,spent,term=runprefix(reorder(w,order),h)
        row=next(z for z in tensorrows if z['L']==l and z['M']==m and z['controller_order']==name)
        require(bill,Q(row['prefix_bad_bill']));require(term,Q(row['terminal_probability']))
        require(spent,(1-Q(sum(h),len(h)))*influence(w)/2)
        out.append({'L':l,'M':m,'order':name,'bill':str(bill),'spent_I':str(spent),'terminal_probability':str(term)})
    (R/'out/DIRECT_PREFIXES.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
result={'status':'PASS','prefixes':len(out),'memoized_actual_controller_nodes':nodes,'exact_sign_calls':signcalls,'integer_certificates':2,'seconds':time.perf_counter()-start,'representation':'explicit physical F spectrum and edge products; no transport helper imported','independent_agent_review':False}
(R/'out/DIRECT_VALIDATION.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
