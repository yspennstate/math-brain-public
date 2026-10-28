"""Frozen n=4 exact stopping audit; standard library; no background children."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import importlib.util, hashlib, json, time, argparse, itertools, math

ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261023T123929Z-account03-A063-information-revelation'/'code'/'quadratic_audit.py'
spec=importlib.util.spec_from_file_location('old_quadratic',OLD)
Q=importlib.util.module_from_spec(spec); spec.loader.exec_module(Q)
checks=edges=0
START=time.monotonic()
def ck(x,label):
    global checks
    checks+=1
    if not x: raise AssertionError(label)
    if time.monotonic()-START>60: raise RuntimeError('frozen 60s limit; preserve partial failure')

def klpow(p,ref,L=16):
    """Exactly 2^(L KL(p||ref)), for probabilities whose denominators divide L."""
    ans=F(1)
    for a,b in zip(p,ref):
        if a:
            ck(b>0 and (a*L).denominator==1,'supported source and exact exponent')
            ans*=(a/b)**int(a*L)
    return ans

def transport(tab,ref,i):
    z=Q.info(tab); N=len(tab)//2
    pbar=tuple(z['p'][Q.insert(t,i,0)]+z['p'][Q.insert(t,i,1)] for t in range(N))
    rbar=tuple(ref[Q.insert(t,i,0)]+ref[Q.insert(t,i,1)] for t in range(N))
    children=[]; masses=[]
    for b in (0,1):
        child=Q.restrict(tab,i,b); c=Q.info(child)
        raw=tuple(rbar[t]*(c['p'][t]/(2*pbar[t]) if pbar[t] else F(1,2)) for t in range(N))
        mass=sum(raw); ck(mass>0,'positive reached outcome')
        children.append((child,tuple(v/mass for v in raw))); masses.append(mass)
    ck(sum(masses)==1,'complete reference outcomes')
    # Squaring clears the physical 1/2 branch average; no floating logs.
    K=klpow(z['p'],ref); Kbar=klpow(pbar,rbar)
    E=K/Kbar; O=klpow((F(1,2),F(1,2)),masses)
    ck(E>=1 and O>=1,'erasure and outcome KL nonnegative')
    childprod=math.prod(klpow(Q.info(t)['p'],r) for t,r in children)
    ck(K*K==E*E*O*O*childprod,'actual E/O/K chain, both branches')
    return children

@lru_cache(maxsize=12000)
def walk(tab,ref,reset_allowed):
    global edges
    z=Q.info(tab); n=len(tab).bit_length()-1
    ck(sum(ref)==1 and all(ref[j]>0 for j,a in enumerate(z['p']) if a),'normalized supported inherited reference')
    best=F(1<<(16*z['r'])) # stop here; exp2(16 H)
    if reset_allowed and ref!=z['Q']:
        reset=max(F(1),F(1<<(16*(z['m']-z['r'])))/klpow(z['p'],ref))
        best=max(best,reset*walk(tab,z['Q'],False))
    for i in range(n):
        edges+=1
        for child,newref in transport(tab,ref,i):
            best=max(best,walk(child,newref,True))
    return best

@lru_cache(maxsize=12000)
def noreset(tab,ref):
    z=Q.info(tab); n=len(tab).bit_length()-1
    ck(tuple(ref)==z['p'],'source-equal reference hereditary without product admission')
    best=z['r']
    for i in range(n):
        for t,r in transport(tab,ref,i): best=max(best,noreset(t,r))
    return best

def rawlaw(tab):
    a=list(tab); h=1
    while h<len(a):
        for k in range(0,len(a),2*h):
            for j in range(k,k+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return tuple(F(v*v,len(a)**2) for v in a)

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--pilot',action='store_true'); args=parser.parse_args()
    tested=[]; pairs=list(itertools.combinations(range(4),2))
    for mask in range(64):
        tab=Q.make(4,[p for j,p in enumerate(pairs) if mask>>j&1],0,0)
        z=Q.info(tab)
        if z['r']!=4: continue
        ref=tuple(F(j+1,136) for j in range(16))
        value=walk(tab,ref,True)
        ck(value<=1<<64,'ALL prefix/reset/cut gross+H <= bent original n')
        tested.append({'matrix_mask':mask,'worst_exp2_16_gross_plus_H':str(value)})
        if len(tested)==(1 if args.pilot else 3): break
    selector={}
    if not args.pilot:
        dense=tuple((-1)**(((x&3)&(x>>2)).bit_count()%2) for x in range(16))
        sparse=tuple((-1)**(((x&3).bit_count()*(x>>2).bit_count())%2) for x in range(16))
        pd,ps=rawlaw(dense),rawlaw(sparse)
        L={0,3,12,15}; rd=tuple(F(4 if t in L else 20,256) for t in range(16))
        root=tuple(v for pair in zip(dense,sparse) for v in pair); pr=rawlaw(root)
        influences=[sum(p for t,p in enumerate(pr) if t>>i&1) for i in range(5)]
        ck(influences[1:]==[F(1,2)]*4,'original actual data influences')
        qr=tuple(math.prod(d if t>>i&1 else 1-d for i,d in enumerate(influences)) for t in range(32))
        qbar=tuple(pr[2*t]+pr[2*t+1] for t in range(16)); rbar=tuple(qr[2*t]+qr[2*t+1] for t in range(16))
        masses=[]; refs=[]
        for p in (pd,ps):
            raw=tuple(rbar[t]*p[t]/(2*qbar[t]) for t in range(16)); mass=sum(raw)
            masses.append(mass); refs.append(tuple(a/mass for a in raw))
        ck(masses==[F(4,5),F(1,5)] and refs==[rd,ps],'actual inherited references from ORIGINAL product')
        ck(walk(dense,rd,True)<=1<<64,'out-of-cone dense subtree ALL cuts')
        ck(noreset(sparse,ps)==2,'sparse subtree retains zero source KL and full entropy<=2')
        # Independently certify root H>=average child H=3 by integer products.
        Hpow=F(1)
        for p in pr:
            if p: Hpow*=(1/p)**int(p*256)
        ck(Hpow>=1<<(3*256),'root entropy lower bound exact')
        I=sum(influences); ck(3*I-5>=1,'SAME original 4I after old quarter leaves>=1')
        selector={'original_I':str(I),'pi':[str(v) for v in masses],'root_H_ge':3,
                  'original_bank_residual_lower_bound':str(3*I-5),'sparse_product_gap_avoided':2}
    result={'status':'PASS','rung':'exact finite certificate plus analytic proof; not independent agent acceptance',
            'roots':tested,'selector':selector,'assertions':checks,'helper_assertions':Q.ASSERTIONS,
            'query_states':edges,'cache':str(walk.cache_info()),'elapsed_seconds':time.monotonic()-START,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'prior_helper_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest()}
    out=ROOT/'out'/('pilot.json' if args.pilot else 'main.json'); out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__': main()
