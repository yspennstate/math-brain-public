from pathlib import Path
from functools import lru_cache
import json,time,sys
run=Path(__file__).resolve().parents[1]
helper=run.parent/'20261012T003951Z-account05-A062-influence-compensator/code/check_reserve.py'
env={'__file__':str(helper)}
exec(compile(helper.read_text().split('core_rows=[]')[0],str(helper),'exec'),env)
F=env['F']; point=env['point']; plus=env['plus']; minus=env['minus']; mul=env['mul']; pos=env['pos']; measure=env['measure']; equal=env['equal']; leq=env['leq']; fmt=env['fmt']
def absupper(a): return max(abs(a[0]),abs(a[1]))
start=time.perf_counter()
@lru_cache(None)
def tree(values,order,C):
    if len(set(values))==1: return point(0),point(0),F(0)
    _,H,infs=measure(values)
    i=next((i for i in order if infs[i]),None)
    assert i is not None
    children=[tuple(values[x] for x in range(len(values)) if ((x>>i)&1)==bit) for bit in (0,1)]
    rest=tuple(j if j<i else j-1 for j in order if j!=i)
    ch=[tree(f,rest,C) for f in children]
    D=minus(H,mul(plus(ch[0][1],ch[1][1]),F(1,2)))
    R=pos(plus(minus(D,point(C*infs[i])),mul(plus(ch[0][0],ch[1][0]),F(1,2))))
    I=infs[i]+sum(c[2] for c in ch)/2
    equal(I,sum(infs),'complete_owned_influence')
    return R,H,I
pilot='--pilot' in sys.argv
domains=[]
for mask in range(16):
    g=tuple(1 if (mask>>x)&1 else -1 for x in range(4))
    domains.append((g,(1,) if pilot else (1,2,6),(1,) if pilot else (1,2,3,4)))
if not pilot: domains.append((tuple(-1 if x==0 else 1 for x in range(8)),(1,2,6),(1,2,3,4,5,6)))
rows=[]; rootcount=0
for g,prices,qs in domains:
 r=len(g).bit_length()-1
 gv=tuple(-v if x==0 else v for x,v in enumerate(g))
 for C in prices:
    R,H,I=tree(g,tuple(range(r)),C)
    Rv,_,_=tree(gv,tuple(range(r)),C)
    core_diff=absupper(minus(Rv,R))
    for q in qs:
        values=tuple(-g[x&((1<<r)-1)] if x==0 else g[x&((1<<r)-1)] for x in range(1<<(r+q)))
        order=tuple(range(r,r+q))+tuple(range(r))
        Rq,Hq,Iq=tree(values,order,C)
        d=F(2,1<<(r+q)); delta=d/2
        err=F(1,1<<q)*core_diff+d*q*(r+4+C+F(q,2))
        leq(absupper(minus(Rq,R)),err,'reserve_padding_error')
        # Reconstruct the first dummy split independently from its truth table.
        ch=[tuple(values[x] for x in range(len(values)) if ((x>>r)&1)==bit) for bit in (0,1)]
        child_order=tuple(range(r,r+q-1))+tuple(range(r))
        z=[tree(f,child_order,C) for f in ch]
        D=minus(Hq,mul(plus(z[0][1],z[1][1]),F(1,2)))
        equal(measure(values)[2][r],d,'padded_query_influence')
        equal(z[1][0],R,'clean_child_retains_core_reserve')
        equal(Rq,pos(plus(minus(D,point(C*d)),mul(plus(z[0][0],z[1][0]),F(1,2)))),'physical_recurrence')
        fvalues=tuple((-g[(x>>1)&((1<<r)-1)] if (x&1) else g[(x>>1)&((1<<r)-1)])*(-1 if x==0 else 1) for x in range(1<<(r+q+1)))
        forder=(0,)+tuple(i+1 for i in order)
        RF,HF,IF=tree(fvalues,forder,C)
        limit=pos(minus(R,point(C)))
        charerr=err/2+delta*(r+q+C+F(9,2))
        leq(absupper(minus(RF,limit)),charerr,'character_limit_error')
        equal(measure(fvalues)[2][0],1-delta,'character_owned_influence')
        Fc=[tuple(fvalues[x] for x in range(len(fvalues)) if (x&1)==bit) for bit in (0,1)]
        equal(Fc[0],values,'edited_actual_child')
        equal(Fc[1],tuple(-g[x&((1<<r)-1)] for x in range(len(values))),'clean_opposite_actual_child')
        Dc=minus(HF,mul(plus(Hq,H),F(1,2)))
        # Ignore differences in zero/dummy representations only for entropy.
        expected=pos(plus(minus(Dc,point(C*(1-delta))),mul(plus(Rq,R),F(1,2))))
        leq(max(RF[0],expected[0]),min(RF[1],expected[1]),'character_complete_reserve_overlap')
        if r==3 and C==1:
            leq(F(1),R[0],'positive_retained_core_reserve')
            if q==6: leq(F(3,4),RF[0],'positive_character_residual')
        rows.append({'r':r,'g':list(g),'q':q,'C':C,'core_R':fmt(R),'padded_R':fmt(Rq),'character_R':fmt(RF),'character_limit':fmt(limit),'padding_error_bound':str(err),'character_error_bound':str(charerr)})
        rootcount+=2
elapsed=time.perf_counter()-start
assert elapsed<60,elapsed
out={'helper_version':'A062-arbitrary-core-reserve-v1','pilot':pilot,'root_count':rootcount,'assertions':sum(env['counts'].values()),'counts':dict(env['counts']),'runtime_seconds':elapsed,'failures':0,'distinct_internal_states':tree.cache_info().currsize,'rows':rows}
(run/'out'/('PILOT.json' if pilot else 'EXACT_TRANSFER.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
