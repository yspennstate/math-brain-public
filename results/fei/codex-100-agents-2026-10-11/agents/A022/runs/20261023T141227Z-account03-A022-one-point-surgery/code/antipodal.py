from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
source=(ROOT/'code/independent.py').read_text(encoding='utf-8').split('counts=')[0]
exec(compile(source,'independent-primitives','exec'))
for m in range(1,7):
    a=tuple(1 if z==0 else -1 for z in range(1<<m));c=tuple(1 if z==(1<<m)-1 else -1 for z in range(1<<m));r=F(1,1<<m)
    rr=-2*r+4*r*r*(m%2);gg=m*(-4*r+4*r*r*(1+m%2))
    eq(rem(a,c),{2:rr} if rr else {});eq(drift(a,c),{2:gg} if gg else {})
    d=F(sum(x!=y for x,y in zip(a,c)),len(a));assert d==2*r;count+=1
    assert abs(gg)/d==2*m-2*m*r*(1+m%2);count+=1
    assert time.monotonic()-start<60
out={'status':'PASS','cases':6,'m':'1..6','assertions':count,'elapsed_seconds':time.monotonic()-start,'scope':'actual antipodal point spectra, BOTH physical restrictions and exact signed logarithmic formulas; all-m passage analytic','peak_memory':'unmeasured'}
(ROOT/'out/antipodal.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
