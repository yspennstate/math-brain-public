from pathlib import Path
import json,time
run=Path(__file__).resolve().parents[1]
helper=run.parent/'20261012T003951Z-account05-A062-influence-compensator/code/check_reserve.py'
env={'__file__':str(helper)}
exec(compile(helper.read_text().split('core_rows=[]')[0],str(helper),'exec'),env)
F=env['F']; measure=env['measure']; leq=env['leq']; equal=env['equal']; minus=env['minus']; plus=env['plus']; mul=env['mul']; fmt=env['fmt']
start=time.perf_counter(); k,r=4,8
values=[]
for x in range(1<<(1+k+r)):
    s=x&1; controls=(x>>1)&((1<<r)-1); data=x>>(1+r)
    bent=(-1)**sum(((data>>(2*j))&1)*((data>>(2*j+1))&1) for j in range(k//2))
    values.append(1 if controls else (-bent if s and data==0 else bent))
values=tuple(values)
_,H,infs=measure(values)
children=[tuple(values[x] for x in range(len(values)) if (x&1)==bit) for bit in (0,1)]
Hs=[measure(g)[1] for g in children]
D=minus(H,mul(plus(Hs[0],Hs[1]),F(1,2)))
cert=json.loads((run/'out/EXACT_OWNER.json').read_text())['compressed'][0]
expected=(F(cert['D_seed']['lower']),F(cert['D_seed']['upper']))
leq(max(D[0],expected[0]),min(D[1],expected[1]),'raw_compressed_selector_drop_overlap')
equal(infs[0],F(cert['Inf_seed']),'raw_compressed_actual_selector_influence')
elapsed=time.perf_counter()-start
assert elapsed<60,elapsed
out={'dimension':13,'truth_table_values':len(values),'method':'integer Walsh and physical edges on the actual seed and both physical children, no compressed multiplicities assumed','assertions':sum(env['counts'].values()),'counts':dict(env['counts']),'failures':0,'runtime_seconds':elapsed,'D':fmt(D),'Inf_selector':str(infs[0])}
(run/'out/RAW_SEED.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='D'},indent=2))
