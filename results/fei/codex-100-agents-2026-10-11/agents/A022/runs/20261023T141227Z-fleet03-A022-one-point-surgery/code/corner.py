from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
exec(compile((ROOT/'code/independent.py').read_text(encoding='utf-8').split('counts=')[0],'independent-primitives','exec'))
b=tuple((-1 if x&7==0 else 1)*(-1 if x>>3==0 else 1) for x in range(64));f=tuple(-v if x in (0,1) else v for x,v in enumerate(b))
amp=lambda a:tuple(F(sum(a[x]*(-1 if (x&S).bit_count()%2 else 1) for x in range(len(a))),len(a)) for S in range(len(a)))
before,after=amp(b),amp(f)
for S in range(64):
    expected=before[S]-(F(1,16) if S&1 else 0)
    assert after[S]==expected;count+=1
    assert (after[S]==0)==bool((S&1) and (S>>3));count+=1
assert all(x for x in before);count+=1
zeros=[S for S in range(64) if not after[S]];assert len(zeros)==28;count+=1
for m in range(1,7):
    a=tuple(1 if z==0 else -1 for z in range(1<<m));c=tuple(1 if z==(1<<m)-1 else -1 for z in range(1<<m));h=tuple(a[z] if y==0 else c[z] for z in range(len(a)) for y in (0,1));r=F(1,1<<m);rr=-2*r+4*r*r*(m%2)
    for j in range(m+1):
        eq(v(child(h,j,0)),v(a));eq(v(child(h,j,1)),v(a));eq(add(v(h),scale(v(a),-1)),{2:rr} if rr else {})
    gv=add(*(add(v(h),scale(add(v(child(h,j,0)),v(child(h,j,1))),-F(1,2))) for j in range(m+1)))
    eq(gv,{2:(m+1)*rr} if rr else {})
    assert time.monotonic()-start<60
out={'status':'PASS','cases':7,'assertions':count,'elapsed_seconds':time.monotonic()-start,'zero_rows':zeros,'all_seed_coefficients_nonzero':True,'antipodal_m':'1..6','scope':'exact seed-cancellation certificate and all-coordinate negative V drift; finite checks supplement analytic proofs','peak_memory':'unmeasured'}
(ROOT/'out/corner.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
