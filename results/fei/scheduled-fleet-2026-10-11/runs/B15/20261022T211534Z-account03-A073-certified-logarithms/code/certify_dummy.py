"""Independent rational checker. No imports from another agent; no floating logs."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import hashlib, json, time, sys, itertools
RUN=Path(__file__).resolve().parents[1]
OUT=RUN/'out'; OUT.mkdir(exist_ok=True)
START=time.monotonic(); ASSERTS=0; N=12
PILOT='--pilot' in sys.argv
CAP=55 if PILOT else 240
def save(name,obj):
    (OUT/name).write_text(json.dumps(obj,indent=2,default=str)+'\n',encoding='utf-8')
def ck(ok):
    global ASSERTS
    ASSERTS+=1
    if not ok: raise AssertionError('predicate '+str(ASSERTS))
    if time.monotonic()-START>CAP: raise TimeoutError('frozen runtime cap')
def add(x,y): return x[0]+y[0],x[1]+y[1]
def sub(x,y): return x[0]-y[1],x[1]-y[0]
def mul(c,x): return (c*x[0],c*x[1]) if c>=0 else (c*x[1],c*x[0])
def ln_unit(q):
    z=(q-1)/(q+1); value=2*sum((z**(2*k+1)/F(2*k+1) for k in range(N)),F(0))
    tail=2*z**(2*N+1)/(F(2*N+1)*(1-z*z))
    return value,value+tail
LN2=ln_unit(F(2))
@lru_cache(maxsize=30000)
def log2(q):
    ck(q>0)
    k=q.numerator.bit_length()-q.denominator.bit_length()
    t=q/(F(2)**k)
    if t<1: k-=1; t*=2
    ck(1<=t<2)
    if t==1:return F(k),F(k)
    a,b=ln_unit(t)
    return k+a/LN2[1],k+b/LN2[0]
def ce(p,q):
    v=(F(0),F(0))
    for x,y in zip(p,q):
        if x:
            ck(y>0); v=add(v,mul(-x,log2(y)))
    return v
def pairs(v,j):
    for u in range(len(v)//2):
        lo=u&((1<<j)-1); hi=u>>j
        x=lo|(hi<<(j+1)); yield v[x],v[x|(1<<j)]
def marginal(v,j):return tuple(x+y for x,y in pairs(v,j))
def erasure(p,j):
    value=(F(0),F(0))
    for x,y in pairs(p,j):
        if x and y:
            value=add(value,mul(x+y,log2(x+y)))
            value=add(value,mul(-x,log2(x)))
            value=add(value,mul(-y,log2(y)))
    return value
def source(a,b):
    s=F(1,2**a); mu=1-2*s
    return tuple(mu*mu if T==0 else 4*s*s if T<2**a else F(0) for T in range(2**(a+b)))
def calibrate(R,zero):
    ck(sum(R)==1 and R[0]<1 and 0<=zero<1)
    return (zero,)+tuple(x*(1-zero)/(1-R[0]) for x in R[1:])
def ref(a,b,mode):
    p=source(a,b)
    if mode=='matching':return p
    weights=[F(0)]+[F(1+(17*T+3)%11) for T in range(1,len(p))]
    if mode=='spiked':weights[1<<a]=F(1000)
    z=sum(weights)
    return (p[0],)+tuple((1-p[0])*x/z for x in weights[1:])
@lru_cache(maxsize=4000)
def node(a,b,r,R):
    n=a+b; s=F(1,2**a); t=F(1,2**n); e=F(2,2**(n+r)); mu=1-2*s
    gh=tuple(mu if T==0 else -2*s if T<2**a else F(0) for T in range(2**n))
    amp=tuple((gh[S%2**n] if S<2**n else 0)+e for S in range(2**(n+r)))
    p=tuple(x*x for x in amp); ck(sum(p)==1)
    Re=tuple((1-e/s)*R[T]+(e/s)*mu*(T==0)+2*e*t for T in range(2**n))
    ck(sum(Re)==1 and min(Re)>0)
    M=tuple(sum(p[T+(U<<n)] for U in range(2**r)) for T in range(2**n))
    q=tuple(Re[S%2**n]*p[S]/M[S%2**n] for S in range(len(p)))
    ck(sum(q)==1)
    c=ce(source(a,b),R); W=add(c,(10*e*(n+r),)*2)
    full=ce(p,q);ck(full[1]<=W[0])
    return amp,p,q,c,W,e
def physical_check(a,b,r):
    d=a+b+r; size=2**d
    vals=[(1-2*(x%(2**a)==0)+2*(x==0)) for x in range(size)]
    # Direct character sums, independent of the analytic coefficient formula.
    direct=tuple(F(sum(vals[x]*(-1 if (x&T).bit_count()%2 else 1) for x in range(size)),size) for T in range(size))
    expected=node(a,b,r,source(a,b))[0]
    ck(direct==expected)
    infl=F(sum(vals[x]!=vals[x^(1<<j)] for x in range(size) for j in range(d)),size)
    e=F(2,size); Ig=F(2*a,2**a)
    ck(infl==Ig+e*(b+r-a))
    for j in range(d):
        ck(sum(direct[T]**2 for T in range(size) if T&(1<<j))==F(sum(vals[x]!=vals[x^(1<<j)] for x in range(size)),size))
def advance(a,b,r,R,kind):
    amp,p,q,c,W,e=node(a,b,r,R)
    j=0 if kind=='A' else a if kind=='D' else a+b
    pa=tuple((x+y)**2 for x,y in pairs(amp,j)); po=tuple((x-y)**2 for x,y in pairs(amp,j))
    inherited=marginal(q,j); B=erasure(p,j); off=ce(po,inherited)
    ck(sum(pa)==sum(po)==sum(inherited)==1)
    if kind=='A':
        if a==1:
            end=add(B,mul(F(1,2),add(off,ce(pa,pa))))
            ck(end[1]<=W[0]);return None,end,None
        aa,bb,rr=a-1,b,r
        Rnew=calibrate(marginal(R,j),(1-F(2,2**aa))**2)
    elif kind=='D':
        aa,bb,rr=a,b-1,r
        Rnew=calibrate(marginal(R,j),(1-F(2,2**a))**2)
    else:aa,bb,rr,Rnew=a,b,r-1,R
    new=node(aa,bb,rr,Rnew);ck(new[1]==pa)
    local=add(B,mul(F(1,2),add(off,new[4])))
    if kind=='A': ck(local[1]<=W[0])
    else:
        ck(B[1]<12*e)
        ck(sub(off,c)[1]<11*e)
        ck(local[1]<W[0]+8*e)
        if kind=='D':ck(all(Rnew[T]>=R[T] for T in range(2**a)))
    Z=sub(ce(pa,new[2]),ce(pa,inherited))
    return (aa,bb,rr,Rnew),local,{'kind':kind,'j':j,'e':e,'B':B,'off_excess':sub(off,c),'local_surplus_over_W':sub(local,W),'reset_Z':Z,'nonflat':len(set(x for x in pa if x))>1,'both_children_nonconstant':pa[0]<1 and po[0]<1}
ROOTS=[(2,1,2)] if PILOT else list(itertools.product([1,2],[1,2],[1,2]))
MODES=['matching','increasing'] if PILOT else ['matching','increasing','spiked']
spec={'helper':'certify_dummy.py/v1','sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'F=1-2A_a+2A_(a+b+r)','domain':ROOTS,'references':MODES,'case_count_roots':len(ROOTS)*len(MODES),'symmetry':'No reference-sensitive label quotient. All eligible query TYPE words, fixed least remaining coordinate within each type. Analytic proof covers labels.','arithmetic':'Fraction; N12 atanh outward tail, range reduction to [1,2), no float logarithms','memory_estimate_MB':120,'max_runtime_seconds':CAP,'precision_stop':'N12 fixed; any undecided sign fails, no refinement','pilot':PILOT}
save('FROZEN_PILOT.json' if PILOT else 'FROZEN_SPEC.json',spec)
ROWS=[]; COUNTS={'roots':0,'history_nodes':0,'dummy_steps':0,'control_steps':0,'active_steps':0,'final_active':0}
MARGINS=[]
def visit(state,spent,term,reach,quota,root_e,root_nonactive,path):
    a,b,r,R=state; amp,p,q,c,W,e=node(*state)
    COUNTS['history_nodes']+=1
    ledger=add(add(spent,term),mul(reach,ce(p,q)))
    ck(quota-ledger[1]>=12*root_e)
    MARGINS.append((quota-ledger[1])/root_e)
    for kind in ['A']+(['D'] if b else [])+(['C'] if r>=2 else []):
        child,local,row=advance(*state,kind)
        B=erasure(p,0 if kind=='A' else a if kind=='D' else a+b)
        j=0 if kind=='A' else a if kind=='D' else a+b
        inherited=marginal(q,j)
        po=tuple((x-y)**2 for x,y in pairs(amp,j)); off=ce(po,inherited)
        newspent=add(spent,mul(reach,B));newterm=add(term,mul(reach/2,off))
        if child is None:
            COUNTS['final_active']+=1
            end=add(add(spent,term),mul(reach,local));ck(quota-end[1]>=12*root_e)
        else:
            COUNTS[{'A':'active_steps','D':'dummy_steps','C':'control_steps'}[kind]]+=1
            if row and kind=='D':
                row.update({'history':path+kind,'reach':reach,'booked_before':spent,'other_terminals_before':term,'root_e':root_e})
                ROWS.append(row)
            visit(child,newspent,newterm,reach/2,quota,root_e,root_nonactive,path+kind)
for a,b,r in ROOTS:
    physical_check(a,b,r)
    for mode in MODES:
        R=ref(a,b,mode); st=(a,b,r,R); _,p,q,c,W,e=node(*st)
        Ig=F(2*a,2**a)
        # Exact ceiling of c_upper/Ig, without a floating conversion.
        z=c[1]/Ig; C0=max(F(4),F((z.numerator+z.denominator-1)//z.denominator))
        quota=(2*C0+10)*(Ig+e*(b+r-a));ck(c[1]<=C0*Ig)
        ck(quota-W[1]>=5*a*2**(b+r)*e)
        visit(st,(F(0),F(0)),(F(0),F(0)),F(1),quota,e,b+r,'')
        COUNTS['roots']+=1
        save('pilot_checkpoint.json' if PILOT else 'checkpoint.json',{'counts':COUNTS,'assertions':ASSERTS,'elapsed_seconds':time.monotonic()-START})
ck(LN2[0]>F(2,3))
mixed=[x for x in ROWS if len(x['history'])>1 and x['nonflat'] and x['both_children_nonconstant']]
ck(bool(mixed)); chosen=mixed[-1]
result={'status':'PASS','rung':'analytic proof with exact finite validation; independent review pending','counts':COUNTS,'assertions':ASSERTS,'minimum_certified_remaining_over_root_e':min(MARGINS),'example_spent_nonflat_dummy_row':chosen,'dummy_rows':len(ROWS),'runtime_seconds':time.monotonic()-START,'precision_terms':N,'precision_refinements':0,'Lean':'NOT_CHECKED; separate admission required','full_FEI':'OPEN'}
save('PILOT_RESULT.json' if PILOT else 'RESULT.json',result)
save('PILOT_ROWS.json' if PILOT else 'DUMMY_ROWS.json',ROWS)
print(json.dumps(result,default=str,indent=2))
