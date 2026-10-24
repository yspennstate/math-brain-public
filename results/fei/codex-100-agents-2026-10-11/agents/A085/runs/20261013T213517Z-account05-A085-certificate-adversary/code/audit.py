from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations,combinations
import hashlib,json,time,sys,math
import numpy as np
sys.set_int_max_str_digits(100000)
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'out'; OUT.mkdir(exist_ok=True)
LEAD=Path(r'~\brain_workers\FEI100_20261011\claude\B17\runs\20261011T224300Z-claude-B17-erasure-census-affine-bridge')
A071=Path(r'~\brain_workers\FEI100_20261011\agents\A071\runs\20261011T233808Z-account05-A071-search-space-design')
START=time.perf_counter(); checks=0
def ck(v):
    global checks
    assert v; checks+=1
def save(name,x): (OUT/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf8')
def guard(limit=180):
    if time.perf_counter()-START>limit: raise RuntimeError('Frozen cap exceeded')
S=1<<192; TERMS=64
@lru_cache(None)
def ln_unit(x):
    ck(1<=x<=2); z=(x-1)/(x+1); power=z; zz=z*z; lo=0
    for j in range(TERMS):
        term=2*S*power/(2*j+1); lo+=term.numerator//term.denominator; power*=zz
    tail=2*S*power/((2*TERMS+1)*(1-zz))
    return lo,lo+TERMS+(tail.numerator+tail.denominator-1)//tail.denominator
@lru_cache(None)
def log(x):
    x=Q(x); ck(x>0); k=x.numerator.bit_length()-x.denominator.bit_length(); r=x/Q(2)**k
    if r<1: r*=2; k-=1
    if r==1: return Q(k),Q(k)
    l,h=ln_unit(r); dl,dh=ln_unit(Q(2)); return Q(k)+Q(l,dh),Q(k)+Q(h,dl)
def add(a,b): return a[0]+b[0],a[1]+b[1]
def mul(c,a): return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def form(v):
    ans=(Q(0),Q(0))
    for p,e in v.items(): ans=add(ans,mul(Q(e),log(int(p))))
    return ans
def subtract(v,w):
    d={p:Q(v.get(p,0))-Q(w.get(p,0)) for p in set(v)|set(w)}
    return {p:e for p,e in d.items() if e}
def pack_interval(v): return [str(v[0]),str(v[1])]
@lru_cache(None)
def factor(m):
    d={}; p=2
    while p*p<=m:
        while m%p==0: d[p]=d.get(p,0)+1; m//=p
        p+=1
    if m>1:d[m]=d.get(m,0)+1
    return d
def mlog(acc,m,c):
    if m<=1:return
    for p,e in factor(m).items():acc[p]=acc.get(p,Q(0))+c*m*e
def fwht(vals):
    a=list(vals); h=1
    while h<len(a):
        for first in range(0,len(a),2*h):
            for x in range(first,first+h): a[x],a[x+h]=a[x]+a[x+h],a[x]-a[x+h]
        h*=2
    return a
def spectrum(n,points):
    N=1<<n; t=[-1 if x in points else 1 for x in range(N)]; W=fwht(t)
    ck(sum(w*w for w in W)==N*N)
    ck(W==[sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(N)])
    ck(fwht(W)==[N*v for v in t]); q=[w*w for w in W]
    rows=[]; Btotal={}; Itotal=0
    for i in range(n):
        bit=1<<i; L=sum(q[s] for s in range(N) if s&bit)
        edges=sum(t[x]!=t[x|bit] for x in range(N) if not x&bit); ck(L==2*N*edges); Itotal+=L
        E={}
        for s in range(N):
            if not s&bit:
                a,b=q[s],q[s|bit]; mlog(E,a+b,1); mlog(E,a,-1); mlog(E,b,-1)
        for p,e in E.items(): Btotal[p]=Btotal.get(p,Q(0))+e
        if L:
            v={p:e/L for p,e in E.items() if e}; rows.append({'i':i,'I':str(Q(L,N*N)),'L':L,'vector':{str(p):str(e) for p,e in v.items()},'interval':pack_interval(form(v))})
    H={2:Q(2*n*N*N)}
    for a in q:mlog(H,a,-1)
    return {'n':n,'negative_points':sorted(points),'walsh':W,'rows':rows,'H_I_vector':{str(p):str(e/Itotal) for p,e in H.items() if e},'B_I_vector':{str(p):str(e/Itotal) for p,e in Btotal.items() if e}}
def generate_orbit(n,points):
    negative=set()
    for perm in permutations(range(n)):
        image=[sum(((x>>j)&1)<<perm[j] for j in range(n)) for x in points]
        for t in range(1<<n):negative.add(sum(1<<(x^t) for x in image))
    allmask=(1<<(1<<n))-1; result=negative|{allmask^m for m in negative}
    return negative,result
def screen_audit(pilot):
    # Execute only a local byte-identical helper copy: no external imports/cache writes.
    data=(LEAD/'code/certlog.py').read_bytes(); p=ROOT/'code/source_certlog.py'; p.write_bytes(data)
    import importlib.util
    spec=importlib.util.spec_from_file_location('local_source_certlog',p); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    maxval=256 if pilot else 4409; ll=mod.LinLog(maxval); m=len(ll.P); ck(m==(54 if pilot else 600))
    floats=ll.logf
    unit=Q(1,1<<53)
    # Check exact source floating constants against independent true-log intervals.
    for prime,f in zip(ll.P,floats):
        l,h=log(prime); exactf=Q.from_float(float(f))
        ck(abs(exactf-l)<=unit*l and abs(exactf-h)<=unit*l)
    gamma=Q(m)*unit/(1-m*unit); eta=unit+(1+unit)*gamma
    ck(eta<Q(1,1<<43)); ck(Q(1,1<<40)*(1-eta)>eta)
    if pilot: ck(eta<Q(1,1<<46))
    # Force nearly half-ULP upward errors under sequential strided reduction.
    E=np.ones(m,dtype=np.int64); E[0]=1<<49; acc=float(E[0]); selected=[]
    for j in range(1,m):
        candidates=np.arange(1,4097,dtype=np.int64)
        terms=candidates.astype(np.float64)*floats[j]
        errors=(acc+terms)-acc-terms
        k=int(np.argmax(errors)); E[j]=candidates[k]; acc+=float(terms[k])
        selected.append(float(errors[k]))
    cf=np.array([E,E],dtype=np.int64,order='C'); ff=np.array([E,E],dtype=np.int64,order='F')
    rows=[]; failing=[]
    lengths=[m] if pilot else range(2,m+1)
    for length in lengths:
        # Source LinLog expects all columns. Prefix represented by trailing zeros.
        a=ff.copy(order='F'); a[:,length:]=0
        sg,val=ll.float_screen(a)
        coeff={p:int(e) for p,e in zip(ll.P,E[:length])}; truth=form(coeff)
        measured=Q.from_float(float(val[0])); error=(measured-truth[1],measured-truth[0]); threshold=truth[1]/(1<<46)
        ck(all(sg==1))
        if error[0]>threshold:
            failing.append(length)
            if len(failing)==1 or length==m:
                rec={'terms':length,'coefficients':{str(p):int(e) for p,e in coeff.items()},'computed_float_hex':float(val[0]).hex(),'error_interval':pack_interval(error),'true_positive_form_interval':pack_interval(truth),'claimed_error_upper':str(threshold),'certified_violation':True}
                rows.append(rec); save('screen_failure_checkpoint.json',rows)
        guard(55 if pilot else 180)
    def summarize(layout):
        sg,val=ll.float_screen(layout); truth=form({p:int(e) for p,e in zip(ll.P,E)}); vf=Q.from_float(float(val[0])); return {'computed_hex':float(val[0]).hex(),'error_interval':pack_interval((vf-truth[1],vf-truth[0])),'positive_screen':bool(all(sg==1))}
    result={'helper_sha256':hashlib.sha256(data).hexdigest(),'prime_count':m,'max_log_relative_error_verified':str(unit),'u':str(unit),'gamma_m':str(gamma),'safe_eta':str(eta),'safe_eta_below_2^-43':True,'source_threshold_2^-40_sign_safe':True,'source_2^-46_bound_valid_for_this_prime_count':pilot,'first_failed_prefix_in_constructed_row':min(failing) if failing else None,'failures':rows,'C_layout':summarize(cf),'F_layout':summarize(ff),'checks':checks,'runtime_seconds':time.perf_counter()-START,'numpy_version':np.__version__}
    save('screen_pilot.json' if pilot else 'screen_audit.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ('failures','C_layout','F_layout')},indent=2),flush=True)
def math_audit():
    kb4={2:Q(4),5:Q(5,2),3:-Q(9,2)}; kd4={2:Q(12),3:-Q(9,2)}
    h4={2:Q(12),7:-Q(49,16)}; agg4={2:Q(4),3:-Q(9,4),5:-Q(35,16),13:Q(13,16),17:Q(17,16)}
    five={2:Q(16,3),3:-Q(3,8),13:-Q(169,24),89:Q(89,24)}
    fivehigh={2:Q(16),3:-Q(63,8),5:Q(15),13:-Q(169,8),17:Q(85,8)}
    witnesses=[]
    for n,points,target in [(4,{0,1},kb4),(4,{0},None),(4,{0,1,2},None),(5,{5,12,13},five),(6,{0,1,2,4,8,16,32,6,17,40},None)]:
        rec=spectrum(n,points)
        if target:
            ratios=[{int(p):Q(e) for p,e in row['vector'].items()} for row in rec['rows']]
            ck(any(v==target for v in ratios))
            for v in ratios:
                d=subtract(v,target); ck(not d or form(d)[0]>0)
        if n==4 and points=={0}:ck({int(p):Q(e) for p,e in rec['H_I_vector'].items()}==h4)
        if n==4 and points=={0,1,2}:ck({int(p):Q(e) for p,e in rec['B_I_vector'].items()}==agg4)
        if n==5:
            ck([row['I'] for row in rec['rows']]==['1/16','3/16','3/16','1/16','3/16'])
            ck(all({int(p):Q(e) for p,e in row['vector'].items()}== (fivehigh if row['i'] in (0,3) else five) for row in rec['rows']))
            ck(form(subtract(five,{2:Q(107,40)}))[0]>0); ck(form(subtract({2:Q(107,40)},kb4))[0]>0)
        if n==6:
            ck(all(form(subtract({int(p):Q(e) for p,e in row['vector'].items()},{2:Q(368,125)}))[0]>0 for row in rec['rows']))
            ck(form(subtract({2:Q(368,125)},five))[0]>0)
        witnesses.append(rec); save('witness_checkpoint.json',witnesses)
    # Exact decrement expression at the three-bit point-function witness, using physical children.
    n=4;N=16;t=[-1 if x in {0,1} else 1 for x in range(N)]; W=fwht(t); E={2:Q(2*n*N*N)}
    for a in W: mlog(E,a*a,-1)
    for i in (1,2,3):
        selected={p:Q(e) for p,e in E.items()}; bit=1<<i
        for value in (0,1):
            child=[t[x] for x in range(N) if bool(x&bit)==bool(value)]
            # parent-scale 256 * avg entropy subtract: child denominator 64.
            for a in fwht(child):mlog(selected,a*a,2)
            selected[2]-=Q(2*3*64*2)
        L=sum(W[s]**2 for s in range(N) if s&bit)
        ck({p:e/L for p,e in selected.items() if e}==kd4)
    orbits=[]
    for n,points,expected in [(4,{0,1},64),(4,{0},32),(4,{0,1,2},192),(5,{0,1,2},640)]:
        neg,allm=generate_orbit(n,points);ck(len(allm)==expected);ck(len(allm)==2*len(neg))
        if n==4 and points=={0,1}:
            direct={sum(1<<x for x in (a,a^(1<<i))) for a in range(16) for i in range(4)}; ck(direct==neg)
        if len(points)==3:
            direct={sum(1<<x for x in (a,a^(1<<i),a^(1<<j))) for a in range(1<<n) for i,j in combinations(range(n),2)}; ck(direct==neg)
        orbits.append({'n':n,'points':sorted(points),'negative_orbit':len(neg),'including_complements':len(allm),'negative_orbit_sha256':hashlib.sha256(json.dumps(sorted(neg)).encode()).hexdigest()})
    # Independently recheck every 40-bit upper lookup entry against a narrower own interval.
    data=(A071/'code/sparse_search.py').read_bytes(); local=ROOT/'code/source_sparse.py';local.write_bytes(data)
    import importlib.util
    sp=importlib.util.spec_from_file_location('local_sparse',local); mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod)
    minslack=None
    for a in range(17):
        for b in range(17):
            l,h=mod.g(a*a,b*b); fast_upper=(h+(1<<56)-1)//(1<<56)
            if a==0 or b==0:ck(fast_upper==0);continue
            truth=add(mul(a*a+b*b,log(a*a+b*b)),add(mul(-a*a,log(a*a)),mul(-b*b,log(b*b))))
            ck(truth[1]<=Q(fast_upper,1<<40))
    ck(Q(2964159675584,1<<40)<form(five)[0])
    # n5 int64 lookup/summation/cross-division arithmetic bounds, all exact.
    packet_max=512*(1<<40);sum_max=16*(packet_max+1);division_numerator_max=sum_max+256
    ck(division_numerator_max<(1<<63))
    # n4 prime exponent absolute bounds from Parseval and coefficient support.
    # m log m exponents <= 8m; total mass <=256. Conservative per-coordinate vectors.
    bounds={'n4_H_prime_abs':4096,'n4_B_prime_abs':4096,'n4_Delta_prime_abs':4096,'n4_aggregate_B_prime_abs':16384,'max_cross_comparison_prime_abs':2*1024*16384,'n5_lookup_upper_bound':packet_max+1,'n5_16packet_sum_upper':sum_max,'n5_division_numerator_upper':division_numerator_max}
    ck(bounds['max_cross_comparison_prime_abs']<(1<<50))
    result={'witnesses':witnesses,'orbits':orbits,'lookup_entries':289,'all_lookup_upper_bounds_verified':True,'seed_lower_verified':True,'integer_range_bounds':bounds,'n5_covering_filters':'Output complement/minority then coordinate permutation sorting physical influences then anchored translation-minimum; all are covering, not unique-orbit assertions','full_census_rerun':False,'checks':checks,'runtime_seconds':time.perf_counter()-START}
    save('math_audit.json',result);print(json.dumps({k:v for k,v in result.items() if k!='witnesses'},indent=2),flush=True)
def recheck_failure():
    saved=json.loads((OUT/'screen_audit.json').read_text()); row=saved['failures'][0]
    import importlib.util
    p=ROOT/'code/source_certlog.py';sp=importlib.util.spec_from_file_location('source_recheck',p);mod=importlib.util.module_from_spec(sp);sp.loader.exec_module(mod)
    coeff={int(p):int(e) for p,e in row['coefficients'].items()}; ll=mod.LinLog(max(coeff));ck(len(ll.P)==130)
    vec=[coeff[p] for p in ll.P]; E=np.array([vec,vec],dtype=np.int64,order='F')
    ck(E.shape==(2,130) and E.flags.f_contiguous and not E.flags.c_contiguous)
    ck(max(map(abs,vec))<(1<<50));sg,val=ll.float_screen(E);truth=form(coeff)
    vf=Q.from_float(float(val[0]));err=(vf-truth[1],vf-truth[0]); exact_bound=truth[1]/(1<<46); computed_bound=vf/(1<<46)
    ck(err[0]>exact_bound and err[0]>computed_bound)
    ck(Q(80557,10000)<err[0]<=err[1]<Q(40279,5000));ck(exact_bound<Q(80001,10000))
    C=np.array([vec,vec],dtype=np.int64,order='C');_,cv=ll.float_screen(C);cf=Q.from_float(float(cv[0])); cerr=(cf-truth[1],cf-truth[0])
    ck(all(sg==1));ck(truth[0]>0)
    # Near-zero exact fallbacks from independently generated rational approximants.
    fallbacks=[]
    l,h=log(3)
    for k in (1,4,8,16,24,32,40):
        r=((l+h)/2).limit_denominator(1<<k); formv={3:r.denominator,2:-r.numerator}; interval=form(formv)
        ck(interval[0]>0 or interval[1]<0)
        expected=1 if interval[0]>0 else -1
        E1=np.zeros((1,130),dtype=np.int64);E1[0,ll.idx[3]]=r.denominator;E1[0,ll.idx[2]]=-r.numerator
        ss,vv=ll.float_screen(E1); ck(ss[0] in (0,expected))
        actual=ll.sign(E1[0]);ck(actual==expected);fallbacks.append({'denominator_limit_bits':k,'prime_coefficients':{str(p):int(e) for p,e in formv.items()},'screen':'UNDECIDED' if ss[0]==0 else 'CORRECTLY_DECIDED','exact_sign':actual})
    ck(sum(r['screen']=='UNDECIDED' for r in fallbacks)>=3)
    ck(mod.sign_form({})==0)
    result={'helper_sha256':saved['helper_sha256'],'terms':130,'numpy_version':np.__version__,'layout':'Fortran-contiguous shape (2,130), two identical rows','coefficients':row['coefficients'],'computed_hex':float(val[0]).hex(),'true_interval':pack_interval(truth),'error_interval':pack_interval(err),'certified_human_error_bounds':['80557/10000','40279/5000'],'claimed_error_bound_upper':str(exact_bound),'computed_S_error_bound':str(computed_bound),'claimed_bound_below':'80001/10000','C_layout_error_interval':pack_interval(cerr),'sign_screen_still_correct':True,'smallest_tested_prefix':130,'global_minimality_claimed':False,'exact_fallback_fixtures':fallbacks,'checks':checks,'runtime_seconds':time.perf_counter()-START}
    save('small_failure_certificate.json',result);print(json.dumps({k:v for k,v in result.items() if k in ['terms','layout','certified_human_error_bounds','claimed_bound_below','smallest_tested_prefix','global_minimality_claimed','checks','runtime_seconds']},indent=2),flush=True)
def main():
    mode=sys.argv[1]
    if mode=='pilot':screen_audit(True)
    elif mode=='screen':screen_audit(False)
    elif mode=='math':math_audit()
    elif mode=='recheck':recheck_failure()
    else:raise ValueError(mode)
if __name__=='__main__':main()
