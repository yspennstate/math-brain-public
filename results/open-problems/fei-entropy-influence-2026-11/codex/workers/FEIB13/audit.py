"""Independent restriction sums, all n=4 truth tables, and family cross-checks."""
import os
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
import numpy as np,math,json,hashlib,resource,sys,time
from pathlib import Path
import experiment as e
import families as fam
import mux

def direct(f):
    f=np.atleast_2d(f);B,N=f.shape;n=N.bit_length()-1
    mu=np.zeros((B,N));up=mu.copy();p=mu.copy()
    for S in range(N):
        ins=[x for x in range(N) if x&S==x];outs=[x for x in range(N) if x&S==0]
        signs=np.array([(-1)**x.bit_count() for x in ins])
        g=(f[:,np.array(outs)[:,None]|np.array(ins)]*signs).sum(2)/len(ins)
        mu[:,S]=g.mean(1)**2;up[:,S]=(g*g).mean(1);p[:,S]=(g!=0).mean(1)
    return mu,up,p,np.array([S.bit_count() for S in range(N)])

def main():
    start=time.time();report={'nice':os.getpriority(os.PRIO_PROCESS,0)};errs={}
    extrema={};violations={};n=4;N=1<<n
    for lo in range(0,1<<N,1024):
        tt=np.arange(lo,lo+1024,dtype=np.uint32)
        f=1-2*((tt[:,None]>>np.arange(N,dtype=np.uint32))&1).astype(np.int8)
        a=direct(f);b=e.data(f)
        for name,x,y in zip(('mu','up','p'),a[:3],b[:3]):errs[name]=max(errs.get(name,0.),float(abs(x-y).max()))
        out=e.metrics(*a);e.update(extrema,out,f)
        I=out['I'];V=out['Var'];P=out['P'];A=out['A']
        checks={'P_le_A':P-A,'A_le_P_2I':A-P-2*(I-V)}
        mu,up,p,pc=a
        checks['noise_support_bound']=np.max(e.zeta(mu,.5)-up*p**(1/3),axis=1)
        for theta in (1.,.5,.25):
            for c in (2.,4.,8.):
                checks[f'Jensen_c{c}_th{theta}']=theta*A-math.log2(c)*I-out[f'W_c{c:g}_th{theta:g}']
        for t in e.TS:checks[f'T{t}_le_P_tail']=out[f'T{t:g}']-P-(1-t)*I
        for key in ('ref_tau0.5','ref_mixture_uniform'):
            checks[key+'_upper']=out[key]-out['H']-I
            checks[key+'_lower']=out['H']-out[key]
        for key,v in checks.items():violations[key]=max(violations.get(key,-math.inf),float(v.max()))
    report['all4_count']=1<<N;report['direct_derivative_errors']=errs;report['inequality_max_lhs_minus_rhs']=violations
    rng=np.random.default_rng(1300013);f=rng.choice([-1,1],(1000,64)).astype(np.int8)
    mu,up,p,pc=e.data(f)
    report['noise_support_sample6_count']=len(f)
    report['noise_support_sample6_max_violation']=float(np.max(e.zeta(mu,.5)-up*p**(1/3)))
    cen=json.load(open('census.json'));report['all4_maximum_ratio_errors']={key:abs(extrema[key]['ratio']-cen['npn4'][key]['ratio']) for key in extrema if isinstance(extrema[key],dict)}
    # Independently reconstruct every saved extremal truth table, including n=5 and samples.
    werr=0.;wcount=0
    for name,rec in cen.items():
        for key,entry in rec.items():
            if not isinstance(entry,dict):continue
            n=entry['n'];tt=int(entry['tt'],16);f=np.array([1-2*((tt>>x)&1) for x in range(1<<n)])
            out=e.metrics(*direct(f));ratio=float(out[key][0]/out['I'][0]);werr=max(werr,abs(ratio-entry['ratio']));wcount+=1
    report['witness_checks']=wcount;report['witness_max_ratio_error']=werr
    # Formula checks against independent restriction sums.
    ferr={};merr={};serr={}
    for name,f in e.functions():
        if len(f)>512:continue
        out={k:float(v[0]) for k,v in e.metrics(*direct(f)).items()}
        if name.startswith('tribes'):
            w=int(name.split('_')[1][1:]);m=int(name.split('_')[2][1:]);row=fam.tribes(w,m)
            for key in out:
                if key in row and key not in ('bound_violation',) and not key.startswith('W_'):
                    ferr[key]=max(ferr.get(key,0.),abs(out[key]-row[key]))
        if name.startswith('majority') or name.startswith('AND'):
            kind=name.split('_')[0];row=fam.symmetric(int(name.split('_')[1]),kind)
            for key in out:
                if key in row and not key.startswith('W_'):serr[key]=max(serr.get(key,0.),abs(out[key]-row[key]))
        if name.startswith('MUX'):
            L=int(name.split('_')[1][1:]);k=int(name.split('_')[2][1:]);g=np.array([f[x<<L] for x in range(1<<k)])
            row=mux.calculate(L,g)
            for key in out:
                if key in row and not key.startswith('W_'):merr[key]=max(merr.get(key,0.),abs(out[key]-row[key]))
    report['tribes_formula_max_errors']=ferr;report['symmetric_formula_max_errors']=serr;report['mux_formula_max_errors']=merr
    quad=[]
    for w in (16,32,64):
        m=round(math.log(2)*2**w);a=fam.tribes(w,m,64);b=fam.tribes(w,m,128)
        quad.append({'w':w,'uniform_mix_cost_error':abs(a['ref_mixture_uniform']-b['ref_mixture_uniform']),'omitted_mass':a['omitted_spectral_mass']})
    report['quadrature']=quad
    families=json.load(open('families.json'))
    report['tribes_weakened_W_max_logK']=max(r['W_K_c3.41421356237_th0.5'] for r in families if 'w' in r)
    report['tribes_support_bound_violation']=max(r['P']-(1+2/math.log(2))*r['I'] for r in families if 'w' in r)
    report['npn_counts']={str(n):len(np.fromfile(f'npn{n}.bin',dtype='<u4')) for n in range(1,6)}
    report['npn_sha256']={str(n):hashlib.sha256(Path(f'npn{n}.bin').read_bytes()).hexdigest() for n in range(1,6)}
    report['max_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report['elapsed_seconds']=time.time()-start
    Path('audit.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
    assert max(errs.values())<1e-12
    assert max(violations.values())<1e-10
    assert max(report['all4_maximum_ratio_errors'].values())<1e-10
    assert werr<1e-10
    for er in (ferr,serr,merr):assert max(er.values())<1e-9
    assert report['tribes_weakened_W_max_logK']<=3+1e-10
    assert report['noise_support_sample6_max_violation']<1e-10
    print('AUDIT PASS')
if __name__=='__main__':main()
