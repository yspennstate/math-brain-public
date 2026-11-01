import numpy as np,math,json,pathlib,itertools
out={'pigeonhole_gap':[],'exceptional_pairs':[],'sampling_tail':[]}
rng=np.random.default_rng(93)
for p in [5,7,11,23,101,1009]:
    B=math.floor(math.sqrt(p-1));j=np.arange(1,p)
    cases=list(itertools.product(range(p),repeat=2)) if p<=23 else [tuple(map(int,rng.integers(p,size=2))) for _ in range(150)]
    max_ratio=0
    for a,b in cases:
        if a==b==0:continue
        lam=.5+.25*(np.cos(2*math.pi*j*a/p)+np.cos(2*math.pi*j*b/p))
        gap=1-float(lam.max())
        assert gap<=math.pi**2/B**2+1e-10
        max_ratio=max(max_ratio,gap/(math.pi**2/B**2))
    out['pigeonhole_gap'].append({'p':p,'pairs_checked':len(cases),'largest_ratio_to_bound':max_ratio})
# The exceptional pair projects exactly to the lazy nearest-neighbor cycle.
for p in [5,11,23,101]:
    law=np.zeros(p);law[0]=1
    tm=None
    for t in range(1,math.ceil(p*p*math.log(9)/8)+1):
        law=.5*law+.25*(np.roll(law,1)+np.roll(law,-1))
        if .5*np.abs(law-1/p).sum()<=.25:tm=t;break
    lower=math.log(2)*p*p/(2*math.pi**2)
    assert tm is not None and tm>=lower-1e-10
    out['exceptional_pairs'].append({'p':p,'projected_mixing_time_quarter':tm,'quadratic_lower':lower})
# Monte Carlo only for illustrating scale variability; not needed by the proof.
for p in [101,503,1009]:
    eps=.25;times=[math.ceil(u*p) for u in [.5,1,2,4]];fail=np.zeros(len(times),dtype=int)
    x=np.arange(2*p)
    js=np.arange(p)
    for _ in range(100):
        a,b=map(int,rng.integers(p,size=2))
        while a==b==0:a,b=map(int,rng.integers(p,size=2))
        signs=(1,1) if rng.random()<1/3 else ((1,0) if rng.random()<.5 else (0,1))
        # CRT index x maps to (x mod 2, x mod p).
        z1=a if a%2==signs[0] else a+p
        z2=b if b%2==signs[1] else b+p
        freq=np.arange(2*p)
        lam=.5+.25*(np.cos(2*math.pi*freq*z1/(2*p))+np.cos(2*math.pi*freq*z2/(2*p)))
        for i,t in enumerate(times):
            law=np.fft.ifft(lam**t).real
            tv=.5*np.abs(law-1/(2*p)).sum()
            fail[i]+=tv>eps
    out['sampling_tail'].append({'p':p,'samples':100,'times_over_p':[t/p for t in times],'quotient_failure_fractions':list(map(float,fail/100))})
pathlib.Path(__file__).with_name('second_boundary_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
