"""Independent direct integer Fourier/containment audit and adversarial checks."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import itertools,json,math,resource,hashlib,time
from pathlib import Path
import numpy as np
from compute import metrics,fhex,from_tables,QS,truth_hex,zeta
from analytic_families import and_row,tribes_row,address_row,bent_row,majority_row

def direct(f):
    N=len(f);n=N.bit_length()-1
    c=[sum(int(f[x])*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)) for s in range(N)]
    m=[x*x for x in c];u=[sum(m[t] for t in range(N) if t&s==s) for s in range(N)]
    numerator=sum(a*b for a,b in zip(m,u));den=N**4
    I=sum(s.bit_count()*m[s] for s in range(N))/N**2
    A=sum(m[s]/N**2*math.log2(N**2/u[s]) for s in range(N) if m[s])
    H=sum(m[s]/N**2*math.log2(N**2/m[s]) for s in range(N) if m[s])
    return dict(n=n,tt_hex=truth_hex(f),WC_numerator=numerator,WC_denominator=den,WC=numerator/den,I=I,H_bits=H,A_bits=A,
                L_over_I=-math.log2(numerator/den)/I if I else 0,
                balanced_L_over_I_minus_1=-math.log2(numerator/den)/(I-1) if c[0]==0 and I>1 else None)

def derivative_wc(f):
    N=len(f);n=N.bit_length()-1;coeff=[];up=[]
    for S in range(N):
        # Average alternating signs over the coordinates in S for every outside assignment.
        inside=[x for x in range(N) if x&S==x];outside=[x for x in range(N) if x&S==0]
        g=[sum(int(f[x|y])*(-1 if y.bit_count()%2 else 1) for y in inside)/len(inside) for x in outside]
        coeff.append(sum(g)/len(g));up.append(sum(x*x for x in g)/len(g))
    return sum(a*a*b for a,b in zip(coeff,up))

def npn4():
    unseen=set(range(1<<15));reps=[];sizes=[];perms=list(itertools.permutations(range(4)))
    while unseen:
        t=min(unseen);orbit=set();reps.append(t)
        for p in perms:
            tr=[sum(((x>>i)&1)<<p[i] for i in range(4)) for x in range(16)]
            u=sum(((t>>x)&1)<<tr[x] for x in range(16))
            for a in range(16):
                v=sum(((u>>x)&1)<<(x^a) for x in range(16));orbit.add(min(v,65535^v))
        assert orbit<=unseen;unseen-=orbit;sizes.append(len(orbit))
    assert len(reps)==222 and sum(sizes)==32768
    return dict(classes=len(reps),complement_normalized_tables=sum(sizes))

def main():
    start=time.time();out={};errors={};witnesses=[]
    for n in range(1,5):
        N=1<<n;idx=np.arange(N);had=np.array([[(-1 if (int(s)&int(x)).bit_count()%2 else 1) for x in idx] for s in idx],dtype=np.int64)
        inc=np.array([[int(t&s==s) for t in range(N)] for s in range(N)],dtype=np.int64)
        err=0.;count=0
        for f in from_tables(np.arange(1<<(1<<n),dtype=np.uint64),n):
            c=f.astype(np.int64)@had;mi=c*c;ui=mi@inc.T;num=(mi*ui).sum(axis=1);d=metrics(f)
            err=max(err,float(np.abs(d['WC']-num/N**4).max()),float(np.abs(d['c']-c).max()));count+=len(f)
        assert err==0;errors[f'all_n{n}_direct_integer_vs_fast']=dict(tables=count,max_abs_error=err)
    files=list(Path('.').glob('census_n*.json'))
    for file in files:
        d=json.loads(file.read_text());n=d['n'];seen=set()
        for group in ['best_over_I','best_balanced_over_I_minus_1','comparisons']:
            for w in d[group].values():
                if 'tt_hex' not in w or w['tt_hex'] in seen:continue
                seen.add(w['tt_hex']);f=fhex(int(w['tt_hex'],16),n);r=direct(f)
                assert abs(r['WC']-w['WC'])<1e-14 and abs(r['A_bits']-w['A_bits'])<2e-12
                assert abs(derivative_wc(f)-r['WC'])<1e-14
                r['corpus']=file.name;witnesses.append(r)
    out['census_witnesses']=witnesses
    out['independent_npn4']=npn4()
    # Granularity for true real Fourier degree d: every coefficient is a multiple of 2^(1-d).
    gran=0;mono=0;restriction_error=0.;tensor_error=0.;degree_error=0.;conditional_error=0.;quadratic_error=0.;rng=np.random.default_rng(9921)
    worst_restriction=dict(gap=-1e9)
    for f in from_tables(np.arange(1<<16,dtype=np.uint64),4):
        d=metrics(f);c=d['c'];support=d['mu']>0;pc=np.array([x.bit_count() for x in range(16)])
        deg=np.where(support,pc,0).max(axis=1)
        degree_error=max(degree_error,float((d['A']-np.maximum(2*deg-2,0)*d['var']).max()))
        quadratic_error=max(quadratic_error,float((d['L'][:,0]-16*d['I']**2-13*d['I']).max()))
        # Directly delete the empty atom and use the dense incidence matrix.
        positive=d['mu'].copy();positive[:,0]=0
        positive_integer=np.rint(positive*256).astype(np.int64)
        plus_numerator=((positive_integer@inc.T)*positive_integer).sum(axis=1)/65536
        assert np.isfinite(plus_numerator).all()
        conditional_error=max(conditional_error,float(np.abs(d['WC']-(1-d['var'])-plus_numerator).max()))
        for j in range(len(f)):
            step=2**max(0,5-max(1,int(deg[j])))
            assert all(int(x)%step==0 for x in c[j]);gran+=1
        mon=np.all(f[:,[x for x in range(16) if x&1==0]]>=f[:,[x|1 for x in range(16) if x&1==0]],axis=1)
        for i in range(1,4):
            lo=[x for x in range(16) if not x&(1<<i)];mon&=np.all(f[:,lo]>=f[:,[x|(1<<i) for x in lo]],axis=1)
        # Increasing 0/1 output corresponds to decreasing +/-1 values.
        singleton=d['up'][:,[1,2,4,8]];lhs=(d['mu'][:,[1,2,4,8]]-singleton**2)[mon]
        assert lhs.size==0 or np.abs(lhs).max()==0;mono+=int(mon.sum())
        assert np.all(d['L'][mon,0]<=24*d['I'][mon]+1e-12)
        f0=f[:,:8];f1=f[:,8:];a=(f0+f1)/2;dd=(f0-f1)/2
        da=metrics(a);db=metrics(dd);cross=(da['mu']*db['up']).sum(axis=1)
        err=np.abs(d['WC']-da['WC']-db['WC']-cross).max();restriction_error=max(restriction_error,float(err))
        m0=metrics(f0);m1=metrics(f1)
        gap=d['L'][:,0]-(m0['L'][:,0]+m1['L'][:,0])/2
        j=int(np.argmax(gap))
        if gap[j]>worst_restriction['gap']:worst_restriction=dict(gap=float(gap[j]),tt_hex=truth_hex(f[j]),WC=float(d['WC'][j]),WC_restrict0=float(m0['WC'][j]),WC_restrict1=float(m1['WC'][j]),Inf_coordinate=float(db['mu'][j].sum()))
    for _ in range(200):
        f=1-2*rng.integers(2,size=8);g=1-2*rng.integers(2,size=8);fg=(f[:,None]*g[None,:]).ravel()
        a=metrics(f);b=metrics(g);c=metrics(fg)
        tensor_error=max(tensor_error,float(np.max(np.abs(c['L']-a['L']-b['L']))))
        assert abs(c['WC'][0]-a['WC'][0]*b['WC'][0])<1e-14
    assert degree_error<1e-12 and quadratic_error<1e-12 and conditional_error<1e-12
    out['proof_checks']=dict(degree_granularity_tables=gran,monotone_tables=mono,degree_A_bound_max_positive_error=degree_error,quadratic_max_positive_error=quadratic_error,conditional_identity_max_abs_error=conditional_error,restriction_recurrence_max_abs_error=restriction_error,tensor_tests=200,tensor_Lq_max_abs_error=tensor_error,naive_restriction_counterexample=worst_restriction)
    # All explicit target-family formulas checked against truth tables where feasible.
    family=json.loads(Path('families.json').read_text());analytic_errors=[]
    for row in family:
        name=row['name'];n=row['n']
        assert row['Lq_bits']['1.0']<=16*row['I']**2+13*row['I']+1e-12
        assert row['Lq_bits']['1.0']<=row['A_bits']+1e-12<=row['H_bits']+2e-12
        if name=='random_read_once_AND_OR_XOR':assert row['H_bits']<=10*row['I']+1e-12
        if name in ['AND','tribes','majority','PM_K33','PM_K33_plus_9_coins']:assert row['Lq_bits']['1.0']<=24*row['I']+1e-12
        if name=='AND':a=and_row(n)
        elif name=='tribes':a=tribes_row(row['width'],row['tribes'])
        elif name=='address_MUX':a=address_row(row['address_bits'])
        elif name=='bent_quadratic_pairs':a=bent_row(n)
        elif name=='majority':a=majority_row(n)
        else:continue
        e=max(abs(a[k]-row[k]) for k in ['I','H_bits','A_bits','WC'])
        e=max(e,max(abs(a['Lq_bits'][q]-row['Lq_bits'][q]) for q in a['Lq_bits']))
        analytic_errors.append(e);assert e<2e-10,(name,n,e)
    out['analytic_vs_truth_table']=dict(rows=len(analytic_errors),max_abs_error=max(analytic_errors))
    # NPN invariance on arbitrary generated transformations of sampled 5-variable representatives.
    reps=[int(x,16) for x in Path('npn5.txt').read_text().split()];viol=0.
    for t in rng.choice(reps,1000):
        p=rng.permutation(5);a=int(rng.integers(32));t=int(t);u=0
        for x in range(32):
            y=sum(((x>>i)&1)<<int(p[i]) for i in range(5))^a
            u|=((t>>x)&1)<<y
        d=metrics(fhex(t,5));e=metrics(fhex(u,5));viol=max(viol,float(np.abs(d['L']-e['L']).max()))
    assert viol<1e-12;out['npn_invariance']=dict(tests=1000,max_Lq_abs_error=viol)
    out['errors']=errors;out['resources']=dict(wall_seconds=time.time()-start,max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,nice=os.getpriority(os.PRIO_PROCESS,0))
    out['npn5_sha256']=hashlib.sha256(Path('npn5.txt').read_bytes()).hexdigest()
    Path('audit.json').write_text(json.dumps(out,indent=2));print(json.dumps(out['proof_checks']));print(json.dumps(out['resources']))

if __name__=='__main__':main()
