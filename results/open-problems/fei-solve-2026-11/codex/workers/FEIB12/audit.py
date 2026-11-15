"""Independent re-evaluation of every census representative and exact witnesses."""
import json,itertools,math,time
from fractions import Fraction
from pathlib import Path
import mpmath as mp
from numerics import *

def exact(tt,n):
    N=1<<n;f=[-1 if tt>>x&1 else 1 for x in range(N)]
    # Direct character sums, independent of butterfly/zeta implementations.
    h=[sum(f[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)) for s in range(N)]
    mu=[Fraction(a*a,N*N) for a in h];I=sum(s.bit_count()*mu[s] for s in range(N));v=1-mu[0]
    mp.mp.dps=80
    def mm(x):return mp.mpf(x.numerator)/x.denominator
    ph=[]
    for u in [Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(7,8),Fraction(1)]:
        F=[sum(mu[U]*u**((U^S).bit_count()) for U in range(N) if U&S==S) for S in range(N)]
        ph.append(-sum(mm(mu[S])*mp.log(mm(F[S]),2) for S in range(N) if mu[S]))
    vals=[x/mm(I) for x in ph] if I else [mp.nan]*6
    if I:vals +=[(ph[2]-ph[-1])/mm(I),(ph[2]-ph[-1])/mm(I-v) if I>v else mp.nan]
    return dict(n=n,tt=hex(tt),I=str(I),var=str(v),phi=[mp.nstr(x,75) for x in ph],ratios=[mp.nstr(x,75) for x in vals])

def main():
    out=[];exactrows=[];rng=np.random.default_rng(12312026)
    for n in range(1,6):
        ts=np.fromfile(f'npn{n}.bin',dtype='<u4');c=json.load(open(f'census{n}.json'));mx=np.full(9,-np.inf);ties=[[] for _ in range(9)]
        for lo in range(0,len(ts),4096):
            sub=ts[lo:lo+4096];d=data(from_tt(sub,n));I=d['I'];ok=I>0;den=np.where(ok,I,1)
            Z,kl,C=coupling(d);cost=d['phi'][:,2]-d['A'];ex=I-d['var']
            vals=np.column_stack([d['phi']/den[:,None],cost/den,np.where(ex>0,cost/np.where(ex>0,ex,1),-np.inf),C/den])
            vals[~ok]=-np.inf
            for k in range(9):
                M=vals[:,k].max()
                if M>mx[k]+1e-12:mx[k]=M;ties[k]=[]
                if np.isfinite(M) and M>=mx[k]-1e-12:ties[k].extend(hex(int(sub[j])) for j in np.flatnonzero(abs(vals[:,k]-mx[k])<1e-12))
        diff=max(abs(mx[k]-c['suprema'][k]['value']) for k in range(9) if np.isfinite(mx[k]));assert diff<1e-12,(n,diff)
        equiv_err=0.
        for _ in range(100):
            t=int(rng.choice(ts));f=from_tt([t],n);p=rng.permutation(n);a=int(rng.integers(1<<n));ids=np.array([sum(((x>>int(p[i]))&1)<<i for i in range(n))^a for x in range(1<<n)])
            ff=f[:,ids]*(1 if rng.integers(2) else -1);d0=data(f);d1=data(ff)
            equiv_err=max(equiv_err,float(abs(d0['phi']-d1['phi']).max()))
        assert equiv_err<1e-12
        for t in sorted(set(int(c['suprema'][k]['tt'],16) for k in range(8) if c['suprema'][k]['tt'] is not None)):
            exa=exact(t,n);dd=data(from_tt([t],n));err=max(abs(float(mp.mpf(exa['phi'][j]))-dd['phi'][0,j]) for j in range(6));assert err<1e-12
            exactrows.append(exa)
        out.append(dict(n=n,classes=len(ts),max_census_disagreement=diff,random_NPN_invariance_error=equiv_err,suprema=[float(x) if np.isfinite(x) else None for x in mx],extremal_representatives=ties))
        print(n,len(ts),diff,flush=True)
    # Independent full orbit partition in dimension four.
    n=4;N=16;seen=set();reps=[];sizes=[]
    for t in range(65536):
        if t in seen:continue
        bits=[(t>>x)&1 for x in range(N)];orb=set()
        for p in itertools.permutations(range(n)):
            ids=[sum(((x>>p[i])&1)<<i for i in range(n)) for x in range(N)]
            for a in range(N):
                tt=sum(bits[ids[x]^a]<<x for x in range(N));orb.add(tt);orb.add(tt^65535)
        reps.append(t);sizes.append(len(orb));seen.update(orb)
    assert reps==np.fromfile('npn4.bin',dtype='<u4').tolist()
    assert sum(sizes)==65536
    Path('npn4_orbit_audit.json').write_text(json.dumps(dict(classes=len(reps),covered_functions=sum(sizes),orbit_sizes=sizes),indent=2))
    Path('census_audit.json').write_text(json.dumps(out,indent=2,allow_nan=False));Path('exact_extrema.json').write_text(json.dumps(exactrows,indent=2))
    print('independent orbit partition',len(reps),sum(sizes),flush=True)
if __name__=='__main__':main()
