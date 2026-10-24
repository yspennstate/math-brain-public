import numpy as np, math,json,pathlib
out=[]
for n in [3,4,5,8,16,32,64]:
    p=np.zeros(n);p[0]=1
    lam=math.cos(math.pi/n)**2
    tmax=math.ceil(n*n*math.log(9)/8)
    tm=None
    for t in range(1,tmax+1):
        p=.5*p+.25*(np.roll(p,1)+np.roll(p,-1))
        tv=float(.5*np.abs(p-1/n).sum())
        low=lam**t/2
        up=.5*math.sqrt(2/math.expm1(8*t/(n*n)))
        assert low<=tv+1e-10<=up+2e-10
        if tv<=.25 and tm is None:tm=t
    assert tm is not None
    out.append({'n':n,'mixing_time_quarter':tm,'upper_bound':tmax,'spectral_lower_bound':math.log(2)/(-math.log(lam))})
pathlib.Path(__file__).with_name('cycle_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
